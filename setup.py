from setuptools import setup, find_packages

setup(
    name="securop",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "securop": ["hooks/*", "scripts/*", "templates/*"],
    },
    install_requires=[
        "click",
        "pyyaml",
        "semgrep",
    ],
    entry_points={
        "console_scripts": [
            "securop=securop.cli:cli",
        ],
    },
)
