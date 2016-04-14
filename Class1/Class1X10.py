# Import Modules
from ciscoconfparse import CiscoConfParse

# Parse Configuration File
cisco_config = CiscoConfParse("cisco_ipsec.txt")

# Find Crypto Objects without Specific Children
crypto_woaes = cisco_config.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES-SHA")

# Print Crypto Objects
for i in crypto_woaes:
    print(i.text)
    for child in i.children:
        print(child.text)
