@echo off
%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\powershell.exe -Command "&{[Net.ServicePointManager]::SecurityProtocol = 3072}; """"&{$(Invoke-WebRequest -UseBasicParsing 'https://spotx-official.github.io/run.ps1')}  -version 1.2.13.661.ga588f749-4064 -confirm_spoti_recomended_over -confirm_uninstall_ms_spoti -old_lyrics -podcasts_off -block_update_on -start_spoti -no_shortcut """" | Invoke-Expression
pause
exit /b