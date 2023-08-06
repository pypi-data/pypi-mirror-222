import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("Version.txt", "r") as fh:
    version = fh.read()

setuptools.setup(
    name="jutool.spider_util",
    version=version,
    author="Ke",
    author_email="jiangke1207@icloud.com",
    description="Some base methods for get web data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.example.com/~cschultz/bvote/",
    packages=setuptools.find_packages(),
    install_requires=['jutool==' + version, 'selenium==4.5.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
