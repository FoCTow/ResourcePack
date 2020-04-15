#----------------------------------------------------------------------------------------------------------
PATH_MINECRAFT = r"AppData\Roaming\.minecraft"
PATH_TEXTURES = r"\resourcepacks"
#----------------------------------------------------------------------------------------------------------
NAME_BASE = "LoliLife"
NAME_SUFFIX = [128, 256, 512]
NAME_SUFFIX_RAW = "Raw"
NAME_PACKS = [("{}{}".format(NAME_BASE, name_suffix)) for name_suffix in NAME_SUFFIX]
#----------------------------------------------------------------------------------------------------------
COPY_MODELS = r"\assets\minecraft\models"
COPY_BLOCKSTATES = r"\assets\minecraft\blockstates"
#----------------------------------------------------------------------------------------------------------
COPY_QUE = [COPY_MODELS, COPY_BLOCKSTATES]
#----------------------------------------------------------------------------------------------------------