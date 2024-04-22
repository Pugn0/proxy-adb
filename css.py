from colorama import Fore, Style, init

def icon(simbolo):
    if simbolo == 'v' or simbolo == "V":
        return Fore.WHITE + "[" + Fore.GREEN + "✓" + Fore.WHITE + "]" + Fore.WHITE
    elif simbolo == 'x' or simbolo == "X":
        return Fore.WHITE + "[" + Fore.RED + "✗" + Fore.WHITE + "]" + Fore.WHITE
    elif simbolo == '!':
        return Fore.WHITE + "[" + Fore.YELLOW + "!" + Fore.WHITE + "]" + Fore.WHITE
    elif simbolo == '-':
        return Fore.YELLOW  + "-" + Fore.WHITE
    elif simbolo == '𖦿':
        return Fore.CYAN  + "𖦿" + Fore.WHITE
    else:
        return "error simbolo"
#print(icon('𖢊'))
