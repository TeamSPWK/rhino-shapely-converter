import pytest

import rhino3dm as r3d
import shapely.geometry as sgeom

from src.rhino_shapely_converter.converter import rhino_geometry_to_shapely_geometry

@pytest.mark.parametrize("x, y, z", [(1, 2, 3), (4, 5, 6), (7, 8, 9)])
def test_rhino_point_to_shapely_point(x, y, z):
    rhino_point = r3d.Point(x, y, z)
    shapely_point = rhino_geometry_to_shapely_geometry(rhino_point)
    assert shapely_point == sgeom.Point(x, y, z)

def test_rhino_point3d_to_shapely_point():
    rhino_point = r3d.Point3d(1, 2, 3)
    shapely_point = rhino_geometry_to_shapely_geometry(rhino_point)
    assert shapely_point == sgeom.Point(1, 2, 3)

def test_rhino_point3d_to_shapely_point():
    rhino_point = r3d.Point3d(1, 2, 3)
    shapely_point = rhino_geometry_to_shapely_geometry(rhino_point)
    assert shapely_point == sgeom.Point(1, 2, 3)
