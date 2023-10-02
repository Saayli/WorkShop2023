import wmi
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
for sensor in temperature_infos:
    if sensor.SensorType == u'Temperature' or sensor.SensorType == u'Power':
        print(sensor.Name)
        print(sensor.SensorType)
        print(sensor.Value)