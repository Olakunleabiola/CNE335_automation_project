# This is the template code for the CNE335 Final Project
# oLakunleabiola
# CNE 335 Fall

import subprocess

class Server:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def ping(self):
        try:

            result = subprocess.run(['ping', '-c', '4', self.ip_address], capture_output=True, text=True, check=True)  # Run the ping command and capture the output
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"

def print_program_info():
    print("Server Automator v0.1 by Your Name")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()


    server_ip = '34.221.172.36' # TODO - Replace '34.221.172.36' with the actual IP address you want to ping


    server = Server(server_ip)  # Create a Server object


    ping_result = server.ping()   # Call Ping method and print the results
    print(f"Ping Results for {server_ip}:\n{ping_result}")
