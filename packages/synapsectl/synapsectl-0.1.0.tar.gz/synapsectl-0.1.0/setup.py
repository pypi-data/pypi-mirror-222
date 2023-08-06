from setuptools import setup

setup(
    name='synapsectl',
    version='0.1.0',
    packages=['synapsectl'],
    url='https://git.sr.ht/~martijnbraam/synapsectl',
    license='GPL3',
    author='Martijn Braam',
    author_email='martijn@brixit.nl',
    description='A more convenient way to run matrix-synapse admin commands',
    entry_points={
        'console_scripts': [
            'synapsectl=synapsectl.__main__:main'
        ]
    }
)