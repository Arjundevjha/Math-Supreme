from setuptools import setup, find_packages

setup(
    name='Math',
    version='0.0.1',
    description='Deep Library of mathematical operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aarav Rastogi, Arjun Dev Jha',
    author_email='arjundevjha111@gmail.com, aarav.rastogi24@gmail.com',
    packages=find_packages(),
    install_requires=[
        "pytest"
    ],
    license='MIT',
    python_requires='>=3.7',

)
