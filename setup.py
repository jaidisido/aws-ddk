import setuptools

with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="aws-ddk-core",
    version="0.1.2",
    description="DDK Core",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="author",
    package_dir={"": "aws_ddk_core"},
    packages=setuptools.find_packages(where="aws_ddk_core"),
    install_requires=open("requirements.txt").read().strip().split("\n"),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
