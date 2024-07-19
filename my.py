#Recreating gundam Barbatos Lupus's sword mace as a piece of ascii art 
import time 
import sys 
from colorama import Fore 
sword_mace_ascii_art=f''' 
                           /\   
                         /_/\_\ 
                        / /  \ \ 
                       / /    \ \ 
                      / / ____ \ \ 
                     / / /    \ \ \ 
                     | | |_   | | |
                     | | | |  | | |
                     | | | |  | | |
                     | | |_|  | | |
                     | | |    | | |
                     | | | |  | | | 
                     | | | |  | | |
                     | | | |  | | |
                     | | | |  | | |
                     | | | |  | | |
                     | | | |  | | |
                     | | | |  | | |
                     | | |    | | |
                     | | |  /|| | |
                     | | |  \|| | |
                     | | |    | | |
                     | | | |  | | |
                     | | | |  | | |
                     | | | |  | | |
                     | | | |  | | |
                     | | | |  | | |
                     | | | |  | | |
                     | | |    | | | 
                     | | |    | | |
                     | | |    | | |
                     | | |_   | | |
                     | | | |  | | |
                     | | | |  | | | 
                     | | |_|  | | |
                    /||| |    ||||\\
                    |||| |    |||||
                    |||| |    ||||| 
                    \|\| |    ||/|/
                      \  \    /  /
                     / /\_\__/_/\\ \\
                    | |_|  || |_| |
                    \_\_| -||-|_/_/
                        |__\/_|
                         |___| 
                         |   |
                         |   |
                         |   |
                         |___|                         
                         |   |
                         |   |
                         |   |
                         |   |
                         |   |
                         |   |
                         |   |
                         |   |
                         |   |
                         |   |
                         |   |
                         |   |
                         |   |
                        _/___\\_
                      || |   | ||
                      ||_|___|_||
                         \\___/
                         '''
def loop_over(sequence,color,delay_time):
  for text in sequence:
    sys.stdout.flush()
    time.sleep(delay_time)
    sys.stdout.write(f'{color}{text}')
  else:
    print(f'{Fore.RESET}')
    
loop_over(sequence='Gundam Barbatos Lupus\'s sword mace:\n\t',delay_time=0.01,color=Fore.BLUE)
time.sleep(1)
loop_over(sequence=sword_mace_ascii_art,delay_time=0.001,color=Fore.BLACK)
