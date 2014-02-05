"""
Set Exposure for HDR
-
Provided by Honybee 0.0.10
    
    Args:
        HDRFilePath: Path to an HDR image file
        exposure: A number between 0 and 1
        render: Set to True to render the new image
    Returns:
        outputFilePath: Path to the result HDR file

"""

ghenv.Component.Name = "Honeybee_Set Exposure for HDR"
ghenv.Component.NickName = 'setHDRExposure'
ghenv.Component.Message = 'VER 0.0.42\nJAN_24_2014'
ghenv.Component.Category = "Honeybee"
ghenv.Component.SubCategory = "4 | Daylight | Daylight"
ghenv.Component.AdditionalHelpFromDocStrings = "3"

import os
import scriptcontext as sc
import Grasshopper.Kernel as gh

def main():
    
    # import the classes
    if sc.sticky.has_key('honeybee_release'):
        hb_folders = sc.sticky["honeybee_folders"]
        hb_RADPath = hb_folders["RADPath"]
        hb_RADLibPath = hb_folders["RADLibPath"]
        
    else:
        print "You should first let Honeybee to fly..."
        w = gh.GH_RuntimeMessageLevel.Warning
        ghenv.Component.AddRuntimeMessage(w, "You should first let Honeybee to fly...")
        return
    
    # check for pfilt.exe
    if not os.path.isfile(hb_RADPath + "\\pfilt.exe"):
        msg = "Cannot find pfilt.exe at " + hb_RADPath + \
              "Make sure that Radiance is fully installed on your system."
        ghenv.Component.AddRuntimeMessage(gh.GH_RuntimeMessageLevel.Warning, msg)
        return
        
    validExt = ["HDR", "PIC"]
    if HDRFilePath.split('.')[-1].upper() not in validExt:
        msg = "Input file is not a valid HDR file."
        ghenv.Component.AddRuntimeMessage(gh.GH_RuntimeMessageLevel.Warning, msg)
        return
    else:
        inputFilePath = HDRFilePath.replace("\\" , "/")
        fileAddress = inputFilePath.replace(inputFilePath.split("/")[-1], "")
        fileName = "".join(inputFilePath.split("/")[-1].split('.')[:-1])
        outputFile = fileAddress + fileName + "@exp_" + "%.3f"%exposure + ".HDR"
        
    batchStr = "SET RAYPATH=.;" + hb_RADLibPath + "n" + \
                "PATH=" + hb_RADPath + ";$PATH\n\n" + \
           "pfilt -e " + "%.3f"%exposure + " " + inputFilePath + " > " + outputFile + \
           "\nexit"
    
    batchFileName = fileAddress + 'SETEXPOSURE.BAT'
    batchFile = open(batchFileName, 'w')
    batchFile.write(batchStr)
    batchFile.close()
    os.system("start /min /B /wait " + batchFileName)
    return outputFile


if HDRFilePath and render:
    if exposure == None: exposure = 1
    outputFilePath = main()