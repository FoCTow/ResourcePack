#----------------------------------------------------------------------------------------------------------
import shutil
import os
#----------------------------------------------------------------------------------------------------------
from pathlib import Path
#----------------------------------------------------------------------------------------------------------
from . import attributes as AT
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
def run():
    #------------------------------------------------------------------------------------------------------
    overwriteFiles()
#----------------------------------------------------------------------------------------------------------
def getTexturePATH():
    #------------------------------------------------------------------------------------------------------
    userPATH = str(Path.home())
    #------------------------------------------------------------------------------------------------------
    return r"{}\{}{}".format(userPATH, AT.PATH_MINECRAFT, AT.PATH_TEXTURES )
#----------------------------------------------------------------------------------------------------------
def getSourcePATH():
    #------------------------------------------------------------------------------------------------------
    texturePATH = getTexturePATH()
    #------------------------------------------------------------------------------------------------------
    return r"{}\{}{}".format(texturePATH, AT.NAME_BASE, AT.NAME_SUFFIX_RAW)
#----------------------------------------------------------------------------------------------------------
def getTargetPaths():
    #------------------------------------------------------------------------------------------------------
    texturePATH = getTexturePATH()
    #------------------------------------------------------------------------------------------------------
    return [(r"{}\{}".format(texturePATH, packNAME)) for packNAME in AT.NAME_PACKS]
#----------------------------------------------------------------------------------------------------------
def overwriteFiles():
    #------------------------------------------------------------------------------------------------------
    sourcePATH = getSourcePATH()
    targetPATHS = getTargetPaths()
    #------------------------------------------------------------------------------------------------------
    for targetPATH in targetPATHS:
        for copyPATH in AT.COPY_QUE:
            #----------------------------------------------------------------------------------------------
            og = r"{}{}".format(sourcePATH, copyPATH)
            copy = r"{}{}".format(targetPATH, copyPATH)
            #----------------------------------------------------------------------------------------------
            #print("os.path.isdir({}) = {}".format(copy, os.path.isdir(copy)))
            #----------------------------------------------------------------------------------------------
            if os.path.isdir(copy): shutil.rmtree(copy)
            shutil.copytree(og, copy)
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------


