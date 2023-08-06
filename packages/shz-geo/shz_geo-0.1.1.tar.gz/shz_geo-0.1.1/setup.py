from setuptools import setup, find_packages

with open("README.md", "r") as arq:
    readme = arq.read()

project_name = 'shz_geo'

setup(name=project_name,
      version='0.1.1',
      license='MIT License',
      author='Eliseu Brito',
      long_description=readme,
      long_description_content_type="text/markdown",
      author_email='eliseubrito776@gmail.com',
      keywords='shz geo shzgeo shz_geo',
      description=u'Personal types for my projects',
      packages=find_packages(),
      install_requires=['shz_types>=0.0.3', 'typeguard==4.0.1'], )
