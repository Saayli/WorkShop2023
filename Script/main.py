import wmi

w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
for sensor in temperature_infos:
        print(sensor.Name)
        print(sensor.SensorType)
        print(sensor.Value)

"""
w_temp = wmi.WMI(namespace="root\\wmi")
print((w_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0) - 273.15)
"""
