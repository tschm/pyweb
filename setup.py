from setuptools import setup, find_packages

setup(
    name='pyweb',
    version="0.0.1",
    package_dir={'pyweb': "pyweb"},
    packages=find_packages(include=["pyweb*"]),
    package_data={'pyweb':['blueprints/**/templates/**/*.*', 'blueprints/**/static/**/*.*']},
    #packages=find_packages("pyweb"),
    #package_dir={'': "pyweb"},
    #package_data={
    #    '': ['*.html']
    #},
    include_package_data=True,
    author='Thomas Schmelzer',
    author_email='thomas.schmelzer@lobnek.com',
    description='', install_requires=['pandas>=0.23.4','flask==1.0.2','flask-sqlalchemy==2.3.2','flask-restplus==0.12.1', 'Flask-WTF==0.14.2','flask-caching==1.4.0'],
    #package_data = {'pyweb': ['*.html']},
    #packages = ['templates','static'],
    #package_data={'templates':['*'],'static':['*']}

    #include_package_data=True
)


