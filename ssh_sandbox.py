import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('139.59.111.67', username='kkiarie', password='kiarie1234', timeout=10)

stdin, stdout, stderr = ssh.exec_command('python3 /home/kkiarie/error_report/log_filter.py')
