@echo off
set str=%1
for /f "usebackq" %%a in ('%str%') do (
set str=%%~a
)
echo %str%
pause
