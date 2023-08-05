from setuptools import setup, find_packages

setup(
    name='ANALITools',
    version='0.1',
    author='NEVNORME',
    author_email='dev.nevermore696@gmail.com',
    description='Tools for The Open Network',
    packages=find_packages(),
    install_requires=[
        'asyncio',
        'aiohttp',
        'tonconnect',
        'dedust',
        'tontools',
        'xjet'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)