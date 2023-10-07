import tkinter as tk
from tkinter import ttk

# https://github.com/SpotX-Official/SpotX/discussions/60

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

# Language options. 
languages = {
    "bn": "Bengali",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "es": "Spanish",
    "fa": "Persian",
    "fi": "Finnish",
    "fil": "Filipino",
    "fr": "French",
    "hi": "Hindi",
    "hu": "Hungarian",
    "id": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "ka": "Georgian",
    "ko": "Korean",
    "lv": "Latvian",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "sr": "Serbian",
    "sv": "Swedish",
    "tr": "Turkish",
    "vi": "Vietnamese",
    "zh": "Chinese",
}

param_descriptions ={
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

### Tk
## Tk setup. 
window = tk.Tk()

## Tk vars. 
version_to_gen = ""
language_choice = tk.StringVar(window)
language_choice.set("English")

## Tk widgets. 
# Install section. 
install_header_lbl = tk.Label(text="Install", font=("Arial", 16))
version_lbl = tk.Label(text="Version")
version_ent = tk.Entry(textvariable=version_to_gen, width=20)
csro_ckb = ttk.Checkbutton(text="confirm_spoti_recomended_over")
csru_ckb = ttk.Checkbutton(text="confirm_spoti_recomended_uninstall")
cums_ckb = ttk.Checkbutton(text="confirm_uninstall_ms_spoti")
# Experimental section. 
experimental_header_lbl = tk.Label(text="Experimental", font=("Arial",16))
exp_spotify_ckb = ttk.Checkbutton(text="exp_spotify")
enhance_like_off_ckb = ttk.Checkbutton(text="enhance_like_off")
enhance_playlist_off_ckb = ttk.Checkbutton(text="enhance_playlist_off")
smartShuffle_off_ckb = ttk.Checkbutton(text="smartShuffle_off")
hide_col_icon_off_ckb = ttk.Checkbutton(text="hide_col_icon_off")
new_theme_ckb = ttk.Checkbutton(text="new_theme")
rightsidebar_off_ckb = ttk.Checkbutton(text="rightsidebar_off")
rightsidebarcolor_ckb = ttk.Checkbutton(text="rightsidebarcolor")
old_lyrics_ckb = ttk.Checkbutton(text="old_lyrics")
lyrics_stat_ckb = ttk.Checkbutton(text="lyrics_stat")
adsections_off_ckb = ttk.Checkbutton(text="adsections_off")
funnyprogressBar_ckb = ttk.Checkbutton(text="funnyprogressBar")
# Language section. 
language_header_lbl = tk.Label(text="Language", font=("Arial", 16))
language_lbl = tk.Label(text="Language")
language_opm = tk.OptionMenu(window, language_choice, *[str(i) for i in languages.values()])
# Podcast section. 
podcast_header_lbl = tk.Label(text="Podcast", font=("Arial",16))
podcasts_off_ckb = ttk.Checkbutton(text="podcasts_off")
podcasts_on_ckb = ttk.Checkbutton(text="podcasts_on")
# Update section. 
Update_header_lbl = tk.Label(text="Update", font=("Arial",16))
block_update_on_ckb = ttk.Checkbutton(text="block_update_on")
block_update_off_ckb = ttk.Checkbutton(text="block_update_off")
# Other section. 
other_header_lbl = tk.Label(text="Other", font=("Arial", 25))
cache_limit_ckb = ttk.Checkbutton(text="Cache Limit")
premium_ckb = ttk.Checkbutton(text="premium")
urlform_goofy_ckb = ttk.Checkbutton(text="urlform_goofy")
start_spoti_ckb = ttk.Checkbutton(text="start_spoti")
no_shortcut_ckb = ttk.Checkbutton(text="no_shortcut")
# Generate section. 
generate_header_lbl = tk.Label(text="Generate", font=("Arial", 16))
generate_btn = tk.Button(text="Generate Installer")

# Return start of base batch command. 
def get_base_start():
    a = "%SYSTEMROOT%\System32\WindowsPowerShell\\v1.0\powershell.exe -Command "
    b = '"&{[Net.ServicePointManager]::SecurityProtocol = 3072}; "'
    c = '"""&{$(Invoke-WebRequest -UseBasicParsing \'https://spotx-official.github.io/run.ps1\')}'
    return f"{a}{b}{c}"

# Return end of base batch command. 
def get_base_end():
    return '"""" | Invoke-Expression'

def main():
    rows = 0
    cols = 0

    # Install section. 
    install_header_lbl.grid(row=rows, column=0, columnspan=2)
    rows += 1
    version_lbl.grid(row=rows, column=0, sticky="W")
    version_ent.grid(row=rows, column=0, sticky="E")
    rows += 1
    csro_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    csru_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    cums_ckb.grid(row=rows, column=0, sticky="W")
    
    # Language section. 
    rows += 1
    language_header_lbl.grid(row=rows, column=0)
    rows += 1
    language_lbl.grid(row=rows, column=0, sticky="W")
    language_opm.grid(row=rows, column=0)

    # Podcast section. 
    rows += 1
    podcast_header_lbl.grid(row=rows, column=0)
    rows += 1
    podcasts_off_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    podcasts_on_ckb.grid(row=rows, column=0, sticky="W")

    # Update section. 
    rows += 1
    Update_header_lbl.grid(row=rows, column=0)
    rows += 1
    block_update_on_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    block_update_off_ckb.grid(row=rows, column=0, sticky="W") 

    # Experimental section. 
    rows += 1
    experimental_header_lbl.grid(row=rows, column=0, columnspan=2)
    rows += 1
    exp_spotify_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    enhance_like_off_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    enhance_playlist_off_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    smartShuffle_off_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    hide_col_icon_off_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    new_theme_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    rightsidebar_off_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    rightsidebarcolor_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    old_lyrics_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    lyrics_stat_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    adsections_off_ckb.grid(row=rows, column=0, sticky="W")
    rows += 1
    funnyprogressBar_ckb.grid(row=rows, column=0, sticky="W")

    # Other section. 
    rows += 1
    other_header_lbl.grid(row=rows,column=0)
    rows += 1
    cache_limit_ckb.grid(row=rows,column=0, sticky="W")
    rows += 1
    premium_ckb.grid(row=rows,column=0, sticky="W")
    rows += 1
    urlform_goofy_ckb.grid(row=rows,column=0, sticky="W")
    rows += 1
    start_spoti_ckb.grid(row=rows,column=0, sticky="W")
    rows += 1
    no_shortcut_ckb.grid(row=rows,column=0, sticky="W")

    # Generate section. 
    rows += 1
    generate_header_lbl.grid(row=rows, column=0, columnspan=2)
    rows += 1
    generate_btn.grid(row=rows, column=0, columnspan=2, ipadx=10)

    window.mainloop()

# Produce batch installer. 
def generate_batch():
    with open("install.bat", "w+") as file:
        file.write("@echo off\n")
        file.write(f"{get_base_start()} {gen_command()} {get_base_end()}" + "\n")
        file.write("pause\n")
        file.write("exit /b\n")

# Build command string. 
# Any parameter with a truthy value will be added to command string. 
def gen_command():
    param_str = ""
    for k, v in params.items(): 
        if v and k in binary_params:
            param_str += f" -{k}"
        if v and k not in binary_params:
            param_str += f" -{k} {v}"
    return param_str

# Write command string to file. 
def write_out_command():
    with open("output.txt", "w+") as file:
        file.write(get_base_start() + gen_command() + get_base_end())

if __name__ == "__main__":
    main()
