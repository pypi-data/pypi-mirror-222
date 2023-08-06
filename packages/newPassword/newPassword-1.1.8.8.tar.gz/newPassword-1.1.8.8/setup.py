import setuptools
from version import __version__

setuptools.setup(
    name="newPassword",
    version=__version__,
    author="Nipun Dogra",
    description="Password generator package",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[]
)

