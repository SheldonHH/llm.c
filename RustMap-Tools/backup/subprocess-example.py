import subprocess

# 设置新项目的名称
project_name = "my_project"

# 构建命令
command = ["cargo", "new", project_name]

# 运行命令
result = subprocess.run(command, capture_output=True, text=True)

# 检查命令是否成功执行
if result.returncode == 0:
    print("项目创建成功！")
    print(result.stdout)  # 打印输出信息
else:
    print("项目创建失败：")
    print(result.stderr)  # 打印错误信息

