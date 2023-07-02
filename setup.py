from setuptools import setup, find_packages

def readme():
	with open('README.md') as f:
		return f.read()

setup(
	long_description=readme(),
	long_description_content_type='text/markdown',
)