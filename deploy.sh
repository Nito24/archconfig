#!/bin/sh


# Neofetch
#
# Base-devel (for Make)
# Git
# Yay
#
# Qtile 
#  - Qtile-extras (AUR)
#  - Picom
#
# Nitrogen
#  - Archlinux-wallpaper
# 
# Unclutter
# 
# Dunst
#
# Xbindkeysrc
# 
# Fonts
#  - CaskaydiaCove Nerd Font (https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/CascadiaCode.zip)
#
# Alacritty
#
# Dmenu (compile with patches)(https://github.com/Nito24/dmenu)(make install)
#
# Alsa
#  - Pulse-audio-mixer
#  - Pavucontrol
#  - Volumeicon
#
# Spotify
#  - Spicetify
#
# Zsh
#  - Ohmyzsh
# 
# Neovim pluggins
#
# Custom scripts (wget)
#
# Custom icons

LIST_OF_DEVEL_APPS="base-devel git make wget curl fakeroot p7zip neovim man htop" #git is not really needed since thats how you have suposedly downloaded the config. Same goes with nvim, it should already be installed
LIST_OF_APPS="neofetch xf86-video-vesa xorg xorg-server xorg-xinit qtile picom archlinux-wallpaper unclutter dunst brightnessctl alacritty firefox alsa-utils python-psutil pulseaudio pulseaudio-alsa volumeicon zsh lsd powerline-fonts"
LIST_OF_APPS_AUR="qtile-extras" # spotify spicetify-cli


echo -e "Nito's arch installation script, be sure to run this as a user (with home directory) and with sudo privileges.\nAlready working internet connection is needed for this script to work"
echo "Type [Y] to continue with the installation or [N] (or Crt + C) to cancel"
echo -n "> "


read -t 10 ans
if [[ $ans == 'Y' ]] || [[ $ans == 'y' ]]
then
	echo "Initializing install..."

	# Creating a temporal directory to place everything
	execpath=$(dirname -- "$(readlink -f "${BASH_SOURCE}")")
	mkdir $execpath"/tempnitoinstall"
	userhome="/home/"$USER
	temppath=$execpath"/tempnitoinstall"
	cd $temppath

	sudo pacman -Syy # Update pacman
	
	echo "Installing devel packages"
	sudo pacman -S $LIST_OF_DEVEL_APPS --needed --noconfirm

	echo "Installing normal packages"
	sudo pacman -S $LIST_OF_APPS --needed --noconfirm

	
	# Install YAY
	echo "Installing YAY AUR package manager"
	git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si

	echo "Installing AUR packages"
	yay -S $LIST_OF_APPS_AUR --needed --noconfirm
	
	# Install fonts
	cd $temppath
	mkdir font && cd font
	wget 'https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/CascadiaCode.zip'
	7z x CascadiaCode.zip
	mkdir -p $userhome"/.local/share/fonts"
	cp *.ttf $userhome"/.local/share/fonts"
	fc-cache -f -v


	# Install Dmenu
	cd $temppath
	git clone https://github.com/Nito24/dmenu
	cd dmenu
	sudo make install

	# Move and setup all the configs and extra scripts
	echo "Copying all configurations"
	cd $execpath
	
	rm -r .config/rofi # Deprecated with Dmenu
	rm -r .config/spicetify # Cant be installed automatically (at least I dont know how)

	cp -r .config $userhome
	cp -r .local $userhome
 	cd /
	sudo cp -r $execpath"/usr" / # Custom scripts
        sudo chmod +x /usr/local/bin/* 
 	cd $execpath
	cp .xbindkeysrc $userhome
	cp .xinitrc $userhome
	#cp .zshrc


 	# Stop the ANOYING BIOS BEEP
  	sudo echo blacklist pcspkr >> /etc/modprobe.d/blacklist.conf

 
	echo "Installation complete, you can now safely remove/delete this directory"
	#chsh $USER -s /bin/zsh # Set zsh as users terminal
	#wget --no-check-certificate http://install.ohmyz.sh -O - | sh (INSTALLER)
	
	#sudo chmod a+wr /opt/spotify # Gain persmison in spotify before apliying Spicetify
	#sudo chmod a+wr /opt/spotify/Apps -R
	
	#spicetify
	#spicetify backup apply enable-devtools

else
	echo -e "\nExiting installation"
fi
#sudo echo $LIST_OF_APPS
#sudo pacman -S nano --noconfirm


