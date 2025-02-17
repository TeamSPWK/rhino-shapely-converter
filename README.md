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
- Rhino Point will be converted to Shapely Point.
- Rhino PointCloud will be converted to Shapely MultiPoint.
- Rhino Line will be converted to Shapely LineString.
- Rhino Polyline will be converted to Shapely LineString.
- Rhino Brep will be converted to Shapely MultiPolygon.

## Usage

```python
from rhino_shapely_converter import rhino_geometry_to_shapely_geometry

# Convert rhino geometry to shapely geometry
shapely_geometry = rhino_geometry_to_shapely_geometry(rhino_geometry)
```
