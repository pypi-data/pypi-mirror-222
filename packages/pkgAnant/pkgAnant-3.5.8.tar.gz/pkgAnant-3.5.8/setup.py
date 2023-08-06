import setuptools
import os

# Get the version from the environment variable (RELEASE_VERSION) set by the GitHub Action workflow
version = os.getenv("RELEASE_VERSION", "3.5.8")  # Provide a default version if RELEASE_VERSION is not set

setuptools.setup(
    name="pkgAnant",
    version=version,
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
