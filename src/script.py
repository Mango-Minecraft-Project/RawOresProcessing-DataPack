from json import dump, loads

# default = {
#     "type": "{type}",
#     "group": "rawOres",
#     "ingredient": [
#         {
#             "item": "{modid}:raw_{ore}_block"
#         }
#     ],
#     "result": "{modid}:{ore}_block",
#     "experience": "{experience}",
#     "cookingtime": "{cookingtime}"
# }

default = '{"type": "{type}","group": "rawOres","ingredient": [{"item": "{modid}:raw_{ore}_block"}],"result": "{modid}:{ore}_block","experience": "{experience}","cookingtime": "{cookingtime}"}'

for modid, ore in zip(("minecraft", "minecraft", "minecraft", "create", ), 
                      ("iron", "copper", "gold", "zinc", )):
    new = loads(default)
    new["ingredient"][0]["item"] = f'{modid}:raw_{ore}_block'
    new["result"] = f'{modid}:{ore}_block'
    for type, exp, time in (("smelting", 6.3, 1800),
                            ("blasting", 6.3, 900)):
        new["experience"] = exp
        new["cookingtime"] = time
        new["type"] = type
        with open(f'./[ROP-D] Raw Ores Processing Datapack/data/raw_ores_processing/recipes/{modid}_{ore}_{type}.json', 'w') as file:
            dump(new, file, indent=4)