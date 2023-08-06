from setuptools import setup, find_packages

install_requires = ['rdkit', 'networkx']

setup(
    name='UniDockTools',
    version='1.0.3',
    author='DP BayMax',
    description="UniDock, a GPU-accelerated molecular docking program developed by DP Technology",
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    #scripts=['UniDock/bin/unidock'],
    package_data={
        "UniDock": ["data"],
    },
    entry_points={
        'console_scripts': [
            'Unidock = UniDock.unidock:main',
        ],
    },
)
