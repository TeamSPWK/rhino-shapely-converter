import pytest

import rhino3dm as r3d
import shapely.geometry as sgeom

from src.rhino_shapely_converter.converter import rhino_geometry_to_shapely_geometry

@pytest.mark.parametrize("x, y, z", [(1, 2, 3), (4, 5, 6), (7, 8, 9)])
def test_rhino_point_to_shapely_point(x, y, z):
    rhino_point = r3d.Point3d(x, y, z)
    shapely_point = rhino_geometry_to_shapely_geometry(rhino_point)
    assert shapely_point == sgeom.Point(x, y, z)

def test_rhino_point_cloud_to_shapely_point_cloud():
    rhino_point_cloud = r3d.PointCloud()
    rhino_point_cloud.Add(r3d.Point3d(1, 2, 3))
    rhino_point_cloud.Add(r3d.Point3d(4, 5, 6))
    rhino_point_cloud.Add(r3d.Point3d(7, 8, 9))
    shapely_point_cloud = rhino_geometry_to_shapely_geometry(rhino_point_cloud)
    assert shapely_point_cloud == sgeom.MultiPoint([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
