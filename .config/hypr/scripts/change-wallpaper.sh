#! /bin/zsh

#change wallpaper
waypaper --random 

#wait a bit
sleep 0.5

#update swaync style
swaync-client --reload-css 

#update pywal fox
pywalfox update 

#run script to put current wallpaper in a folder to host a local server from
~/.config/waypaper/wallpaper_server.sh

#refresh discord
hyprctl dispatch sendshortcut CONTROL, r, vesktop