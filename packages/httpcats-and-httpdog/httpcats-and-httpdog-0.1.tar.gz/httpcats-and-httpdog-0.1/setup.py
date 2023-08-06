from setuptools import setup

# 从README.md文件中读取长描述
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="httpcats-and-httpdog",
    version="0.1",
    author="cacaview",
    author_email="cacaview@foxmail.com",
    description="A simple httpcat and httpdog call function returns image data when called",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["httpcats_and_httpdog"],
    install_requires=["requests"],
    url="https://github.com/cacaview/http_cat",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
