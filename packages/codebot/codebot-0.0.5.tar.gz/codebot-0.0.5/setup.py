from setuptools import setup, find_packages

setup(
    name="codebot",
    version="0.0.5",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "codebot = src:main",
        ],
    },
    install_requires=[
        "chainlit==0.5.2",
        "loguru==0.5.3",
        "tiktoken==0.4.0",
        "prompt_toolkit==3.0.39",
        "jupyter",
        "mysql-connector-python",
        "pillow",
        "pyngrok"
    ],
    include_package_data=True,  # Add this line
)
