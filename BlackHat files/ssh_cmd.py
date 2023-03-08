import paramiko
def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('---Output---')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    import getpass
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter the server IP: ') 
    port = input ('Enter the port: ') or 2222
    cmd = input ('enter a command: ') or 'id'
    ssh_command( ip, port, user, password, cmd)