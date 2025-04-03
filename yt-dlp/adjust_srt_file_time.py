import srt
from datetime import timedelta


def delay_srt(input_file, output_file, delay_seconds=2):
    # 读取原始字幕文件
    with open(input_file, "r", encoding="utf-8") as f:
        subs = list(srt.parse(f.read()))

    # 创建时间增量对象
    delay = timedelta(seconds=delay_seconds)

    # 调整每个字幕的时间
    modified_subs = []
    for sub in subs:
        new_start = sub.start + delay
        new_end = sub.end + delay
        modified_subs.append(
            srt.Subtitle(
                index=sub.index, start=new_start, end=new_end, content=sub.content
            )
        )

    # 写入新文件
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(srt.compose(modified_subs))


if __name__ == "__main__":
    input_srt = "Ne.Zha.English1.srt"
    output_srt = "Ne.Zha.English.srt"
    delay_srt(input_srt, output_srt, delay_seconds=2)
    print(f"字幕已延迟 2 秒并保存为 {output_srt}")
