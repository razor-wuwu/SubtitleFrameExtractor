# 介绍

[English Version](./README.md)

本项目包含一个Python脚本，它可以从视频文件中提取帧，并创建一个字幕拼贴。该脚本使用OpenCV和PIL来处理视频和图像。该脚本在指定的时间点捕捉帧，并从这些帧中提取字幕区域。然后，这些帧将垂直合并，以创建一个带有相应时间点标签的字幕区域的最终图像。


项目预览
![预览](./assets/p1.png)

# 安装
要安装必要的依赖项，你可以使用以下命令：

```
pip install opencv-python-headless
pip install pillow
```
# 使用方法
1. 设置脚本

下载script.py文件，并用你喜欢的代码编辑器打开它。

2. 修改时间点

在运行脚本之前，建议你修改脚本中的time_points变量以满足你的需求。它目前设置为从第2秒到第20秒每秒捕捉一帧。调整np.arange函数中的值和步长来指定不同的时间点。

```python
time_points = np.arange(2, 20, 1)  # 根据需要修改这些值
```

3. 运行脚本

该脚本是设计成从命令行用以下参数运行的：

- video_path: 视频文件的路径
- y_start: 字幕区域的开始Y坐标
- y_end: 字幕区域的结束Y坐标
- output_path: 保存输出图像的路径
示例：

```bash
python script.py video_path y_start y_end output_path
```
将video_path，y_start，y_end和output_path替换为你实际用例的相应值。