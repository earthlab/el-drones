import geopandas as gpd
import os, sys

def decdeg2dms(dd):
    
    ''' grabbed from 
    https://stackoverflow.com/questions/2579535/convert-dd-decimal-degrees-to-dms-degrees-minutes-seconds-in-python'''
    
    is_positive = dd >= 0
    dd = abs(dd)
    minutes,seconds = divmod(dd*3600,60)
    degrees,minutes = divmod(minutes,60)
    degrees = degrees if is_positive else -degrees
    return (degrees,minutes,seconds)

# generate NOTAM formatted X-Y coordinate and overwrite
def genNOTAMcoord(poly):
    
    # get DMS for centroid
    x, y = poly.centroid.x, poly.centroid.y
    x_dms = decdeg2dms(x)
    y_dms = decdeg2dms(y)
    
    # construct the string
    if (x_dms[0] < 0) and (y_dms[0] < 0): # W and S
    
        notam_str = '{0}{1}{2:1.1f}S{3}{4}{5:1.1f}W'.format(int(-y_dms[0]), int(y_dms[1]), int(y_dms[2]),
                                                            int(-x_dms[0]), int(x_dms[1]), int(x_dms[2]))
    
    elif (x_dms[0] > 0) and (y_dms[0] < 0): # E and S

        notam_str = '{0}{1}{2:1.1f}S{3}{4}{5:1.1f}E'.format(int(-y_dms[0]), int(y_dms[1]), int(y_dms[2]),
                                                            int(x_dms[0]), int(x_dms[1]), int(x_dms[2]))

    elif (x_dms[0] < 0) and (y_dms[0] > 0): # W and N (CONUS)

        notam_str = '{0}{1}{2:1.1f}N{3}{4}{5:1.1f}W'.format(int(y_dms[0]), int(y_dms[1]), int(y_dms[2]),
                                                            int(-x_dms[0]), int(x_dms[1]), int(x_dms[2]))

    else: # E and N

        notam_str = '{0}{1}{2:1.1f}N{3}{4}{5:1.1f}E'.format(int(y_dms[0]), int(y_dms[1]), int(y_dms[2]),
                                                            int(x_dms[0]), int(x_dms[1]), int(x_dms[2]))
        
    return notam_str
    

shp = '../boulder_area_aois.shp'
df = gpd.read_file(shp) # change CRS to 4326 if not already

# get the geometry and generate the coordinate
geom = df.geometry[0]
genNOTAMcoord(geom)

