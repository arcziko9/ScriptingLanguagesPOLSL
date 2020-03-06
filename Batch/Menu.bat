@echo off

cls

goto menu





:menu

echo ====MENU WYBORU FUNKCJI====

echo.

echo 1. Funkcja 1

echo 2. Funkcja 2

echo 3. Wyjscie

echo.

set /p option=Wybierz funkcje: 



if %option%==1 goto f1

if %option%==2 goto f2

if %option%==3 goto exit



:f1

echo.Funkcja 1

pause

cls

goto menu



:f2

echo.Funkcja 2

pause

cls

goto menu



:exit

echo koniec

pause

cls