import tomllib

generate_dir = "./src/datapack/data/raw_ores_processing/recipes/"

with open("./data/items.toml", "rb") as file:
    items_data = tomllib.load(file)
