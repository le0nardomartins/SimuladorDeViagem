from setuptools import setup, find_packages

setup(
    name="simulador_viagem",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "PySide6>=6.9.0",
        "requests>=2.31.0",
    ],
) 