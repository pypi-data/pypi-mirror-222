#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import argparse
from colorama import init, Fore
from time import sleep
import pyperclip

init()

class UsersGenerator:
    def __init__(self, args):
        self.args = args

    def check_version(self):
        if sys.version_info < (3, 0):
            print(Fore.RED + "Disculpa, la aplicacion usa python 3.x\n")
            sys.exit(1)

    def logo(self):
        header = '''
 _   _                     _____                           _             
| | | |                   |  __ \                         | |            
| | | |___  ___ _ __ ___  | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| | | / __|/ _ \ '__/ __| | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_| \__ \  __/ |  \__ \ | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
 \___/|___/\___|_|  |___/  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   

                                      Autor: AbelJM, angussMoody
                                       Web: abeljm.github.io
        '''
        print(header)

    def read_file(self, usersfile):
        users = []
        with open(usersfile, "r") as user:
            for line in user:
                users.append(line.rstrip().lower())
        return users

    def generate_users(self, name, fsurname=None, ssurname=None):
        users = []
        i_name = name[0] if name else ''
        i_fsurname = fsurname[0] if fsurname else ''
        i_ssurname = ssurname[0] if ssurname else ''

        if fsurname is not None:
            users.extend([
                name,
                fsurname,
                name + fsurname,
                name + "-" + fsurname,
                name + "_" + fsurname,
                name + "." + fsurname,
                i_name + i_fsurname,
                i_name + "-" + i_fsurname,
                i_name + "_" + i_fsurname,
                i_name + "." + i_fsurname,
                name + i_fsurname,
                name + "-" + i_fsurname,
                name + "_" + i_fsurname,
                name + "." + i_fsurname
            ])

        if ssurname is not None:
            users.extend([
                ssurname,
                name + ssurname,
                name + fsurname + ssurname,
                name + "-" + ssurname,
                name + "_" + ssurname,
                name + "." + ssurname,
                i_name + i_ssurname,
                i_name + i_fsurname + i_ssurname,
                i_fsurname + i_ssurname,
                i_name + i_ssurname,
                i_name + "-" + i_ssurname,
                i_name + "_" + i_ssurname,
                i_name + "." + i_ssurname,
                name + i_ssurname,
                name + "-" + i_ssurname,
                name + "_" + i_ssurname,
                name + "." + i_ssurname
            ])

        return users

    def save_file(self, g_users, name_file):
        path = os.getcwd()
        path_file = "%s/%s" % (path, name_file)
        with open(path_file, mode='w', encoding='utf-8') as file:
            for g_user in g_users:
                file.write('%s\n' % (g_user))
        return path_file

    def run(self):
        if not self.args.quiet:
            self.logo()
        self.check_version()

        try:
            userfile = self.args.users
            file_g = self.args.output
            g_users = []
            users = self.read_file(userfile)
            print(Fore.GREEN + "[*] Lista de usuarios" + Fore.RESET)
            for user in users:
                print("[+] %s" % (user.rstrip()))
                name, *surnames = user.rstrip().split(" ")
                g_users.extend(self.generate_users(name, *surnames))
                sleep(0.1)

            print(Fore.GREEN + f"\n[*] Generar usuarios" + Fore.RESET)
            for g_user in g_users:
                print("[+] %s" % (g_user))
                sleep(0.01)

            if self.args.clipboard:
                users_text = "\n".join(g_users)
                pyperclip.copy(users_text)
                print(Fore.GREEN + "\n[+] Usuarios generados copiados al portapapeles." + Fore.RESET)
                sleep(0.1)

            elif self.args.output:                
                print(Fore.GREEN + f"\n[*] guardando usuarios" + Fore.RESET)
                file_g = self.save_file(g_users, file_g)
                if os.path.isfile(file_g):
                    print("[+] Archivo guardado: " + Fore.YELLOW + file_g + Fore.RESET)

        except Exception as e:
            print(e)

def main():
    parser = argparse.ArgumentParser(description='Ejemplo:', epilog="python3 usersgenerator.py -u users.txt -o resultado.txt")
    parser.add_argument("-u", "--users", type=str, required=True, help="lista de usuarios en archivo de texto, ejemplo: -u users.txt")
    parser.add_argument("-o", "--output",  type=str, help="Guardar resultado en archivo de texto, poner nombre ejemplo: -o resultado.txt")
    parser.add_argument("-c", "--clipboard", action="store_true", help="Copiar los usuarios generados al portapapeles")
    parser.add_argument("-q", "--quiet", action="store_true", help="Imprimir solo los usuarios generados sin logo")
    args = parser.parse_args()

    users_generator = UsersGenerator(args)
    users_generator.run()

if __name__ == '__main__':
    main()