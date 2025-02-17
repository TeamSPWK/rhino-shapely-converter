import rhino3dm as r3d

import shapely.geometry as sgeom


def rhino_geometry_to_shapely_geometry(
    geometry: r3d.GeometryBase,
) -> sgeom.base.BaseGeometry:
    # Point
    if isinstance(geometry, r3d.Point):
        return sgeom.Point(geometry.X, geometry.Y, geometry.Z)
    elif isinstance(geometry, r3d.Point3d):
        return sgeom.Point(geometry.X, geometry.Y, geometry.Z)
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
                (geometry.Point1.X, geometry.Point1.Y, geometry.Point1.Z),
                (geometry.Point2.X, geometry.Point2.Y, geometry.Point2.Z),
            ]
        )
    # Polyline
    elif isinstance(geometry, r3d.Polyline):
        return sgeom.LineString(
            list(map(lambda point: (point.X, point.Y, point.Z), geometry.Points))
        )
    elif isinstance(geometry, r3d.PolylineCurve):
        return sgeom.LineString(
            list(map(lambda point: (point.X, point.Y, point.Z), geometry.Points))
        )

    # Brep
    elif isinstance(geometry, r3d.Brep):
        return sgeom.MultiPolygon(
            list(
                map(
                    lambda face: sgeom.Polygon(
                        list(
                            map(lambda point: (point.X, point.Y, point.Z), face.Points)
                        )
                    ),
                    geometry.Faces,
                )
            )
        )
    else:
        raise ValueError(f"Unsupported geometry type: {type(geometry)}")
