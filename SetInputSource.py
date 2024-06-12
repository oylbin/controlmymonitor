# coding: utf-8
import sys
import os
import subprocess


def getInputSourceNumber(inputSource):
    if inputSource == "DP1":
        return 15
    elif inputSource == "DP2":
        return 16
    elif inputSource == "HDMI1":
        return 17
    elif inputSource == "HDMI2":
        return 18
    else:
        return -1


monitorName = sys.argv[1]
inputSource = sys.argv[2]

print("Monitor Name: ", monitorName)
print("Input Source: ", inputSource)
inputSourceNumber = getInputSourceNumber(inputSource)
if inputSourceNumber == -1:
    print("Input Source not found")
    exit()

# run ControlMyMonitor.exe /smonitors monitors.txt
os.system("ControlMyMonitor.exe /smonitors monitors.txt")

monitor_name_to_device_name = {}
monitor_device_name = ""
# read monitors.txt line by line
with open("monitors.txt", "r", encoding="utf-16le") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        # print(hex(ord(line[0]))) is 0xfeff, which is BOM
        # do not use line.startswith("Monitor Device Name:") because it may have BOM
        if line.find("Monitor Device Name:") != -1:
            monitor_device_name = line.split(":")[1].strip().replace('"', '')
        elif line.find("Monitor Name:") != -1:
            monitor_name = line.split(":")[1].strip().replace('"', '')
            monitor_name_to_device_name[monitor_name] = monitor_device_name

print("All Monitors: ")
for monitor_name in monitor_name_to_device_name:
    print(monitor_name, monitor_name_to_device_name[monitor_name])

if monitorName not in monitor_name_to_device_name:
    print("Monitor not found")
    exit()

monitor_device_name = monitor_name_to_device_name[monitorName]

print("Monitor Device Name: ", monitor_device_name)
print("Input Source Number: ", inputSourceNumber)

print(f"ControlMyMonitor.exe /SetValue {monitor_device_name} 60 {inputSourceNumber}")
subprocess.check_call(["ControlMyMonitor.exe", "/SetValue", monitor_device_name, "60", str(inputSourceNumber)])
