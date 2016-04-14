# Import Modules
from ciscoconfparse import CiscoConfParse

# Parse Configuration File
cisco_config = CisconConfParse("cisco_ipsec.txt")

# Search for Crypto Objects
crypto = cisco_config.find_objects(r"^crypto map CRYPTO")

# Print Crypto Objects
for i in crypto:
    print(i.text)
    for child in i.children:
        print(child.text)
