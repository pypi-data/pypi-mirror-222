from setuptools import setup, find_packages

setup(
    name='model-connect',
    version='0.0.1',
    packages=find_packages(
        include=[
            'model_connect',
            'model_connect.*'
        ],
        exclude=[
            'tests',
            'tests.*'
        ]
    ),
    install_requires=[
        'setuptools~=60.2.0',
    ]
)