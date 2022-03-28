def read_file():
    with open("HarryPotterNames.txt", "r", encoding="utf8") as f:
        names = []
        for line in f:
            names.append(list(sorted(line.lower().strip())))
        return names

print(read_file())

names_list = read_file()

for name in names_list:
    pass
