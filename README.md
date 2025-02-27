# vdscript_info

Description:
This script converts VirtualDub or VirtualDub2 .vdscript files into a simple text file containing all the timecodes for the wanted parts, followed by the frame numbers (start - end), followed by the length in time, then frames. On the 3rd last line, we have "Total Length" in time, then frames, & on the 2nd last line, we have fps. This can be useful if you forget whether you input the correct frame rate or not.
NOW WORKS IN BATCH MODE!!!
This script was tested and works with:
- Python 3.13.2
- VirtualDub 1.10.4 .vdscript files
- VirtualDub2 (build 44282) .vdscript files

Usage:
1. Place this script in a folder containing 1 or more vdscript files.
   WARNING: They must ALL have the same frame rate! Create separate 
   folders if they don't (e.g., "23.976", "25"), & copy this script 
   to each one.
2. Run the script.
3. Enter the correct frame rate when asked.
4. A text file will be created for each vdscript, with the same name, 
   but "_info.txt" will be appended to each.