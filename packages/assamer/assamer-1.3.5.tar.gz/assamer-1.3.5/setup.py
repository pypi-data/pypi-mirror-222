from setuptools import setup, find_packages

setup(
    name="assamer",
    version="1.3.5",
    author="Veysel KANTARCILAR",
    author_email="kantrveysel@gmail.com",
    description="ASAP2 (A2L) and ASSAM Library",
    packages=find_packages(),
    py_modules=["A2L", "hexa2l", "ASSAM", "TrackA2L"],
    install_requires=[
        "intelhex",
        "numpy",
    ],
    package_data={
        "": ["README.md"],
    },
)
