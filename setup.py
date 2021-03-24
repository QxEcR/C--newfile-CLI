from setuptools import setup
setup(
    name = 'code-file-generator-cli',
    version = '0.1.2',
    packages = ['maincli'],
    entry_points = {
        'console_scripts': [
            'cpp-nf = maincli.__main__:cpp',
            'jv-nf = maincli.__main__:java'
        ]
    })