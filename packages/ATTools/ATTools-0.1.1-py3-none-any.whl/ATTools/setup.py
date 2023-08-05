from setuptools import setup, find_packages

setup(
    name='ATTools',
    version='0.1.1',
    author='NEVNORME',
    author_email='dev.nevermore696@gmail.com',
    description='Tools for The Open Network',
    #packages=find_packages(),
    packages=['ATTools'],
    install_requires=[
        'asyncio',
        'aiohttp',
        'tonconnect',
        'dedust',
        'tontools',
        'xjet'
    ],
    python_requires='>=3.6'
)