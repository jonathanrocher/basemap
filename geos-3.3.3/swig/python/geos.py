# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.

import _geos
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class PySwigIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_PySwigIterator
    __del__ = lambda self : None;
    def value(*args): return _geos.PySwigIterator_value(*args)
    def incr(*args): return _geos.PySwigIterator_incr(*args)
    def decr(*args): return _geos.PySwigIterator_decr(*args)
    def distance(*args): return _geos.PySwigIterator_distance(*args)
    def equal(*args): return _geos.PySwigIterator_equal(*args)
    def copy(*args): return _geos.PySwigIterator_copy(*args)
    def next(*args): return _geos.PySwigIterator_next(*args)
    def previous(*args): return _geos.PySwigIterator_previous(*args)
    def advance(*args): return _geos.PySwigIterator_advance(*args)
    def __eq__(*args): return _geos.PySwigIterator___eq__(*args)
    def __ne__(*args): return _geos.PySwigIterator___ne__(*args)
    def __iadd__(*args): return _geos.PySwigIterator___iadd__(*args)
    def __isub__(*args): return _geos.PySwigIterator___isub__(*args)
    def __add__(*args): return _geos.PySwigIterator___add__(*args)
    def __sub__(*args): return _geos.PySwigIterator___sub__(*args)
    def __iter__(self): return self
PySwigIterator_swigregister = _geos.PySwigIterator_swigregister
PySwigIterator_swigregister(PySwigIterator)

GEOS_VERSION_MAJOR = _geos.GEOS_VERSION_MAJOR
GEOS_VERSION_MINOR = _geos.GEOS_VERSION_MINOR
GEOS_VERSION = _geos.GEOS_VERSION
GEOS_JTS_PORT = _geos.GEOS_JTS_PORT
GEOS_CAPI_VERSION_MAJOR = _geos.GEOS_CAPI_VERSION_MAJOR
GEOS_CAPI_VERSION_MINOR = _geos.GEOS_CAPI_VERSION_MINOR
GEOS_CAPI_VERSION_PATCH = _geos.GEOS_CAPI_VERSION_PATCH
GEOS_CAPI_FIRST_INTERFACE = _geos.GEOS_CAPI_FIRST_INTERFACE
GEOS_CAPI_LAST_INTERFACE = _geos.GEOS_CAPI_LAST_INTERFACE
GEOS_CAPI_VERSION = _geos.GEOS_CAPI_VERSION
GEOS_POINT = _geos.GEOS_POINT
GEOS_LINESTRING = _geos.GEOS_LINESTRING
GEOS_LINEARRING = _geos.GEOS_LINEARRING
GEOS_POLYGON = _geos.GEOS_POLYGON
GEOS_MULTIPOINT = _geos.GEOS_MULTIPOINT
GEOS_MULTILINESTRING = _geos.GEOS_MULTILINESTRING
GEOS_MULTIPOLYGON = _geos.GEOS_MULTIPOLYGON
GEOS_GEOMETRYCOLLECTION = _geos.GEOS_GEOMETRYCOLLECTION
GEOS_WKB_XDR = _geos.GEOS_WKB_XDR
GEOS_WKB_NDR = _geos.GEOS_WKB_NDR
version = _geos.version
class CoordinateSequence(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _geos.new_CoordinateSequence(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _geos.delete_CoordinateSequence
    __del__ = lambda self : None;
    def clone(*args): return _geos.CoordinateSequence_clone(*args)
    def setX(*args): return _geos.CoordinateSequence_setX(*args)
    def setY(*args): return _geos.CoordinateSequence_setY(*args)
    def setZ(*args): return _geos.CoordinateSequence_setZ(*args)
    def setOrdinate(*args): return _geos.CoordinateSequence_setOrdinate(*args)
    def getX(*args): return _geos.CoordinateSequence_getX(*args)
    def getY(*args): return _geos.CoordinateSequence_getY(*args)
    def getZ(*args): return _geos.CoordinateSequence_getZ(*args)
    def getOrdinate(*args): return _geos.CoordinateSequence_getOrdinate(*args)
    def getSize(*args): return _geos.CoordinateSequence_getSize(*args)
    def getDimensions(*args): return _geos.CoordinateSequence_getDimensions(*args)
CoordinateSequence_swigregister = _geos.CoordinateSequence_swigregister
CoordinateSequence_swigregister(CoordinateSequence)

class Geometry(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_Geometry
    __del__ = lambda self : None;
    def clone(*args): return _geos.Geometry_clone(*args)
    def geomType(*args): return _geos.Geometry_geomType(*args)
    def typeId(*args): return _geos.Geometry_typeId(*args)
    def normalize(*args): return _geos.Geometry_normalize(*args)
    def getSRID(*args): return _geos.Geometry_getSRID(*args)
    def setSRID(*args): return _geos.Geometry_setSRID(*args)
    def getDimensions(*args): return _geos.Geometry_getDimensions(*args)
    def getNumGeometries(*args): return _geos.Geometry_getNumGeometries(*args)
    def intersection(*args): return _geos.Geometry_intersection(*args)
    def buffer(*args): return _geos.Geometry_buffer(*args)
    def convexHull(*args): return _geos.Geometry_convexHull(*args)
    def difference(*args): return _geos.Geometry_difference(*args)
    def symDifference(*args): return _geos.Geometry_symDifference(*args)
    def boundary(*args): return _geos.Geometry_boundary(*args)
    def union(*args): return _geos.Geometry_union(*args)
    def pointOnSurface(*args): return _geos.Geometry_pointOnSurface(*args)
    def getCentroid(*args): return _geos.Geometry_getCentroid(*args)
    def getEnvelope(*args): return _geos.Geometry_getEnvelope(*args)
    def relate(*args): return _geos.Geometry_relate(*args)
    def lineMerge(*args): return _geos.Geometry_lineMerge(*args)
    def simplify(*args): return _geos.Geometry_simplify(*args)
    def topologyPreserveSimplify(*args): return _geos.Geometry_topologyPreserveSimplify(*args)
    def relatePattern(*args): return _geos.Geometry_relatePattern(*args)
    def disjoint(*args): return _geos.Geometry_disjoint(*args)
    def touches(*args): return _geos.Geometry_touches(*args)
    def intersects(*args): return _geos.Geometry_intersects(*args)
    def crosses(*args): return _geos.Geometry_crosses(*args)
    def within(*args): return _geos.Geometry_within(*args)
    def contains(*args): return _geos.Geometry_contains(*args)
    def overlaps(*args): return _geos.Geometry_overlaps(*args)
    def equals(*args): return _geos.Geometry_equals(*args)
    def equalsExact(*args): return _geos.Geometry_equalsExact(*args)
    def isEmpty(*args): return _geos.Geometry_isEmpty(*args)
    def isValid(*args): return _geos.Geometry_isValid(*args)
    def isSimple(*args): return _geos.Geometry_isSimple(*args)
    def isRing(*args): return _geos.Geometry_isRing(*args)
    def hasZ(*args): return _geos.Geometry_hasZ(*args)
    def area(*args): return _geos.Geometry_area(*args)
    def length(*args): return _geos.Geometry_length(*args)
    def distance(*args): return _geos.Geometry_distance(*args)
Geometry_swigregister = _geos.Geometry_swigregister
Geometry_swigregister(Geometry)

class Point(Geometry):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_Point
    __del__ = lambda self : None;
    def getCoordSeq(*args): return _geos.Point_getCoordSeq(*args)
Point_swigregister = _geos.Point_swigregister
Point_swigregister(Point)

class LineString(Geometry):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_LineString
    __del__ = lambda self : None;
    def getCoordSeq(*args): return _geos.LineString_getCoordSeq(*args)
LineString_swigregister = _geos.LineString_swigregister
LineString_swigregister(LineString)

class LinearRing(Geometry):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_LinearRing
    __del__ = lambda self : None;
    def getCoordSeq(*args): return _geos.LinearRing_getCoordSeq(*args)
LinearRing_swigregister = _geos.LinearRing_swigregister
LinearRing_swigregister(LinearRing)

class Polygon(Geometry):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_Polygon
    __del__ = lambda self : None;
    def getExteriorRing(*args): return _geos.Polygon_getExteriorRing(*args)
    def getNumInteriorRings(*args): return _geos.Polygon_getNumInteriorRings(*args)
    def getInteriorRingN(*args): return _geos.Polygon_getInteriorRingN(*args)
Polygon_swigregister = _geos.Polygon_swigregister
Polygon_swigregister(Polygon)

class GeometryCollection(Geometry):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_GeometryCollection
    __del__ = lambda self : None;
    def getGeometryN(*args): return _geos.GeometryCollection_getGeometryN(*args)
GeometryCollection_swigregister = _geos.GeometryCollection_swigregister
GeometryCollection_swigregister(GeometryCollection)

class MultiPoint(GeometryCollection):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_MultiPoint
    __del__ = lambda self : None;
MultiPoint_swigregister = _geos.MultiPoint_swigregister
MultiPoint_swigregister(MultiPoint)

class MultiLineString(GeometryCollection):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_MultiLineString
    __del__ = lambda self : None;
MultiLineString_swigregister = _geos.MultiLineString_swigregister
MultiLineString_swigregister(MultiLineString)

class MultiLinearRing(GeometryCollection):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_MultiLinearRing
    __del__ = lambda self : None;
MultiLinearRing_swigregister = _geos.MultiLinearRing_swigregister
MultiLinearRing_swigregister(MultiLinearRing)

class MultiPolygon(GeometryCollection):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _geos.delete_MultiPolygon
    __del__ = lambda self : None;
MultiPolygon_swigregister = _geos.MultiPolygon_swigregister
MultiPolygon_swigregister(MultiPolygon)

createPoint = _geos.createPoint
createLineString = _geos.createLineString
createLinearRing = _geos.createLinearRing
createPolygon = _geos.createPolygon
geomFromWKT = _geos.geomFromWKT
geomToWKT = _geos.geomToWKT
getWKBOutputDims = _geos.getWKBOutputDims
setWKBOutputDims = _geos.setWKBOutputDims
getWKBByteOrder = _geos.getWKBByteOrder
setWKBByteOrder = _geos.setWKBByteOrder
geomFromWKB = _geos.geomFromWKB
geomToWKB = _geos.geomToWKB
geomFromHEX = _geos.geomFromHEX
geomToHEX = _geos.geomToHEX


