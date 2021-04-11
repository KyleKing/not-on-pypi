"""Raise error to indicate that the wrong package was installed."""


class WrongPackageInstalledError(RuntimeError):
    """More specific error."""

    pass


raise WrongPackageInstalledError("""
This package was downloaded from the public pypi.org repository,
but should have been downloaded from an internal repository.

Please update the installer's configuration and download from the proper repository
""")
