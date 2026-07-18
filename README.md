# ci-test

## python環境の準備

以下のコマンドを実行する

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

src, test配下に、`__pycache__`ディレクトリができるので手動で削除する