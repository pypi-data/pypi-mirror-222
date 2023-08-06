from setuptools import setup, find_packages

install_requires = ['rdkit', 'networkx']

setup(
    name='UniDockTools',
    version='1.0.0',
    author='DP BayMax',
    url='https://github.com/UR-Free/UniDockTools',
    description="A tools used for preprossing and postprocessing of UniDock, a GPU-accelerated molecular docking program developed by DP Technology",
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    
    package_data={
        "UniDock": ["data"],
    },
    entry_points={
        'console_scripts': [
            'Unidock = UniDockTools.unidock:main',
        ],
    },
)
