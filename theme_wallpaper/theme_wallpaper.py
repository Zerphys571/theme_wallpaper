#!/usr/bin/env python3

import argparse
from wall_theme.diretorio import verificar_dependencia, verificar_diretorios
from wall_theme.functions import verificar_formato, criar_log, verificar_pastas


def app() -> None:
  verificar_diretorios()
  verificar_dependencia()
  

  parser = argparse.ArgumentParser(
    prog="theme_wallpaper",
    description="Define fundos de papel de parede"
  )

  parser.add_argument("target", nargs="?")
  parser.add_argument("-r", "--random", action="store_true")


  args = parser.parse_args()

  if args.random:
    verificar_pastas()
  elif args.target:
    verificar_formato(args.target)
  else:
    criar_log(f"Erro: nenhum arquivo alvo encontrado > {args.target}")
    exit(1)

if __name__ == "__main__":
  app()