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
        a_df.dropna(subset=['Even'], inplace=True)

        print(f"""\

A table
-------
{a_df}
""")

        enter_key = input(f"""\

Even 列に値の入っている行だけを抽出できました

しかし、インデックスの番号が飛び番になってしまいました。
インデックスの番号を振り直してみましょう

それでは、エンター・キーを打鍵してみてください
> """)

        a_df.reset_index(inplace=True)

        print(f"""\

"No" インデックスが列に変わり、それとは別に行番号が追加されたことに注目してください

A table
-------
{a_df}
""")

        enter_key = input(f"""\

これで、行番号でアクセスできるようになりました

[1]行目、[0]行目、[2]行目の順に Even 列の値を取得してみましょう。
それでは、エンター・キーを打鍵してみてください
> """)

        print(f"""\

[1]行目のEven {a_df.at[1,'Even']}
[0]行目のEven {a_df.at[0,'Even']}
[2]行目のEven {a_df.at[2,'Even']}

[1]行目、[0]行目、[2]行目の順に Even 列の値を取得できました
""")

        enter_key = input(f"""\

しかしこれでは、インデックスを付けたまま連番にランダムアクセスするということができません

そこで、インデックスはそのままに、連番の列を新しく追加してみましょう。
それでは、エンター・キーを打鍵してみてください
> """)

        a_df.set_index('No', inplace=True)

        # EvenNo 列の追加
        a_df['EvenNo'] = range(0, len(a_df.index))

        print(f"""\

A table
-------
{a_df}

EvenNo 列を最終列に追加できました
""")

        enter_key = input(f"""\

EvenNo 列を、列の左端に移動しましょう。
それでは、エンター・キーを打鍵してみてください
> """)

        a_df = a_df[['EvenNo', 'Even', 'Odd']]

        print(f"""\

A table
-------
{a_df}

EvenNo 列を、列の左端に移動できました
""")

        print("おわり。")


    except Exception as err:
        print(f"""\
おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
