# This file is autogenerated
import threading
import ctypes
import os
from .autd3capi_def import GeometryPtr


class GeometryViewerPtr(ctypes.Structure):
    _fields_ = [("_0", ctypes.c_void_p)]


class Singleton(type):
    _instances = {}  # type: ignore
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class NativeMethods(metaclass=Singleton):

    def init_dll(self, bin_location: str, bin_prefix: str, bin_ext: str):
        try:
            self.dll = ctypes.CDLL(os.path.join(bin_location, f'{bin_prefix}autd3capi_geometry_viewer{bin_ext}'))
        except Exception:
            return

        self.dll.AUTDGeometryViewer.argtypes = [] 
        self.dll.AUTDGeometryViewer.restype = GeometryViewerPtr

        self.dll.AUTDGeometryViewerSize.argtypes = [GeometryViewerPtr, ctypes.c_uint32, ctypes.c_uint32]  # type: ignore 
        self.dll.AUTDGeometryViewerSize.restype = GeometryViewerPtr

        self.dll.AUTDGeometryViewerVsync.argtypes = [GeometryViewerPtr, ctypes.c_bool]  # type: ignore 
        self.dll.AUTDGeometryViewerVsync.restype = GeometryViewerPtr

        self.dll.AUTDGeometryViewerRun.argtypes = [GeometryViewerPtr, GeometryPtr]  # type: ignore 
        self.dll.AUTDGeometryViewerRun.restype = ctypes.c_int32

    def geometry_viewer(self) -> GeometryViewerPtr:
        return self.dll.AUTDGeometryViewer()

    def geometry_viewer_size(self, viewer: GeometryViewerPtr, width: int, height: int) -> GeometryViewerPtr:
        return self.dll.AUTDGeometryViewerSize(viewer, width, height)

    def geometry_viewer_vsync(self, viewer: GeometryViewerPtr, vsync: bool) -> GeometryViewerPtr:
        return self.dll.AUTDGeometryViewerVsync(viewer, vsync)

    def geometry_viewer_run(self, viewer: GeometryViewerPtr, geometry: GeometryPtr) -> ctypes.c_int32:
        return self.dll.AUTDGeometryViewerRun(viewer, geometry)
