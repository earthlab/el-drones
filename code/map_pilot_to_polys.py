from xml.etree import ElementTree as ET
import pandas as pd
import geopandas as gpd
from shapely.geometry import box, Polygon, Point
from fiona.crs import from_epsg
import sys
import os

if __name__ == '__main__':
    
    print(sys.argv)
    
    f = sys.argv[1]
    
    if len(sys.argv) > 2:
        outfile = sys.argv[2]
    else:
        print ('no output provided, using input filename')
        outfile = os.path.basename(f).split('.')[0] + '.shp'
    
    
    # parse the tree and get the bounding box and waypoint arrays
    tree = ET.parse(f)
    root = tree.getroot()[0]
    bb, wp = root.findall('array')
    
    # record the coordinates
    bb_lons, bb_lats = [],[]
    for coord in bb:
        bb_lons.append(float(coord[0].text.strip()))
        bb_lats.append(float(coord[1].text.strip()))
        
    
    wp_lons, wp_lats = [],[]
    for coord in wp:
        wp_lons.append(float(coord[0].text.strip()))
        wp_lats.append(float(coord[1].text.strip()))
        
    
    # make a polygon for the bounding box
    bb_minx = min(bb_lons)
    bb_maxx = max(bb_lons)
    bb_miny = min(bb_lats)
    bb_maxy = max(bb_lats)
    bbox = box(bb_minx, bb_miny, bb_maxx, bb_maxy)

    # make a polygon for the waypoints using the convex hull
    wp_points = [Point(x,y) for x,y in zip(wp_lons, wp_lats)]

    pts_df = gpd.GeoDataFrame({'geometry': wp_points}, crs=from_epsg(4326))

    poly_list = [bbox, pts_df.unary_union.convex_hull]
    desc = ['bounding box', 'convex hull from waypoints']

    # save to outfile
    poly_gdf = gpd.GeoDataFrame({'geometry':poly_list, 'desc': desc}, crs=from_epsg(4326))
    poly_gdf.to_file(outfile)

    




