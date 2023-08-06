from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='mcptbr',
    version='0.2.1',
    packages=find_packages(),
    install_requires=[
        "mcpi", # Dependências necessárias para sua biblioteca (se houver).
    ],
    author='Lucas Pereira',
    author_email='lucasthe2@gmail.com',
    description='Biblioteca para manipular o Minecraft através do python.',
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type='text/markdown',
    #url='https://github.com/seu_usuario/minha_biblioteca',
    license='MIT',  # Substitua pela licença adequada.
)
