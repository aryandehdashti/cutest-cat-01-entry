import pathlib, shutil
src = pathlib.Path(__file__).resolve().with_name("entry.jpg")
dst = pathlib.Path("/output/entry.png")
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, dst)
