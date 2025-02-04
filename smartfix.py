import os
import subprocess
from tkinter import Tk, filedialog

def select_files():
    """Open a file dialog to select multiple media files."""
    root = Tk()
    root.withdraw()  # Hide the root window
    files = filedialog.askopenfilenames(
        title="Select Media Files",
        filetypes=[("Media Files", "*.mp4 *.mp3 *.wav *.avi *.mkv *.flv *.mov")]
    )
    return root.tk.splitlist(files)

def combine_files(file_list, output_file):
    """Combine multiple media files into a single file using FFmpeg."""
    with open("file_list.txt", "w") as f:
        for file in file_list:
            f.write(f"file '{file}'\n")
    
    command = [
        "ffmpeg", "-f", "concat", "-safe", "0", "-i", "file_list.txt",
        "-c", "copy", output_file
    ]
    
    subprocess.run(command)
    os.remove("file_list.txt")

def main():
    print("Welcome to SmartFix!")
    files = select_files()
    if not files:
        print("No files selected. Exiting.")
        return
    
    output_file = filedialog.asksaveasfilename(
        title="Save Combined File As",
        defaultextension=".mp4",
        filetypes=[("MP4 Files", "*.mp4"), ("All Files", "*.*")]
    )
    
    if not output_file:
        print("No output file specified. Exiting.")
        return
    
    print(f"Combining {len(files)} files into {output_file}...")
    combine_files(files, output_file)
    print("Combination complete!")

if __name__ == "__main__":
    main()