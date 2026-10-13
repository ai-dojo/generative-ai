def read_iliad(
    data_path="../.assets/data/iliad/iliad.txt"
):
    with open(data_path) as txt_file:
        return txt_file.read()
