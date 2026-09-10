import csv
import random
from datetime import datetime

def generate_security_logs(filename="security_logs.csv", num_rows=50):
    ip_addresses = ["192.168.1.10", "10.0.0.45", "172.16.0.22", "192.168.0.105", "203.0.113.5"]
    users = ["admin_cenco", "jperez", "analyst_sec", "cpalacios", "system_bot"]
    actions = ["LOGIN_SUCCESS", "LOGIN_FAILED", "CONFIG_CHANGE", "UNAUTHORIZED_ACCESS"]

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escribir encabezados
        writer.writerow(["timestamp", "ip_address", "username", "action", "status_code"])

        for _ in range(num_rows):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ip = random.choice(ip_addresses)
            user = random.choice(users)
            action = random.choice(actions)
            code = 200 if action in ["LOGIN_SUCCESS", "CONFIG_CHANGE"] else 403

            writer.writerow([timestamp, ip, user, action, code])
    
    print(f"Archivo {filename} generado exitosamente con {num_rows} registros.")

if __name__ == "__main__":
    generate_security_logs()
