# Developer Guide

## Publishing

1. Modify `PACKAGE_NAME` in the `setup.py` file
2. Run: `rm -rf dist && python setup.py sdist`
3. Publish with `twine` (TBD)
    1. (See notes below for testing with `test.pypi.org` first)

## Testing

For testing, create an account on [TestPyPi](https://test.pypi.org)

<!--
FYI: Old poetry instructions (can't handle pre-install scripts)

```sh
poetry config repositories.testpypi https://test.pypi.org/simple/
poetry config pypi-token.testpypi ...

poetry build --format sdist
poetry publish --repository testpypi
# If you didn't configure a token, you will need to provide your username and password to publish

# If needed, once can clear the poetry environment (be careful!)
# poetry run pip freeze | xargs poetry run pip uninstall -y
poetry run pip uninstall -y package_name
# Then test installing from test.pypi
poetry run pip install --index-url https://test.pypi.org/simple/ package_name
# Note: if poetry isn't found, might need to use extra-index-url instead (if not also on )
poetry run pip install --extra-index-url https://test.pypi.org/simple/ package_name
```
 -->

```sh
python -m pip install twine

# Test uploading to Test PyPi
twine upload dist/* -r testpypi
# Note: should work with --index-url, but setuptools isn't on PyPi
pip install --extra-index-url https://test.pypi.org/simple/ --upgrade package_name
```

Publish to the real PyPi

```sh
twine upload dist/*
pip install package_name
```

## Links

- [PyPi-Parker](https://github.com/mattsb42/pypi-parker): Helper tooling for parking PyPI namespaces to combat typosquatting
- [Using setup.py](https://stackoverflow.com/questions/20288711/post-install-script-with-python-setuptools)
- [Undocumented Poetry Feature for build scripts](https://aotu.ai/en/blog/2021/01/19/publishing-a-proprietary-python-package-on-pypi-using-poetry/)
- [Contribution notes from cz_legacy](https://github.com/KyleKing/cz_legacy/blob/dc01e162861607d59f450ae842ae785d3ea38794/CONTRIBUTING.md)
- and [calcipy documentation](https://github.com/KyleKing/calcipy/tree/e2db03480f5967f17f57396c6eaced3f85ed9832/docs)
