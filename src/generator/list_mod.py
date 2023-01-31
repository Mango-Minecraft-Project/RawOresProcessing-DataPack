import tomllib

with open('./src/generator/items.toml', 'rb') as file:
    data = tomllib.load(file)

with open('./src/generator/modlist.txt', 'w') as file:
    file.writelines('\n'.join(f'- {mod}' for mod in sorted([*data.keys()]) if mod != 'minecraft'))