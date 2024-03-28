from netmiko import ConnectHandler
import sys

# Extracting username, password, and command from the arguments
if len(sys.argv) != 5:
    print("Usage: script.py <host> <username> <password> <command>")
    sys.exit(1)

host = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
command = sys.argv[4]

# Setting up device information
device = {
    'device_type': 'nokia_srl',
    'host': host,
    'username': username,
    'password': password,
}

# Establishing the connection
try:
    net_connect = ConnectHandler(**device)
    # Executing the command
    output = net_connect.send_command(command)
    print(output)
finally:
    # Ensuring the session is closed properly
    net_connect.disconnect()
