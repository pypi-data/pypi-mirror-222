import setuptools
import pycur

setuptools.setup(
	name="pycur",
	version=pycur.__version__,
	author="RixTheTyrunt",
	author_email="rixthetyrunt@gmail.com",
	description="Modifying cursors is now easier than ever!",
	packages=["pycur"],
	python_requires=">=3",
	long_description=open("../README.md").read(),
	long_description_content_type="text/markdown"
)