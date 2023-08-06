from setuptools import setup, find_packages

setup(
    name="pythonGPT",
    version="0.7",
    packages=find_packages(),
    install_requires=[
        "IPython",
        "requests"
    ]
)
