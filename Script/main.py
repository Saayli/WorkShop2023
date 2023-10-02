import psutil

def get_cpu_temperature():
    cpu_temperature = psutil.sensors_temperatures()['coretemp'][0].current
    return cpu_temperature

print("CPU Temperature:", get_cpu_temperature(), "°C")