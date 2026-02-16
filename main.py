#!/usr/bin/env python3
import argparse
import subprocess
import sys

def check_credentials(host, username, password):
    # Add or remove services from this list as needed
    services = ['smb', 'ldap', 'ftp', 'ssh', 'winrm', 'rdp', 'mssql']
    
    separator = "=" * 100
    
    for service in services:
        print(f"\n[*] Trying credentials against {service.upper()}...")
        print(separator)
        
        # subprocess.run with a list is safer than os.system with a string.
        # It handles special characters in passwords natively without shell escaping.
        command = ['netexec', service, host, '-u', username, '-p', password]
        
        try:
            subprocess.run(command, check=False)
        except FileNotFoundError:
            print("[!] Error: 'netexec' is not installed or not in your system PATH.")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user. Exiting...")
            sys.exit(0)
            
        print(separator)

if __name__ == '__main__':
    # argparse automatically handles missing arguments and generates a -h help menu
    parser = argparse.ArgumentParser(description="Automate netexec credential testing across multiple protocols.")
    parser.add_argument("host", help="Target IP or hostname")
    parser.add_argument("username", help="Username to test")
    parser.add_argument("password", help="Password to test")
    
    args = parser.parse_args()
    
    print(f"[*] Starting enumeration against {args.host} for user '{args.username}'")
    check_credentials(args.host, args.username, args.password)
    print("\n[*] Enumeration complete.")
