"""Test `_not_on_pypi`."""

import pytest


def test_import():
    """Raises a 'PackageNotFoundError' to prevent actual use of the package."""
    with pytest.raises(RuntimeError):
        import not_on_pypi  # noqa: F401
