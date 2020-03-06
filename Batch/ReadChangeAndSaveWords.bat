@echo off
cls
SETLOCAL enabledelayedexpansion

SET "key=o"
SET "new=0"

echo Przed zamiana:
for /f "tokens=*" %%i in (%1) do (
echo %%i
)

echo.>>%2

echo Po zamianie:
SET "line="
for /f "tokens=* delims=" %%x in (%1) do (
set line=%%x
echo !line:%key%=%new%!>>%2
)

ENDLOCAL
pause