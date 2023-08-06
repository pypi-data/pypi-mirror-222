from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="xavier-themes",
    version="0.0.6",
    license="MIT",
    description="Library Python Beautiful Text And Panel In Terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Fall Xavier",
    author_email="falahfajrul802@gmail.com",
    url="https://github.com/Fall-Xavier/xavier",
    download_url="https://github.com/Fall-Xavier/xavier/archive/xavier.tar.gz",
    keywords=["rich", "module rich", "xavier", "module xavier"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
)
