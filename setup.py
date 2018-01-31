from setuptools import setup

setup(
    name='libcomcom-python',
    version='0.0.1',
    packages=['comcom'],
    url='libcomcom-python',
    license='LGPLv3',
    author='Victor Porton',
    author_email='porton@narod.ru',
    description='LibComCom Python wrapper',
    setup_requires = ["cffi>=1.0.0"],
    cffi_modules = ["comcom/low_level_build.py:ffibuilder"],
    install_requires = ["cffi>=1.0.0"],
)
