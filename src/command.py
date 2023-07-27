import subprocess 
import os 

def runCommand(item_name, item_quantity):
    command = ['reg.exe', 'add', 'HKEY_CURRENT_USER\Software\Kinetic Games\Phasmophobia', '/v', f'{item_name}', '/t', 'REG_DWORD', '/d', f'{item_quantity}', '/f']
    subprocess.run(command)
    return f"Added {item_quantity} to {item_name}"

def clear():
    os.system('cls')

