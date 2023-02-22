with open('new_file.txt', 'w', encoding='utf-8') as f:
    # 'w'는 쓰기와 덮어쓰기에 해당한다.
    # 'a'는 파일이 없는 경우 파일을 만들고
    # 기존의 파일이 있는 경우에는 파일에 추가한다.
    f.write("Hello world!\n")
    f.write("My name is Codeit.\n")

with open('new_file.txt', 'a', encoding='utf-8') as f:
    f.write("Hello world!\n")
    f.write("My name is Codeit.\n")
