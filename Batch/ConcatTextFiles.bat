@echo off
cls
set /p c1=<%1\dane1.txt
set /p c2=<%1\dane2.txt
set c3=%c1%%c2%
echo %c3%
pause