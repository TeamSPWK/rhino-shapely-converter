import pytest

try:
    # For Rhino
    import Rhino.Geometry as r3d
except ImportError:
    import rhino3dm as r3d
import shapely.geometry as sgeom

from rhino_shapely_converter.from_rhino_to_shapely import (
    convert_rhino_geometry_to_shapely_geometry,
)


@pytest.mark.parametrize("x, y, z", [(1, 2, 3), (4, 5, 6), (7, 8, 9)])
def test_rhino_point_to_shapely_point(x, y, z):
    # Create rhino point
    rhino_point3d = r3d.Point3d(x, y, z)
    rhino_point2d = r3d.Point2d(x, y)
    rhino_point = r3d.Point(rhino_point3d)

    # Convert to shapely
    shapely_point_from_point3d = convert_rhino_geometry_to_shapely_geometry(
        rhino_point3d
    )
    shapely_point_from_point2d = convert_rhino_geometry_to_shapely_geometry(
        rhino_point2d
    )
    shapely_point_from_point = convert_rhino_geometry_to_shapely_geometry(rhino_point)

    # Check if those are the same
    assert shapely_point_from_point3d == sgeom.Point(x, y, z)
    assert shapely_point_from_point2d == sgeom.Point(x, y)
    assert shapely_point_from_point == sgeom.Point(x, y, z)


def test_rhino_point_cloud_to_shapely_point_cloud():
    # Create rhino point cloud
    rhino_point_cloud = r3d.PointCloud()
    rhino_point_cloud.Add(r3d.Point3d(1, 2, 3))
    rhino_point_cloud.Add(r3d.Point3d(4, 5, 6))
    rhino_point_cloud.Add(r3d.Point3d(7, 8, 9))

    # Convert to shapely
    shapely_point_cloud = convert_rhino_geometry_to_shapely_geometry(rhino_point_cloud)

    # Check if those are the same
    assert shapely_point_cloud == sgeom.MultiPoint([(1, 2, 3), (4, 5, 6), (7, 8, 9)])


def test_rhino_line_to_shapely_line():
    # Create rhino line
    rhino_line = r3d.Line(r3d.Point3d(1, 2, 3), r3d.Point3d(4, 5, 6))

    # Convert to shapely
    shapely_line = convert_rhino_geometry_to_shapely_geometry(rhino_line)

    # Check if those are the same
    assert shapely_line == sgeom.LineString([(1, 2, 3), (4, 5, 6)])


def test_rhino_polyline_to_shapely_line():
    # Create rhino polyline
    rhino_polyline = r3d.Polyline()
    rhino_polyline.Add(1, 2, 3)
    rhino_polyline.Add(4, 5, 6)
    rhino_polyline.Add(7, 8, 9)

    # Convert to shapely
    shapely_polyline = convert_rhino_geometry_to_shapely_geometry(rhino_polyline)

    # Check if those are the same
    assert shapely_polyline == sgeom.LineString([(1, 2, 3), (4, 5, 6), (7, 8, 9)])


def test_rhino_polyline_curve_to_shapely_line():
    # Create rhino polyline curve
    rhino_polyline_curve = r3d.PolylineCurve(
        [
            r3d.Point3d(1, 2, 3),
            r3d.Point3d(4, 5, 6),
            r3d.Point3d(7, 8, 9),
        ]
    )

    # Convert to shapely
    shapely_polyline_curve = convert_rhino_geometry_to_shapely_geometry(
        rhino_polyline_curve
    )

    # Check if those are the same
    assert shapely_polyline_curve == sgeom.LineString([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
