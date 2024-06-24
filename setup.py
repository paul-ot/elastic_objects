from setuptools import setup, find_packages

setup(
    name="liquidpy",
    version="0.1.1",
    author="Paul Marclay",
    author_email="paul.eduardo.marclay@gmail.com",
    description="LiquidPy introduces the concept of 'liquid objects' in Python - a flexible approach to object-oriented programming.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/paul-ot/liquidpy",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
)