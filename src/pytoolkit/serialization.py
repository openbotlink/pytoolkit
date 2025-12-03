from typing import Any

import json

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore


def to_json(data: Any, indent: int = 2) -> str:
    """Serialize data to JSON."""
    return json.dumps(data, indent=indent, ensure_ascii=False)


def from_json(text: str) -> Any:
    """Deserialize JSON into Python objects."""
    return json.loads(text)


def to_yaml(data: Any) -> str:
    """Serialize data to YAML if PyYAML is available."""
    if yaml is None:
        raise RuntimeError("PyYAML is not installed")
    return yaml.safe_dump(data, sort_keys=False)


def from_yaml(text: str) -> Any:
    """Deserialize YAML into Python objects."""
    if yaml is None:
        raise RuntimeError("PyYAML is not installed")
    return yaml.safe_load(text)
