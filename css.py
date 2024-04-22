from colorama import Fore, Style, init

def icon():
    print(Fore.WHITE + "[" + Fore.GREEN + "✓" + Fore.WHITE + "]")
    print(Fore.WHITE + "[" + Fore.RED + "✗" + Fore.WHITE + "]")
    print(Fore.WHITE + "[" + Fore.YELLOW + "!" + Fore.WHITE + "]")

icon()