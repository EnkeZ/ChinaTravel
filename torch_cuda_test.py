import torch
print(torch.__version__) # 打印PyTorch版本
# 检查 CUDA 是否可用
print("CUDA 可用:", torch.cuda.is_available())

# 查看 CUDA 版本（框架检测到的版本）
print("CUDA 版本:", torch.version.cuda)

# 查看 GPU 型号
if torch.cuda.is_available():
    print("GPU 型号:", torch.cuda.get_device_name(0))