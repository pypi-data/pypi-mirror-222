from setuptools import setup, find_packages

setup(
    name='gfx_perps_sdk',
    version='0.2.1',
    description='Your SDK description',
    long_description='Long description of your SDK',
    author='Arvind Krishnan',
    author_email='arvind98krishnan@gmail.com',
    url='https://github.com/GooseFX1/gfx-perps-python-sdk',
    packages=find_packages(),
    install_requires=[
        # List the dependencies of your SDK here
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