import shutil

version = '1.2'

shutil.make_archive(
    base_name = f'./src/generator/result/Raw-Ore-Processing-v{version}',
    format = 'zip',
    root_dir = './src/datapack/'
)