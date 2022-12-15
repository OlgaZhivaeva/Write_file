files = ['1.txt', '2.txt', '3.txt']
len_dict = {}
lines_dict = {}
for file in files:
    with open(file, 'rt', encoding='utf-8') as f:
       res = f.readlines()
       lines_dict[file] = res
       len_dict[file] = len(res)
sort_len = sorted(len_dict, key=len_dict.get)
with open('Res.txt', 'at', encoding='utf-8') as f:
    for file in sort_len:
        f.write(f'{file}\n')
        f.write(f'{str(len_dict[file])}\n')
        for line in lines_dict[file]:
            f.write(line)
        f.write('\n')
