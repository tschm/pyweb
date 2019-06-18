from setuptools import setup, find_packages

# http://blog.codekills.net/2011/07/15/lies,-more-lies-and-python-packaging-documentation-on--package_data-/

setup(
    name='pyweb',
    version="0.0.3",
    package_dir={'pyweb': "pyweb"},
    packages=find_packages(include=["pyweb*"]),
    package_data={'pyweb': ['pyweb/blueprints/**/templates/**', 'pyweb/blueprints/**/static/**']},
    include_package_data=True,
    author='Thomas Schmelzer',
    author_email='thomas.schmelzer@lobnek.com',
    description='',
    install_requires=['pandas>=0.24.0', 'flask==1.0.2', 'flask-sqlalchemy==2.3.2', 'flask-caching==1.4.0', 'flask-pymongo']
)
