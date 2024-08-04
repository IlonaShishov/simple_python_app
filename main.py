import yaml

# Define some data to write to a YAML file
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}

# Write the data to a YAML file
with open('data.yaml', 'w') as file:
    yaml.dump(data, file)

print("Data has been written to data.yaml")

# Read the data back from the YAML file
with open('data.yaml', 'r') as file:
    loaded_data = yaml.safe_load(file)

print("Data read from data.yaml:")
print(loaded_data)
