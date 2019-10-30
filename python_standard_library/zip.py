from pathlib import Path
from zipfile import ZipFile


# with ZipFile("files.zip", "w") as zip:

#     for path in Path("python_standard_library/ecommerce").rglob("*.*"):
#         zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("python_standard_library/ecommerce/temp2.txt")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("python_standard_library/extracted")
