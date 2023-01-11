import setuptools

setuptools.setup(
    name='dataclean',
    version='0.0.1', 
    description='For data quality checks, cleaning, and manipulation',
    url='https://github.com/jaciz/dataclean.git',
    author='Jaci',
    install_requires=['altair'],
    author_email='jacquelinezhangg@gmail.com',
    packages=setuptools.find_packages(),
    zip_safe=False
)