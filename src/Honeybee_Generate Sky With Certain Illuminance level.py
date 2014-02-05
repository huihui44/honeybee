"""
Genrate a Uniform CIE Sky Based on Illuminace Value
-
Provided by Honybee 0.0.10
    
    Args:
        _illuminanceValue : Desired value for horizontal sky illuminance in Lux
    Returns:
        skyFilePath: Sky file location on the local drive

"""

ghenv.Component.Name = "Honeybee_Generate Sky With Certain Illuminance level"
ghenv.Component.NickName = 'genSkyIlluminanceLevel'
ghenv.Component.Message = 'VER 0.0.42\nJAN_24_2014'
ghenv.Component.Category = "Honeybee"
ghenv.Component.SubCategory = "2 | Daylight | Sky"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

import os

def RADDaylightingSky(illuminanceValue):
    
    # gensky 12 4 +12:00 -c -B 55.866 > skies/sky_10klx.mat
    
    return  "# start of sky definition for daylighting studies\n" + \
            "# horizontal sky illuminance: " + `illuminanceValue` + " lux\n" + \
            "!gensky 12 6 12:00 -u -B " +  '%.3f'%(illuminanceValue/179) + "\n" + \
            "skyfunc glow sky_mat\n" + \
            "0\n" + \
            "0\n" + \
            "4\n" + \
            "1 1 1 0\n" + \
            "sky_mat source sky\n" + \
            "0\n" + \
            "0\n" + \
            "4\n" + \
            "0 0 1 180\n" + \
            "skyfunc glow ground_glow\n" + \
            "0\n" + \
            "0\n" + \
            "4\n" + \
            "1 .8 .5 0\n" + \
            "ground_glow source ground\n" + \
            "0\n" + \
            "0\n" + \
            "4\n" + \
            "0 0 -1 180\n" + \
            "# end of sky definition for daylighting studies\n\n"


def main(illuminanceValue):
    
    path  = "c:/Ladybug/skylib/basedOnIlluminanceLevel/"
    
    if not os.path.isdir(path): os.mkdir(path)
    
    outputFile = path + `int(illuminanceValue)` + "_lux.sky"
    
    skyStr = RADDaylightingSky(illuminanceValue)
    
    skyFile = open(outputFile, 'w')
    skyFile.write(skyStr)
    skyFile.close()
    
    return outputFile , "Sky with horizontal illuminance of: " + `illuminanceValue` + " lux"
    
if not _illuminanceValue: _illuminanceValue = 1000
skyFilePath, skyDescription = main(_illuminanceValue)