This document is a working guide for planning UAV missions using the Map Pilot software. Major source of information is Megan Cattau's [UASWorkflows repo](https://github.com/mcattau/UASWorkflows) 

#### Map Pilot (MP) product  
- Designed by Maps Made Easy. They're quick to respond to user questions and feedback  
- Compatible only with DJI products and works only on iOS. Easier to use on iPad than on iPhone due to larger screen. [General FAQs and guides for MP for DJI](https://support.dronesmadeeasy.com/hc/en-us/categories/200739936-Map-Pilot-for-DJI)
- Base version $9.99. Business version (has terrain awareness) is one-time $40  
    - Terrain awareness allows for a consistent GSD despite terrain changes. MP uses specially formatted SRTM data at 30m res from 2000 between 60N and 56S latitudes. It’s coarse and will miss things <30m res and/or appearing after 2000.    
- Mike, Megan, Anna, Joe have experience with Map Pilot  

#### Workflow to create a new mission in MP 
1. In MP app, click *New Mission* in menu  
2. Establish area of interest (AOI)  
    1. Download/create .kml of AOI on computer  
    2. Email KML to yourself  
    3. In device used for flying (e.g., iPad), open email > right-click KML > tap share icon > tap MP icon (MP must be open for this to work)   
3. Set flight boundary to match KML boundary:  
    1. Hold down with one finger to set boundary point (orange circle). Repeat 2 more times. Hold and drag these nodes to move them. Single tap to remove a node
    2. Hold down a midpoint (small orange circle) and move to create more boundary points. 
4. Flight plan will automatically be generated
    - You can [simulate a planned flight](https://support.dronesmadeeasy.com/hc/en-us/articles/211468103-In-App-Simulator). Try in airplane mode to make sure it will work in remote area


#### Configure parameters for desired mission  
1. Open *Options* pullout menu (top)  
2. Click *Terrain Awareness* to see terrain changes  
    - Saving the mission (with Terrain Awareness enabled?) will cache the terrain data as well  
3. Configure flight path type to norm, grid, or lines  
4. Specify overlap (90-95% for forests)   
5. Max speed – leave at 15 m/s. User can set max speed, but max speed of mission is calculated based on other parameters. Lower flight altitudes, higher overlap, and lower light conditions require slower movement (it’s limited by how quickly pics can be taken and stored).   
6. Set max time or battery limited. If time, drone will return to home and land close to that time. If battery limited, will return to home with low battery.  
7. Offset. You would use this if you were taking off / landing higher or lower than your mapping plane. This adds to / subtracts from the altitude selected in the Altitude Adjustment pullout menu below. For example, if you wanted to have the pixel size you specified in the Altitude Adjustment pullout menu at the top of the canopy, you would increase the offset value to the average height of those trees. If trees are on average 10m high, you would specify a 10m offset. Works with Terrain Awareness. *Note: flight below takeoff level is hard to maintain RC link (e.g., when flying down into a canyon).*


#### Edit an existing mission
1. In MP app, go to *Mission Management* menu item > Select saved mission
2. To edit the name of an existing mission, wwipe right on the mission name > tap *Edit*
3. Edit the configuration of a mission, tap on desired mission > tap unlock (top left) > make any adjustments > tap floppy disk icon to save. ***Note:** You cannot simply update an existing mission. When you edit and save an existing mission, it saves a new mission with a new name*  
4. To delete a mission, swipe right on the mission name > tap *Delete*


#### Questions from using MP in the field
Q: We had a windy flight within a mission. Is there a feature where we can just re-fly that one segment within a flight?  
A: Try manual restart - [MP forum post](https://support.dronesmadeeasy.com/hc/en-us/articles/115005940746-Manual-Restarting-Point)

Q: Does MP plan on updating their DEM?  
A: When you plan a mission, SRTM is the default, but there could be other DEMs to choose from that you can load directly from Maps Made Easy - [related MP forum post](https://support.dronesmadeeasy.com/hc/en-us/articles/360000745623-Custom-Terrain-Source-for-Terrain-Awareness)    
A: You can also upload your own DEM to use, but this costs 2 Maps made Easy points per acre 

Q: We are restarting the MP app nearly every time we change a battery (i.e., the airplane button to upload the flight won't pop up without restarting the app)  
A: Check to make sure we don't have the DJI Go app open too - [related MP forum post](https://support.dronesmadeeasy.com/hc/en-us/community/posts/204318736-Clarification-on-Multiple-Battery-Missions )  
A: You may want to try unplugging the iOS device and then plugging it back in to force a reconnection when this happens - [MP forum post](https://support.dronesmadeeasy.com/hc/en-us/community/posts/360048220952-Have-to-restart-Map-Pilot-after-battery-change)

*Unanswered Questions*
*Q: What is Active Connect? Connectionless mode uses distance aircraft has traveled to trigger camera, but the pictures will likely be less uniform throughout the mission.*  
*Q: Does a flight plan buffer your AOI and by how much?*  
*Q: Are flight metrics attached to model of drone? The overlap isn’t sensor specific, so how does this work with different FOVs?*  
*Q: Do you need to have terrain awareness enabled to cache the SRTM data when you save a mission, or is the SRTM data cached anytime you save a mission*  
