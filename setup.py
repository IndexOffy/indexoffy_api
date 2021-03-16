from setuptools import find_packages, setup

with open('requirements.txt') as requirements_file:
    REQUIREMENTS = [r.replace('\n', '') for r in requirements_file.readlines()]

setup(
    name='indexoffy',
    version='1.0.0',
    description='IndexOffy API',
    author='IndexOffy',
    author_email='indexoffy@gmail.com',
    url='http://www.indexoffy.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False
)