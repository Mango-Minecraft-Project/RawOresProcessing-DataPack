import json
import tomllib
from typing import Final
from os import path, mkdir

GENERATE_DIR: Final[str] = "./src/datapack/data/raw_ores_processing/recipes/"

with open("./data/items.toml", "rb") as file:
    ITEMS_DATA: Final[dict[str, dict[str, str]]] = tomllib.load(file)

SORT_KEYS: Final[list[str]] = [
    "fabric:load_conditions",
    "conditions",
    "type",
    "ingredient",
    "result",
    "experience",
    "cookingtime",
]


def generate_json(
    namespace: str,
    ingredient_id: str,
    result_id: str,
    recipe_type: str,
    cooking_time: int,
) -> dict:
    if ":" not in ingredient_id:
        ingredient_id = f"{namespace}:{ingredient_id}"
    if ":" not in result_id:
        result_id = f"{namespace}:{result_id}"

    recipe_data = {
        "type": f"minecraft:{recipe_type}",
        "ingredient": [{"item": f"{ingredient_id}"}],
        "result": f"{result_id}",
        "experience": 3.6,
        "cookingtime": cooking_time,
    }
    if namespace != "minecraft":
        recipe_data |= {
            "fabric:load_conditions": [
                {"condition": "fabric:all_mods_loaded", "values": [namespace]}
            ],
            "conditions": [{"type": "forge:mod_loaded", "modid": namespace}],
        }

    return dict(sorted(recipe_data.items(), key=lambda item: SORT_KEYS.index(item[0])))


for namespace, mod_items in ITEMS_DATA.items():
    data_path = GENERATE_DIR + namespace
    if not path.isdir(data_path):
        mkdir(data_path)

    for ingredient_id, result_id in mod_items.items():
        for recipe_type, cooking_time in (("blasting", 900), ("smelting", 1800)):
            recipe_path = f"{data_path}/{ingredient_id}_{recipe_type}.json"
            recipe_data = generate_json(
                namespace, ingredient_id, result_id, recipe_type, cooking_time
            )
            with open(recipe_path, "w") as json_file:
                json.dump(recipe_data, json_file, indent=2)
