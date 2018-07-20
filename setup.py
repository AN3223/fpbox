from setuptools import setup, find_packages

setup(
    name='fpbox',
    version='0.5.0',
    description='A toolbox for functional programming in Python',
    url='https://github.com/AN3223/fpbox',
    author='AN3223',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['build', 'doc', 'dist', 'contrib', 'docs'])
)
