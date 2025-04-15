from setuptools import setup, find_packages

setup(
    name="pydmlaran",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["python-dotenv"],
    author="Daniel Lara",
    author_email="mat.daniel.lara@gmail.com",
    description="Funciones reutilizables para proyectos de análisis de datos",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tuusuario/mi_paquete",  # opcional
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.10",
)
