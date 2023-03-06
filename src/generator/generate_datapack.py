import json
from os import path, mkdir

from packages.local_data import *


def gen_json(mod_id: str, ingredient_item: str, result_item: str, type: str) -> dict:
    ingredient_item = f"{(mod_id + ':') * ((':' in ingredient_item)^1)}{ingredient_item}"
    result_item = f"{(mod_id + ':') * ((':' in result_item)^1)}{result_item}"
    
    data = {
        "type": f"minecraft:{type}",
        "ingredient": [{"item": f"{ingredient_item}"}],
        "result": f"{result_item}",
        "experience": 3.6,
        "cookingtime": 900,
    }
    if mod_id != "minecraft":
        data = {
            "fabric:load_conditions": [
                {"condition": "fabric:all_mods_loaded", "values": [mod_id]}
            ],
            "forge:conditions": [{"type": "forge:mod_loaded", "modid": mod_id}],
        } | data
    return data


for mod_id, items in items_data.items():

    mod_path = generate_dir + mod_id
    if not path.isdir(mod_path):
        mkdir(mod_path)

    for ingredient_item, result_item in items.items():
        for type in {"blasting", "smelting"}:
            with open(f"{mod_path}/{ingredient_item}_{type}.json", "w") as json_file:
                json.dump(
                    obj=gen_json(mod_id, ingredient_item, result_item, type),
                    fp=json_file,
                    indent=2,
                )
