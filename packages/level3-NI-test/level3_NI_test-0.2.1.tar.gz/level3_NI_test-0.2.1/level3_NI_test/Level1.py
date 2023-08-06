def main(fileName):
    with open(fileName, 'r') as f:
        lines = f.read().split('\n')
        for l in lines[1:]:
            data = l.split(',')
            line = ''
            for f in data[1:]:
                line += f'{f},'
            line = line[:-1]
            print(line)