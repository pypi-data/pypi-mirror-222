
from setuptools import setup, find_packages

setup(
    name='passwordless-client',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Matthew Fiallos',
    author_email='matthew.fiallos@randstadusa.com',
    description='A client library for Passwordless.dev API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/passwordless-client',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
