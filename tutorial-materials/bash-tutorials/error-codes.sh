#!/usr/bin/env bash

# Source: https://www.cyberciti.biz/faq/linux-bash-exit-status-set-exit-statusin-bash/
# Alternatively, use `perror <ERROR_CODE_NUM>` for error code explanation
#     - Requires `sudo apt install mysql-server-core-8.0`, or
#                `sudo apt install mariadb-server-10.3`

case "$1" in
    0)
        echo "Error Code 0: Success"
        ;;
    1)
        echo "Error Code 1: Operation not permitted"
        ;;
    2)
        echo "Error Code 2: No such file or directory"
        ;;
    3)
        echo "Error Code 3: No such process"
        ;;
    4)
        echo "Error Code 4: Interrupted system call"
        ;;
    5)
        echo "Error Code 5: Input/output error"
        ;;
    6)
        echo "Error Code 6: No such device or address"
        ;;
    7)
        echo "Error Code 7: Argument list too long"
        ;;
    8)
        echo "Error Code 8: Exec format error"
        ;;
    9)
        echo "Error Code 9: Bad file descriptor"
        ;;
    10)
        echo "Error Code 10: No child processes"
        ;;
    11)
        echo "Error Code 11: Resource temporarily unavailable"
        ;;
    12)
        echo "Error Code 12: Cannot allocate memory"
        ;;
    13)
        echo "Error Code 13: Permission denied"
        ;;
    14)
        echo "Error Code 14: Bad address"
        ;;
    15)
        echo "Error Code 15: Block device required"
        ;;
    16)
        echo "Error Code 16: Device or resource busy"
        ;;
    17)
        echo "Error Code 17: File exists"
        ;;
    18)
        echo "Error Code 18: Invalid cross-device link"
        ;;
    19)
        echo "Error Code 19: No such device"
        ;;
    20)
        echo "Error Code 20: Not a directory"
        ;;
    21)
        echo "Error Code 21: Is a directory"
        ;;
    22)
        echo "Error Code 22: Invalid argument"
        ;;
    23)
        echo "Error Code 23: Too many open files in system"
        ;;
    24)
        echo "Error Code 24: Too many open files"
        ;;
    25)
        echo "Error Code 25: Inappropriate ioctl for device"
        ;;
    26)
        echo "Error Code 26: Text file busy"
        ;;
    27)
        echo "Error Code 27: File too large"
        ;;
    28)
        echo "Error Code 28: No space left on device"
        ;;
    29)
        echo "Error Code 29: Illegal seek"
        ;;
    30)
        echo "Error Code 30: Read-only file system"
        ;;
    31)
        echo "Error Code 31: Too many links"
        ;;
    32)
        echo "Error Code 32: Broken pipe"
        ;;
    33)
        echo "Error Code 33: Numerical argument out of domain"
        ;;
    34)
        echo "Error Code 34: Numerical result out of range"
        ;;
    35)
        echo "Error Code 35: Resource deadlock avoided"
        ;;
    36)
        echo "Error Code 36: File name too long"
        ;;
    37)
        echo "Error Code 37: No locks available"
        ;;
    38)
        echo "Error Code 38: Function not implemented"
        ;;
    39)
        echo "Error Code 39: Directory not empty"
        ;;
    40)
        echo "Error Code 40: Too many levels of symbolic links"
        ;;
    41)
        echo "Error Code 41: <UNUSED>"
        ;;
    42)
        echo "Error Code 42: No message of desired type"
        ;;
    43)
        echo "Error Code 43: Identifier removed"
        ;;
    44)
        echo "Error Code 44: Channel number out of range"
        ;;
    45)
        echo "Error Code 45: Level 2 not synchronized"
        ;;
    46)
        echo "Error Code 46: Level 3 halted"
        ;;
    47)
        echo "Error Code 47: Level 3 reset"
        ;;
    48)
        echo "Error Code 48: Link number out of range"
        ;;
    49)
        echo "Error Code 49: Protocol driver not attached"
        ;;
    50)
        echo "Error Code 50: No CSI structure available"
        ;;
    51)
        echo "Error Code 51: Level 2 halted"
        ;;
    52)
        echo "Error Code 52: Invalid exchange"
        ;;
    53)
        echo "Error Code 53: Invalid request descriptor"
        ;;
    54)
        echo "Error Code 54: Exchange full"
        ;;
    55)
        echo "Error Code 55: No anode"
        ;;
    56)
        echo "Error Code 56: Invalid request code"
        ;;
    57)
        echo "Error Code 57: Invalid slot"
        ;;
    58)
        echo "Error Code 58: <UNUSED>"
        ;;
    59)
        echo "Error Code 59: Bad font file format"
        ;;
    60)
        echo "Error Code 60: Device not a stream"
        ;;
    61)
        echo "Error Code 61: No data available"
        ;;
    62)
        echo "Error Code 62: Timer expired"
        ;;
    63)
        echo "Error Code 63: Out of streams resources"
        ;;
    64)
        echo "Error Code 64: Machine is not on the network"
        ;;
    65)
        echo "Error Code 65: Package not installed"
        ;;
    66)
        echo "Error Code 66: Object is remote"
        ;;
    67)
        echo "Error Code 67: Link has been severed"
        ;;
    68)
        echo "Error Code 68: Advertise error"
        ;;
    69)
        echo "Error Code 69: Srmount error"
        ;;
    70)
        echo "Error Code 70: Communication error on send"
        ;;
    71)
        echo "Error Code 71: Protocol error"
        ;;
    72)
        echo "Error Code 72: Multihop attempted"
        ;;
    73)
        echo "Error Code 73: RFS specific error"
        ;;
    74)
        echo "Error Code 74: Bad message"
        ;;
    75)
        echo "Error Code 75: Value too large for defined data type"
        ;;
    76)
        echo "Error Code 76: Name not unique on network"
        ;;
    77)
        echo "Error Code 77: File descriptor in bad state"
        ;;
    78)
        echo "Error Code 78: Remote address changed"
        ;;
    79)
        echo "Error Code 79: Can not access a needed shared library"
        ;;
    80)
        echo "Error Code 80: Accessing a corrupted shared library"
        ;;
    81)
        echo "Error Code 81: .lib section in a.out corrupted"
        ;;
    81)
        echo "Error Code 82: Attempting to link in too many shared libraries"
        ;;
    81)
        echo "Error Code 83: Cannot exec a shared library directly"
        ;;
    81)
        echo "Error Code 84: Invalid or incomplete multibyte or wide character"
        ;;
    81)
        echo "Error Code 85: Interrupted system call should be restarted"
        ;;
    81)
        echo "Error Code 86: Streams pipe error"
        ;;
    81)
        echo "Error Code 87: Too many users"
        ;;
    81)
        echo "Error Code 88: Socket operation on non-socket"
        ;;
    81)
        echo "Error Code 89: Destination address required"
        ;;
    81)
        echo "Error Code 90: Message too long"
        ;;
    91)
        echo "Error Code 91: Protocol wrong type for socket"
        ;;
    92)
        echo "Error Code 92: Protocol not available"
        ;;
    93)
        echo "Error Code 93: Protocol not supported"
        ;;
    94)
        echo "Error Code 94: Socket type not supported"
        ;;
    95)
        echo "Error Code 95: Operation not supported"
        ;;
    96)
        echo "Error Code 96: Protocol family not supported"
        ;;
    97)
        echo "Error Code 97: Address family not supported by protocol"
        ;;
    98)
        echo "Error Code 98: Address already in use"
        ;;
    99)
        echo "Error Code 99: Cannot assign requested address"
        ;;
    100)
        echo "Error Code 100: Network is down"
        ;;
    101)
        echo "Error Code 101: Network is unreachable"
        ;;
    102)
        echo "Error Code 102: Network dropped connection on reset"
        ;;
    103)
        echo "Error Code 103: Software caused connection abort"
        ;;
    104)
        echo "Error Code 104: Connection reset by peer"
        ;;
    105)
        echo "Error Code 105: No buffer space available"
        ;;
    106)
        echo "Error Code 106: Transport endpoint is already connected"
        ;;
    107)
        echo "Error Code 107: Transport endpoint is not connected"
        ;;
    108)
        echo "Error Code 108: Cannot send after transport endpoint shutdown"
        ;;
    109)
        echo "Error Code 109: Too many references"
        ;;
    110)
        echo "Error Code 110: Connection timed out"
        ;;
    111)
        echo "Error Code 111: Connection refused"
        ;;
    112)
        echo "Error Code 112: Host is down"
        ;;
    113)
        echo "Error Code 113: No route to host"
        ;;
    114)
        echo "Error Code 114: Operation already in progress"
        ;;
    115)
        echo "Error Code 115: Operation now in progress"
        ;;
    116)
        echo "Error Code 116: Stale file handle"
        ;;
    117)
        echo "Error Code 117: Structure needs cleaning"
        ;;
    118)
        echo "Error Code 118: Not a XENIX named type file"
        ;;
    119)
        echo "Error Code 119: No XENIX semaphores available"
        ;;
    120)
        echo "Error Code 120: Is a named type file"
        ;;
    121)
        echo "Error Code 121: Remote I/O error"
        ;;
    122)
        echo "Error Code 122: Disk quota exceeded"
        ;;
    123)
        echo "Error Code 123: No medium found"
        ;;
    124)
        echo "Error Code 124: <UNUSED>"
        ;;
    125)
        echo "Error Code 125: Operation canceled"
        ;;
    126)
        echo "Error Code 126: Required key not available"
        ;;
    127)
        echo "Error Code 127: Key has expired"
        ;;
    128)
        echo "Error Code 128: Key has been revoked"
        ;;
    129)
        echo "Error Code 129: Key was rejected by service"
        ;;
    130)
        echo "Error Code 130: Owner died"
        ;;
    131)
        echo "Error Code 131: State not recoverable"
        ;;
    132)
        echo "Error Code 132: Operation not possible due to RF-kill"
        ;;
    133)
        echo "Error Code 133: Memory page has hardware error"
        ;;
    *)
        echo "Invalid Error Code: $1"
        ;;
esac
