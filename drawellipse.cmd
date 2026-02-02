@echo off
set ANACONDA_ROOT=C:\Anaconda3
@call "%ANACONDA_ROOT%\Scripts\activate.bat" %ANACONDA_ROOT%
@start "" pythonw "%~dp0\DrawEllipse.py"