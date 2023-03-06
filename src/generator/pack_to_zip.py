from shutil import make_archive

VERSION = "1.3"

make_archive(
    base_name=f"./src/generator/result/Raw-Ore-Processing-v{VERSION}",
    format="zip",
    root_dir="./src/datapack/",
)
