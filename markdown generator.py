import os

'''
TODO:
1. Add more functions to Paragraph:
1.1 Split Line;
1.2 Delete Line;
1.3 Underline;
1.4 Foot Note;
2. Add more functions to List:
2.1 List nesting;
3. Add more functions to Block:
3.1 Block nesting;
4. Add more functions to Code:
4.1 Inline code mode, delete last line '\\n'
5. Fix Link bug:
5.1 Delete last line '\\n'
'''


def processing():
    print('''
    0. Exit and Save my file
    1. Add paragraph
    2. Add title
    3. Add list
    4. Add block
    5. Add code
    6. Add link
    7. Add image
    8. Add table
    ''')
    choice = input('Your Choice (Number): ')
    # 0. Exit and Save my file ---- ----
    if choice == '0':
        global on_input
        on_input = False
    # 1. Add paragraph ---- ----
    elif choice == '1':
        font_type = input('font-type: 0.(Normal, Default) 1.(Italic) 2.(Bold) 3.(Bold & Italic): ')
        if font_type == '' or font_type == '0':
            data = signal_replace(input())
            f.write(data + "\n")
        elif font_type == '1':
            data = signal_replace(input())
            f.write('*' + data + '*\n')
        elif font_type == '2':
            data = signal_replace(input())
            f.write('**' + data + '**\n')
        elif font_type == '3':
            data = signal_replace(input())
            f.write('***' + data + '***\n')
    # 2. Add title ---- ----
    elif choice == '2':
        font_size = int(input('font-size: 1(big)~6(small): '))
        data = signal_replace(input())
        f.write('#' * font_size + ' ' + data + '\n')
    # 3. Add list ---- ----
    elif choice == '3':
        list_type = input('type: 1.(ordered list) 2.(unordered list): ')
        item_num = int(input('number of items: '))
        if list_type == '1':
            for i in range(1, item_num + 1):
                data = signal_replace(input())
                f.write(f'{i}. ' + data + '\n')
            f.write('\n')
        elif list_type == '2':
            for i in range(item_num):
                data = signal_replace(input())
                f.write('* ' + data + '\n')
            f.write('\n')
        else:
            pass
    # 4. Add block ---- ----
    elif choice == '4':
        data_in = input()
        while data_in != '':
            f.write('> ' + data_in + '\n')
            data_in = input()
    # 5. Add code ---- ----
    elif choice == '5':
        code_form = input('code form: 1.(inline code) 2.(code block): ')
        if code_form == '1':
            pass
        elif code_form == '2':
            data_in = input()
            while data_in != '':
                f.write('    ' + data_in + '\n')
                data_in = input()
        else:
            pass
    # 6. Add link ---- ----
    elif choice == '6':
        next_line = input('go to next line? [Y/N] (N for default): ')
        link_title = signal_replace(input('link title: '))
        link_address = signal_replace(input('link address: '))
        if next_line == 'Y':
            f.write(f'[{link_title}]({link_address})\n')
        elif next_line == '' or next_line == 'N':
            f.write(f'[{link_title}]({link_address})')
        else:
            pass
    # 7. Add image ---- ----
    elif choice == '7':
        image_url = signal_replace(input('your image address: '))
        title_text = signal_replace(input('(Optional) your image title: '))
        replace_text = signal_replace(input('(Optional) Show this text when image fail to show: '))
        f.write(f'![{replace_text}]({image_url} "{title_text}")\n')
    # Add table ---- ----
    elif choice == '8':
        row_num = int(input('Row number of table: '))
        col_num = int(input('Column number of table: '))
        for i in range(row_num):
            f.write('|')
            for j in range(col_num):
                data_in = signal_replace(input(f'Row {i + 1} Column {j + 1}: '))
                f.write(f' {data_in} |')
            f.write('\n')
            if i == 0:
                f.write('|' + ' :----: |' * col_num + '\n')


def signal_replace(data_in):
    signal = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!']
    data_out = ""
    for char in data_in:
        if char in signal:
            data_out += '\\' + char
        else:
            data_out += char
    return data_out


fileName = input('your new markdown filename: ')
src = os.getcwd()
print(f'your markdown file in {src}\\{fileName}.md')
on_input = True
with open(fileName + '.md', 'w', encoding='utf-8') as f:
    while on_input:
        processing()
    f.close()
