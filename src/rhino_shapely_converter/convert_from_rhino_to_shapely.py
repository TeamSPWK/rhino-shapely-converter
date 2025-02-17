import rhino3dm as r3d

import shapely.geometry as sgeom


def rhino_geometry_to_shapely_geometry(
    geometry: r3d.GeometryBase,
) -> sgeom.base.BaseGeometry:
    # Point
    if isinstance(geometry, r3d.Point):
        return sgeom.Point(
            geometry.Location.X, geometry.Location.Y, geometry.Location.Z
        )

    elif isinstance(geometry, r3d.Point3d):
        return sgeom.Point(geometry.X, geometry.Y, geometry.Z)
    # PointCloud
    elif isinstance(geometry, r3d.PointCloud):
        return sgeom.MultiPoint(
            list(map(lambda point: (point.X, point.Y, point.Z), geometry.GetPoints()))
        )
    # Line
    elif isinstance(geometry, r3d.Line):
        return sgeom.LineString(
            [
                (geometry.PointAt(0).X, geometry.PointAt(0).Y, geometry.PointAt(0).Z),
                (geometry.PointAt(1).X, geometry.PointAt(1).Y, geometry.PointAt(1).Z),
            ]
        )
    # Polyline
    elif isinstance(geometry, r3d.Polyline):
        points = [geometry.PointAt(i) for i in range(geometry.Count)]
        return sgeom.LineString(
            list(map(lambda point: (point.X, point.Y, point.Z), points))
        )
    elif isinstance(geometry, r3d.PolylineCurve):
        points = [geometry.PointAt(i) for i in range(geometry.PointCount)]
        return sgeom.LineString(
            list(map(lambda point: (point.X, point.Y, point.Z), points))
        )

    else:
        raise ValueError(f"Unsupported geometry type: {type(geometry)}")
