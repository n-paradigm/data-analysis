import os
import json
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# 全局变量
image_list = []  # 存储图片文件路径
current_index = 0  # 当前图片索引
json_folder = ""  # 存储 JSON 文件的文件夹路径

# 选择文件夹
def select_folder():
    global image_list, json_folder, current_index
    folder = filedialog.askdirectory()
    if not folder:
        return
    
    json_folder = folder
    image_list = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    current_index = 0

    if image_list:
        show_image(image_list[current_index])

# 显示图片
def show_image(img_path):
    img = Image.open(img_path)
    img = img.resize((400, 300))  # 调整图片大小
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

# 显示上一张图片
def prev_image():
    global current_index
    if current_index > 0:
        current_index -= 1
        show_image(image_list[current_index])

# 显示下一张图片
def next_image():
    global current_index
    if current_index < len(image_list) - 1:
        current_index += 1
        show_image(image_list[current_index])

# 点击“是”按钮后，修改 JSON 文件
def mark_as_healthy():
    if not image_list:
        return
    
    img_path = image_list[current_index]
    json_path =   "datasets/annotations/annotations.json"  # 图片对应的 JSON 文件
    
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        # 修改 JSON 数据
        if "annotations" in data:
            data["annotations"] =({"是否健康": "是"})
        
        # 保存修改后的 JSON
        with open(json_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        status_label.config(text=f"已标记 {os.path.basename(img_path)} 为健康")
    else:
        status_label.config(text=f"未找到 {os.path.basename(json_path)}")
def mark_as_nothealthy():
    if not image_list:
        return
    
    img_path = image_list[current_index]
    json_path =   "datasets/annotations/annotations.json"  # 图片对应的 JSON 文件
    
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        # 修改 JSON 数据
        if "annotations" in data:
            data["annotations"] =({"是否健康": "是"})
        
        # 保存修改后的 JSON
        with open(json_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        status_label.config(text=f"已标记 {os.path.basename(img_path)} 为健康")
    else:
        status_label.config(text=f"未找到 {os.path.basename(json_path)}")
# 创建 GUI 界面
root = tk.Tk()
root.title("测试集标注器")

# 选择文件夹按钮
select_button = tk.Button(root, text="选择文件夹", command=select_folder)
select_button.pack()

# 显示图片的 Label
image_label = tk.Label(root)
image_label.pack()

# 按钮
btn_frame = tk.Frame(root)
btn_frame.pack()

prev_button = tk.Button(btn_frame, text="上一张", command=prev_image)
prev_button.pack(side=tk.LEFT, padx=10)

next_button = tk.Button(btn_frame, text="下一张", command=next_image)
next_button.pack(side=tk.LEFT, padx=10)

yes_button = tk.Button(root, text="是", command=mark_as_healthy, fg="white", bg="green")
yes_button.pack(pady=10)

no_button = tk.Button(root,text="否",command=mark_as_nothealthy,fg="white",bg="green")
no_button.pack(pady=20)
# 状态提示
status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

# 运行 GUI
root.mainloop()
