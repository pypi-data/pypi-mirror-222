from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()



setup(
    name="simpeval",
    version="0.1.0",
    description="Evaluation of text simplification with TUPA and SAMSA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.6",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    author="Fernando Alva-Manchego <feralvam@gmail.com>, Louis Martin <louismartincs@gmail.com>, Jessy Nierichlo <jessynchl@gmail.com>,",
    url="https://github.com/jessy3ric/git_memoire/tree/main/annotation_tool",
    packages=find_packages(exclude=["tests"]),
    test_suite="tests",
    entry_points={"console_scripts": ["simpeval = simpeval.cli:cli"]},
)
