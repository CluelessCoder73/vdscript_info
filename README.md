# vdscript_info

Description:
This script converts VirtualDub or VirtualDub2 "vdscript" files into a simple text file, containing all the timecodes for the wanted parts, followed by the frame numbers (start - end), followed by the length in time, then frames. & lastly, we have "Total Length" in time, then frames.

This script was tested and works with:
 - Python 3.12.5
 - VirtualDub 1.10.4 .vdscript files
 - VirtualDub2 (build 44282) .vdscript files
 
Here's an output example (source vdscript had two "cut" ranges):

00:00:18.352 - 00:00:30.989 (Frames 440 - 743)   Length: 00:00:12.679 (304 frames)
00:00:48.841 - 00:00:55.264 (Frames 1171 - 1325) Length: 00:00:06.465 (155 frames)
--------------------------------------------------------------------------------
Total Length: 00:00:19.144 (459 frames)