from setuptools import setup, find_packages

setup(
    name="sallu_bhai",
    version="0.1.3",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sallu-bhai=sallu_bhai.cli_tool:main"
        ]
    },
    install_requires=[
        "ollama>=0.1.0",  # Add required dependencies here
    ],
)
