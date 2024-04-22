import api
import css
def main():
    android_id = api.get_android_id()
    if android_id is None:
        print("Não foi possível obter o Android ID.")
        return False

    # Processa o Android ID independentemente de ter sido visto antes
    android_id, root_status = api.read_or_save_android_id()
    
    if root_status:
        if api.is_root_enabled_via_adb():
            try:
                api.toggle_airplane_mode(True)  # Ativa modo avião
                api.time.sleep(5)  # Espera 10 segundos com o modo avião ativado
                api.toggle_airplane_mode(False)  # Desativa modo avião
                api.time.sleep(10)
                print(f"{css.icon("𖦿")} Android ID: {android_id} {css.icon("v")} {css.icon("-")} Enraizado {css.icon("v")} {css.icon("-")} Root está habilitado {css.icon("-")} {css.icon("v")} {api.get_public_ip()}")
            except Exception as e:
                print(f"Erro ao manipular o modo avião: {e}")
        else:
            print(f"{css.icon("𖦿")} Android ID: {android_id} {css.icon("v")} {css.icon("-")} Enraizado {css.icon("x")} {css.icon("-")} Root habilitado {css.icon("-")} {css.icon("!")} {api.get_public_ip()}")
    else:
        print(f"{css.icon("𖦿")} Android ID: {android_id} {css.icon("x")} {css.icon("-")} Enraizado  {css.icon("-")} {css.icon("!")} {api.get_public_ip()}")
    return True

if __name__ == "__main__":
    while True:
        try:
            if not main():
                break  # Encerra o loop se main retornar False
            api.time.sleep(10)  # Intervalo entre as verificações
        except KeyboardInterrupt:
            print("Script interrompido pelo usuário.")
            break