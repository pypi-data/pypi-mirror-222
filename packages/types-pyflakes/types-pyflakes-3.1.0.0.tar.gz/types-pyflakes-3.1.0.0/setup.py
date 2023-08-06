from setuptools import setup

name = "types-pyflakes"
description = "Typing stubs for pyflakes"
long_description = '''
## Typing stubs for pyflakes

This is a PEP 561 type stub package for the `pyflakes` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`pyflakes`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/pyflakes. All fixes for
types and metadata should be contributed there.

This stub package is marked as [partial](https://peps.python.org/pep-0561/#partial-stub-packages).
If you find that annotations are missing, feel free to contribute and help complete them.


See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `a079b0de6e703fcb615a1169a32bc2186efee9bd` and was tested
with mypy 1.4.1, pyright 1.1.319, and
pytype 2023.7.21.
'''.lstrip()

setup(name=name,
      version="3.1.0.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/pyflakes.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['pyflakes-stubs'],
      package_data={'pyflakes-stubs': ['__init__.pyi', 'api.pyi', 'checker.pyi', 'messages.pyi', 'reporter.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
