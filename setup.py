import setuptools
import prescient

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prescient",
    version=prescient.__version__,
    author="Sachit Saksena; Grace Hui-Ting Yeo",
    author_email="sachit@mit.edu",
    license="MIT License",
    description="Method for simulating single cells using longitudinal scRNA-seq.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gifford-lab/prescient",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3"
    ],
    include_package_data=True,
    install_requires=[
        "matplotlib>=3.1",
        "numpy>=1.14",
        "pandas>=0.25",
        "scikit-learn>=0.21",
        "scipy>=1.3",
        "setuptools>=41.6",
        "torch>=1.5",
        "torchvision>=1.5",
        "geomloss==0.2.3",
        "pykeops>=1.3"
    ],
    python_requires=">=3.4",
    entry_points={
        "console_scripts": ["prescient=prescient.__main__:main"]
    }
)
