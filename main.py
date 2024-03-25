from requests import post
from os import system , name
from colorama import Fore , init

init()

red = Fore.LIGHTRED_EX; yellow = Fore.LIGHTYELLOW_EX; green = Fore.LIGHTGREEN_EX; magenta = Fore.LIGHTMAGENTA_EX; cyan = Fore.LIGHTCYAN_EX; blue = Fore.LIGHTBLUE_EX;

system('cls' if name == 'nt' else 'clear')

bn = f'''
     _ _                          _    _                 _                 
    {red}| (_)                        | |  | |               | |                
  _ | |_  ___  ____ ___   ____ _ | |  | | _   ___  ____ | | _   ____  ____ 
 / || | |/___)/ ___) _ \ / ___) || |  | || \ / _ \|    \| || \ / _  )/ ___)
( (_| | |___ ( (__| |_| | |  ( (_| |  | |_) ) |_| | | | | |_) | (/ /| |    
 \____|_(___/ \____)___/|_|   \____|  |____/ \___/|_|_|_|____/ \____)_|    
                        {green}Created {red}By {cyan}John {yellow}Wick
                          {blue}TEAM {red}PYTHO {yellow}LEARN

'''

print(bn)

token = input(f'{red}[{yellow}+{red}] {green}PLS ENTER YOUR TOKEN {red}={yellow}>{green} ')
message = input(f'{red}[{yellow}+{red}] {green}PLS ENTER YOUR MESSAGE TO NEXT STEP {red}={yellow}>{green} ')
id_m = input(f'{red}[{yellow}+{red}] {green}PLS ENTER YOUR TARGET CHANNEL ID {red}={yellow}>{green} ')

payload = {
    'content' : message
}

header = {
    'authorization' : token
}


def main():
    while True:
        req = post(f'https://discord.com/api/v9/channels/{id_m}/messages', data=payload, headers=header)
        print(f'{red}[{yellow}+{red}] {green} MESSAGE SENT ==> {red}| {green}Response {yellow}: {magenta}{req}')

main()
