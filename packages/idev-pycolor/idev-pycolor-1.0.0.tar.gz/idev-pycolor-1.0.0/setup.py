import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "idev-pycolor",
    version = "1.0.0",
    author = "IrtsaDevelopment",
    author_email = "irtsa.development@gmail.com",
    description = "A python collection of classes and functions to convert between rgb, hsv, hsl, xyz, ycc, cmyk, and hex color formats and generate palettes from said colors.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/IrtsaDevelopment/PyColor",
    project_urls = {
        "Bug Tracker": "https://github.com/IrtsaDevelopment/PyColor/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "idev-pycolor"},
    packages=["PyColor"],
    python_requires = ">=3.6"
)