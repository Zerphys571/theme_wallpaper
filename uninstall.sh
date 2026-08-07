#!/usr/bin/env bash 
DEPENDENCIAS=("ffmpeg" "mpv" "awww" "mpvpaper" "libnotify")

echo "====================================="
echo "  DESINSTALADOR DE THEME WALLPAPER   "
echo "====================================="

echo "Dependências a serem removidas: ${DEPENDENCIAS[*]}"
read -rp "Desinstalar todos as dependências e arquivos baixados: [y/n]" opcao

case $opcao in

	y)
		ERROS=()

		for i in "${DEPENDENCIAS[@]}"; do

			if sudo pacman -Rns "${i}" --noconfirm; then
				echo "Remoção concluida de: ${i}"
			elif yay -Rns "${i}" --noconfirm; then
				echo "Remoção concluida de: ${i}"
			else
				echo "Erro ao remover: ${i}"
				ERROS+=("${i}")
			fi
		done
		if [ ${#ERROS[@]} -eq 0 ]; then
			echo "Dependencias removidas: ${DEPENDENCIAS[*]}"
		else
			echo "Erro ao remover as dependências: ${ERROS[*]}"
		fi

		if [ -L "${HOME}/.local/bin/theme_wallpaper" ]; then

			COD_DIR=$(dirname "$(readlink -f ~/.local/bin/theme_wallpaper)")
			if [ "$(basename "${COD_DIR}")" == "theme_wallpaper" ]; then
				rm ~/.local/bin/theme_wallpaper && rm -rf "${HOME}/.logs/" && rm -rf "${COD_DIR}"
			else
				echo "Erro: A pasta do script não se chama 'theme_wallpaper'. Remoção abortada por segurança."
				exit 1
			fi
		else
			echo "Erro ao remover os arquivos instalados"
			exit 1
		fi

		echo "Fim da execução do desinstalador"
		exit 0
	;;

	n)
		echo "Saindo do desinstalador!"
		exit 0
	;;

	*)
		echo "Opção inválida, execute novamente o script!"
		exit 1
	;;
esac

