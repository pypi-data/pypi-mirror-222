import setuptools

setuptools.setup(
    name="thinkPass",
    version="1.0.0",
    author="Anant Chaudhary",
    description="password generator package",
    long_description="A package for generating passwords.",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={'thinkPass': ['data/*.csv']},  # Correct the package_data key
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add any dependencies here
    ]
)


