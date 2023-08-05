import setuptools

setuptools.setup(
    name="passwordP",                     # This is the name of the package
    version="1.1.7.7",                        # The initial release version
    author="Nipun dogra",                     # Full name of the author
    description="password generator package",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["quicksample"],             # Name of the python package
    install_requires=[]                     # Install other dependencies if any
)
