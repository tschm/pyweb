from setuptools import setup, find_packages
from pyweb import __version__ as version
# http://blog.codekills.net/2011/07/15/lies,-more-lies-and-python-packaging-documentation-on--package_data-/

# read the contents of your README file
with open('README.md') as f:
    long_description = f.read()


setup(
    name='pyweb',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=version,
    package_dir={'pyweb': "pyweb"},
    packages=find_packages(include=["pyweb*"]),
    package_data={'pyweb': ['pyweb/blueprints/**/templates/**', 'pyweb/blueprints/**/static/**']},
    include_package_data=True,
    author='Thomas Schmelzer',
    author_email='thomas.schmelzer@lobnek.com',
    url='https://github.com/lobnek/pyweb',
    description='',
    install_requires=['pandas>=1.0.1', 'requests>=2.22.0', 'flask>=1.1.1', 'flask-caching>=1.7.2',
                      'waitress>=1.3.0', 'dash>=1.3.0', 'dash-daq>=0.2.1', 'flask-mongoengine']
)
