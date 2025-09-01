import os, shutil

SRC = r"C:\Users\ADMIN\Downloads\emotion classification\Data\images"  # or r"C:\path\to\your\images"
DST = SRC.rstrip("/\\") + "_renamed"
os.makedirs(DST, exist_ok=True)

for entry in os.scandir(SRC):
    if not entry.is_file():
        continue
    base = entry.name
    stem, ext = os.path.splitext(base)

    trimmed = stem[:-2] if len(stem) >= 2 else stem
    new = trimmed + ext
    target = os.path.join(DST, new)

    # avoid collisions by adding _1, _2, ...
    i = 1
    while os.path.exists(target):
        target = os.path.join(DST, f"{trimmed}_{i}{ext}")
        i += 1

    shutil.copy2(entry.path, target)
