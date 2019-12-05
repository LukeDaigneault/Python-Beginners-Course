from pathlib import Path

path = Path("python_standard_library/ecommerce")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

print(path.iterdir())

paths = [p for p in path.iterdir() if p.is_file()]

print(paths)

txt_files = [p for p in path.rglob("*.txt")]
print(txt_files)
