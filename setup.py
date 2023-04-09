from setuptools import setup, find_packages


with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='bolt-scanner',
    packages=find_packages(exclude="tests"),
    license="MIT",
    version='0.8.5',
    description='Offensive Security Tool for Reconnaissance and Information Gathering',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Evyatar Meged',
    author_email='evyatarmeged@gmail.com',
    url='https://github.com/prath-10',
    install_requires=['beautifulsoup4',
                      'requests',
                      'dnspython',
                      "lxml",
                      "click",
                      "fake-useragent",
                      "requests[socks]",
                      "xmltodict"],
    package_data={
        "bolt_src": [
            "wordlists/*"
        ]
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bolt=bolt_src.main:main'
        ]
    },
)
