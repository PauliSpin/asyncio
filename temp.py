from colorama import init, Fore, Style
from termcolor import colored

init()
print(colored('This is Green on Red', 'green', 'on_red'))
print(colored('This is Red on White', 'red', 'on_white'))
