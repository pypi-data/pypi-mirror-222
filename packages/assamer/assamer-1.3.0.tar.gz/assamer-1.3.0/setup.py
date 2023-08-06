from setuptools import setup, find_packages

setup(
    name="assamer",
    version="1.3.0",
    author="Veysel KANTARCILAR",
    author_email="kantrveysel@gmail.com",
    description="ASAP2 (A2L) and ASSAM Library",
    packages=find_packages(),
    py_modules=["A2L", "hexa2l", "ASSAM"],
    install_requires=[
        "intelhex",
        "numpy",
    ],
)
