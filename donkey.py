import fiona
import fiona.crs
import click
import os.path


@click.command()
@click.option('--epsg', default=4326, type=int, help='Type in the EPSG of the shape file')
@click.argument('file_input')
@click.argument('file_output')
def convert(file_input, file_output, epsg):
    extension_input = os.path.splitext(file_input)[1]
    extension_output = os.path.splitext(file_output)[1]
    if extension_input == '.shp':
        if extension_output == '.gpkg':
            with fiona.open(file_input) as source:
                with fiona.open(
                        file_output,
                        'w',
                        driver='GPKG',
                        crs=fiona.crs.from_epsg(epsg),
                        schema=source.schema) as sink:
                    for rec in source:
                        sink.write(rec)
        else:
            print('This program will only convert to geopackages.')
    else:
        print('This program will only convert from shapefiles.')


if __name__ == "__main__":
    convert()
