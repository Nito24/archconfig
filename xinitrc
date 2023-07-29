xset -b

#screensaver and screen blanking
xset s off -dpms

setxkbmap -layout es

picom &

unclutter --jitter 10 --ignore-scrolling --start-hidden --timeout 10 --fork

#nitrogen --restore

nitrogen --set-zoom-fill --random /usr/share/backgrounds/archlinux &

#randomwallpaper &

volumeicon &

xbindkeys &

qtile start


