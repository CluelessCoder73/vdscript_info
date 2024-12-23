# vdscript_info

Description:
This script converts VirtualDub or VirtualDub2 "vdscript" files into a simple text file, containing all the timecodes for the wanted parts, followed by the frame numbers (start - end), followed by the length in time, then frames. & lastly, we have "Total Length" in time, then frames. The goal here, is to convert the vdscript into a nice "human readable" layout of the cutlist.

This script was tested and works with:
 - Python 3.12.5
 - VirtualDub 1.10.4 .vdscript files
 - VirtualDub2 (build 44282) .vdscript files