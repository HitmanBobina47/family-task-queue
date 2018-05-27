from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    dependencies = f.read().split("\n")

setup(
    name="family_task_queue",
    version="0.1.0a0",
    description="A webserver to give tasks to your family and optionally give incentives for completing them.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HitmanBobina47/family-task-queue",
    author="HitmanBobina47",
    author_email="hitmanbobina47@gmail.com",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Framework :: Flask",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6"
    ],
    keywords="",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=dependencies,
    project_urls={
        "Bug Reports": "https://github.com/HitmanBobina47/family-task-queue/issues",
        "Funding": "https://paypal.me/hitmanbobina47",
        "Source": "https://github.com/HitmanBobina47/family-task-queue"
    }
)
