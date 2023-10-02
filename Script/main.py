import GPUtil

def get_gpu_temperature():
    gpus = GPUtil.getGPUs()
    gpu_temperature = gpus[0].temperature
    return gpu_temperature

print("GPU Temperature:", get_gpu_temperature(), "°C")