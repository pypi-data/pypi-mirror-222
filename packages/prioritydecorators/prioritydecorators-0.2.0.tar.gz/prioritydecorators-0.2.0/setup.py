from setuptools import find_packages, setup
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='prioritydecorators',
    packages=find_packages(include=['prioritydecorators']),
    version='0.2.0',
    description='Library for adding/removing multiple decorators to a method with priorities',
    author='Maxim Gorbach',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['sortedcontainers==2.4.0'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.0'],
    license='MIT',
)