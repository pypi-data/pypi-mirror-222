from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='local_llm_cli',
    version='0.1.3',
    description='Converse with GPT4 LLM locally',
    author='Harsh Avinash',
    author_email='harsh.avinash.official@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "langchain",
        "python-dotenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
