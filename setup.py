import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fst", # Replace with your own username
    version="0.0.0",
    author="Rishabh Bhatnagar",
    author_email="bhatnagarrishabh4@gmail.com",
    description=long_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RishabhBhatnagar/fst",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

