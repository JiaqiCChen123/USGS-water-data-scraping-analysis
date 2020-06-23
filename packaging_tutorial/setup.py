import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="USGSwaterinfo", # Replace with your own username
    version="0.0.1",
    author="Jiaqi Chen",
    author_email="jiaqichen321@gmail.com",
    description="This package is used for extracting water resource data from USGS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JiaqiCChen123/USGS-water-data-scraping-analysis",
    packages=['USGSwaterinfo'],
    include_package_data=True,
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)