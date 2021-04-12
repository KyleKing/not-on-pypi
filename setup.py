# Generated with poetry run dephell deps convert --from-format poetry --from-path pyproject.toml --to-format setuppy --to-path setup.py

from setuptools import setup


if __name__ == '__main__':
    setup(
        long_description='',
        name='common_app',
        version='0.0.0a1',
        description='Reserved package name',
        python_requires='*',
        project_urls={"documentation": "https://github.com/KyleKing/not-on-pypi", "repository": "https://github.com/KyleKing/not-on-pypi"},
        author='Kyle King',
        author_email='dev.act.kyle@gmail.com',
        packages=['not_on_pypi'],
        package_dir={"": "."},
        package_data={},
        install_requires=[],
        extras_require={"dev": ["dephell==0.*,>=0.8.3"]},
    )
