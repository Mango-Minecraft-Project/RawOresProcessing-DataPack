import os
import tomllib
import json
from os import path

result_paths = ['./src/generator/result/', './src/datapack/data/raw_ores_processing/']
items_path = './src/generator/items.toml'

with open(items_path, 'rb') as file:
    items_data = tomllib.load(file)

logs = []

def log(string: str, level: int = 0):
    string = '  '*level + string
    logs.append(string + '\n')
    print(string)

for modid, items in items_data.items():
    log(f'{modid = }, {items = }')
    for result_path in result_paths:
        correct_path = result_path + modid
        log(f'{result_path = }, {correct_path = }', 1)
        if not path.isdir(correct_path):
            os.mkdir(correct_path)
            log(f'mkdir {correct_path}', 2)
        for ingredient, result in items.items():
            log(f'{ingredient = }, {result = }', 2)
            for type, cookingtime in (('blasting', 900), ('smelting', 1800)):        
                log(f'{type = }, {cookingtime = }', 3)
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

with open('./src/generator/run.log', 'w') as file:
    file.writelines(logs)