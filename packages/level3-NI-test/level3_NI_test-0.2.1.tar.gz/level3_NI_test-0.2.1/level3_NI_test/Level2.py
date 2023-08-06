main_file = open('sample002.csv')
content = main_file.read()
lines = content.split('\n')
for line in lines[1:]:
    fields = []
    to_append = ""
    split_flag = True
    for c in range(len(line)):
        if line[c] == ',' and split_flag:
            fields.append(to_append)
            to_append = ''
        elif line[c] == '"':
            if line[c-1] == '"':
                to_append += '"'
            elif line[c+1] == '"':
                continue
            else:
                split_flag = not split_flag
        else:
            to_append += line[c]
    fields.append(to_append)
    for f in range(1,6):
        try:
            print(f'{fields[f]}',end='')
        except:
            print(None, end='')
        if f < 5:
            print(";",end='')
    print()
main_file.close()