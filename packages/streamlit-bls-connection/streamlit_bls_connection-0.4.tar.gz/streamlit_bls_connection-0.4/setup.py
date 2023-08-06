from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='streamlit_bls_connection',
    version='0.4',
    description='A package to fetch Bureau of Labor Statistics data using Streamlit',
    author='Tony Hollaar',
    author_email='thollaar@gmail.com',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'requests',
        'pandas',
    ],
)
