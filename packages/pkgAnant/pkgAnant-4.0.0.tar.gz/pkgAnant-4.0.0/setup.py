import setuptools
from version import ver

setuptools.setup(
    name="pkgAnant",
    version=ver,
    author="Anant Chaudhary",
    description="password generator package",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["quicksample"],
    install_requires=[
        # Add any dependencies your package requires here
        # For example:
        # "numpy",
        # "requests",
    ]
)
