from setuptools import setup, find_packages

setup(
    name='SliceCommander',
    version='0.1',
    description='FABRIC Slice Commander',
    url='https://github.com/fabric-testbed/slice-commander',
    author='Ezra Kissel',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    keywords='fabric slice command',

    packages=find_packages(),

    install_requires=['ptyprocess', 'libtmux', 'pygments', 'docopt'],

    entry_points = {
        'console_scripts': [
            'slice-commander = commander.cli:main',
        ]
    }
)
