import pathlib
import csv

class Reader:
    def __init__(self, file_name):
        self.path = pathlib.Path(file_name)
    
    def read(self, id):
        value = None
        with self.path.open() as f:
            lines = csv.reader(f)
            for line in lines:
                if line[0] == str(id):
                    value = line[1]
        return value

def main():
    # ここにメインの処理を書きます
    print("Hello, World!")
    print("プログラムが実行されました。")

# このスクリプトが直接実行された場合のみ、main() を呼び出す
if __name__ == "__main__":
    main()