import subprocess

dotname = ".mftheme"

source = input("input the folder >>>")
target = source + dotname


subprocess.run([
    "pwsh",
    "-Command",
    f"Compress-Archive -Path {source}\\* -destinationPath {target} -force"
])

