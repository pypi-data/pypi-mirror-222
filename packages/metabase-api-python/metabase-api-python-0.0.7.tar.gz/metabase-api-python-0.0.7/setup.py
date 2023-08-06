from setuptools import setup, find_packages


# Read requirements.txt file
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name='metabase-api-python',
    version='0.0.7',
    url='https://github.com/Cisco141632/metabase-api-python',
    author='Cisco141632',
    author_email='durgaprasad141632@gmail.com',
    description='A Python wrapper for the Metabase REST API. This package provides easy-to-use functions to interact with Metabase programmatically, enabling operations like fetching data from saved questions, archiving or deleting cards, and more. Ideal for data engineers, data analysts, or anyone looking to integrate Metabase with their Python applications.',
    packages=find_packages(),    
    install_requires=requirements,
)
