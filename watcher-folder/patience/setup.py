import setuptools

REQUIRES = [
	   'watchdog==0.8.3'
]

setuptools.setup(
    name="patience",
    author="Fabio Reis",
    author_email="fabio.reis@stormsec.com.br",
    use_scm_version=False,

    description="Watcher library",
    long_description=open('README.rst').read(),


    packages=setuptools.find_packages(),
    setup_requires=[
        
    ],
    install_requires=REQUIRES, )
