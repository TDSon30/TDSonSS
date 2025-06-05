import os
import re
import subprocess
import glob
from IPython.display import Image, display

def get_latest_folder(base_dir, prefix='train'):
    folders = [f for f in os.listdir(base_dir) if f.startswith(prefix) and os.path.isdir(os.path.join(base_dir, f))]
    if not folders:
        raise FileNotFoundError(f'Không tìm thấy folder bắt đầu bằng "{prefix}" trong {base_dir}')
 def extract_number(name):
        match = re.match(rf'{prefix}(\d*)', name)
        return int(match.group(1)) if match and match.group(1).isdigit() else 0

    folders.sort(key=extract_number, reverse=True)
    return os.path.join(base_dir, folders[0])

# Lấy folder train mới nhất
train_dir = get_latest_folder('/content/YOLO/runs/detect', 'train')
best_pt_path = os.path.join(train_dir, 'weights/best.pt')
val_images = '/content/YOLO/data/validation/images'

# Chạy lệnh predict
subprocess.run([
    'yolo',
    'predict',
    f'model={best_pt_path}',
    f'source={val_images}',
    'save=True'
])

# Lấy folder predict mới nhất
predict_dir # In và hiển thị ảnh .jpg
jpg_files = glob.glob(os.path.join(predict_dir, '*.jpg'))

for file in jpg_files:
    display(Image(filename=file))= get_latest_folder('/content/YOLO/runs/detect', 'predict')
