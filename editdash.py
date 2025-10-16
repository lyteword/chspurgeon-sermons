import os

folder = "volume-5"

for filename in os.listdir(folder):
    if "_" in filename:
        new_name = filename.replace("_", "-")
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

