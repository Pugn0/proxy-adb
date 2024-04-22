import subprocess
import time
import os

def toggle_airplane_mode(enable):
    """ Função para ativar ou desativar o modo avião no dispositivo Android. """
    state = '1' if enable else '0'
    command = f"adb shell su -c 'settings put global airplane_mode_on {state}; am broadcast -a android.intent.action.AIRPLANE_MODE --ez state {enable}'"
    try:
        # Executando o comando silenciosamente
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True if enable else False 
    except subprocess.CalledProcessError as e:
        print("Erro ao tentar mudar o estado do modo avião:", e)
        return None

def execute_adb_command(command):
    try:
        result = subprocess.run(['adb', 'shell'] + command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o comando ADB:", e)
        return None
    
def get_android_id():
    """Obtém o Android ID do dispositivo conectado."""
    command = ["settings", "get", "secure", "android_id"]
    android_id = execute_adb_command(command)
    if android_id:
        return android_id
    else:
        print("Não foi possível obter o Android ID")
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
        return f"Endereço IP Público IPv4: {ipv4}"
    else:
        return "Não foi possível obter o endereço IP público IPv4."
    
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

    return rooted

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

def read_or_save_android_id(filename="android_id.txt"):
    """Lê ou salva o Android ID em um arquivo se não estiver presente e retorna o Android ID e o status de root."""
    android_id = get_android_id()  # Obtém o Android ID atual
    if android_id is None:
        print("Falha ao obter o Android ID. Nada foi salvo.")
        return None, False

    # Inicializa uma variável para armazenar os IDs existentes e status de root
    existing_ids = {}
    
    # Verifica se o arquivo existe e lê os IDs existentes
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                if '|' in line:
                    id_part, root_part = line.strip().split('|')
                    existing_ids[id_part] = root_part == 'root=True'

    # Verifica se o Android ID atual já está registrado
    if android_id in existing_ids:
        return android_id, existing_ids[android_id]  # Retorna o Android ID e o status de root
    else:
        # Android ID não registrado, adiciona ao arquivo
        root_status = check_for_root_artifacts()  # Verifica se o dispositivo está rootado
        with open(filename, 'a') as file:  # Abre o arquivo em modo append
            file.write(f"{android_id}|root={root_status}\n")
            print(f"Novo Android ID adicionado ao arquivo: {android_id}")
        return android_id, root_status  # Retorna o Android ID e o status de root
