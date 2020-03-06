@echo off
title %Projekt Jezyki Skryptowe%


set mydateyear=%date:~6,4%
set mydatemonth=%date:~3,2%
set mydateday=%date:~0,2%

:main
cls
echo.
echo ALGORYTMION Zadanie 5 - "KLOPOT ROWERZYSTY"
echo.
echo 1. Start
echo 2. Informacje
echo 3. Backup
echo 4. Zakoncz
echo.
set /p answer="Twoj wybor: "
if %answer%==1 goto start
if %answer%==2 goto info
if %answer%==3 goto backup
if %answer%==4 goto end

:start
start server.exe
start page.py
timeout 2 >nul
start page.html
xcopy /Q /Y page.html .\backup\%mydateyear%\%mydatemonth%\%mydateday%\
xcopy /Q /Y style.css .\backup\%mydateyear%\%mydatemonth%\%mydateday%\
xcopy /Q /Y page.py .\backup\%mydateyear%\%mydatemonth%\%mydateday%\
xcopy /Q /Y .\input .\backup\%mydateyear%\%mydatemonth%\%mydateday%\
xcopy /Q /Y .\output .\backup\%mydateyear%\%mydatemonth%\%mydateday%\
xcopy /Q /Y .\images\chart_%mydateyear%_%mydatemonth%_%mydateday%.png .\backup\%mydateyear%\%mydatemonth%\%mydateday%\
goto main

:info
cls
echo Projekt Jezyki Skryptowe
echo ALGORYTMION Zadanie 5 - "KLOPOT ROWERZYSTY"
echo Arkadiusz Kaluza
echo Informatyka sem III, grupa 2C, RMS
pause
goto main

:backup
cls
dir .\backup /W
pause
goto main

:end
pause
echo on