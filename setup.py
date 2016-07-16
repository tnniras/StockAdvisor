from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='StockAdvisor',
    version=version,
    description='This application is used to get latest Stock price from the RealTime APIs',
    author='Tushar Niras, ',
    author_email='tnniras@gmail.com',
    url='https://github.com/tnniras/StockAdvisor',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)