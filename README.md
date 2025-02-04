# SmartFix

SmartFix is a Python tool designed to combine multiple media files into a single optimized file on Windows platforms. It provides a simple graphical interface to select and merge video/audio files using FFmpeg.

## Features

- Combine various media formats including MP4, MP3, WAV, AVI, MKV, FLV, and MOV.
- Simple graphical interface for file selection.
- Optimized file output using FFmpeg.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- FFmpeg (must be installed and added to system PATH)

## Installation

1. Ensure Python is installed on your Windows system.
2. Install FFmpeg:
   - Download FFmpeg from [FFmpeg website](https://ffmpeg.org/download.html).
   - Extract the files and add the `bin` directory to your system PATH.
3. Save the `smartfix.py` script to your local directory.

## Usage

1. Run the SmartFix script:
   ```bash
   python smartfix.py
   ```
2. Use the file dialog to select the media files you want to combine.
3. Specify the output file name and location.
4. Wait for the process to complete.

## License

SmartFix is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## Acknowledgements

SmartFix leverages the powerful capabilities of FFmpeg for media processing.