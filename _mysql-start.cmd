@echo off
set db_name="netmarket"
set username="netmarket"
set pass="wearethebest"

mysql -b -u %username% -p%pass% %db_name%
pause