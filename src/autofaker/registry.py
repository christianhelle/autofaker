"""
Type-resolution registry.

A single ordered set of rules maps a requested type to the generator that
produces anonymous data for it. This replaces the scattered ``if``/``elif``
dispatch and the parallel "supported types" list that previously lived across
``generator.py`` and ``factory.py``.

Resolution order::

    user "front" rules  (overrides, registered before built-ins)
    built-in rules      (fixed, structural -> scalar -> date -> enum -> literal)
    user "back" rules   (custom types, registered before the fallback)
    fallback            (dataclass vs plain class) -- always last

Built-in rules are registered by ``generator.py`` at import time via the
internal ``_register_builtin`` / ``_set_fallback`` helpers, keeping this module
free of any dependency on the generator classes (avoiding an import cycle).
"""

import threading
from typing import Callable, List, NamedTuple, Optional

from autofaker.base import TypeDataGeneratorBase

# A predicate decides whether a rule applies to a requested type. It receives
# the raw type and its normalized (lowercased) name.
Predicate = Callable[[object, str], bool]

# A factory builds the generator for a matched type. It always receives the
# full context so fake-string generation (needs ``field_name``) and nested
# generation (needs ``use_fake_data``) keep working.
Factory = Callable[[object, Optional[str], bool], TypeDataGeneratorBase]


class Rule(NamedTuple):
    predicate: Predicate
    factory: Factory


_lock = threading.RLock()

_builtin_rules: List[Rule] = []
_user_front: List[Rule] = []
_user_back: List[Rule] = []
_fallback: Optional[Factory] = None

_PRIMITIVE_TYPE_NAMES = {
    "int", "float", "str", "complex", "range", "bytes", "bytearray",
    "bool", "memoryview",
}


def get_type_name(t) -> str:
    """Return the routing name for a type.

    Handles the ``from __future__ import annotations`` case where annotations
    arrive as plain strings, so resolution still works without the actual type
    object.
    """
    try:
        return t.__name__
    except AttributeError:
        attributes = dir(t)
        if "_name" in attributes:
            if t._name is not None:
                return t._name
        elif isinstance(t, str) and t in _PRIMITIVE_TYPE_NAMES:
            return t
        return type(t).__name__


# --- internal registration (used by generator.py at import time) ----------

def _register_builtin(predicate: Predicate, factory: Factory) -> None:
    _builtin_rules.append(Rule(predicate, factory))


def _set_fallback(factory: Factory) -> None:
    global _fallback
    _fallback = factory


# --- public registration API ----------------------------------------------

def register_type(type_, factory: Factory, override: bool = False) -> None:
    """Register a generator factory for an exact type.

    :param type_: the type to match (matched by identity or by name).
    :param factory: ``factory(t, field_name, use_fake_data) -> generator``.
    :param override: when ``True`` the rule is consulted *before* the built-in
        rules, allowing it to override built-in behaviour. When ``False``
        (default) it is consulted *after* the built-ins but before the
        dataclass/class fallback -- the right place for genuinely new types.
    """
    type_name = get_type_name(type_).lower()

    def predicate(t, name):
        return t is type_ or name == type_name

    _register_predicate_rule(Rule(predicate, factory), override)


def register_predicate(
    predicate: Predicate,
    factory: Factory,
    priority: str = "before_fallback",
) -> None:
    """Register a generator factory guarded by a custom predicate.

    :param priority: ``"before_builtins"`` to override built-in rules, or
        ``"before_fallback"`` (default) to apply only when no built-in matches.
    """
    if priority not in ("before_builtins", "before_fallback"):
        raise ValueError(
            "priority must be 'before_builtins' or 'before_fallback', "
            f"got {priority!r}"
        )
    _register_predicate_rule(Rule(predicate, factory), priority == "before_builtins")


def _register_predicate_rule(rule: Rule, front: bool) -> None:
    with _lock:
        if front:
            _user_front.append(rule)
        else:
            _user_back.append(rule)


def reset_registry() -> None:
    """Remove all user-registered rules, restoring the built-in defaults."""
    with _lock:
        _user_front.clear()
        _user_back.clear()


class registry_context:
    """Context manager that restores user rules on exit.

    Useful in tests: register temporary generators inside the ``with`` block
    and have them automatically removed afterwards.
    """

    def __enter__(self):
        with _lock:
            self._front = list(_user_front)
            self._back = list(_user_back)
        return self

    def __exit__(self, *exc):
        with _lock:
            _user_front[:] = self._front
            _user_back[:] = self._back
        return False


# --- resolution -------------------------------------------------------------

def resolve(
    t, field_name: Optional[str] = None, use_fake_data: bool = False
) -> TypeDataGeneratorBase:
    """Resolve a type to its generator using the ordered rule set."""
    type_name = get_type_name(t).lower()
    with _lock:
        rules = (*_user_front, *_builtin_rules, *_user_back)
        fallback = _fallback
    for rule in rules:
        if rule.predicate(t, type_name):
            return rule.factory(t, field_name, use_fake_data)
    if fallback is not None:
        return fallback(t, field_name, use_fake_data)
    raise TypeError(f"No generator registered for type {t!r}")
