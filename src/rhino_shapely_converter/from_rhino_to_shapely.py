import rhino3dm as r3d

import shapely.geometry as sgeom

SUPPORTED_GEOMETRY_TYPES = (
    "Point",
    "Point3d",
    "PointCloud",
    "Line",
    "Polyline",
    "PolylineCurve",
)


def convert_rhino_geometry_to_shapely_geometry(
    geometry: r3d.GeometryBase,
) -> sgeom.base.BaseGeometry:
    type_name = type(geometry).__name__

    # Point
    if type_name == "Point":
        return sgeom.Point(
            geometry.Location.X, geometry.Location.Y, geometry.Location.Z
        )

    elif type_name == "Point3d":
        return sgeom.Point(geometry.X, geometry.Y, geometry.Z)
    # PointCloud
    elif type_name == "PointCloud":
        return sgeom.MultiPoint(
            list(map(lambda point: (point.X, point.Y, point.Z), geometry.GetPoints()))
        )
    # Line
    elif type_name == "Line":
        return sgeom.LineString(
            [
                (geometry.PointAt(0).X, geometry.PointAt(0).Y, geometry.PointAt(0).Z),
                (geometry.PointAt(1).X, geometry.PointAt(1).Y, geometry.PointAt(1).Z),
            ]
        )
    # Polyline
    elif type_name == "Polyline":
        points = [geometry.PointAt(i) for i in range(geometry.Count)]
        return sgeom.LineString(
            list(map(lambda point: (point.X, point.Y, point.Z), points))
        )
    elif type_name == "PolylineCurve":
        points = [geometry.PointAt(i) for i in range(geometry.PointCount)]
        return sgeom.LineString(
            list(map(lambda point: (point.X, point.Y, point.Z), points))
        )

    else:
        raise ValueError(
            f"""Supported geometry types: {SUPPORTED_GEOMETRY_TYPES}.
            Unsupported geometry type: {type(geometry)}.
            """
        )
