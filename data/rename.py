import os


def rename(folder_path: str):
    files = os.listdir(folder_path)

    # 初始化图片计数器
    count = 0
    print(folder_path, len(files))
    # # 遍历文件列表
    for file in files:
        # 检查文件是否为图片文件，这里假设图片文件的扩展名为.jpg或.png
        if file.endswith('.jpg') or file.endswith('.png'):
            # 构建新的文件名
            new_file_name = f'val{count}.{file.split(".")[-1]}'
            # 获取原文件的完整路径
            old_file_path = os.path.join(folder_path, file)

            if count < 200:
                # 获取新文件的完整路径
                new_file_path = os.path.join(folder_path, new_file_name)
                # 重命名文件
                os.rename(old_file_path, new_file_path)
            else:
                os.remove(old_file_path)

            # 图片计数器加1
            count += 1

    print(folder_path, "所有图片文件已重命名。")

if __name__ == '__main__':
    rename("./chase256/HR/x4")
    rename("./gong1024/HR/x4")