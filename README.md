# Tutorial for logging - Python 
## Pythonのloggingモジュールを簡単に使うためのおまじない

## このモジュールについて

基本的に`logging_module`をインポートするだけで`logging`モジュールを使えるようになります。

## Directory Structure / ディレクトリ構成

```sh
.
├── test_main.py // メインのPythonファイル
├── logging_model.py // loggingのおまじないファイル
├── say_hello.py // なんらかの外部モジュール
└── log // Logを保存するディレクトリ(任意に指定可能)
    └── test_main.log // Log File, 名称はデフォルトでメインのファイル名と一致する
```
## Usage / 使い方

### コードの書き方

```python
from logging_module import get_logger
from logging import Logger

def main(logger: Logger):
    logger.info("Start : main()")
    # なんらかの処理
    logger.info("End : main()")

if __name__=="__main__":
    result_dir = None # 任意のディレクトリにLogを出力できる
    logger = get_logger(__name__, result_dir=result_dir)
    main(logger)
```

### 実行結果
- `result_dir=None`の場合、以下の内容が`./test_main.log`に出力される
- `result_dir='log'`の場合、以下の内容が`./dir/test_main.log`に出力される

```sh
$ mkdir log
$ python test_main.py
2023-05-03 16:23:39,227 __main__:6 main_func [INFO]: Start : main()
2023-05-03 16:23:39,227 say_hello:5 say_hello_func [INFO]: Start : say_hello()
2023-05-03 16:23:39,227 say_hello:6 say_hello_func [INFO]: Hello !
2023-05-03 16:23:39,227 say_hello:7 say_hello_func [INFO]: End : say_hello()
2023-05-03 16:23:39,227 __main__:12 main_hello_func [INFO]: Start : main()
2023-05-03 16:23:39,228 __main__:13 main_hello_func [INFO]: Hello !
2023-05-03 16:23:39,228 __main__:14 main_hello_func [INFO]: End : main()
2023-05-03 16:23:39,228 __main__:9 main_func [INFO]: End : main()
```
