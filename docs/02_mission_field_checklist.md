This document is a working checklist for executing an automated UAV flight. Map Pilot is used for mission planning. Checklist was put together with forest ecology applications using the Phantom 4 Pro in mind. Major source of information is Megan Cattau's [UASWorkflows repo](https://github.com/mcattau/UASWorkflows) 

#### A couple days before going into the field
- Contact any landowners / managers as a courtesy and to see if there are wildlife closures that aren’t updated online
- Assemble items from the Equipment List and make sure all electronics are charged  
    - Estimate the number of GCPs needed for AOI (is there a rule of thumb?)

#### Field protocol - morning of field day
- Check [NOTAM](https://www.1800wxbrief.com/Website/uoa) to see if anyone else has posted a NOTAM nearby  
- If applicable, contact land managers to remind them that we're flying  
    - For Cold Springs, call (1) the Fort Collins Interagency Dispatch Center 970.295.6800 and (2) the Boulder Regional Communication Center 303.441.4444 to let them know that we'll be there (day, time, est location and duration, as well as contact name and info of on-site lead)  
    
#### Field protocol - pre-mission tasks 
1. Keep electronics temperature-regulated (in shade during warm weather, in car during cold weather)
2. Set out GCPs well-spaced, placing some near edges and in interior of the AOI.  
3. Take GPS measurements at each GCP and make notes to help find GCP in imagery later
4. Identify a good launch point and place any landing platform down
5. Remove the sensor cover from the UAS
6. Brush the sensor to clean it
7. Check that an SD card is inserted
8. Set the UAS on the landing platform
9. Attach the propellers and make sure they are secure
10. Check the battery's power and insert it, ensuring it is completely locked in
11. Turn on the remote control and connect the iPhone or iPad using a cable
12. Turn on the UAS after the remote control is on
13. Open DJI Go and check the return to home height and any other global setting that are relevant
14. Close DJI Go

#### Field protocol - execute mission
1. Open planned flight  
    - In MP app, go to *Mission Management* menu item > Select saved mission
2. Wait for aircraft symbol to connect to program
3. Open Flight Control pullout menu (airplane icon at top right)
4. Upload flight plan to aircraft
5. Check that everything looks correct in your flight 
    - Make sure flight lines still perpendicular to wind direction and/or parallel to topographical changes, if relevant 
    - Open Altitude Adjustment pullout menu (next one down) to change flight altitude / pixel resolution. FAA allows you to fly up to 400 feet, or 121 meters. Try for 5cm/px resolution (2 inches).  
    - Open Map control pullout (next one down) to change the units and to save the mission (left button)
6. Double-tap to mark estimated home point for take-off/landing (purple circle) 
7. Open Flight Plan Status pullout menu (top left) to see flight metrics  
    - Verify terrain awareness: Click Terrain Awareness and review terrain plot to make sure it makes sense. Trace finger along profile and you’ll see a corresponding blue dot along the flight path.  Tap plot to turn off and on terrain plot. 
    - If Terrain Awareness is enabled you’ll be prompted to select yes or no for a terrain adjusted flight. The profile will be recalculated, and you can accept or reject it after you’ve reviewed it. Note: you can check the profile and where the aircraft is along the profile during a flight, which won’t recalculate the profile
    - Note: Terrain aware flights set return-to-home hieght to 40m above highest altitude encountered in flight path so that the drone won't run into anything when returning to home. Watch out for FAA regs: max flight should be 121m. For example, if flight altitude is set for 50m , there is a 100m terrain change, and Terrain Awareness is enabled, your RTH height will only be 90m above the tallest point, but 190m above the lowest point, putting you above 121 m at your lower points. Also think about offset on top of that. The UAS allows for takeoff with a flightplan max <500m (you can change this in DJI Go settings), but this is way above FAA regs. If returning to home is part of completed program mission, the aircraft won’t jump up 40m above max height. It would, for example, with multibattery missions.  
8. Set up your screen how you'd like (e.g., minimize terrain plot and pull up the camera)
12. Press Start
13. The UAS will fly to the start point, collect images along the flight path (leaving grey dots where images are selcted, and the dot graphics are automatically cleaned as more images are collected), and fly to the homepoint after reaching the end point.
14. The UAS will automatically complete the mission, but be ready to land manually. It works well to swivel the aircraft so that it's facing the same direction as the polit when it's hovering above home. This makes it easier to nudge into place.
    - Note: MP will change the speed of the aircraft for wind and light conditions.
    - Note: multibattery missions. A point of abandonment is recorded when the drone returns to home (low battery or commanded home). Leave the RC on and map pilot open, change the battery, and repeat steps 6-12 above. The UAS will return to that point of abandonment when commanded to go again.
    - Note: Don’t fly up and over things. This might violate rule of sight for VO, but also Map Pilot wasn’t designed for this so can lose signal.


#### Field protocol - post-mission tasks
1. Once the UAS has safely landed, turn it off
2. Turn off the remote control after the UAS is off
3. Close Map Pilot and sleep the tablet if you'd like
4. Remove the UAS battery and place it in a shaded spot
5. Remove the SD card, replace it with a clean one, and transfer data
6. If you are not flying another mission immediately: remove propeller blades and repack them, replace the sensor cover, and repack the UAS
7. Once all missions in that AOI are completed, collect the GCPs and replace them with a permanant marker if desired for subsequent missions

#### Post-mission tasks at the office
1. Fill out CU logbook
2. Copy drone and GCP data on external HDs to multiple locations (including S3 buckets)
3. Upload flight logs to Maps Made Easy with Flight Sync (should happen automatically when connected to internet if signed into Maps Made Easy account and Flight Sync enabled in Map Pilot settings) or to AirData if you want to open an account.
4. Post-process in Agisoft Metashape (see Agisoft Metashape Notes)
5. Export data and share with collaborators / feed into further analysis. - Cold Springs: send all footage within one month to Mike Johnson mjohnson10@fs.fed.us
