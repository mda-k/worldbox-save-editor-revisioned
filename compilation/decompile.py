import time
import os
import zlib
from pathlib import Path
from tkinter import messagebox, filedialog
import sys
cdir = Path(__file__).resolve().parent
rdir = cdir.parent / "ui"
if str(rdir) not in sys.path:
    sys.path.insert(0, str(rdir))
from start import *

def decompile(): #pretty self explanatory, for the choose file button
    savefile = filedialog.askopenfilename(title="select your .wbox save", filetypes=[("WorldBox files", "*.wbox")])
    if savefile:
        print(f"\n{savefile}")
    savefile = Path(savefile)
    output = savefile.with_suffix(".json")
    print(output)
    wboxdata = savefile.read_bytes()
    decompiled = None
    try:
        decompiled = zlib.decompress(wboxdata)
        print(f"decompressed. output: {decompiled}")
    except zlib.error:
        messagebox.showerror("zlib decompression error!", "pretty self explanatory. you do not have any other option than to restart the program and try again.")
    decodeddata = decompiled.decode("utf-8")
    print("decoded into utf-8.")
    output.write_text(decodeddata, encoding="utf-8")
    print("wrote out, finished decompiling and decompression!")
    time.sleep(2)
    print("decompile.py, start.py done!")