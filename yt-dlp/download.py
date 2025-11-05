import os
import subprocess
import time
import random


def download_url(url, download_dir):
    try:
        if "youtube" in url:
            subprocess.run(["yt-dlp", url])
        elif "bilibili" in url:
            subprocess.run(["bbdown", url])
        print(f"Downloaded: {url}")
        sleep_time = random.uniform(10, 20)
        time.sleep(sleep_time)

    except subprocess.CalledProcessError as e:
        print(f"Error downloading {url}: {e}")


def main(todo_file, download_dir):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    os.makedirs(download_dir, exist_ok=True)
    try:
        with open(todo_file, "r") as file:
            urls = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{todo_file}' does not exist.")
        return

    os.chdir(download_dir)

    for url in urls:
        url = url.strip()
        if url:
            download_url(url, download_dir)


if __name__ == "__main__":
    todo_file = "ToDownloadFromYouTube.txt"
    download_dir = "fun"
    for _ in range(3):
        main(todo_file, download_dir)
