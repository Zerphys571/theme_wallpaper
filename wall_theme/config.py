from pathlib import Path

"""
Cria as variáveis para os diretórios principais
"""

DIR_HOME = Path.home()

DIR_TMP = Path("/tmp")

DIR_IMAGENS = DIR_HOME / "Imagens"

DIR_WALLPAPER = DIR_IMAGENS / "Wallpapers"

DIR_VIDEOS = DIR_IMAGENS / "videos"

DIR_LOGS = DIR_HOME / ".logs"

LISTA_DIR = [
  DIR_WALLPAPER,
  DIR_VIDEOS,
  DIR_LOGS
]

LISTA_WALLPAPER = [
  DIR_WALLPAPER,
  DIR_VIDEOS
]

"""
Cria os endereços para os arquivos
"""

ARQ_LOG = DIR_LOGS / "wallpaper.log"
THUMB_NOTIFY = DIR_TMP / "thumb.jpg"
ARQ_FRAMEVIDEO = DIR_TMP / "video_frame.jpg"

ARQS_TMP = [
  ARQ_LOG,
  THUMB_NOTIFY
]

"""
DEPENDENCIAS
"""
LISTA_DEPEN = [
	"mpvpaper",
  "ffmpeg",
	"awww",
  "libnotify"
]

"""
Cria as listas com as extensões dos arquivos permitidos
"""
EXT_IMAGEM = [
  ".jpeg",
	".png",
	".jpg",
	".gif"
]
EXT_VIDEO = [
  ".mp4",
	".webm",
	".mkv",
]

"""
Cria variáveis para os efeitos do awww e uma lista dos ângulos
"""
TRANS_TYPE = "wipe"
FPS = "60"
STEP = "90"
TRANS_DURATION = "3"
ANGULOS_POSSIVEIS = ['0', '45', '90', '135', '180', '225', '270', '315']