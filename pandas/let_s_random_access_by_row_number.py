#
# cd pandas
# python let_s_random_access_by_row_number.py
#
# （pandas）行番号でランダムアクセスしよう
#
import traceback
import datetime
import numpy as np
import pandas as pd


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    try:
        a_df = pd.DataFrame(
                {
                    'No': [0, 1, 2, 3, 4, 5],
                    'Even': ['E1', np.nan, 'E2', np.nan, 'E3', np.nan],
                    'Odd': [np.nan, 'O1', np.nan, 'O2', np.nan, 'O3'],
                },  # 列ごとに縦に並んだデータ
                columns=['No', 'Even', 'Odd'])
        a_df.set_index(
                'No',
                inplace=True)   # NOTE `inplace=True` - インデックスを指定したデータフレームを戻り値として返すのではなく、このインスタンス自身を更新します

        print(f"""\

以下のテーブルＡを予め用意しておきます

A table
-------
{a_df}
""")

        enter_key = input(f"""\

ひとまず、 Even 列に値の入っている行だけを抽出してみましょう。
それでは、エンター・キーを打鍵してみてください
> """)

        # インデックスが消えてしまうので、 .reset_index() を使って、インデックスを列として生成します。
        # そしてマージしたあと、その列をインデックスに戻します
        even_df = a_df.dropna(subset=['Even'])

        print(f"""\

A table
-------
{even_df}
""")

        enter_key = input(f"""\

Even 列に値の入っている行だけを抽出できました

しかし、インデックスの番号が飛び番になってしまいました。
インデックスの番号を振り直してみましょう

それでは、エンター・キーを打鍵してみてください
> """)

        even_df.reset_index(
                inplace=True)   # NOTE `inplace=True` - インデックスを指定したデータフレームを戻り値として返すのではなく、このインスタンス自身を更新します

        print(f"""\

"No" インデックスが列に変わり、それとは別に行番号が追加されたことに注目してください

A table
-------
{even_df}
""")

        enter_key = input(f"""\

これで、行番号でアクセスできるようになりました

[1]行目、[0]行目、[2]行目の順に Even 列の値を取得してみましょう。
それでは、エンター・キーを打鍵してみてください。
> """)

        print(f"""\

[1]行目のEven {even_df.at[1,'Even']}
[0]行目のEven {even_df.at[0,'Even']}
[2]行目のEven {even_df.at[2,'Even']}
""")

        print("おわり。")


    except Exception as err:
        print(f"""\
おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
