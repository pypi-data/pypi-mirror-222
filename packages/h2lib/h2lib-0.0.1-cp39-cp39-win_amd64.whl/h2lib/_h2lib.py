from h2lib.dll_wrapper import DLLWrapper
import os


class H2Lib(DLLWrapper):
    def __init__(self, filename=os.path.dirname(__file__) + '/TestLib_64.dll'):
        DLLWrapper.__init__(self, filename, cdecl=True)
