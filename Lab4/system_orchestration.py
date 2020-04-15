import sys, paramiko, os

server_address = "129.21.17.234"
mini_file = "mini_project.tar.gz"
files = ["APM1", "APM2", "APM3", "APM4", "APM5", "APM6"]

#Commands
extract="tar -xvf " + mini_file

username = 'student'
password = 'student'
port = 22

# STFP
t = paramiko.Transport((server_address, port))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
# Act 4, part 2
sftp.put(mini_file, mini_file)

# SSH
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy)
client.connect(server_address, port=port, username=username, password=password)
client.exec_command(extract)
# move files - Act 4, Part 3 & Part 4
print("Listing the files\n")
client.exec_command("mv mini_project/* .")
client.exec_command("mv APMs/* .")
client.exec_command("rm -rf mini_project/")
client.exec_command("rm -rf APMs/")
stdin, stdout, stderr = client.exec_command("ls -l")
print(stdout.read())

# Act 4, part 5
print("\nGetting the APMs files")
getclient = client.open_sftp()
for f  in files:
    getclient.get(f, f)

# Act 4, part 6
pwd = os.getcwd()
dirs = os.listdir(pwd)

print("Printing your current directory....")
for d in dirs:
    print(d)

# close the socket/connection
t.close()
client.close()
getclient.close()

