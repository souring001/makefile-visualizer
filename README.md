# makefile-visualizer

## 実行方法
Makefileと関連するファイルをフォルダに入れて以下を実行する
```bash
LANG=C make -p | python3 make_p_to_json.py | python3 json_to_dot.py | dot -Tpdf >| workflow.pdf
```

## 実行結果
![実行結果](result.png "30日自作OSのMakefileに適用した結果") 

## 謝辞
kshramtさんのコードに手を加えて作成しました。
感謝申し上げます。
[Makefileの依存関係の可視化](https://qiita.com/kshramt/items/dace8875d9686475f6cd)
