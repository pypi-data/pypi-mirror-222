from setuptools import setup

name = "types-paramiko"
description = "Typing stubs for paramiko"
long_description = '''
## Typing stubs for paramiko

This is a PEP 561 type stub package for the `paramiko` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`paramiko`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/paramiko. All fixes for
types and metadata should be contributed there.

This stub package is marked as [partial](https://peps.python.org/pep-0561/#partial-stub-packages).
If you find that annotations are missing, feel free to contribute and help complete them.


See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `fe2ebd69af14d376825f21182d415223bd037485` and was tested
with mypy 1.4.1, pyright 1.1.319, and
pytype 2023.7.21.
'''.lstrip()

setup(name=name,
      version="3.3.0.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/paramiko.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['cryptography>=37.0.0'],
      packages=['paramiko-stubs'],
      package_data={'paramiko-stubs': ['__init__.pyi', '_version.pyi', '_winapi.pyi', 'agent.pyi', 'auth_handler.pyi', 'auth_strategy.pyi', 'ber.pyi', 'buffered_pipe.pyi', 'channel.pyi', 'client.pyi', 'common.pyi', 'compress.pyi', 'config.pyi', 'dsskey.pyi', 'ecdsakey.pyi', 'ed25519key.pyi', 'file.pyi', 'hostkeys.pyi', 'kex_curve25519.pyi', 'kex_ecdh_nist.pyi', 'kex_gex.pyi', 'kex_group1.pyi', 'kex_group14.pyi', 'kex_group16.pyi', 'kex_gss.pyi', 'message.pyi', 'packet.pyi', 'pipe.pyi', 'pkey.pyi', 'primes.pyi', 'proxy.pyi', 'rsakey.pyi', 'server.pyi', 'sftp.pyi', 'sftp_attr.pyi', 'sftp_client.pyi', 'sftp_file.pyi', 'sftp_handle.pyi', 'sftp_server.pyi', 'sftp_si.pyi', 'ssh_exception.pyi', 'ssh_gss.pyi', 'transport.pyi', 'util.pyi', 'win_openssh.pyi', 'win_pageant.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
