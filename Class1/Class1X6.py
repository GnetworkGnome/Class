# Import Modules
import yaml, json

# Create a List

my_list = ["Gnomes Rock.", "Gnomes are needed for Getworking."]
my_list.append({})
my_list[-1]['gnome_address'] = '17.17.17.17'
my_list[-1]['Gnomes'] = list(range(17))

# Write List to YAML File

with open("gnome_list.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

# Write List to JSON File

with open("gnome_list.json", "w") as f:
    json.dump(my_list, f)
