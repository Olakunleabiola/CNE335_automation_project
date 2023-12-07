import paramiko

def upgrade_ubuntu_ssh(ip_address, username, private_key_path):
    # Create an SSH client
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Load the private key
        private_key = paramiko.RSAKey(filename=private_key_path)

        # Connect to the remote server using key-based authentication
        client.connect(ip_address, username=username, pkey=private_key)

        # Run the upgrade command
        command = "sudo apt update && sudo apt upgrade -y"
        stdin, stdout, stderr = client.exec_command(command)

        # Print the output of the command
        print("Output:")
        print(stdout.read().decode())

        # Print any errors
        if stderr:
            print("Errors:")
            print(stderr.read().decode())

        print("Upgrade completed successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SSH connection
        client.close()

ip_address = "34.221.172.36"
username = "ubuntu"
private_key_path = r"C:\Users\olakunlea\.SSH\OlakunleAbiola_keypair.pem"
upgrade_ubuntu_ssh(ip_address, username, private_key_path)
