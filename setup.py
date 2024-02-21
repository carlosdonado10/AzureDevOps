from setuptools import setup, find_packages


def main():
    """
    Uses setuptools to build the python library based on python code and handles the installation of requirements
    from a requirements.txt file.
    :return:
    """
    with open("requirements.txt", "r") as f:
        requirements = f.read().splitlines()

    setup(
        name="AzureDevopsInterface",
        version="0.0.1",
        description="Interface to connect to the Azure DevOps API",
        author="Carlos Donado",
        install_requires=requirements,
        packages=find_packages(),
    )


if __name__ == "__main__":
    main()
