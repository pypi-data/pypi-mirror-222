from setuptools import setup, find_packages

setup(name="mess_client_project1",
      version="0.0.1",
      description="mess_client",
      author="Dima M",
      author_email="hodas.work@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
