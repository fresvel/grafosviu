from setuptools import setup
from setuptools import find_packages

setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    author='Velasteguí Izurieta Homero Javier',
    author_email='fresvel@outlook.com',
    url='https://github.com/fresvel/grafosviu',
    entry_points={
        'console_scripts': [
            'grafoviu=grafoviu.__main__:main'
        ]
    }
)