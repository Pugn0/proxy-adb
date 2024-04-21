import subprocess
import time
import re

def toggle_airplane_mode(enable):
    state = '1' if enable else '0'
    try:
        # Mudar apenas a configuração do modo avião
        subprocess.run([
            'adb', 'shell', 'su', '-c', 
            f'settings put global airplane_mode_on {state}'
        ], check=True)
        print(f"Modo avião {'ativado' if enable else 'desativado'}.")
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o comando ADB:", e)

def timeMain():
    while True:
        try:
            toggle_airplane_mode(True)
            time.sleep(10)
            toggle_airplane_mode(False)
            time.sleep(10)
        except KeyboardInterrupt:
            print("Script interrompido pelo usuário.")
            break



def execute_adb_command(command):
    try:
        result = subprocess.run(['adb', 'shell'] + command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o comando ADB:", e)
        return None

def get_android_version():
    version = execute_adb_command(['getprop', 'ro.build.version.release'])
    if version:
        print(f"Versão do Android: {version}")
    else:
        print("Não foi possível obter a versão do Android.")

def get_public_ip():
    # Solicita o IPv4
    ipv4 = execute_adb_command(['curl', '-4', 'https://ifconfig.me'])
    if ipv4:
        print(f"Endereço IP Público IPv4: {ipv4}")
    else:
        print("Não foi possível obter o endereço IP público IPv4.")
    
    # Solicita o IPv6
    ipv6 = execute_adb_command(['curl', '-6', 'https://ifconfig.me'])
    if ipv6:
        print(f"Endereço IP Público IPv6: {ipv6}")
    else:
        print("Não foi possível obter o endereço IP público IPv6.")

def main():
    get_android_version()
    get_public_ip()

if __name__ == "__main__":
    main()