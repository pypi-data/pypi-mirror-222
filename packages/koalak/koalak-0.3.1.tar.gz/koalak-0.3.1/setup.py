import codecs
import os

from setuptools import find_packages, setup

# Functions/ global variables
HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("VERSION"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


# Metadata
NAME = "koalak"
VERSION = get_version("src/koalak/consts.py")
LICENSE = "MIT"
DESCRIPTION = "Framework manager, framework to create frameworks"
LONG_DESCRIPTION = read("README.md")
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"
URL = "https://github.com/nazime/" + NAME
PROJECT_URLS = {
    "Documentation": "https://" + NAME + ".readthedocs.org/",
    "Bug Tracker": URL + "/issues",
    "Source Code": URL,
}
AUTHOR = "Nazime LAKEHAL"
AUTHOR_EMAIL = "nazime.lkh@gmail.com"
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
KEYWORDS = []
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]

# Packages information
PACKAGES = find_packages(where="src")
PACKAGE_DIR = {"": "src"}
INSTALL_REQUIRES = [
    "sqlalchemy",
    "coloring",
    "attrs",
    "argcomplete",
    "toml",
    "black",
    "typeguard>=4",
    "rich",
    "devtools",
    # relationaldb
    "pymongo",
    "codeg",
    "jinja2",
    # for utils functions
    "openpyxl",
]
EXTRAS_REQUIRE = {
    "docs": ["sphinx", "sphinxcontrib.napoleon", "sphinx-book-theme"],
    "tests": [
        "coverage",
        "hypothesis",
        "pytest>=4.3.0",  # 4.3.0 dropped last use of `convert`
    ],
}
EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["docs"] + ["pre-commit"]
)

EXTRAS_REQUIRE["travis"] = EXTRAS_REQUIRE["dev"] + ["tox", "codecov"]
PYTHON_REQUIRES = ">=3.6"

ZIP_SAFE = False
ENTRY_POINTS = {}
INCLUDE_PACKAGE_DATA = True
PACKAGE_DATA = {"koala": ["data/*"]}

if __name__ == "__main__":
    setup(
        # Metadata
        name=NAME,
        version=VERSION,
        license=LICENSE,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
        url=URL,
        project_urls=PROJECT_URLS,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        # Package information
        packages=PACKAGES,
        package_dir=PACKAGE_DIR,
        install_requires=INSTALL_REQUIRES,
        python_requires=PYTHON_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        zip_safe=ZIP_SAFE,
        include_package_data=INCLUDE_PACKAGE_DATA,
        entry_points=ENTRY_POINTS,
        package_data=PACKAGE_DATA,
    )
