from packages.local_data import *

mod_ids = ["- " + i for i in items_data]

with open("./data/mod_ids.md", "w") as md_file:
    md_file.writelines("\n".join(mod_ids))
