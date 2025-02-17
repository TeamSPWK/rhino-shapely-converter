import rhino3dm as r3d
import shapely.geometry as sgeom

from rhino_shapely_converter.convert_from_shapely_to_rhino import (
    convert_shapely_geometry_to_rhino_geometry,
)


def test_shapely_point_to_rhino_point3d():
    shapely_point = sgeom.Point(1, 2, 3)
    rhino_point3d = convert_shapely_geometry_to_rhino_geometry(shapely_point)
    assert rhino_point3d == r3d.Point3d(1, 2, 3)


def test_shapely_point_cloud_to_rhino_point_cloud():
    shapely_point_cloud = sgeom.MultiPoint([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    rhino_point_cloud = convert_shapely_geometry_to_rhino_geometry(shapely_point_cloud)
    expected_rhino_point_cloud = r3d.PointCloud(
        [r3d.Point3d(1, 2, 3), r3d.Point3d(4, 5, 6), r3d.Point3d(7, 8, 9)]
    )

    assert len(rhino_point_cloud) == len(expected_rhino_point_cloud)
    for i, point in enumerate(expected_rhino_point_cloud):
        assert rhino_point_cloud[i].X == point.X
        assert rhino_point_cloud[i].Y == point.Y
        assert rhino_point_cloud[i].Z == point.Z


def test_shapely_line_to_rhino_polyline():
    shapely_line = sgeom.LineString([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    rhino_polyline = convert_shapely_geometry_to_rhino_geometry(shapely_line)
    expected_rhino_polyline = r3d.Polyline(
        [r3d.Point3d(1, 2, 3), r3d.Point3d(4, 5, 6), r3d.Point3d(7, 8, 9)]
    )
    assert len(rhino_polyline) == len(expected_rhino_polyline)
    for i, point in enumerate(expected_rhino_polyline):
        assert rhino_polyline[i].X == point.X
        assert rhino_polyline[i].Y == point.Y
        assert rhino_polyline[i].Z == point.Z
