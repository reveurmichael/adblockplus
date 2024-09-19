import os
import subprocess

def compress_videos(folder_path):
    video_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]

    for video_file in video_files:
        input_path = os.path.join(folder_path, video_file)
        output_path = os.path.join(folder_path, f"c_{video_file}")
        log_file = os.path.join(folder_path, f"{video_file}.log")

        subprocess.run([
            'ffmpeg', '-y', '-i', input_path,
            '-c:v', 'libx264', '-b:v', '1000k',  
            '-pass', '1', '-an', '-f', 'mp4',
            log_file
        ], check=True)

        subprocess.run([
            'ffmpeg', '-y', '-i', input_path,
            '-c:v', 'libx264', '-b:v', '1000k', 
            '-pass', '2', '-c:a', 'aac', '-b:a', '128k',
            output_path
        ], check=True)

        os.remove(log_file)
        # os.remove(input_path)

        print(f"Processed: {video_file} -> {output_path}")

if __name__ == "__main__":
    folder_name = 'cooking3'
    compress_videos(folder_name)