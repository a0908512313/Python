from tkinter import filedialog
from pathlib import Path
import shutil

src_path: str = filedialog.askopenfilename(title='Pick a file')
directory: str = filedialog.askdirectory(title='Pick a location')
dst_path: Path = Path(directory) / 'copy'

shutil.copy2(src=src_path, dst=dst_path)
