import os
import sys
from datetime import datetime


def create_file(file_path):
    content = []
    print("Enter content line:")
    while True:
        line = input()
        if line.lower() == 'stop':
            break
        content.append(line)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_path, 'a') as file:
        file.write(timestamp + '\n')
        for i, line in enumerate(content, start=1):
            file.write(f"{i} {line}\n")


def main():
    if '-d' in sys.argv:
        directory_index = sys.argv.index('-d') + 1
        directory_path = os.path.join(*sys.argv[directory_index:])
        os.makedirs(directory_path, exist_ok=True)
        print(f"Directory created: {directory_path}")

    if '-f' in sys.argv:
        file_index = sys.argv.index('-f') + 1
        file_name = sys.argv[file_index]
        if '-d' in sys.argv:
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        if os.path.exists(file_path):
            print(f"Appending to existing file: {file_path}")
        else:
            print(f"Creating new file: {file_path}")

        create_file(file_path)


if __name__ == "__main__":
    main()
