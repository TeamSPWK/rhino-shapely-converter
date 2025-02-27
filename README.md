# rhino-shapely-converter

This is to convert rhino geometry to shapely geometry and vice versa.

## Installation

```bash
pip install rhino-shapely-converter
```



## Important Notes

- Shapely is not an appropriate library for 3d calculations.
- It is recommended to use for 2d calculations mainly.

## Notes

- Rhino Point3d will be converted to Shapely Point.
- Rhino Point2d will be converted to Shapely Point.
- Rhino Point will be converted to Shapely Point.
- Rhino PointCloud will be converted to Shapely MultiPoint.
- Rhino Line will be converted to Shapely LineString.
- Rhino Polyline will be converted to Shapely LineString.
- Rhino PolylineCurve will be converted to Shapely LineString.

- Shapely Point will be converted to Rhino Point3d.
- Shapely MultiPoint will be converted to Rhino PointCloud.
- Shapely LineString will be converted to Rhino Polyline.

## Usage

```python
# please check current possible types to convert above
from rhino_shapely_converter import (
    convert_rhino_geometry_to_shapely_geometry,
    convert_shapely_geometry_to_rhino_geometry,
)

# Convert rhino geometry to shapely geometry
shapely_geometry = convert_rhino_geometry_to_shapely_geometry(rhino_geometry)

# Convert shapely geometry to rhino geometry
rhino_geometry = convert_shapely_geometry_to_rhino_geometry(shapely_geometry)
```
