import pytest
import pathlib
import os
from src.reader import Reader

@pytest.fixture
def test_file():
    # 1. テスト用ファイル（一時ファイル）の作成
    file_path = "test_sample.csv"
    path = pathlib.Path(file_path)
    path.write_text("0,test0\n1,test1")
        
    yield file_path  # テスト関数にファイルパスを渡す
    
    # 2. テスト終了後にファイルを削除
    if path.exists():
        path.unlink()

def test_reader_read_ok(test_file):
    r = Reader(test_file)
    assert r.read(0) == "test0"

def test_reader_read_file_not_found_error(test_file):
    r = Reader("no_such_file")
    with pytest.raises(FileNotFoundError):
        r.read(0)

def test_reader_read_is_a_directory_error(test_file):
    r = Reader("")
    with pytest.raises(IsADirectoryError):
        r.read(0)