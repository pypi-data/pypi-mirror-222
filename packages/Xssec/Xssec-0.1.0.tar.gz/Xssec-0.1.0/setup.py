from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Xssec",
    version="0.1.0",
    author="Xssoft",
    author_email="xssoft2022@gmail.com",
    description="一个可以加密文本的库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/Xssec",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
