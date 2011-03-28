from struc import Struc
import ctypes
from win32con import *

class BYTE(Struc):
    core = ctypes.c_ubyte
    
    
class WORD(Struc):
    core = ctypes.c_ushort


class DWORD(Struc):
    core = ctypes.c_ulong


class IMAGE_DOS_HEADER(Struc):
    WORD.e_magic
    WORD.e_cblp
    WORD.e_cp
    WORD.e_crlc
    WORD.e_cparhdr
    WORD.e_minalloc
    WORD.e_maxalloc
    WORD.e_ss
    WORD.e_sp
    WORD.e_csum
    WORD.e_ip 
    WORD.e_cs 
    WORD.e_lfarlc 
    WORD.e_ovno   
    WORD.e_res[4]
    WORD.e_oemid  
    WORD.e_oeminfo
    WORD.e_res2[10]
    DWORD.e_lfanew


class IMAGE_FILE_HEADER(Struc):
    WORD.Machine
    WORD.NumberOfSections
    DWORD.TimeDateStamp
    DWORD.PointerToSymbolTable
    DWORD.NumberOfSymbols
    WORD.SizeOfOptionalHeader
    WORD.Characteristics


class IMAGE_DATA_DIRECTORY(Struc):
    DWORD.VirtualAddress
    DWORD.Size


class IMAGE_OPTIONAL_HEADER32(Struc):
    WORD.Magic
    BYTE.MajorLinkerVersion
    BYTE.MinorLinkerVersion
    DWORD.SizeOfCode
    DWORD.SizeOfInitializedData
    DWORD.SizeOfUninitializedData
    DWORD.AddressOfEntryPoint
    DWORD.BaseOfCode
    DWORD.BaseOfData
    DWORD.ImageBase
    DWORD.SectionAlignment
    DWORD.FileAlignment
    WORD.MajorOperatingSystemVersion
    WORD.MinorOperatingSystemVersion
    WORD.MajorImageVersion
    WORD.MinorImageVersion
    WORD.MajorSubsystemVersion
    WORD.MinorSubsystemVersion
    DWORD.Win32VersionValue
    DWORD.SizeOfImage
    DWORD.SizeOfHeaders
    DWORD.CheckSum
    WORD.Subsystem
    WORD.DllCharacteristics
    DWORD.SizeOfStackReserve
    DWORD.SizeOfStackCommit
    DWORD.SizeOfHeapReserve
    DWORD.SizeOfHeapCommit
    DWORD.LoaderFlags
    DWORD.NumberOfRvaAndSizes
    IMAGE_DATA_DIRECTORY.DataDirectory[IMAGE_NUMBEROF_DIRECTORY_ENTRIES]


class IMAGE_NT_HEADERS(Struc):
    DWORD.Signature
    IMAGE_FILE_HEADER.FileHeader
    IMAGE_OPTIONAL_HEADER32.OptionalHeader
    

if __name__ == '__main__':
    f = open('C:/windows/notepad.exe', 'rb')
    mz = IMAGE_DOS_HEADER()
    f.readinto(mz)
    f.seek(mz.e_lfanew)
    pe = IMAGE_NT_HEADERS()
    f.readinto(pe)
    print pe    
    print buffer(pe)[:].encode('hex')
    