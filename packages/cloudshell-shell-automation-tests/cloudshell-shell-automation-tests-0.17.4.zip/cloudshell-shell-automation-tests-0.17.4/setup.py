from setuptools import find_packages, setup


def get_file_content(file_path):
    with open(file_path) as fp:
        return fp.read()


setup(
    name="cloudshell-shell-automation-tests",
    url="http://www.qualisystem.com/",
    author_email="info@qualisystems.com",
    packages=find_packages(),
    install_requires=get_file_content("requirements.txt"),
    version=get_file_content("version.txt").strip(),
    description="QualiSystems automation tests for Shells",
    long_description="QualiSystems automation tests for Shells",
    long_description_content_type="text/x-rst",
    include_package_data=True,
    python_requires="~=3.10",
    entry_points={
        "console_scripts": ["cloudshell-shell-automation-tests = shell_tests.cli:cli"]
    },
)
