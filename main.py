from write_frame_number import process_input
import os
'''
# 示例1：指定完整的输出文件路径
input_path = "/path/to/video.mp4"
output_path = "/path/to/output/custom_name.mp4"
process_input(input_path, output_path)
'''

'''
# 示例2：只指定输出目录，自动添加_with_frame后缀
input_path = "/path/to/video.mp4"
output_path = "/path/to/output/"  # 输出将是 /path/to/output/video_with_frame.mp4
process_input(input_path, output_path) 
'''

# 以上两种方式都可以使用，根据需要选择（二选一）