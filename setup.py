"""
Setup configuration for Key-To-Productivity application
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="key-to-productivity",
    version="1.0.0",
    author="KamUnfazed",
    description="A productivity enhancement application with AI-driven daily routine optimization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KamUnfazed/Key-To-Productivity",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business :: Scheduling",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "python-dateutil>=2.8.2",
    ],
    entry_points={
        "console_scripts": [
            "key-to-productivity=main:main",
        ],
    },
)
