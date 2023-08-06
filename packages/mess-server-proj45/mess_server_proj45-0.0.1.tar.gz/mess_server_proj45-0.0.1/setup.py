from setuptools import setup, find_packages

setup(name="mess_server_proj45",
      version="0.0.1",
      description="mess_server_proj45",
      author="ivan",
      author_email="dilbazi.mardaliyeva@bk.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy==1.4.49', 'pycryptodome', 'pycryptodomex']
      )
