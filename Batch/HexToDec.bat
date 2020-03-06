@echo off
set /p number=Podaj liczbe: 
set /a dec=0x%number%
echo %number% (hex) = %dec% (dec)
pause
echo on