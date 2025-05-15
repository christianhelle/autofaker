import os
import setuptools

# Get the absolute path to the directory containing this file (setup.py)
here = os.path.abspath(os.path.dirname(__file__))

# Path to the documentation file
readme_path = os.path.join(here, "docs", "pypi.md")

# Try to read the long description from docs/pypi.md, but fall back to a basic description if not available
try:
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "Python library designed to minimize the setup/arrange phase of your unit tests"

setuptools.setup(
    name="autofaker",
    version="0.1.0",
    url="https://github.com/christianhelle/autofaker",
    license="MIT License",
    license_files=["LICENSE"],
    author="Christian Helle",
    author_email="christian.helle@outlook.com",
    description="Python library designed to minimize the setup/arrange phase of your unit tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=["pandas", "faker", "typing_inspect"],
)
