import os

path_ = os.environ.get("APPDATA")
folder_path  = os.path.join(path_, ".system_arcx64\\testdir")
os.mkdir(folder_path)
