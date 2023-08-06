from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='mechanics',
    version='0.1.2',
    description='A library for solving simple mechanics problems',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='alextras',
    author_email='alextrasias@gmail.com',
    py_modules=['mechanics'],
    install_require=[],
)
