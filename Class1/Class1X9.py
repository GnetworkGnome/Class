# Import Modules
from ciscoconfparse import CiscoConfParse

# Parse Configuration File
cisco_config = CiscoConfParse("cisco_ipsec.txt")

# Find Crypto Objects with Specific Children
crypto_specific = cisco_config.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

# Print Crypto Objects
for i in crypto_specific:
    print(i.text)
    for child in i.children:
        print(child.text)
