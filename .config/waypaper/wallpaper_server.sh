#! /bin/zsh

wallpaper_path=`grep "wallpaper = ~" ~/.config/waypaper/config.ini | awk '{print $3}' | sed "s|~|$HOME|"`

rm -rf ~/current_wallpaper/*

cp "$wallpaper_path" ~/current_wallpaper/current.${wallpaper_path##*.}
