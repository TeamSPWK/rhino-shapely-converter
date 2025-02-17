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
        polyline_curve = geometry.ToPolylineCurve()
        return sgeom.LineString(
            list(map(lambda point: (point.X, point.Y, point.Z), polyline_curve.Points))
        )
    elif isinstance(geometry, r3d.PolylineCurve):
        return sgeom.LineString(
            list(map(lambda point: (point.X, point.Y, point.Z), geometry.GetPoints()))
        )

    elif isinstance(geometry, r3d.Surface):
        return sgeom.MultiPolygon(
            list(
                map(lambda face: sgeom.Polygon(
                    list(map(lambda point: (point.X, point.Y, point.Z), face.Points))
                ),
                geometry.Faces,
                )
            )
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
