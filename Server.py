# oLakunleabiola
# CNE 335 Fall

import os


class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        try:

            response = os.system(f"ping -n 4 {self.server_ip}")  # Use os module to ping the server
            if response == 0:
                return f"Server {self.server_ip} is reachable."
            else:
                return f"Server {self.server_ip} is unreachable."
        except Exception as e:
            return f"Error while pinging the server: {str(e)}"


def print_program_info():
    print("Server Automator v0.1 by Olakunleabiola")


# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()


    server_ip = "34.221.172.36"    # Create a Server object
    server = Server(server_ip)


    result = server.ping()  # Call Ping method and print the results
    print(result)
