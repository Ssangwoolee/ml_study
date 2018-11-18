import ctypes as c

lib = c.WinDLL('OpenRPLT')
func = lib['Open']
func.argtypes = (c.c_double,)
func.restype = c.c_double

res = func(5.5)

print(res)