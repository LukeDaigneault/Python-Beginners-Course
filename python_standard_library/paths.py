from pathlib import Path

# absolute path
Path("/home/luke")

# current folder
Path()

# relative
path = Path("../classes/ecommerce/__init__.py")

# addition

Path() / Path("ecommerce")
Path() / "ecommerce"

# user home path
Path.home()

path.exists()
path.is_file()
path.is_dir()

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

path = path.with_suffix(".txt")

print(path.absolute())
