import os
import re
import argparse


def get_video_groups(directory):
    video_extensions = {
        "mp4",
        "mkv",
        "avi",
        "mov",
        "flv",
        "wmv",
        "webm",
    }  # Extend as needed
    video_files = [
        f for f in os.listdir(directory) if f.split(".")[-1].lower() in video_extensions
    ]

    grouped_files = {}
    for file in video_files:
        base_name = re.split(r"\.[^.]+$", file)[0]  # Remove only the last extension
        if base_name not in grouped_files:
            grouped_files[base_name] = []
        grouped_files[base_name].append(file)

    return grouped_files


def remove_smaller_videos(directory):
    grouped_files = get_video_groups(directory)

    for base_name, files in grouped_files.items():
        if len(files) > 1:
            file_sizes = {
                file: os.path.getsize(os.path.join(directory, file)) for file in files
            }
            largest_file = max(file_sizes, key=file_sizes.get)

            for file in files:
                if file != largest_file:
                    os.remove(os.path.join(directory, file))
                    print(f"Removed: {file}, kept: {largest_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Remove smaller duplicate video files."
    )
    parser.add_argument("directory", type=str, help="Path to the video directory")
    args = parser.parse_args()

    remove_smaller_videos(args.directory)


if __name__ == "__main__":
    main()
