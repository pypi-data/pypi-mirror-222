from setuptools import setup, find_packages
from pathlib import Path

readme_content = """
# mcptbr


mcptbr é uma pequena biblioteca que permite o usuário a manipular blocos do Minecraft com python.

## Para quem serve?
Material criado para os alunos do curso de programação em python no Minecraft.

Observação: Versão em português de outras bibliotecas já existentes.



## Instalação
Vá ao CMD e digite 
```
pip install mcptbr.
```


## Exemplo de uso
```
from mcptbr.model import *


print(pegarPosicaoJogador())
```

"""

setup(
    name='mcptbr',
    version='0.2.5',
    packages=find_packages(),
    install_requires=[
        "mcpi", # Dependências necessárias para sua biblioteca (se houver).
    ],
    author='Lucas Pereira',
    author_email='lucasthe2@gmail.com',
    description='Biblioteca para manipular o Minecraft através do python.',
    long_description=readme_content,
    #long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type='text/markdown',
    #url='https://github.com/seu_usuario/minha_biblioteca',
    license='MIT',  # Substitua pela licença adequada.
)
