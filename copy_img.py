import glob
import os
import shutil

ROOT = "/home/ciplab/data/unseen/kubric360_v2"
RGBOUT = "./data/imgs"
MASKOUT = "./data/masks"

for scene in os.listdir(ROOT):
    scene = os.path.join(ROOT, scene)
    if not os.path.isdir(scene):
        continue
    print(scene)

    scene_idx = os.path.basename(scene)
    for rgbpred in glob.glob(os.path.join(scene, "*rgb_test.png")):
        idx = int(os.path.basename(rgbpred).split("_")[0])
        shutil.copyfile(rgbpred, os.path.join(RGBOUT, f"{int(scene_idx):02d}_{idx:02d}.png"))

    for mask in glob.glob(os.path.join(scene, "*mask.png")):
        idx = int(os.path.basename(mask).split("_")[0])
        shutil.copyfile(mask, os.path.join(MASKOUT, f"{int(scene_idx):02d}_{idx:02d}.png"))