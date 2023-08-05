from setuptools import setup, find_packages

setup(
    name='PDFAgent',
    version='0.2.0',
    url='https://github.com/mr-gpt/PDFAgent',
    author='Twilix Team',
    author_email='jacky@twilix.io',
    description='Production Ready PDF Agent',
    packages=find_packages(),    
    install_requires=['blitzchain>=0.8.1'],
)
