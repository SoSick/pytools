import os



def GetProgramPath():
    if hasattr(os.sys, 'frozen'):
        return os.sys.executable
    else:
        return os.path.realpath(os.sys.argv[0])

def StripCRLF(s):
    if not s:
        return s
    
    crlf = "\r\n"
    cr = "\r"
    lf = "\n"
    if isinstance(s, (bytes, bytearray)):
        crlf = b"\r\n"
        cr = b"\r"
        lf = b"\n"
        
    if s[-2:] == crlf:
        return s[:-2]
    if s[-1:] == lf or s[-1:] == cr:
        return s[:-1]
    return s
