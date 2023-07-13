from typing import Final
import tomllib

with open("./data/items.toml", "rb") as file:
    ITEMS_DATA: Final[dict[str, dict[str, str]]] = tomllib.load(file)
    
mod_ids = ["- " + i for i in ITEMS_DATA]

with open("./data/mod_ids.md", "w") as md_file:
    md_file.writelines("\n".join(mod_ids))
