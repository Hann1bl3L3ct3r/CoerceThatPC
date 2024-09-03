# CoerceThatPC
Script to automate the exploitation of a computer object being a member of an Administrators group within Active Directory.

This script automates the process of using known credentials to coerce NTLM authentication using named pipes via the Coercer package to an attackers PC where the Impacket ntlmrelayx package relays that authentication request to the Domain Controller to add a computer account and grant it DCSync privileges. This can be used any time a computer account exists in an administrator group which I have seen in multiple different corporate domains. 
