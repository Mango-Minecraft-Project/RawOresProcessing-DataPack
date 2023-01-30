import os
import tomllib
import json
from os import path

result_path = './src/generator/result/'
# result_path = './src/datapack/data/raw_ores_processing/'
items_path = './src/generator/items.toml'

with open(items_path, 'rb') as file:
    items_data = tomllib.load(file)

for modid, items in items_data.items():
    correct_path = result_path + modid
    if not path.isdir(correct_path):
        os.mkdir(correct_path)
    for ingredient, result in items.items():
        for type, cookingtime in (('blasting', 900), ('smelting', 1800)):        
            data = {
                "type": f"minecraft:{type}",
                "ingredient": [
                    {
                        "item": f"{modid}:{ingredient}"
                    }
                ],
                "result": f"{modid}:{result}",
                "experience": 3.6,
                "cookingtime": cookingtime
            }
            if modid != 'minecraft':
                data = {
                    "fabric:load_conditions": [
                        {
                            "condition": "fabric:all_mods_loaded",
                            "values": [
                                modid
                            ]
                        }
                    ],
                    "conditions": [
                        {
                            "type": "forge:mod_loaded",
                            "modid": modid
                        }
                    ]
                } | data
            
            with open(f'{correct_path}/{modid}_{result}_{type}.json', 'w') as file:
                json.dump(data, file, indent=2)
        