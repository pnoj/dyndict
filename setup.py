import setuptools
import subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()

gitcommand = subprocess.run(["git", "describe", "--always", "--abbrev=0"], stdout=subprocess.PIPE, universal_newlines=True)
version = gitcommand.stdout.strip("\n")

setuptools.setup(
    name="dyndict",
    version=version,
    author="Paul (Kyunghan) Lee",
    author_email="contact@paullee.dev",
    description="Dynamic Dictionary Class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hillcrestpaul0719/dyndict",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.5',
)
