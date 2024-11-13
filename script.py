def fileopener(file):
    with open(file, "r") as file:
        names = file.readlines()
        name_list = [name.split() for name in names]
        name_dict = {}
        for fl in name_list:
            name_dict[fl[0]] = fl[1]
        print(name_dict["Joel"])
        





fileopener("data.txt")
