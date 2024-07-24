import cv2
import os
from tqdm import tqdm

def process_video(input_path, output_path, max_frames):
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_number = 0
    
    for _ in tqdm(range(max_frames), desc="Processing video"):
        ret, frame = cap.read()
        if ret:
            frame_number += 1
            cv2.putText(frame, f'frame: {frame_number}', (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            out.write(frame)
        else:
            break

    cap.release()
    out.release()
   
def process_directory(input_dir, output_dir, max_frames=300):
    files = [f for f in os.listdir(input_dir) if f.endswith(".mp4")] 
    # calculate the number of files
    for filename in tqdm(files, desc="Processing directory"):
        output_filename = f"{os.path.splitext(filename)[0]}_300frame.mp4"
        process_video(os.path.join(input_dir, filename),
                      os.path.join(output_dir, output_filename),
                      max_frames)

def process_input(input_path, output_path, max_frames=300):
    if os.path.isfile(input_path):
        # input a file
        process_video(input_path, output_path, max_frames)
    elif os.path.isdir(input_path):
        # input a directory
        process_directory(input_path, output_path, max_frames)
    else:
        print("Please check the input path.")