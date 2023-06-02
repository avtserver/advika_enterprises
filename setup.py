from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in advika_enterprises/__init__.py
from advika_enterprises import __version__ as version

setup(
	name="advika_enterprises",
	version=version,
	description="This app will mannaged all Enterprises workflow with supplier or vendor",
	author="MD Faiyaz Ansari",
	author_email="faiyaz@avtutoring.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
