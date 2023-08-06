from setuptools import setup, find_packages

setup(
    name = "sheCry",

    version = "0.0.9",
    
    author = "Tahsin Ahmed",

    description = "SHE Cryptography is architectured by Tahsin Ahmed.",

    long_description = open("README.md", encoding="utf-8").read(),
    
    keywords = ["cryptography", "encryption", "decryption", "SHE", "SHE cryptography", "Symmetric Hybrid Encryption", "Symmetric Hybrid Encryption cryptography", "sheCry"],
    
    url = "",
    
    install_requires = [""],
    
    packages = find_packages(),

    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Natural Language :: English"
    ]
)