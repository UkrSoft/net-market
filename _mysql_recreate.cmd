@echo off
set dbname="netmarket"
set username="netmarket"
set pass="wearethebest"

echo This will DROP existing DB and create it from the scratch!!!
echo.
echo ARE YOU SURE?
pause
mysql -b -u %username% -p%pass% -e "drop database %dbname%;" >nul
mysql -b -u %username% -p%pass% -e "create database %dbname%;" >nul
echo DONE.
pause