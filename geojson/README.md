

# Learning GeoJSON: Examples and Tests

## [csv2geojson.py](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/csv2geojson.py)
* A python program to convert a CSV file into a FeatureCollection of Points.
* The CSV file can be in any order but must contain a header line with "name", "lat", and "lon" where "name", "lat", and "lon" are lower-case.

#### Example CSV format:
| name    | lon   | lat  |
| ----    | ----  | ---- |
| name00  | -78.7 | 40.9 | 
| name01  | -78.8 | 40.0 |
| name02  | -78.9 | 39.8 |

For a complete CSV file example see [stations_474.csv](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/stations_474.csv)

#### Runing Program:
To run the Python program:
``` 
python csv2geojson.py 
```

* The program will ask for the CSV file to read in, enter the name of the CSV file using the keyboard.
* The output file name will be the input CSV file name with a .geojson extension.


## [stations_474.csv](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/stations_474.csv)
CSV file of 474 points

## [stations_474.geojson](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/stations_474.geojson)
A GeoJSON FeatureCollection with 474 points. GeoJSON file produced using stations_474.csv file and csv2geojson.py Python program.


## [01-Point.geojson](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/01-Point.geojson)
A simple Point geometery type

## [02-MultiPoint.geojson](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/02-MultiPoint.geojson)
A simple MultiPoint geometry type

## [03-LineString.geojson](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/03-LineString.geojson)
A simple LineString geometry type

## [04-MultiLineString.geojson](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/04-MultiLineString.geojson)
A simple MultiLineString geometry type

## [05-Polygon_noHoles.geojson](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/05-Polygon_noHoles.geojson)
A Polygon geometry type with an exterior ring and no interior ring

## [06-Polygon_holes.geojson](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/06-Polygon_holes.geojson)
A Polygon geometry type with an exterior and interior ring

## [07-MultiPolygon.geojson](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/07-MultiPolygon.geojson)
A MultiPolygon geometry type with only exterior rings

## [08-GeometryCollection.geojson](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/08-GeometryCollection.geojson)
A GeometryCollection of a LineString and a Point

## [09-MultiLineString_Antimeridian.geojson](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/09-MultiLineString_Antimeridian.geojson)
A simple example of how to break up a line for the antimeridian

## [10-Feature_Point.geojson](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/10-Feature_Point.geojson)
A GeoJSON Feature type with a Point geometry type

## [11-FeatureCollection](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/11-FeatureCollection.geojson)
A GeoJSON FeatureCollection type with a LineString and a Point geometry type 

## [12-FeatureCollection_githubStyling.geojson](https://github.com/bclayton-usgs/coding_sandbox/blob/master/geojson/12-FeatureCollection_githubStyling.geojson)
A GeoJSON FeatureCollection type with a LineString and a Point geometry with [GitHub styling properties](https://help.github.com/articles/mapping-geojson-files-on-github/#styling-features) for GeoJSON


