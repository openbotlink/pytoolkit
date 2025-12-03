from typing import Any, Dict, Iterable, Mapping


def merge_dicts(*dicts: Mapping[str, Any]) -> Dict[str, Any]:
    """Shallow merge multiple dictionaries into a new dictionary.

    Later dictionaries override earlier ones.
    """
    result: Dict[str, Any] = {}
    for d in dicts:
        result.update(d)
    return result


def deep_merge(*dicts: Mapping[str, Any]) -> Dict[str, Any]:
    """Deeply merge multiple dictionaries.

    Nested dictionaries are merged recursively, other values are overwritten by
    later dictionaries.
    """
    result: Dict[str, Any] = {}
    for d in dicts:
        for key, value in d.items():
            if (
                key in result
                and isinstance(result[key], dict)
                and isinstance(value, dict)
            ):
                result[key] = deep_merge(result[key], value)  # type: ignore[arg-type]
            else:
                result[key] = value
    return result


def select_keys(source: Mapping[str, Any], keys: Iterable[str]) -> Dict[str, Any]:
    """Return a new dictionary containing only the given keys."""
    return {k: source[k] for k in keys if k in source}
