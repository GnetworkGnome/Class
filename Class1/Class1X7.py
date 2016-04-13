# Import Modules

import yaml, json

# Read YAML File

with open("gnome_list.yml") as f:
    gnome_yaml = yaml.load(f)

# Read JSON File

with open("gnome_list.json") as f:
    gnome_json = json.load(f)

# Print Out Variations

print("The following is the YAML List:")
print(gnome_yaml)
print("\nThe follwing is the JSON List:")
print(gnome_json)
