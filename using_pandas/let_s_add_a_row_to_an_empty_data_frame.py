# cd using_pandas
# python let_s_add_a_row_to_an_empty_data_frame.py
#
#   空のデータフレームに行を追加しよう
#
import traceback
import datetime
import pandas as pd


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    try:

        # 空のデータフレームを作ります
        df = pd.DataFrame()

        # 空のデータフレームはテーブルが表示されない
        print(df)

        try:
            df.loc[len(df)] = {'age':44}
        except ValueError as e:
            print(f"存在しない列を指定して行を追加しようとすると、例外が投げられてくる {e=}")


        # 列がないので、列を追加することになる。列の初期値も指定する（指定列の全ての行に値が埋められる）
        df['age'] = 0
        print(df)

        # この書き方では、末尾ではなく、インデックスが -1 のところに行が追加される
        # df.loc[-1] = {'age':44}

        # インデックスが０から始まる連番なら、以下の書き方で最終行に追加される
        df.loc[len(df)] = {'age':44}
        print(df)


        print("おわり")


    except Exception as err:
        print(f"""\
おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
