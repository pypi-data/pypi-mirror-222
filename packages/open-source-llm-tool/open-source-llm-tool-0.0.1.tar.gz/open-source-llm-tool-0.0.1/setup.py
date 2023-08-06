import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="open-source-llm-tool",
    version="0.0.1",
    author="Matthew DeGuzman",
    author_email="t-madeguzman@microsoft.com",
    description="Package to use Foundation Models in Prompt Flow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    entry_points={"package_tools": ["open_source_llm = open_source_llm.tools.utils:list_package_tools"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
