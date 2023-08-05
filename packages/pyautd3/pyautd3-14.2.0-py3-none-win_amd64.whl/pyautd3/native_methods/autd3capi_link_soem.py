# This file is autogenerated
import threading
import ctypes
import os
from .autd3capi_def import Level, LinkPtr, TimerStrategy

from enum import IntEnum

class SyncMode(IntEnum):
    FreeRun = 0
    DC = 1

    @classmethod
    def from_param(cls, obj):
        return int(obj)


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
            self.dll = ctypes.CDLL(os.path.join(bin_location, f'{bin_prefix}autd3capi_link_soem{bin_ext}'))
        except Exception:
            return

        self.dll.AUTDGetAdapterPointer.argtypes = [] 
        self.dll.AUTDGetAdapterPointer.restype = ctypes.c_void_p

        self.dll.AUTDGetAdapterSize.argtypes = [ctypes.c_void_p] 
        self.dll.AUTDGetAdapterSize.restype = ctypes.c_uint32

        self.dll.AUTDGetAdapter.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_char_p, ctypes.c_char_p] 
        self.dll.AUTDGetAdapter.restype = None

        self.dll.AUTDFreeAdapterPointer.argtypes = [ctypes.c_void_p] 
        self.dll.AUTDFreeAdapterPointer.restype = None

        self.dll.AUTDLinkSOEM.argtypes = [] 
        self.dll.AUTDLinkSOEM.restype = LinkPtr

        self.dll.AUTDLinkSOEMSendCycle.argtypes = [LinkPtr, ctypes.c_uint16]  # type: ignore 
        self.dll.AUTDLinkSOEMSendCycle.restype = LinkPtr

        self.dll.AUTDLinkSOEMSync0Cycle.argtypes = [LinkPtr, ctypes.c_uint16]  # type: ignore 
        self.dll.AUTDLinkSOEMSync0Cycle.restype = LinkPtr

        self.dll.AUTDLinkSOEMBufSize.argtypes = [LinkPtr, ctypes.c_uint32]  # type: ignore 
        self.dll.AUTDLinkSOEMBufSize.restype = LinkPtr

        self.dll.AUTDLinkSOEMTimerStrategy.argtypes = [LinkPtr, TimerStrategy]  # type: ignore 
        self.dll.AUTDLinkSOEMTimerStrategy.restype = LinkPtr

        self.dll.AUTDLinkSOEMSyncMode.argtypes = [LinkPtr, SyncMode]  # type: ignore 
        self.dll.AUTDLinkSOEMSyncMode.restype = LinkPtr

        self.dll.AUTDLinkSOEMIfname.argtypes = [LinkPtr, ctypes.c_char_p]  # type: ignore 
        self.dll.AUTDLinkSOEMIfname.restype = LinkPtr

        self.dll.AUTDLinkSOEMStateCheckInterval.argtypes = [LinkPtr, ctypes.c_uint32]  # type: ignore 
        self.dll.AUTDLinkSOEMStateCheckInterval.restype = LinkPtr

        self.dll.AUTDLinkSOEMOnLost.argtypes = [LinkPtr, ctypes.c_void_p]  # type: ignore 
        self.dll.AUTDLinkSOEMOnLost.restype = LinkPtr

        self.dll.AUTDLinkSOEMLogLevel.argtypes = [LinkPtr, Level]  # type: ignore 
        self.dll.AUTDLinkSOEMLogLevel.restype = LinkPtr

        self.dll.AUTDLinkSOEMLogFunc.argtypes = [LinkPtr, ctypes.c_void_p, ctypes.c_void_p]  # type: ignore 
        self.dll.AUTDLinkSOEMLogFunc.restype = LinkPtr

        self.dll.AUTDLinkSOEMTimeout.argtypes = [LinkPtr, ctypes.c_uint64]  # type: ignore 
        self.dll.AUTDLinkSOEMTimeout.restype = LinkPtr

        self.dll.AUTDLinkRemoteSOEM.argtypes = [ctypes.c_char_p, ctypes.c_char_p] 
        self.dll.AUTDLinkRemoteSOEM.restype = LinkPtr

        self.dll.AUTDLinkRemoteSOEMTimeout.argtypes = [LinkPtr, ctypes.c_uint64]  # type: ignore 
        self.dll.AUTDLinkRemoteSOEMTimeout.restype = LinkPtr

    def get_adapter_pointer(self) -> ctypes.c_void_p:
        return self.dll.AUTDGetAdapterPointer()

    def get_adapter_size(self, adapters: ctypes.c_void_p) -> ctypes.c_uint32:
        return self.dll.AUTDGetAdapterSize(adapters)

    def get_adapter(self, adapters: ctypes.c_void_p, idx: int, desc: ctypes.Array[ctypes.c_char], name: ctypes.Array[ctypes.c_char]) -> None:
        return self.dll.AUTDGetAdapter(adapters, idx, desc, name)

    def free_adapter_pointer(self, adapters: ctypes.c_void_p) -> None:
        return self.dll.AUTDFreeAdapterPointer(adapters)

    def link_soem(self) -> LinkPtr:
        return self.dll.AUTDLinkSOEM()

    def link_soem_send_cycle(self, soem: LinkPtr, cycle: int) -> LinkPtr:
        return self.dll.AUTDLinkSOEMSendCycle(soem, cycle)

    def link_soem_sync_0_cycle(self, soem: LinkPtr, cycle: int) -> LinkPtr:
        return self.dll.AUTDLinkSOEMSync0Cycle(soem, cycle)

    def link_soem_buf_size(self, soem: LinkPtr, buf_size: int) -> LinkPtr:
        return self.dll.AUTDLinkSOEMBufSize(soem, buf_size)

    def link_soem_timer_strategy(self, soem: LinkPtr, timer_strategy: TimerStrategy) -> LinkPtr:
        return self.dll.AUTDLinkSOEMTimerStrategy(soem, timer_strategy)

    def link_soem_sync_mode(self, soem: LinkPtr, mode: SyncMode) -> LinkPtr:
        return self.dll.AUTDLinkSOEMSyncMode(soem, mode)

    def link_soem_ifname(self, soem: LinkPtr, ifname: bytes) -> LinkPtr:
        return self.dll.AUTDLinkSOEMIfname(soem, ifname)

    def link_soem_state_check_interval(self, soem: LinkPtr, interval_ms: int) -> LinkPtr:
        return self.dll.AUTDLinkSOEMStateCheckInterval(soem, interval_ms)

    def link_soem_on_lost(self, soem: LinkPtr, on_lost_func: ctypes.c_void_p) -> LinkPtr:
        return self.dll.AUTDLinkSOEMOnLost(soem, on_lost_func)

    def link_soem_log_level(self, soem: LinkPtr, level: Level) -> LinkPtr:
        return self.dll.AUTDLinkSOEMLogLevel(soem, level)

    def link_soem_log_func(self, soem: LinkPtr, out_func: ctypes.c_void_p, flush_func: ctypes.c_void_p) -> LinkPtr:
        return self.dll.AUTDLinkSOEMLogFunc(soem, out_func, flush_func)

    def link_soem_timeout(self, soem: LinkPtr, timeout_ns: int) -> LinkPtr:
        return self.dll.AUTDLinkSOEMTimeout(soem, timeout_ns)

    def link_remote_soem(self, addr: bytes, err: ctypes.Array[ctypes.c_char]) -> LinkPtr:
        return self.dll.AUTDLinkRemoteSOEM(addr, err)

    def link_remote_soem_timeout(self, soem: LinkPtr, timeout_ns: int) -> LinkPtr:
        return self.dll.AUTDLinkRemoteSOEMTimeout(soem, timeout_ns)
