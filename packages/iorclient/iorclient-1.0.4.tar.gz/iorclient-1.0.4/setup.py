import setuptools

with open("README.MD", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="iorclient",
  version="1.0.4",
  author="Jie Guan",
  author_email="jguanisme@163.com",
  description="ior client sdk for ior standard",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/tzspace-ior/iorclient",
  packages=setuptools.find_packages(),
  include_package_data=True,
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)