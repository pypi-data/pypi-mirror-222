from setuptools import setup, find_packages
import pypandoc

# Convert README.md to reStructuredText format
with open("README.md", "r", encoding="utf-8") as f:
    long_description = pypandoc.convert_text(f.read(), "rst", format="md")

setup(
    name="assamer",
    version="1.3.7",
    author="Veysel KANTARCILAR",
    author_email="kantrveysel@gmail.com",
    description="ASAP2 (A2L) and ASSAM Library",
    packages=find_packages(),
    py_modules=["A2L", "hexa2l", "ASSAM", "TrackA2L"],
    install_requires=[
        "intelhex",
        "numpy",
    ],
    long_description=long_description,
    package_data={
        "": ["README.md"],
    },
)
