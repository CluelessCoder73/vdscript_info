import re

# ----------------------------------------------------------------------
# Script: vdscript_info_v1.1.0.py
# Description:
# This script converts VirtualDub or VirtualDub2 .vdscript files into a 
# simple text file containing all the timecodes for the wanted parts, 
# followed by the frame numbers (start - end), followed by the length in 
# time, then frames. & lastly, we have "Total Length" in time, then frames.

def frames_to_timecode(frame, fps):
    """Convert frame number to timecode (HH:MM:SS.mmm) based on fps."""
    seconds = frame / fps
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:06.3f}"

def calculate_length(start_frame, end_frame, fps):
    """Calculate the length of a cut in timecodes and number of frames."""
    frame_count = end_frame - start_frame + 1  # Endpoint inclusive
    length_timecode = frames_to_timecode(frame_count, fps)
    return length_timecode, frame_count

def parse_vdscript(vdscript_content, fps):
    """Parse the VirtualDub script and convert frame ranges to timecodes."""
    # Regular expression to capture the frame range details
    range_pattern = r"VirtualDub\.subset\.AddRange\((\d+),(\d+)\);"
    
    # List to store the extracted timecodes and frames
    timecode_list = []
    total_frames = 0  # To accumulate the total number of frames

    # Search for all ranges in the script
    for match in re.finditer(range_pattern, vdscript_content):
        start_frame = int(match.group(1))
        total_range_frames = int(match.group(2))
        end_frame = start_frame + total_range_frames - 1  # Making it endpoint-inclusive
        
        # Convert frames to timecodes
        start_timecode = frames_to_timecode(start_frame, fps)
        end_timecode = frames_to_timecode(end_frame, fps)
        
        # Calculate length and frames for the current range
        length_timecode, frame_count = calculate_length(start_frame, end_frame, fps)
        total_frames += frame_count
        
        # Format output as timecodes, frame range, length, and frame count
        timecode_entry = (f"{start_timecode} - {end_timecode} (Frames {start_frame} - {end_frame}) "
                          f"Length: {length_timecode} ({frame_count} frames)")
        timecode_list.append(timecode_entry)
    
    # Calculate total length and total frames
    total_length_timecode = frames_to_timecode(total_frames, fps)
    total_entry = f"Total Length: {total_length_timecode} ({total_frames} frames)"
    
    # Add a separator and the total entry
    timecode_list.append("-" * 80)
    timecode_list.append(total_entry)
    
    return "\n".join(timecode_list)

def convert_vdscript_to_timecodes(file_path, fps):
    """Convert a .vdscript file to a text file with timecodes."""
    with open(file_path, 'r') as f:
        vdscript_content = f.read()

    # Parse and get the timecodes
    timecodes_output = parse_vdscript(vdscript_content, fps)

    # Write the output to a new text file
    output_file = file_path.replace(".vdscript", "_timecodes.txt")
    with open(output_file, 'w') as f:
        f.write(timecodes_output)

    print(f"Timecodes saved to {output_file}")

# Example usage:
fps = ?  # Frame rate of the video - Replace '?' with the correct value (e.g., 23.976, 25)
convert_vdscript_to_timecodes('example.vdscript', fps)
