@echo [BOROH]BlockOfRawOreHandle便捷开发工具 by.STRVS
@echo 温馨提示:请勿连续输出相同的,会崩的
@set /p m=ModID:
@set /p i=ItemID:
@echo ============================================================
@echo 正在加载……
@echo ============================================================
@echo 请将这些文件放在
@echo [BOROH]BlockOfRawOreHandle\data\boroh\recipes(已经自动放置成功)
@echo ============================================================
@echo 熔炉文件:
@echo raw_%m%_%i%_smelting.json
@echo ============================================================
@echo 正在输出文件……
@echo {>>data\boroh\recipes\raw_%m%_%i%_smelting.json
@echo.  "type": "minecraft:smelting",>>data\boroh\recipes\raw_%m%_%i%_smelting.json
@echo.  "group": "boroh",>>data\boroh\recipes\raw_%m%_%i%_smelting.json
@echo.  "ingredient": [>>data\boroh\recipes\raw_%m%_%i%_smelting.json
@echo.    {>>data\boroh\recipes\raw_%m%_%i%_smelting.json
@echo.      "item": "%m%:raw_%i%_block">>data\boroh\recipes\raw_%m%_%i%_smelting.json
@echo.    }>>data\boroh\recipes\raw_%m%_%i%_smelting.json
@echo.  ],>>data\boroh\recipes\raw_%m%_%i%_smelting.json
@echo.  "result": "%m%:%i%_block",>>data\boroh\recipes\raw_%m%_%i%_smelting.json
@echo.  "experience": 2.7,>>data\boroh\recipes\raw_%m%_%i%_smelting.json
@echo.  "cookingtime": 1800>>data\boroh\recipes\raw_%m%_%i%_smelting.json
@echo.}>>data\boroh\recipes\raw_%m%_%i%_smelting.json
@echo ============================================================
@echo 高炉文件:
@echo raw_%m%_%i%_blasting.json
@echo ============================================================
@echo 正在输出文件……
@echo {>>data\boroh\recipes\raw_%m%_%i%_blasting.json
@echo.  "type": "minecraft:blasting",>>data\boroh\recipes\raw_%m%_%i%_blasting.json
@echo.  "group": "boroh",>>data\boroh\recipes\raw_%m%_%i%_blasting.json
@echo.  "ingredient": [>>data\boroh\recipes\raw_%m%_%i%_blasting.json
@echo.    {>>data\boroh\recipes\raw_%m%_%i%_blasting.json
@echo.      "item": "%m%:raw_%i%_block">>data\boroh\recipes\raw_%m%_%i%_blasting.json
@echo.    }>>data\boroh\recipes\raw_%m%_%i%_blasting.json
@echo.  ],>>data\boroh\recipes\raw_%m%_%i%_blasting.json
@echo.  "result": "%m%:%i%_block",>>data\boroh\recipes\raw_%m%_%i%_blasting.json
@echo.  "experience": 3.6,>>data\boroh\recipes\raw_%m%_%i%_blasting.json
@echo.  "cookingtime": 800>>data\boroh\recipes\raw_%m%_%i%_blasting.json
@echo.}>>data\boroh\recipes\raw_%m%_%i%_blasting.json
@echo ============================================================
@echo 文件输出成功!
@echo 已添加由%m%:raw_%i%_block烧制成%m%:%i%_block的配方!
@echo 如果是如果是之前的存档请/reload刷新数据包!
@echo 如果需要,请继续添加:
%0