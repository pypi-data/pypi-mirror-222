from setuptools import setup

setup(
    name='bake',
    entry_points={
        'console_scripts': [
            'bake = bake:main',
        ],
    }
)