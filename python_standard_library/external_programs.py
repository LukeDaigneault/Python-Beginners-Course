import subprocess

completed = subprocess.run(["ls", "-l"], capture_output=True)
print(type(completed))

print("args", completed.args)
print("return code", completed.returncode)
print("standard error", completed.stderr)
print("standard out", completed.stdout)
