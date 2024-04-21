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

def info():
    get_android_version()
    get_public_ip()

def check_for_root_artifacts():
    # Lista de comandos que checam a existência de binários/diretórios comuns de root
    root_checks = [
        "ls /system/xbin/su",
        "ls /system/bin/su",
        "ls /sbin/su",
        "ls /system/su",
        "ls /system/bin/.ext",
        "ls /system/xbin/busybox",
        "ls /system/app/Superuser.apk",
        "ls /data/local/xbin/su",
        "ls /data/local/bin/su",
        "ls /data/local/su",
        "ls /system/app/SuperSU",
        "ls /su/bin/su",
        "ls /su/xbin/su",
        "ls /system/usr/we-need-root/su-backup",
        "ls /system/xbin/daemonsu",
        "ls /system/etc/init.d/99SuperSUDaemon",
        "ls /system/bin/.ext/.su",
        "ls /system/etc/.has_su_daemon",
        "ls /system/etc/.installed_su_daemon",
        "ls /dev/com.koushikdutta.superuser.daemon/",
        "ls /system/app/Kinguser.apk",
        "ls /system/app/Kingoroot.apk",
        "ls /system/app/Kingo SuperUser.apk",
        "ls /system/app/KingoRoot.apk",
        "ls /data/app/eu.chainfire.supersu-*",
        "ls /data/app/eu.chainfire.supersu*/",
        "ls /data/app/com.kingouser.com/",
        "ls /data/app/com.kingroot.kinguser/",
        "ls /data/app/com.kingroot.RushRoot/",
        "ls /data/app/com.kingroot.kinguser/*",
        "ls /data/app/com.noshufou.android.su/",
        "ls /data/app/com.noshufou.android.su-*/",
        "ls /data/app/com.thirdparty.superuser/",
        "ls /data/app/com.yellowes.su/",
        "ls /data/dalvik-cache/*com.koushikdutta.superuser*",
        "ls /data/dalvik-cache/*com.thirdparty.superuser*",
        "ls /data/dalvik-cache/*com.kingroot.kinguser*",
        "ls /data/dalvik-cache/*com.kingouser.com*",
        "ls /sbin/supersu",
        "ls /sbin/su",
        "ls /sbin/.core/img",
        "ls /sbin/.core/su",
        "ls /system/sbin/su",
        "ls /system/bin/failsafe/su",
        "ls /system/bin/cpufreq/su",
        "ls /system/sd/xbin/su",
        "ls /system/usr/we-need-root/",
        "ls /cache/su.bin",
        "ls /data/su.bin",
        "ls /dev/su"
    ]

    
    rooted = False

    for command in root_checks:
        try:
            result = subprocess.run(['adb', 'shell', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.stdout and 'No such file or directory' not in result.stdout:
                print(f"Root artifact found: {command}")
                rooted = True
        except subprocess.CalledProcessError as e:
            print("Error executing command:", e)

    if rooted:
        print("Root artifacts detected. Device is likely rooted.")
    else:
        print("No root artifacts detected. Device is likely not rooted.")



def is_root_enabled_via_adb():
    try:
        # Tentando executar um comando que requer privilégios de root
        result = subprocess.run(['adb', 'shell', 'su', '-c', 'id'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Verifica se o comando foi bem sucedido (código de saída 0) e se a saída contém 'uid=0(root)'
        if result.returncode == 0 and 'uid=0(root)' in result.stdout:
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao executar o comando ADB: {e}")
        return False

# Exemplo de como usar a função
if is_root_enabled_via_adb():
    print("Root está habilitado no dispositivo.")
else:
    print("Root não está habilitado ou não foi possível verificar.")