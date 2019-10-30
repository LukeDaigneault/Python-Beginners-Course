from pathlib import Path
from time import ctime
import shutil

path = Path("python_standard_library/ecommerce/temp.txt")

# path.exists()
# path.rename("test2.txt")
# path.unlink()

print(ctime(path.stat().st_ctime))

print(path.read_text())
path.write_text("BBAJAJZE")


source = Path("python_standard_library/ecommerce/temp.txt")
target = Path("python_standard_library/ecommerce/temp2.txt")
# "tedious"
# target.write_text(source.read_text())

shutil.copy(source, target)
