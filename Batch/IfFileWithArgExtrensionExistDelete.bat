@echo off

set /p fileExtension=Podaj typ pliku: 

IF EXIST *.%fileExtension% (FORFILES /m *.%fileExtension% /c "cmd /c del @file") else (echo nie istnieje)

echo Zakonczono
pause

echo on