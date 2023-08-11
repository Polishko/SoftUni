import pyfiglet
from pyfiglet import figlet_format


def print_figlet_art(msg):
    print(figlet_format(msg))


print_figlet_art(input())
