from setuptools import setup, find_packages

setup(
    name='ecoindex-journey-scrapper',
    version='1.0.0',
    packages=find_packages(),
    description='Calcul du lecoindex du un parcours',
    author='Orange Inovation',
    install_requires=[
        "python>=3.10",
        "ecoindex>=5.4.2",
        "undetected-chromedriver==3.5.0",
        "Pillow>=9.2.0",
        "selenium==4.9",
        "jinja2>=3.1.0"
    ],
)
