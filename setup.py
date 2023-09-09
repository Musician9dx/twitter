import setuptools

__version__ = "0.0.0"
REPO_NAME = "twitter"
AUTHOR_USER_NAME = "Musician9dx"
SRC_REPO = "twitter"
AUTHOR_EMAIL = "musician9dx@gmail.com"

setuptools.setup(
    name="twitter",
    version=__version__,
    author="Musician9dx",
    author_email="musician9dx@gmail.com",
    description="nops performed",
    url="https://github.com/Musician9dx/twitter",
    project_urls={
        "Bug Tracker": "https://github.com/Musician9dx/twitter" + "/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
