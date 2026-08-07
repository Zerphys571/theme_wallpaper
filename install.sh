#!/usr/bin/env bash 

DEPENDENCIAS=("ffmpeg" "mpv" "awww" "mpvpaper" "libnotify")
ERROS=()


echo "====================================="
echo "  Instalador do Theme Wallpaper      "
echo "====================================="
echo "1) Instalação Completa (Dependências + Script)"
echo "2) Instalar apenas as dependências do sistema"
echo "3) Sair"
echo "====================================="


read -rp "Escolha uma opção [1-3]: " opcao

case $opcao in

	1)
		echo "Iniciando a instalação completa..."

		if git clone https://github.com/Zerphys571/theme_wallpaper.git; then

			cd theme_wallpaper && chmod +x theme_wallpaper.py
			ln -s "${PWD}/theme_wallpaper.py" ~/.local/bin/theme_wallpaper

			echo "Dependências que serão instaladas: ${DEPENDENCIAS[*]}"
			read -rp "Deseja instalar todos esses pacotes? [y/n]" escolha

			case $escolha in
				
				y)
					for i in "${DEPENDENCIAS[@]}"; do
						if sudo pacman -S "${i}" --noconfirm; then
							echo "Instalação concluída de: ${i}"

						elif yay -S "${i}" --noconfirm; then
							echo "Instalação concluída de: ${i}"

						else
							echo "Erro na instalação de: ${i}"
							ERROS+=("${i}")
						fi
					done
			
					if [ ${#ERROS[@]} -eq 0 ]; then
						echo "Todas as dependencias instaladas com sucesso: ${DEPENDENCIAS[*]}"
					else
						echo "Erro na instalação das dependências: ${ERROS[*]}"
					fi
					;;
				n)
					echo "Abortando instalação das dependências... Saindo do instalador!"
					exit 0
					;;
				*)
					echo "Opção inválida! Execute o script novamente."
					;;
			esac
		else
			echo "Erro ao clonar repositório abortando instalação!"
			exit 1
		fi
		;;
	2)
		echo "Instalando dependências ${DEPENDENCIAS[*]}"
		read -rp "Deseja instalar todos esses pacotes? [y/n]" escolha

		case $escolha in

			y)
				for i in "${DEPENDENCIAS[@]}"; do
					if sudo pacman -S "${i}" --noconfirm; then
			
						echo "Instalação concluída de: ${i}"

					elif yay -S "${i}" --noconfirm; then

						echo "Instalação concluída de: ${i}"

					else
						echo "Erro na instalação de: ${i}"
						ERROS+=("${i}")

					fi
				done

				if [ "${#ERROS[@]}" -eq 0 ]; then
					echo "Todas as dependencias instaladas com sucesso: ${DEPENDENCIAS[*]}"
				else
					echo "Erro na instalação das dependências: ${ERROS[*]}"
				fi
				;;
			n)
				echo "Abortando instalação das dependências... Saindo do instalador!"
				exit 0
				;;
			*)
				echo "Opção inválida! Execute o script novamente."
				exit 1
				;;
			esac
		;;
	3)
		echo "Saindo do instalador!"
		exit 0
		;;
	*)
		echo "Opção inválida! Execute o script novamente."
		;;
esac