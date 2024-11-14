import cv2
import os
from tqdm import tqdm

def get_video_codec(output_path):
    """根据输出文件扩展名选择合适的编码器"""
    ext = os.path.splitext(output_path)[1].lower()
    codec_map = {
        '.mp4': 'mp4v',  # 或者使用 'avc1' 用于 H.264 编码
        '.avi': 'XVID',
        '.mov': 'mp4v',
        '.mkv': 'mp4v',
        '.wmv': 'WMV2',
        '.flv': 'FLV1',
        '.webm': 'VP80'
    }
    return codec_map.get(ext, 'mp4v')

def process_video(input_path, output_path, max_frames=None):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {input_path}")
        return
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # 获取适合的编码器
    codec = get_video_codec(output_path)
    fourcc = cv2.VideoWriter_fourcc(*codec)
    
    try:
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        if not out.isOpened():
            print(f"Error: Could not create output video file {output_path}")
            return

        frame_number = 0
        frames_to_process = max_frames if max_frames is not None else total_frames
        
        for _ in tqdm(range(frames_to_process), desc="Processing video"):
            ret, frame = cap.read()
            if not ret:
                break
                
            frame_number += 1
            # 添加帧数文本
            cv2.putText(frame, f'frame: {frame_number}', (10,50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            out.write(frame)

    except Exception as e:
        print(f"Error processing video: {str(e)}")
    
    finally:
        cap.release()
        out.release()

def process_directory(input_dir, output_dir, max_frames=None):
    # 支持的视频格式
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm')
    
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 获取所有支持格式的视频文件
    files = [f for f in os.listdir(input_dir) if f.lower().endswith(video_extensions)]
    
    if not files:
        print(f"No video files found in {input_dir}")
        return
        
    for filename in tqdm(files, desc="Processing directory"):
        file_ext = os.path.splitext(filename)[1]
        output_filename = f"{os.path.splitext(filename)[0]}_with_frame{file_ext}"
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, output_filename)
        
        print(f"\nProcessing: {filename}")
        process_video(input_file, output_file, max_frames)

def process_input(input_path, output_path, max_frames=None):
    if not os.path.exists(input_path):
        print(f"Error: Input path '{input_path}' does not exist.")
        return
        
    if os.path.isfile(input_path):
        # 如果输出路径是目录，则在目录中创建带有_with_frame后缀的文件
        if os.path.isdir(output_path):
            input_filename = os.path.basename(input_path)
            name, ext = os.path.splitext(input_filename)
            output_filename = f"{name}_with_frame{ext}"
            output_path = os.path.join(output_path, output_filename)
        
        # 确保输出目录存在
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        process_video(input_path, output_path, max_frames)
    elif os.path.isdir(input_path):
        process_directory(input_path, output_path, max_frames)
    else:
        print("Please check the input path.")