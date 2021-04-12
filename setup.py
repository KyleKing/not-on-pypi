"""Setup File."""

from pathlib import Path
from setuptools import setup
from setuptools.command.install import install

PACKAGE_NAME = 'common_app'
"""Modify the package name here which is to be seen on PyPi."""

AUTHOR = 'Kyle King'
AUTHOR_EMAIL = 'dev.act.kyle@gmail.com'

# --------------------------------------------------------------------------------------


class WrongPackageInstalledError(RuntimeError):
    """More specific error."""

    pass


class RaiseErrorPreInstall(install):
    """Customized setuptools install command - prints a friendly greeting."""

    def run(self):
        raise WrongPackageInstalledError("""
This package was downloaded from the public pypi.org repository, but
should have been downloaded from an internal repository.

Please update the installer's configuration and download from the proper index-url
""")



if __name__ == '__main__':
    setup(
        name=PACKAGE_NAME,
        version='0.0.0a1',
        packages=[PACKAGE_NAME],
        description = 'Reserved package name',
        long_description = Path('README.md').read_text(),
        long_description_content_type='text/markdown',
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url='https://github.com/KyleKing/not-on-pypi',
        license = 'Unlicense',
        classifiers=['License :: Public Domain'],
        cmdclass={
            'install': RaiseErrorPreInstall,
        },
        # repository = 'https://github.com/KyleKing/not-on-pypi',
        # documentation = 'https://github.com/KyleKing/not-on-pypi',
        # 'Bug Tracker' = 'https://github.com/KyleKing/not-on-pypi/issues',
        # include = [ 'LICENSE.md',],
        # scripts = [],
    )
