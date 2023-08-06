def convert_to_hex(lines):
    lines = lines.strip().split('\n')
    dataSizes = {}
    data = {}
    data['fnames'] = []
    data['lnames'] = []
    data['ages'] = []
    data['genders'] = []
    for line in lines:
        id, fname, lname, age, gender, none = line.strip().split(',')
        data['fnames'].append(fname)
        data['lnames'].append(lname)
        data['ages'] .append(age)
        data['genders'].append(gender)
    fnames = sorted(data['fnames'],key=len)
    lnames = sorted(data['lnames'],key=len)
    ages = sorted(data['ages'],key=len)
    genders = sorted(data['genders'],key=len)

    dataSizes['fnames'] = len(fnames[-1])
    dataSizes['lnames'] = len(lnames[-1])
    dataSizes['ages'] = len(ages[-1])
    dataSizes['genders'] = len(genders[-1])
    finalLine = ''
    for x in range(len(lines)):
        finalLine += f"{data['fnames'][x].ljust(dataSizes['fnames'])}{data['lnames'][x].ljust(dataSizes['lnames'])}{data['ages'][x].ljust(dataSizes['ages'])}{data['genders'][x].ljust(dataSizes['genders'])}None\n"
    lastLines = finalLine.strip().split('\n')
    formattedLine = bytes(finalLine.strip(), 'cp500').hex().upper()
    formattedLines = formattedLine.split('25')
    to_write = ''
    count = 0
    for l in formattedLines:
        count += 1
        if(not count == len(formattedLines)):
            l+= '25'
        else:
            l += '  '
        to_write += f'{bin(count)[2:].zfill(10)}:'
        for idx in range(len(l)):
            if(idx == 16):
                to_write += ' | '
            elif(idx % 2 == 0):
                to_write += ' '
            to_write += l[idx]
        to_write += f' {lastLines[count-1]}'
        to_write += '\n'
    with open('output003.fwf', 'w') as d:
        d.write(to_write.strip())

def main(mainFile):
    main_file = open(mainFile,encoding='utf-8')
    content = main_file.read()
    cyrillic_translit={'\u0410': 'A', '\u0430': 'a',
    '\u0411': 'B', '\u0431': 'b',
    '\u0412': 'V', '\u0432': 'v',
    '\u0413': 'G', '\u0433': 'g',
    '\u0414': 'D', '\u0434': 'd',
    '\u0415': 'E', '\u0435': 'e',
    '\u0416': 'Zh', '\u0436': 'zh',
    '\u0417': 'Z', '\u0437': 'z',
    '\u0418': 'I', '\u0438': 'i',
    '\u0419': 'I', '\u0439': 'i',
    '\u041a': 'K', '\u043a': 'k',
    '\u041b': 'L', '\u043b': 'l',
    '\u041c': 'M', '\u043c': 'm',
    '\u041d': 'N', '\u043d': 'n',
    '\u041e': 'O', '\u043e': 'o',
    '\u041f': 'P', '\u043f': 'p',
    '\u0420': 'R', '\u0440': 'r',
    '\u0421': 'S', '\u0441': 's',
    '\u0422': 'T', '\u0442': 't',
    '\u0423': 'U', '\u0443': 'u',
    '\u0424': 'F', '\u0444': 'f',
    '\u0425': 'Kh', '\u0445': 'kh',
    '\u0426': 'Ts', '\u0446': 'ts',
    '\u0427': 'Ch', '\u0447': 'ch',
    '\u0428': 'Sh', '\u0448': 'sh',
    '\u0429': 'Shch', '\u0449': 'shch',
    '\u042a': '"', '\u044a': '"',
    '\u042b': 'Y', '\u044b': 'y',
    '\u042c': "'", '\u044c': "'",
    '\u042d': 'E', '\u044d': 'e',
    '\u042e': 'Iu', '\u044e': 'iu',
    '\u042f': 'Ia', '\u044f': 'ia'}

    lines = content.split('\n')
    finalLines = []
    toWrite = ''
    last = ''
    for line in lines[1:]:
        # print(line)
        final = ''
        for chr in line:
            tr = r'\u{:04X}'.format(ord(chr))
            if(chr in cyrillic_translit.keys()):
                final += cyrillic_translit[chr]
            else:
                final+= chr
        last += final       
        final = final.split(',')
        for f in range(1,6):
            try:
                toWrite += f'{len(final[f])},'
            except:
                toWrite += '4,'
        last += ',None\n'
        toWrite = f'{toWrite[:-1]}\n'
    convert_to_hex(last)
    with open('output003.csv','w') as csvF:
        csvF.write(toWrite[:-1])

    main_file.close()
main('sample003.csv')