from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in libery_management/__init__.py
from libery_management import __version__ as version

setup(
	name="libery_management",
	version=version,
	description="libery management system",
	author="Ezra Bernard",
	author_email="bernardezra112@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
