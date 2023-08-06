import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="patent-gpt",
    version="0.0.11",
    author="Zackriya Solutions",
    author_email="sujith@zackriya.com",
    description="A package created to make patent search easier using latest LLM tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zackriya-Solutions/patent-gpt",
    project_urls={
        "Bug Tracker": "https://github.com/Zackriya-Solutions/patent-gpt/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src/patent-gpt"},
    packages=setuptools.find_packages(where="qpi"),
    python_requires=">=3.6",
)