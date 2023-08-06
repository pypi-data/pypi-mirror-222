import setuptools
from pathlib import Path

this_directory   = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
  name="blin",
  version="0.1.4",
  author="lemeni.com",
  description="Python client library for Blin API (natural language to API service)",
  long_description=long_description,
  long_description_content_type='text/markdown',
  packages=["blin"]
  )