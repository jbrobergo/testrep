def fileopener(file):
    with open(file, "r") as file:
        names = file.readlines()
        name_list = [name.strip("\n") for name in names]
        print(name_list)

fileopener("data.txt")
