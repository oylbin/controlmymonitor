
REM ControlMyMonitor.exe /SetValue "\\.\DISPLAY1\Monitor0" 60 15
REM 60 means set input source
REM 15 means DP1

cd %~dp0
python SetInputSource.py "LG Ultra HD" "DP1"
PAUSE
