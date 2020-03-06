@echo off

set /p a="Podaj liczbe: "
set /p b="Podaj kolejna liczbe: "
echo 1.Dodawanie
echo 2.Odejmowanie 
echo 3.Dzielenie
echo 4.Mnozenie
set /p d="Wybor:  "
if %d%==1 (
set /a wynik=%a%+%b%
)
if %d%==2 (
set /a wynik=%a%?%b%
)
if %d%==3 (
set /a wynik=%a%/%b%
)
if %d%==4 (
set /a wynik=%a%*%b%
)
echo Wynik to %wynik%
pause
echo on