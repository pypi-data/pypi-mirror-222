from setuptools import setup, find_packages


with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name="Local_Xampp_Apache",
    version="0.0.3",
    author="Sridhar",
    author_email="sridhardscv@gmail.com",
    description="Access the Windows XamPP Apache Server via Command lines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.selfmade.ninja/SRIDHARDSCV/automate_xampp_windows",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=required_packages,
    entry_points={
        "console_scripts": [
            "My_Apache = src.main:main"
        ]
    }
)
