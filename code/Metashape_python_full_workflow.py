import Metashape
import os, sys, time

# Checking compatibility
compatible_major_version = "1.8"
found_major_version = ".".join(Metashape.app.version.split('.')[:2])
if found_major_version != compatible_major_version:
    raise Exception("Incompatible Metashape version: {} != {}".format(found_major_version, compatible_major_version))

def find_files(folder, types):
    return [entry.path for entry in os.scandir(folder) if (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]

if len(sys.argv) < 3:
    print("Usage: general_workflow.py <image_folder> <output_folder>")
    sys.exit(1)

image_folder = sys.argv[1]
output_folder = sys.argv[2]

photos = find_files(image_folder, [".jpg", ".jpeg", ".tif", ".tiff"])

doc = Metashape.Document()
doc.save(output_folder + '/project.psx')

chunk = doc.addChunk()

chunk.addPhotos(photos)
doc.save()

print(str(len(chunk.cameras)) + " images loaded")

#chunk = PhotoScan.app.document.chunk
out_crs = Metashape.CoordinateSystem("EPSG::26913") #user-defined crs
for camera in chunk.cameras:
    if camera.reference.location:
        camera.reference.location = Metashape.CoordinateSystem.transform(camera.reference.location, chunk.crs, out_crs)
for marker in chunk.markers:
    if marker.reference.location:
        marker.reference.location = Metashape.CoordinateSystem.transform(marker.reference.location, chunk.crs, out_crs)
chunk.crs = out_crs
doc.save()
chunk.updateTransform()
doc.save()

print(" CoordinateSystem updated")

chunk.analyzePhotos()

for i in range(0, len(chunk.cameras)):
    print(i)
    camera = chunk.cameras[i]
    print(camera)
    quality = camera.frames[0].meta["Image/Quality"]
    print(quality)
    if float(quality) < 0.804: #add quality threshold
        camera.enabled = False

doc.save()

chunk.matchPhotos(keypoint_limit = 40000, tiepoint_limit = 10000, generic_preselection = True, reference_preselection = True)
doc.save()

chunk.alignCameras()
doc.save()

chunk.buildDepthMaps(downscale = 2, filter_mode = Metashape.MildFiltering)
doc.save()

chunk.buildModel(source_data = Metashape.DepthMapsData)
doc.save()


chunk.buildDenseCloud(point_colors=True, point_confidence=True, keep_depth=True, max_neighbors=100, subdivide_task=True, workitem_size_cameras=20)
doc.save()

chunk.buildDem(source_data=Metashape.PointCloudData)
doc.save()

chunk.buildOrthomosaic(surface_data=Metashape.ElevationData)
doc.save()

chunk.exportReport(output_folder + '/report.pdf')

chunk.exportRaster(output_folder + '/dsm.tif', source_data = Metashape.ElevationData)

chunk.exportRaster(output_folder + '/orthomosaic.tif', source_data = Metashape.OrthomosaicData)

chunk.exportPoints(output_folder + '/point_cloud.las', source_data = Metashape.PointCloudData, block_width=10, block_height=10)

print('Processing finished, results saved to ' + output_folder + '.')
