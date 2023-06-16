import os

coba = ["bubur",
        "burger", 
        "cakwe", 
        "capcay", 
        "crepes", 
        "donat", 
        "eskrim", 
        "gudeg", 
        "gulai_ikan", 
        "ikan_goreng", 
        "jeruk",
        "kebab",
        "kentang_goreng", 
        "kerak_telor", 
        "nasi_kuning",
        "nasi_pecel",
        "papeda",
        "rendang", 
        "tahu_sumedang"]


for new_name in coba:
    base_dir = fr'E:\Dataset\edited_dataset\test\{new_name}'

    file_list = os.listdir(base_dir)

    for i, filename in enumerate(file_list):
        print(filename)
    #     if filename.endswith('.jpg'):
    #         name, ext = os.path.splitext(filename)
    #         new_filename = f'{new_name}{i}{ext}'
    #         os.rename(os.path.join(base_dir, filename), os.path.join(base_dir, new_filename))
    # print("Successfully renamed all files")

