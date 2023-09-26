import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="procoder",
    version="0.0.1",
    author="Honghua Dong, Yangjun Ruan",
    author_email="honghuad@cs.toronto.edu, yjruan@cs.toronto.edu",
    description="A package for writing prompts in a coding style.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dhh1995/PromptCoder",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
