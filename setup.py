from setuptools import setup, find_packages

setup(name="test_ext",
      version="0.0.1",
      description="Test_ext python EF2 extension",
      author="Dynatrace",
      packages=find_packages(),
      python_requires=">=3.10",
      include_package_data=True,
      install_requires=["dt-extensions-sdk"],
      extras_require={"dev": ["dt-extensions-sdk[cli]"]},
      )
