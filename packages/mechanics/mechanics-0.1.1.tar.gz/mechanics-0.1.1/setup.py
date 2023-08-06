from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='mechanics',
    version='0.1.1',
    description='A library for solving simple mechanics problems',
    author='alextras',
    author_email='alextrasias@gmail.com',
    py_modules=['mechanics'],
    install_require=[],
)
