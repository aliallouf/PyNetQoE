from setuptools import setup, find_packages

setup(
    name="PyNetQoE",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas", "numpy", "scikit-learn", "imbalanced-learn", "joblib"
    ],
    author="Ali Allouf",
    description="Python Library for Network Quality of Experience (QoE) Analysis",
)   