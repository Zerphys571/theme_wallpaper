# Theme Wallpaper

Este projeto é um trocador de planos de fundo(Imagens/videos) para o sistema

## Pré-requisitos

Este projeto foi construído para Linux e não necessita de instalação de dependências no python, pois utiliza as bibliotecas nativas. No entanto, você precisa garantir que as seguintes ferramentas do sistema estejam instaladas (via `pacman`, `apt`, etc.):

* `mpvpaper`
* `awww`
* `libnotify`
* `ffmpeg`

## Compatibilidade
* Para sistemas baseados em Arch pode-se utilizar o script automatizado para instalação, para outras distribuições é recomendado fazer a instalação das dependências separadamente e ir direto para a seção de instalação manual.

## Instalação Automática

Para instalar todos os arquivos e dependências utilize o script automatico:
* `install.sh`

Dê permissão de execução ao script automatizado:
* `chmod +x install.sh`

Para executar utilize:
* `./install.sh`

## Desinstalação Automática

Para remover todos as dependências utilizadas e os arquivos instalados exceto as pastas de wallpapers utilize o script:
* `uninstall.sh`

Dê permissão de execução ao script automatizado:
* `chmod +x uninstall.sh`

Para executar utilize:
* `./uninstall.sh`


## Instalação Manual

Para clonar os arquivos necessários para seu sistema utilize:

* `git clone https://github.com/Zerphys571/theme_wallpaper.git`

Acesse a pasta clonada:
* `cd theme_wallpaper`

Conceda permissão de execução para o arquivo theme_wallpaper.py:
* `chmod +x theme_wallpaper.py`

Para utilizar de qualquer lugar mova ou copie arquivo theme_wallpaper.py para uma pasta com seus scripts no sistema:
* Copiar: `cp theme_wallpaper.py ~/.local/bin/theme_wallpaper` 
* Mover: `mv theme_wallpaper.py ~/.local/bin/theme_wallpaper`

## Diretorios

O programa verifica automaticamente os diretorios, caso não estejam serão criados:

* `~/Imagens/Wallpapers`
* `~/Imagens/videos`
* `~/.logs`

## Como Usar

Para saber todas as flags utilize:
* `theme_wallpaper --help`

Para aplicar um wallpaper chame o arquivo theme_wallpaper com o caminho da imagem ou video
* `theme_wallpaper caminho_imagem`

Para aplicar um wallpaper aleatório de dentro das pasta de videos ou wallpapers utilize:
* `theme_wallpaper -r` ou `theme_wallpaper --random`

## Agradecimento
* `Se você chegou até aqui, agradeço por ter lido esse pequeno projeto pessoal, sinta-se a vontade para alterar qualquer implementação e funcionalidade, e descobrir bugs`

## Autor
* `Luis Guilherme/Zerphys`
