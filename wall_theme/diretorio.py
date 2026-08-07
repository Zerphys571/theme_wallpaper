from wall_theme.config import LISTA_DIR, LISTA_DEPEN
from shutil import which
from wall_theme.functions import criar_log

def verificar_diretorios() -> None:
  for i in LISTA_DIR:
    i.mkdir(parents=True, exist_ok=True)

def verificar_dependencia() -> None:
  for i in LISTA_DEPEN:
    if not which(i):
      criar_log("Erro: falta de dependencia", i)
      exit(1)