from pathlib import Path
from setuptools import setup

# The directory containing this file
HERE = Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="FindMyIP",
    version="1.2.0",
    scripts=["FindMyIP.py"],
    description="Find your IP address (both internal and external) or check your connection state.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Mehran-Seifalinia/FindMyIP",
    author="Mehran Seifalinia",
    author_email="mehran.seifalinia@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)