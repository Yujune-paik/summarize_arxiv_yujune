# Summarize arXiv paper with figures

arXiv の論文を検索してPDFと書誌データ、chatGPTによる要約情報をxmlファイルとして保存する`query_arxiv.py` と、保存したxmlファイル（群）から 図を抜き出して marp 形式ファイル として保存する `mkmd.py`　から成る。

## 準備

`query_arxiv.py` で OpenAI のAPIキーを設定する。
```python
openai.api_key = 'sk-....'
```

## uasge:

arXivから論文を検索、xml形式で保存し、要約を作成
```console
$ python query_arxiv.py  [-d directory] [-n num-papers] [-y from-year] "search keywords"  
```

ダウンロードした情報からスライド(markdown)を作成
```
$ python mkmd.py [-o output.md] [-d directory] "keyword"
```

directory はxmlファイルが保存されるディレクトリ

生成された ***.md ファイルは marp (https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode ) に準拠しているので、　VS Codeで読み込めばスライド形式として閲覧したり、PDFファイルとして保存することができます：

## コマンド例
### Step.1
```
python query_arxiv.py  --dir ./xmls --num 10 --year 2017 "Ryo Suzuki"
```
### Step.2
```
python mkmd.py -o my_output.md -d ./xmls "3D"
```

## 生成例
<img src="./img0.png" width="480">
<img src="./img1.png" width="480">



