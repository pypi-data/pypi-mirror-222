# This file is autogenerated
import threading
import ctypes
import os

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
            self.dll = ctypes.CDLL(os.path.join(bin_location, f'{bin_prefix}autd3capi_simulator{bin_ext}'))
        except Exception:
            return

        self.dll.AUTDSimulator.argtypes = [] 
        self.dll.AUTDSimulator.restype = ctypes.c_void_p

        self.dll.AUTDSimulatorPort.argtypes = [ctypes.c_void_p, ctypes.c_uint16] 
        self.dll.AUTDSimulatorPort.restype = ctypes.c_void_p

        self.dll.AUTDSimulatorWindowSize.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32] 
        self.dll.AUTDSimulatorWindowSize.restype = ctypes.c_void_p

        self.dll.AUTDSimulatorVsync.argtypes = [ctypes.c_void_p, ctypes.c_bool] 
        self.dll.AUTDSimulatorVsync.restype = ctypes.c_void_p

        self.dll.AUTDSimulatorGpuIdx.argtypes = [ctypes.c_void_p, ctypes.c_int32] 
        self.dll.AUTDSimulatorGpuIdx.restype = ctypes.c_void_p

        self.dll.AUTDSimulatorSettingsPath.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p] 
        self.dll.AUTDSimulatorSettingsPath.restype = ctypes.c_void_p

        self.dll.AUTDSimulatorRun.argtypes = [ctypes.c_void_p] 
        self.dll.AUTDSimulatorRun.restype = ctypes.c_int32

        self.dll.AUTDSimulatorSaveSettings.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p] 
        self.dll.AUTDSimulatorSaveSettings.restype = ctypes.c_bool

    def simulator(self) -> ctypes.c_void_p:
        return self.dll.AUTDSimulator()

    def simulator_port(self, simulator: ctypes.c_void_p, port: int) -> ctypes.c_void_p:
        return self.dll.AUTDSimulatorPort(simulator, port)

    def simulator_window_size(self, simulator: ctypes.c_void_p, width: int, height: int) -> ctypes.c_void_p:
        return self.dll.AUTDSimulatorWindowSize(simulator, width, height)

    def simulator_vsync(self, simulator: ctypes.c_void_p, vsync: bool) -> ctypes.c_void_p:
        return self.dll.AUTDSimulatorVsync(simulator, vsync)

    def simulator_gpu_idx(self, simulator: ctypes.c_void_p, idx: int) -> ctypes.c_void_p:
        return self.dll.AUTDSimulatorGpuIdx(simulator, idx)

    def simulator_settings_path(self, simulator: ctypes.c_void_p, path: bytes, err: ctypes.Array[ctypes.c_char]) -> ctypes.c_void_p:
        return self.dll.AUTDSimulatorSettingsPath(simulator, path, err)

    def simulator_run(self, simulator: ctypes.c_void_p) -> ctypes.c_int32:
        return self.dll.AUTDSimulatorRun(simulator)

    def simulator_save_settings(self, simulator: ctypes.c_void_p, path: bytes, err: ctypes.Array[ctypes.c_char]) -> ctypes.c_bool:
        return self.dll.AUTDSimulatorSaveSettings(simulator, path, err)
