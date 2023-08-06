from setuptools import setup, find_packages

setup(
    name='local_llm_cli',
    version='0.1.0',
    description='Converse with GPT4 LLM locally',
    author='Harsh Avinash',
    author_email='harsh.avinash.official@gmail.com',
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
