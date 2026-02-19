from setuptools import find_packages
from setuptools import setup

install_requires = [
    'numpy',
    'pandas',
    'scipy',
    'matplotlib',
    ]

setup(
    name='plot_pfrl',
    version='0.0.0',
    description='Repository for some utils used to plot with pfrl.',
    keywords='PFRL plotting',
    author='Prabhat Nagarajan',
    author_email='nagarajan@ualberta.ca',
    packages=find_packages(),
    install_requires=install_requires,
)
