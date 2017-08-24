#!/bin/python


###########################
#
#......... Import ........
import os
os.system('clear')  # Clear terminal
#------ End Import -------
#
##########################


#############################################################################
#
#........................ Read In CSV Files .................................

print '\n\n Enter the name of the CSV file'
#Fsta = raw_input('File name: ')                   # Get name of CSV file
#print Fsta

Fsta = '13-stations_474.csv'
Fsta_in = open(Fsta,'r')                        # Open the CSV file to read                     

#..................... Read in Header Line .................................
head = Fsta_in.readline().split(',')            # Get header line
js=-1                                           # Counter
for jh in head:                                 # Loop through the header line
  js=js+1
  if   jh.strip() == 'name':                    # Find where name column is 
    jname = js          
  elif jh.strip() == 'lat':                     # Find where latitude column is
    jlat = js
  elif jh.strip() == 'lon':                     # Find where longitude column is
    jlon = js
#---------------------------------------------------------------------------

#..................... Read in Name, Lat, and Lon Columns ..................
name = []                                       # list to put names
lat  = []                                       # List to put latitudes
lon  = []                                       # list to put longitudes

for line in Fsta_in:                            # Loop through lines of CSV file
  name_temp = line.split(',')[jname]            # Get name
  lat_temp  = line.split(',')[jlat]             # Get latitude
  lon_temp  = line.split(',')[jlon]             # Get longitude
  name.append(name_temp.strip())                # Append name to list
  lat.append(float(lat_temp.strip()))           # Append latitude to list
  lon.append(float(lon_temp.strip()))           # Append longitude to list

nsta = len(name)                                # Get length of list
#---------------------------------------------------------------------------

Fsta_in.close()                                 # Close file

#--------------------- End Read In CSV File --------------------------------
#
############################################################################




############################################################################
#
#........................ Make GeoJSON File ................................


Fjson = Fsta.split('.')[0]+'.geojson'               # Make file name for GeoJSON file, input file name with .geojson extension

Fjson_out = open(Fjson,'w')                         # Open file to write

#...................... Write to GeoJSON File .............................
# Example of output:
'''
{
  "type" : "FeatureCollection",
  "features" : [
    {
      "type" : "Feature",
      "geometry" : {
        "type" : "Point",
        "coordinates" : [100.0, 0.0],
      },
      "properties" : {
        "Station" : "001"
      }
    }
  ]
}

'''

Fjson_out.write('''                                 
{
  "type" : "FeatureCollection",
  "features" : [''')

for js in range(nsta):                              # Loop through number of values and write a Feature GeoJSON type for each point
  tag = '%02d'%js
  Fjson_out.write('''
    {
      "type" : "Feature",
      "geometry" : {
        "type" : "Point",
        "coordinates" : [%f, %f]
      },
      "properties" : {
        "Station" : "%s",
        "marker-size" : "small",
        "marker-color" : "00FF00"
      }'''%(lon[js],lat[js],name[js]))   # Input longitude, latitude, and name
  if js == nsta-1:                                            # If on last iteration, end object with no comma
    Fjson_out.write('''
    }''') 
  else:                                                       # Else put comma in to add another object
    Fjson_out.write('''
    },''')

Fjson_out.write('''  
  ]
}
''')


#----------------------------------------------------------------------------


Fjson_out.close()
#------------------- End Make GeoJSON File ----------------------------------
#
#############################################################################
