import shapely.geometry as sgeom

try:
    # For Rhino
    import Rhino.Geometry as r3d
except ImportError:
    import rhino3dm as r3d

from rhino_shapely_converter.from_shapely_to_rhino import (
    convert_shapely_geometry_to_rhino_geometry,
)


def test_shapely_point_to_rhino_point3d():
    shapely_point = sgeom.Point(1, 2, 3)
    shapely_point2d = sgeom.Point(1, 2)

    rhino_point3d = convert_shapely_geometry_to_rhino_geometry(shapely_point)
    rhino_point2d = convert_shapely_geometry_to_rhino_geometry(shapely_point2d)

    assert rhino_point3d == r3d.Point3d(1, 2, 3)
    assert rhino_point2d == r3d.Point3d(1, 2, 0)


def test_shapely_point_cloud_to_rhino_point_cloud():
    shapely_point_cloud = sgeom.MultiPoint([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    shapely_point_cloud2d = sgeom.MultiPoint([(1, 2), (4, 5), (7, 8)])

    rhino_point_cloud = convert_shapely_geometry_to_rhino_geometry(shapely_point_cloud)
    rhino_point_cloud2d = convert_shapely_geometry_to_rhino_geometry(
        shapely_point_cloud2d
    )
    expected_rhino_point_cloud = r3d.PointCloud(
        [r3d.Point3d(1, 2, 3), r3d.Point3d(4, 5, 6), r3d.Point3d(7, 8, 9)]
    )
    expected_rhino_point_cloud2d = r3d.PointCloud(
        [r3d.Point3d(1, 2, 0), r3d.Point3d(4, 5, 0), r3d.Point3d(7, 8, 0)]
    )

    assert len(rhino_point_cloud) == len(expected_rhino_point_cloud)
    for i, point in enumerate(expected_rhino_point_cloud):
        assert rhino_point_cloud[i].X == point.X
        assert rhino_point_cloud[i].Y == point.Y
        assert rhino_point_cloud[i].Z == point.Z

    assert len(rhino_point_cloud2d) == len(expected_rhino_point_cloud2d)
    for i, point in enumerate(expected_rhino_point_cloud2d):
        assert rhino_point_cloud2d[i].X == point.X
        assert rhino_point_cloud2d[i].Y == point.Y
        assert rhino_point_cloud2d[i].Z == point.Z


def test_shapely_line_to_rhino_polyline():
    shapely_line = sgeom.LineString([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    shapely_line2d = sgeom.LineString([(1, 2), (4, 5), (7, 8)])

    rhino_line = convert_shapely_geometry_to_rhino_geometry(shapely_line)
    rhino_line2d = convert_shapely_geometry_to_rhino_geometry(shapely_line2d)

    expected_rhino_polyline = r3d.Polyline(
        [r3d.Point3d(1, 2, 3), r3d.Point3d(4, 5, 6), r3d.Point3d(7, 8, 9)]
    )
    expected_rhino_polyline2d = r3d.Polyline(
        [r3d.Point3d(1, 2, 0), r3d.Point3d(4, 5, 0), r3d.Point3d(7, 8, 0)]
    )

    assert len(rhino_line) == len(expected_rhino_polyline)
    for i, point in enumerate(expected_rhino_polyline):
        assert rhino_line[i].X == point.X
        assert rhino_line[i].Y == point.Y
        assert rhino_line[i].Z == point.Z

    assert len(rhino_line2d) == len(expected_rhino_polyline2d)
    for i, point in enumerate(expected_rhino_polyline2d):
        assert rhino_line2d[i].X == point.X
        assert rhino_line2d[i].Y == point.Y
        assert rhino_line2d[i].Z == point.Z
