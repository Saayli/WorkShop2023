import wmi
import time
import requests


w = wmi.WMI(namespace="root\LibreHardwareMonitor")
infos = w.Sensor()


def get_temp_cpu_max():
    for sensor in infos:
        if sensor.SensorType == 'Temperature' and sensor.Name == 'Core Max':
            return float(f'{sensor.Value:.2f}')

def get_temp_cpu_avg():
    for sensor in infos:
        if sensor.SensorType == 'Temperature' and sensor.Name == 'Core Average':
            return float(f'{sensor.Value:.2f}')


def get_temp_gpu():
    for sensor in infos:
        if sensor.SensorType == 'Temperature' and sensor.Name == 'GPU Core':
            return float(f'{sensor.Value:.2f}')


def get_cons_cpu_total():
    memory = 0
    package = 0
    cores = 0
    total = 0
    for sensor in infos:
        if sensor.SensorType == 'Power' and sensor.Name == 'CPU Memory':
            memory = sensor.Value
        if sensor.SensorType == 'Power' and sensor.Name == 'CPU Package':
            package = sensor.Value
        if sensor.SensorType == 'Power' and sensor.Name == 'CPU Cores':
            cores = sensor.Value
    total = package + cores + memory
    return float(f'{total:.2f}')


def get_cons_cpu_memory():
    for sensor in infos:
        if sensor.SensorType == 'Power' and sensor.Name == 'CPU Memory':
            return float(f'{sensor.Value:.2f}')


def get_cons_cpu_package():
    for sensor in infos:
        if sensor.SensorType == 'Power' and sensor.Name == 'CPU Package':
            return float(f'{sensor.Value:.2f}')


def get_cons_cpu_core():
    for sensor in infos:
        if sensor.SensorType == 'Power' and sensor.Name == 'CPU Cores':
            return float(f'{sensor.Value:.2f}')


def get_cons_gpu():
    for sensor in infos:
        if sensor.SensorType == 'Power' and sensor.Name == 'GPU Package':
            return float(f'{sensor.Value:.2f}')


def get_cons_total():
    gpu = 0
    memory = 0
    package = 0
    cores = 0
    total = 0
    for sensor in infos:
        if sensor.SensorType == 'Power' and sensor.Name == 'CPU Memory':
            memory = sensor.Value
        if sensor.SensorType == 'Power' and sensor.Name == 'CPU Package':
            package = sensor.Value
        if sensor.SensorType == 'Power' and sensor.Name == 'CPU Cores':
            cores = sensor.Value
        if sensor.SensorType == 'Power' and sensor.Name == 'GPU Package':
            gpu = sensor.Value
    total = gpu + cores + package + memory
    return float(f'{total:.2f}')


def get_temp_disk():
    for sensor in infos:
        if sensor.SensorType == 'Temperature' and sensor.Name == 'Temperature':
            return float(f'{sensor.Value:.2f}')

while True:
    w = wmi.WMI(namespace="root\LibreHardwareMonitor")
    infos = w.Sensor()
    requests.post(url = "http://127.0.0.1:5000/set-server", data = {
    "cons_cpu_core": get_cons_cpu_core(),
    "cons_cpu_memory": get_cons_cpu_memory(),
    "cons_cpu_package": get_cons_cpu_package(),
    "cons_cpu_total": get_cons_cpu_total(),
    "cons_gpu": get_cons_gpu(),
    "cons_total": get_cons_total(),
    "temp_cpu_avg": get_temp_cpu_avg(),
    "temp_cpu_max": get_temp_cpu_max(),
    "temp_gpu": get_temp_gpu(),
    "temp_disk": get_temp_disk()
    })
    print("send")
    time.sleep(60)

