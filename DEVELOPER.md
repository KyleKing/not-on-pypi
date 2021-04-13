# Developer Guide

## Instructions

1. Modify `PACKAGE_NAME` in the `setup.py` file
2. Run: `rm -rf dist && python setup.py sdist`
3. Publish with `twine` (see notes below)

## Publishing

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
# Note: if poetry isn't found (not on TestPyPi), might need to use extra-index-url instead
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

Full snippet for publishing to the real PyPi

```sh
rm -rf dist && python setup.py sdist
twine upload dist/* --username KyleKing
pip install package_name
```
