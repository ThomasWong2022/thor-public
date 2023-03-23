import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thorml",
    author="Thomas Wong",
    author_email="mw4315@ic.ac.uk",
    description="AutoML tools for Tabular Datasets",
    keywords="autoML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThomasWong2022/thor-public",
    project_urls={
        "Documentation": "https://github.com/ThomasWong2022/thor-public",
        "Bug Reports": "https://github.com/ThomasWong2022/thor-public/issues",
        "Source Code": "https://github.com/ThomasWong2022/thor-public",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        # see https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    # install_requires=['Pillow'],
    extras_require={
        "dev": ["check-manifest"],
    },
)
