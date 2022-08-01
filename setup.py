import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pulley_analytical_solutions",
    version="0.0.1",
    description="Analytical solutions for GT-2 and GT-3 pulley tooth profiles.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trilobio/pulley_analytical_solutions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'sympy',
    ],
    python_requires='>=3.8',
)
