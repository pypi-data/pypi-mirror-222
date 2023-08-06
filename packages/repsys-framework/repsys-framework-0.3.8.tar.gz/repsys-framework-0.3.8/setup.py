import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="repsys-framework",
    version="0.3.8",
    author="Jan Safarik",
    author_email="safarj10@fit.cvut.cz",
    description="Framework for developing and analyzing recommender systems.",
    url="https://github.com/cowjen01/repsys",
    long_description=long_description,
    include_package_data=True,
    long_description_content_type="text/markdown",
    packages=["repsys"],
    license="GPLv3",
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "repsys=repsys.__main__:main",
        ],
    },
    install_requires=[
        "click==8.0.4",
        "sanic==21.9.3",
        "coloredlogs==15.0.1",
        "numpy==1.21.5",
        "scipy==1.7.3",
        "pandas==1.3.5",
        "bidict==0.21.4",
        "scikit-learn==1.0.2",
        "umap-learn==0.5.3",
        "websockets==10.0"
    ],
    extras_require={
        "pymde": ["pymde==0.1.18", "pynndescent==0.5.8"],
    },
    zip_safe=False,
)
