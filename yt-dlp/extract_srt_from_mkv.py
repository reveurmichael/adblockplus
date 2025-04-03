import subprocess


def extract_srt_from_mkv(mkv_path, output_srt="output.srt", subtitle_track=0):
    command = [
        "ffmpeg",
        "-i",
        mkv_path,
        "-map",
        f"0:s:{subtitle_track}",  # 指定字幕轨道索引
        "-c",
        "srt",  # 输出格式为 SRT
        output_srt,
    ]
    subprocess.run(command, check=True)
    print(f"字幕已提取到：{output_srt}")


# 示例：提取第一个字幕轨道
extract_srt_from_mkv(r"E:\ne zha\Ne.Zha.English.mkv")
