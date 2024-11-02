import json
import tomllib
from typing import Final, Literal
from shutil import make_archive, copy
from pathlib import Path


CWD: Final[Path] = Path.cwd()
DATAPACK_RELEASE_VERSION: Final[int] = "1.6"

DATAPACK_DIR: Final[Path] = CWD / "src/datapack"

GENERATE_DIRS: Final[dict[str, Path]] = {
    "1.13-1.20.2": DATAPACK_DIR / "1.13-1.20.2/data/raw_ores_processing/recipes",
    "1.20.3-1.21.1": DATAPACK_DIR / "1.20.3-1.21.1/data/raw_ores_processing/recipe",
    "1.21.2+": DATAPACK_DIR / "1.21.2+/data/raw_ores_processing/recipes",
}


with open(CWD / "data/items.toml", "rb") as file:
    ITEMS_DATA: Final[dict[str, dict[str, str]]] = tomllib.load(file)

SORT_KEYS: Final[list[str]] = [
    "neoforge:conditions",
    "conditions",
    "fabric:load_conditions",
    "type",
    "ingredient",
    "result",
    "experience",
    "cookingtime",
]


def sort_dict(_dict: dict) -> dict:
    return dict(sorted(_dict.items(), key=lambda item: SORT_KEYS.index(item[0])))


def generate_json(
    namespace: str,
    ingredient_id: str,
    result_id: str,
    recipe_type: str,
    cooking_time: int,
    mode: Literal["1.13-1.20.2", "1.20.3-1.21.1", "1.21.2+"],
) -> dict:
    if ":" not in ingredient_id:
        ingredient_id = f"{namespace}:{ingredient_id}"
    if ":" not in result_id:
        result_id = f"{namespace}:{result_id}"

    recipe_data = {
        "type": f"minecraft:{recipe_type}",
        "experience": 3.6,
        "cookingtime": cooking_time,
    }

    match mode:
        case "1.13-1.20.2":
            recipe_data |= {
                "ingredient": [{"item": ingredient_id}],
                "result": result_id,
            }
        case "1.20.3-1.21.1":
            recipe_data |= {
                "ingredient": {"item": ingredient_id},
                "result": {"id": result_id},
            }
        case "1.21.2+":
            recipe_data |= {
                "ingredient": ingredient_id,
                "result": {"id": result_id},
            }

    if namespace != "minecraft":
        recipe_data |= {
            "fabric:load_conditions": [
                {
                    "type": "fabric:and",
                    "values": [
                        {"type": "fabric:mod_loaded", "modid": namespace},
                        {"type": "fabric:item_exists", "item": ingredient_id},
                        {"type": "fabric:item_exists", "item": result_id},
                    ],
                }
            ],
            "conditions": [
                {
                    "type": "forge:and",
                    "values": [
                        {"type": "forge:mod_loaded", "modid": namespace},
                        {"type": "forge:item_exists", "item": ingredient_id},
                        {"type": "forge:item_exists", "item": result_id},
                    ],
                }
            ],
            "neoforge:conditions": [
                {
                    "type": "neoforge:and",
                    "values": [
                        {"type": "neoforge:mod_loaded", "modid": namespace},
                        {"type": "neoforge:item_exists", "item": ingredient_id},
                        {"type": "neoforge:item_exists", "item": result_id},
                    ],
                }
            ],
        }

    return sort_dict(recipe_data)


for support_version_range, GENERATE_DIR in GENERATE_DIRS.items():
    for namespace, mod_items in ITEMS_DATA.items():
        data_path = GENERATE_DIR / namespace
        data_path.mkdir(parents=True, exist_ok=True)

        for ingredient_id, result_id in mod_items.items():
            for recipe_type, cooking_time in (("blasting", 900), ("smelting", 1800)):
                recipe_path = data_path / f"{ingredient_id}_{recipe_type}.json"
                recipe_data = generate_json(
                    namespace, ingredient_id, result_id, recipe_type, cooking_time, support_version_range
                )
                with open(recipe_path, "w") as json_file:
                    json.dump(recipe_data, json_file, indent=2)

    target_dir = DATAPACK_DIR / support_version_range

    copy(
        DATAPACK_DIR / "pack.mcmeta",
        target_dir / "pack.mcmeta",
    )
    copy(
        DATAPACK_DIR / "pack.png",
        target_dir / "pack.png",
    )
    make_archive(
        CWD / f"src/generator/result/Raw-Ore-Processing_v{DATAPACK_RELEASE_VERSION}_{support_version_range}",
        "zip",
        target_dir,
    )
