# ci-test

## python環境の準備

ルートディレクトリで以下のコマンドを実行する

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## pytestの実行方法

ルートディレクトリで以下のコマンドを実行

```sh
pytest
```

## キャッシュファイル等の削除

以下のコマンドで削除できる

```sh
git clean -fdx
```

削除されるファイルを確認する場合、以下でドライランできる

```sh
git clean -ndx
```