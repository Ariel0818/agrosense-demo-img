#!/usr/bin/env python3
import os
import cv2

input_dir = "predict2"  # 👉 改成你自己的图片目录路径

valid_ext = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}
output_dir = input_dir + "_rotated"
os.makedirs(output_dir, exist_ok=True)

for name in os.listdir(input_dir):
    ext = os.path.splitext(name)[1].lower()
    if ext in valid_ext:
        img_path = os.path.join(input_dir, name)
        img = cv2.imread(img_path)
        if img is None:
            print(f"跳过无法读取的文件: {img_path}")
            continue

        # # 顺时针旋转90度
        # img_rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

        # 逆时针旋转 90 度
        img_rot = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)


      

        cv2.imwrite(os.path.join(output_dir, name), img_rot)

        print(f"已旋转: {name}")

print("全部完成！🎉")
