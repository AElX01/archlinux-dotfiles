from os import system
from getpass import getuser


currentUser = getuser()
currentWallpaper = "1345403.jpeg"

script_variables = dict(
    mod = "mod4",
    run_startup_programs = "/home/0xncat/.config/qtile/./autostart.sh",
    terminal = "kitty",
    browser = "firefox",
    app_launcher_mode = "rofi -show drun",
    wallpaper_path = f"/home/{currentUser}/Pictures/wallpapers/{currentWallpaper}"
)


