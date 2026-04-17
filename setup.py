from setuptools import setup, find_packages

setup(
    name="python-automation-toolkit",
    version="1.0.0",
    author="Jonathan Zhang",
    description="Python tools for automation",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "beautifulsoup4>=4.11.0",
        "selenium>=4.0.0",
        "pandas>=1.5.0",
        "openpyxl>=3.0.0",
    ],
    python_requires=">=3.8",
)