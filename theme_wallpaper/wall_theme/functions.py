import subprocess
from pathlib import Path
from datetime import datetime
from random import choice
from wall_theme.config import TRANS_TYPE, TRANS_DURATION, FPS, STEP, ANGULOS_POSSIVEIS
from wall_theme.config import ARQ_LOG, EXT_IMAGEM, EXT_VIDEO, THUMB_NOTIFY, ARQ_FRAMEVIDEO
from wall_theme.config import LISTA_WALLPAPER

def criar_log(mensagem: str, arquivo_erro: str | Path | None) -> None:
  with open(ARQ_LOG, "a") as arquivo:
    data = datetime.now().strftime('%H:%M:%S')
    if arquivo_erro is not None:
      arquivo.write(f"[{data}] {mensagem}: {arquivo_erro}\n")
    else:
      arquivo.write(f"[{data}] {mensagem}\n")
      
def notify_send(arquivo: str | Path, status: str, mensagem: str) -> None:
  if arquivo is not None:
    comando_thumb = [
      "ffmpeg",
      "-i", arquivo,
      "-vf", "scale=76:-1",
      "-y", THUMB_NOTIFY
    ]
    subprocess.run(comando_thumb)

    comando_notify = [
      "notify-send",
      "-i", THUMB_NOTIFY,
      "-u", status,
      mensagem
    ]
    subprocess.run(comando_notify)
  else:
    comando_notify = [
      "notify-send",
      "-u", status,
      mensagem
    ]
    subprocess.run(comando_notify)

def aplicar_imagem(arquivo: str | Path)  -> None:
  lista_awww = [
    "awww",
    "img", arquivo,
    "--transition-type", TRANS_TYPE,
    "--transition-fps", FPS,
    "--transition-step", STEP,
    "--transition-duration", TRANS_DURATION,
    "--transition-angle", choice(ANGULOS_POSSIVEIS)
  ]

  aplicar = subprocess.run(lista_awww)

  if aplicar.returncode == 0:
    notify_send(arquivo, "low", "Trocando wallpaper")
    criar_log("Sucesso (Imagem)", arquivo)
  else:
    criar_log("Erro ao aplicar wallpaper", arquivo)
    exit(1)

def aplicar_video(arquivo: Path) -> None:
  mpvpaper = [
    "mpvpaper",
    "-o", 
    "hwdec=auto no-audio profile=fast framedrop=vo --vf=fade=t=in:st=0:d=1 loop",
    "*", arquivo,
  ]

  subprocess.Popen(mpvpaper, start_new_session=True)
  criar_log("Sucesso (Vídeo)", arquivo)


  comando_frame = [
      "ffmpeg",
      "-i", arquivo, 
      "-vframes",
      "1",
      "-q:v", "2",
      "-y", ARQ_FRAMEVIDEO
  ]

  resultado = subprocess.run(comando_frame)

  if resultado.returncode == 0:
    notify_send(ARQ_FRAMEVIDEO, "low", "Trocando wallpaper")
  else:
    criar_log("Erro ao criar miniatura do video", arquivo)
    exit(1)

def verificar_pastas():
  todos_arquivos = []
  try:
    for item in LISTA_WALLPAPER:
      for arquivo in item.iterdir():
        if arquivo.suffix.lower() in (EXT_VIDEO + EXT_IMAGEM):
          todos_arquivos.append(arquivo)
        else:
          continue
    if not todos_arquivos:
      criar_log(f"Erro, nenhum arquivo dentro da pasta!", None)
    else:
      verificar_formato(choice(todos_arquivos))
  except Exception as error:
    criar_log(f"Erro: {error}", None)

def verificar_formato(arquivo: str | Path) -> None:
  try:
    arquivo = Path(arquivo)
    if  arquivo.is_file():

      subprocess.run(["pkill", "mpvpaper"])

      if arquivo.suffix.lower() in EXT_IMAGEM:
        aplicar_imagem(arquivo)

      elif arquivo.suffix.lower() in EXT_VIDEO:
        aplicar_video(arquivo)

      else:
        criar_log("Erro formato de arquivo não suportado", arquivo)
        exit(1)
    else:
      criar_log("Erro, arquivo não existe", arquivo)
      exit(1)

  except Exception as e:
    criar_log(f"Erro: {e} > {arquivo}")
    exit(1)
