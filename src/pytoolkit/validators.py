import ipaddress
import re
import uuid
from urllib.parse import urlparse


EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_email(value: str) -> bool:
    """Return true if the value looks like an email address."""
    return bool(EMAIL_REGEX.match(value))


def is_url(value: str) -> bool:
    """Return true if the value looks like a HTTP or HTTPS URL."""
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def is_uuid(value: str) -> bool:
    """Return true if the value is a valid UUID string."""
    try:
        uuid.UUID(value)
        return True
    except (ValueError, AttributeError, TypeError):
        return False


def has_extension(filename: str, extension: str) -> bool:
    """Return true if the filename has the given extension.

    The comparison is case insensitive and `extension` may optionally start with a dot.
    """
    ext = extension.lower().lstrip(".")
    return filename.lower().endswith("." + ext)


def is_ipv4(value: str) -> bool:
    """Return true if the value is a valid IPv4 address."""
    try:
        ipaddress.IPv4Address(value)
        return True
    except ipaddress.AddressValueError:
        return False


def is_ipv6(value: str) -> bool:
    """Return true if the value is a valid IPv6 address."""
    try:
        ipaddress.IPv6Address(value)
        return True
    except ipaddress.AddressValueError:
        return False


def min_length(value: str, length: int) -> bool:
    """Return true if the string has at least the given length."""
    return len(value) >= length


def max_length(value: str, length: int) -> bool:
    """Return true if the string has at most the given length."""
    return len(value) <= length
