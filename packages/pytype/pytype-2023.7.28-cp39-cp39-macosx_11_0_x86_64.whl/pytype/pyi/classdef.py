"""Class definitions in pyi files."""

import collections
import sys

from typing import cast, Callable, Dict, List

from pytype.pyi import types
from pytype.pytd import pytd
from pytype.pytd.parse import node as pytd_node

# pylint: disable=g-import-not-at-top
if sys.version_info >= (3, 8):
  import ast as ast3
else:
  from typed_ast import ast3
# pylint: enable=g-import-not-at-top

ParseError = types.ParseError


def get_bases(
    bases: List[pytd.Type], type_match: Callable[..., bool]) -> List[pytd.Type]:
  """Collect base classes."""

  bases_out = []
  namedtuple_index = None
  for i, p in enumerate(bases):
    if p.name and type_match(p.name, "typing.Protocol"):
      if isinstance(p, pytd.GenericType):
        # From PEP 544: "`Protocol[T, S, ...]` is allowed as a shorthand for
        # `Protocol, Generic[T, S, ...]`."
        # https://www.python.org/dev/peps/pep-0544/#generic-protocols
        bases_out.append(p.Replace(base_type=pytd.NamedType("typing.Generic")))
      bases_out.append(pytd.NamedType("typing.Protocol"))
    elif isinstance(p, pytd.NamedType) and p.name == "typing.NamedTuple":
      if namedtuple_index is not None:
        raise ParseError("cannot inherit from bare NamedTuple more than once")
      namedtuple_index = i
      bases_out.append(p)
    elif isinstance(p, pytd.Type):
      bases_out.append(p)
    else:
      msg = f"Unexpected class base: {p}"
      raise ParseError(msg)
  return bases_out


def get_keywords(keywords: List[ast3.keyword]):
  """Get valid class keywords."""

  valid_keywords = []
  for k in keywords:
    keyword, value = k.arg, k.value
    # TODO(rechen): We should validate in load_pytd that "total" is passed only
    # to TypedDict subclasses. We can't do the validation here because external
    # types need to be resolved first.
    if keyword not in ("metaclass", "total"):
      raise ParseError(f"Unexpected classdef kwarg {keyword!r}")
    if isinstance(value, types.Pyval):
      pytd_value = value.to_pytd_literal()
    else:
      pytd_value = cast(pytd.Type, value)
    valid_keywords.append((keyword, pytd_value))
  return valid_keywords


def get_decorators(decorators: List[str], type_map: Dict[str, pytd_node.Node]):
  """Process a class decorator list."""

  # Drop the @type_check_only decorator from classes
  # TODO(mdemello): Workaround for the bug that typing.foo class decorators
  # don't add the import, since typing.type_check_only is the only one.
  decorators = [x for x in decorators if x != "type_check_only"]

  # Check for some function/method-only decorators
  nonclass = {"property", "classmethod", "staticmethod", "overload"}
  unsupported_decorators = set(decorators) & nonclass
  if unsupported_decorators:
    raise ParseError(
        f"Unsupported class decorators: {', '.join(unsupported_decorators)}")

  # Convert decorators to named types. These are wrapped as aliases because we
  # otherwise do not allow referencing functions as types.
  return [pytd.Alias(d, type_map.get(d) or pytd.NamedType(d))
          for d in decorators]


def check_for_duplicate_defs(methods, constants, aliases) -> None:
  """Check a class's list of definitions for duplicates."""
  all_names = (list({f.name for f in methods}) +
               [c.name for c in constants] +
               [a.name for a in aliases])
  duplicates = [name
                for name, count in collections.Counter(all_names).items()
                if count >= 2]
  if duplicates:
    raise ParseError(
        f"Duplicate class-level identifier(s): {', '.join(duplicates)}")
