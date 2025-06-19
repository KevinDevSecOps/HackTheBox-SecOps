import psutil

def monitor_resources():
    print("Uso de CPU:", psutil.cpu_percent(interval=1), "%")
    print("Uso de RAM:", psutil.virtual_memory().percent, "%")
    print("Espacio en disco:", psutil.disk_usage('/').percent, "%")

if __name__ == '__main__':
    monitor_resources()
