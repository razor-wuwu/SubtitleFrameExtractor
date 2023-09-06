# -*- coding: utf-8 -*-
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import argparse


def extract_frames(video_path, y_start, y_end, output_path):
    # 步骤1：从视频中截取帧
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    time_points = np.arange(2, 60, 1.5)  # 可以提供任意多的时间点，单位是秒

    frames = []
    for time_point in time_points:
        cap.set(cv2.CAP_PROP_POS_FRAMES, time_point * fps)
        ret, frame = cap.read()
        if ret:
            frames.append(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))

    # 步骤2：从第一帧中截取全图，从其他帧中截取字幕部分
    first_frame = frames[0]
    subtitle_frames = [frame.crop((0, y_start, video_width, y_end)) for frame in frames[1:]]

    # 步骤3：将所有图片纵向拼接
    final_image = Image.new('RGB', (video_width, video_height + (y_end - y_start) * (len(frames) - 1)))
    final_image.paste(first_frame, (0, 0))

    # 创建一个ImageDraw对象
    draw = ImageDraw.Draw(final_image)

    # 加载一个字体对象
    #font = ImageFont.truetype(font_path, 20)
    font = ImageFont.load_default()

    # 在每个图的左边缘中心处添加时间点标签
    for i, (frame, time_point) in enumerate(zip(subtitle_frames, time_points[1:])):
        final_image.paste(frame, (0, video_height + i * (y_end - y_start)))
        text = str(time_point)
        text_width, text_height = draw.textsize(text, font=font)
        draw.text((10, video_height + i * (y_end - y_start) + ((y_end - y_start) - text_height) // 2), text, fill="red",
                  font=font)

    # 保存结果图片
    final_image.save(output_path)

    # 释放VideoCapture对象
    cap.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract frames from video and create a subtitle collage.')
    parser.add_argument('video_path', help='Path to the video file')
    parser.add_argument('y_start', type=int, help='Start Y-coordinate of the subtitle region')
    parser.add_argument('y_end', type=int, help='End Y-coordinate of the subtitle region')
    parser.add_argument('output_path', help='Path to save the output image')

    args = parser.parse_args()

    extract_frames(args.video_path, args.y_start, args.y_end, args.output_path)
