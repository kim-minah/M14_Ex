from setuptools import setup, find_packages

setup(
    name='HelloPackage',
    version='1.0.0',
    url='https://github.com/kim-minah/M14_Ex.git',
    author='Chelsea and Mina',
    author_email='author@gmail.com',
    description='Hello package',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)
