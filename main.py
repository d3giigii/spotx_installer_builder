# https://github.com/SpotX-Official/SpotX/discussions/60


a = "%SYSTEMROOT%\System32\WindowsPowerShell\\v1.0\powershell.exe -Command "
b = '"&{[Net.ServicePointManager]::SecurityProtocol = 3072}; "'
c = '"""&{$(Invoke-WebRequest -UseBasicParsing \'https://spotx-official.github.io/run.ps1\')}'

# Command strings to be built upon. 
base_cmd_start = f"{a}{b}{c}"
base_cmd_end = '"""" | Invoke-Expression'
param_str = ""

# All parameters with default (non-inclusive) values.
params = {

    # Install options. 
    "version": "",
    "confirm_spoti_recomended_over": "",
    "confirm_spoti_recomended_unistall": "",
    "confirm_uninstall_ms_spoti": "",
    
    # Experimental features. 
    "exp_spotify": "",
    "enhance_like_off": "",
    "enhance_playlist_off": "",
    "smartShuffle_off": "",
    "hide_col_icon_off": "",
    "new_theme": "",
    "rightsidebar_off": "",
    "rightsidebarcolor": "",
    "old_lyrics": "",
    "lyrics_stat": "",
    "adsections_off": "",
    "funnyprogressBar": "",
    
    # Language. 
    "language": "",
    
    # Podcasts on homepage. 
    "podcasts_off": "",
    "podcasts_on": "",
    
    # Automatic updates. 
    "block_update_on": "",
    "block_update_off": "",
    
    # Other. 
    "cache_limit": "",
    "premium": "",
    "urlform_goofy": "",
    "start_spoti": "",
    "no_shortcut": ""
}

# Parameters that do not require input. 
binary_params = [
    "confirm_spoti_recomended_over",
    "confirm_spoti_recomended_unistall",
    "confirm_uninstall_ms_spoti",
    "exp_spotify",
    "enhance_like_off",
    "enhance_playlist_off",
    "smartShuffle_off",
    "hide_col_icon_off",
    "new_theme",
    "rightsidebar_off",
    "old_lyrics",
    "adsections_off",
    "funnyprogressBar",
    "podcasts_off",
    "podcasts_on",
    "block_update_on",
    "block_update_off",
    "premium",
    "urlform_goofy",
    "start_spoti",
    "no_shortcut",
]

# Specify values.
params["version"] = "1.2.13.661.ga588f749-4064"
params["confirm_spoti_recomended_over"] = "1"
params["confirm_uninstall_ms_spoti"] = "1"
params["old_lyrics"] = "1"
params["podcasts_off"] = "1"
params["block_update_on"] = "1"
params["start_spoti"] = "1"
params["no_shortcut"] = "1"


# Build command string. 
# Any parameter with a truthy value will be added to command string. 
for k, v in params.items():
    if v: 
        if k in binary_params:
            param_str += f" -{k}"
        else:
            param_str += f" -{k} {v}"
    

# Print command string. 
with open("output.txt", "w+") as file:
    file.write(base_cmd_start + param_str)

# Produce batch installer. 
spm = "{[Net.ServicePointManager]::SecurityProtocol = 3072}"
with open("install.bat", "w+") as file:
    file.write("@echo off\n")
    file.write(f"{base_cmd_start} {param_str} {base_cmd_end}" + "\n")
    file.write("pause\n")
    file.write("exit /b\n")

