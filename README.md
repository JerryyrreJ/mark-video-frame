# Mark Video Frame

A Python tool for adding frame numbers to videos.

## Features

- Add frame number marks to the top-left corner of each video frame
- Support multiple video formats (mp4, avi, mov, mkv, wmv, flv, webm)
- Process single video file or entire directory
- Maintain original video quality and format
- Display progress bar during processing

## Requirements

- Python 3.6+
- OpenCV (cv2)
- tqdm

## Installation

1. Clone this repository:
```bash
git clone https://github.com/JerryyrreJ/mark-video-frame.git
cd mark-video-frame
```
2. Install required packages:
```bash
pip install opencv-python tqdm
```
## Usage

### 1. Process Single Video File
```python
from write_frame_number import process_input
# Method 1: Specify complete output file path
input_path = "path/to/video.mp4"
output_path = "path/to/output/custom_name.mp4"
process_input(input_path, output_path)

# Method 2: Specify output directory only (will add with_frame suffix)
input_path = "path/to/video.mp4"output_path = "path/to/output/" # Output will be video_with_frame.mp4process_input(input_path, output_path)
```

### 2. Process Directory
```python
from write_frame_number import process_inputinput_path = "path/to/input/folder"output_path = "path/to/output/folder"process_input(input_path, output_path)
```
## Output Format

- Single file processing:
  - If full output path is specified: Uses the exact specified filename
  - If output directory is specified: Adds "_with_frame" suffix automatically

- Directory processing:
  - All output files will have "_with_frame" suffix added
  - Original file extensions are preserved

## Supported Video Formats

- MP4 (.mp4)
- AVI (.avi)
- MOV (.mov)
- MKV (.mkv)
- WMV (.wmv)
- FLV (.flv)
- WebM (.webm)

## Notes

1. Ensure sufficient disk space for output videos
2. Processing large files may take considerable time
3. Output directories will be created automatically if they don't exist
4. Different operating systems may support different video codecs


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details