from setuptools import setup
setup(
    name = 'cpp-newfile-cli',
    version = '0.1.1',
    packages = ['maincli'],
    entry_points = {
        'console_scripts': [
            'cpp-nf = maincli.__main__:main'
        ]
    })