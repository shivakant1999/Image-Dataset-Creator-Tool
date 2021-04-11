import cx_Freeze
import sys
import os
base = None
if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Gunjesh\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Gunjesh\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("employee.py", base=base,icon="profile.ico")]

cx_Freeze.setup(
    name = "EPMS",
    options = {"build_exe": {"packages":["tkinter","os","sys", "opencv", "random", "cv2"], "include_files":['tcl86t.dll','tk86t.dll','profile.ico','Salary_reciept']}},
    version = "1.00",
    description = "IDCT is Image Dataset Creator Tool | Developed by Shivakant Vishwakarma ",
    executables = executables
    )
