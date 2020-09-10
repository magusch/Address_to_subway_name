import setuptools


with open("requirements.txt") as fp:
    install_requires = fp.read().splitlines()

setuptools.setup(
    name="find_metro",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    include_package_data=True,
)
