import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.3',
    author='Mike Huls',
    author_email='mike_huls@hotmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jssuriyakumar/tools',
    project_urls = {
        "Bug Tracker": "https://github.com/jssuriyakumar/tools/issues"
    },
    license='MIT',
    packages=['tools'],
    install_requires=['requests'],
)
