import shapely.geometry as sgeom
try:
    # For Rhino
    import Rhino.Geometry as r3d
except ImportError:
    import rhino3dm as r3d


def shapely_point_to_rhino_point3d(shapely_point: sgeom.Point):
    return r3d.Point3d(shapely_point.x, shapely_point.y, shapely_point.z)


def shapely_multi_point_to_rhino_point_cloud(shapely_multi_point: sgeom.MultiPoint):
    return r3d.PointCloud(
        list(map(shapely_point_to_rhino_point3d, shapely_multi_point.geoms))
    )


def shapely_line_to_rhino_polyline(shapely_line: sgeom.LineString):
    points = [sgeom.Point(coord) for coord in shapely_line.coords]
    return r3d.Polyline(list(map(shapely_point_to_rhino_point3d, points)))


def convert_shapely_geometry_to_rhino_geometry(
    shapely_geometry: sgeom.base.BaseGeometry,
):
    if isinstance(shapely_geometry, sgeom.Point):
        return shapely_point_to_rhino_point3d(shapely_geometry)
    elif isinstance(shapely_geometry, sgeom.MultiPoint):
        return shapely_multi_point_to_rhino_point_cloud(shapely_geometry)
    elif isinstance(shapely_geometry, sgeom.LineString):
        return shapely_line_to_rhino_polyline(shapely_geometry)
    else:
        raise ValueError(f"Unsupported shapely geometry type: {type(shapely_geometry)}")
