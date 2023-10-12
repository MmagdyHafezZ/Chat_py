@echo off

start "Server" /B python Server_group.py
timeout /t 2
start "Client" python Client_Groups.py
pause
