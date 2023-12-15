def read_file(file_path: str) -> list:
    with open(file_path, 'r') as input:
        content = input.read()
        return content
    
if __name__ == "__main__":
    content = read_file('./2015_day01/input.txt')
    position = 0
    for i, ch in enumerate(content):
        if position != -1:
            if ch == "(":
                position += 1
            else:
                position -= 1
        else:
            break
    print(i)