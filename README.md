# Fiona Converter Examples
Programming Fiona in Python to convert geospatial file formats, like converting Shapefile to GeoPackage.

### Example

```
python donkey.py --help
Usage: donkey.py [OPTIONS] FILE_INPUT FILE_OUTPUT

Options:
  --epsg INTEGER  Type in the EPSG of the shape file
  --help          Show this message and exit.

```

```
python donkey.py --epsg 2056 shapefile.shp geopackage.gpkg
```
