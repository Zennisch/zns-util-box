import os
import subprocess

from zns_util_box.Constant import Path

batch_file_path = input("Enter the path to the batch file (.bat): ").strip()

if not os.path.exists(batch_file_path):
    print("The specified batch file does not exist.")
    print("Exiting...")
    exit(1)

icon_file_path = input("Enter the path to the icon file (.ico/png) (optional): ").strip()

if icon_file_path and not os.path.exists(icon_file_path):
    print("The specified icon file does not exist.")
    print("Exiting...")
    exit(1)

os.makedirs(Path.RESOURCE, exist_ok=True)
script_file_path = f"{Path.RESOURCE}/temp.py"
script_content = f"""
import subprocess
subprocess.run(r'{batch_file_path}', shell=True)
"""

with open(script_file_path, "w", encoding="utf-8") as f:
    f.write(script_content)

cmd = f'pyinstaller --onefile "{script_file_path}" --distpath "{Path.RESOURCE}" --workpath "{Path.RESOURCE}" --specpath "{Path.RESOURCE}"'
if icon_file_path:
    cmd += f' --icon "{icon_file_path}"'

print("Generating executable...")
subprocess.run(cmd, shell=True)
print(f"Executable generated successfully. Please check the {Path.RESOURCE} folder.")
os.remove(script_file_path)
