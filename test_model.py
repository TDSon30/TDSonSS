import os
import re
import subprocess
import glob
from IPython.display import Image, display

def get_latest_folder(base_dir, prefix='predict'):
    folders = [f for f in os.listdir(base_dir) if f.startswith(prefix) and os.path.isdir(os.path.join(base_dir, f))]
    if not folders:
        raise FileNotFoundError(f'Không tìm thấy folder bắt đầu bằng "{prefix}" trong {base_dir}')

    def extract_number(name):
        match = re.match(rf'{prefix}(\d*)', name)
        return int(match.group(1)) if match and match.group(1).isdigit() else 0

    folders.sort(key=extract_number, reverse=True)
    return os.path.join(base_dir, folders[0])

# Lấy đường dẫn predict mới nhất
predict_dir = get_latest_folder('/content/YOLO/runs/detect', 'predict')

# In đường dẫn kiểm tra
print("📂 Predict dir:", predict_dir)

# Tìm ảnh trong thư mục con /images nếu có
jpg_files = glob.glob(os.path.join(predict_dir, 'images', '*.jpg'))  # hoặc predict_dir nếu không có images/

# Kiểm tra có ảnh không
if not jpg_files:
    print("❌ Không tìm thấy ảnh .jpg trong folder.")
else:
    print(f"✅ Tìm thấy {len(jpg_files)} ảnh. Hiển thị:")
    for file in jpg_files:
        img = PILImage.open(file)
        display(img)  # PIL + display sẽ chắc chắn hoạt động
