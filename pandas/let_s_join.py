#
# cd pandas
# python let_s_join.py
#
# （pandas）テーブルを結合しよう
#
import traceback
import datetime
import pandas as pd


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    try:
        a_df = pd.DataFrame(
                {
                    'No': [0, 1, 2],
                    'A': ['A1', 'A2', 'A3'],
                    'B': ['B1', 'B2', 'B3'],
                    'C': ['C1', 'C2', 'C3'],
                },  # 列ごとに縦に並んだデータ
                columns=['No', 'A', 'B', 'C'])
        a_df.set_index(
                'No',
                inplace=True)   # NOTE `inplace=True` - インデックスを指定したデータフレームを戻り値として返すのではなく、このインスタンス自身を更新します

        b_df = pd.DataFrame(
                {
                    'No': [0, 1, 2],
                    'D': ['D1', 'D2', 'D3'],
                    'E': ['E1', 'E2', 'E3'],
                    'F': ['F1', 'F2', 'F3'],
                },
                columns=['No', 'D', 'E', 'F'])
        b_df.set_index(
                'No',
                inplace=True)

        print(f"""\
２つのテーブルＡ、Ｂを予め用意しておきます

a_df:
{a_df}

b_df:
{b_df}
""")

        enter_key = input(f"""\

これらのテーブルの No インデックスを一致させて、１つのテーブルに結合してみましょう。
それでは、エンター・キーを打鍵してみてください。
> """)

        # インデックスが消えてしまうので、 .reset_index() を使って、インデックスを列として生成します。
        # そしてマージしたあと、その列をインデックスに戻します
        ab_df = pd.merge(a_df.reset_index(), b_df.reset_index(), on='No').set_index('No')

        print(f"""\
ab_df:
{ab_df}
""")

        enter_key = input(f"""\

１つのテーブルに結合できました。

しかし、いくつかの操作を一度にやってしまって、途中で何をしたのか分からなかったかもしれません。
途中の操作を見ていきましょう。

それでは、エンター・キーを打鍵してみてください。
> """)

        print(f"""\
"No" に注目してください

a_df.reset_index():
{a_df.reset_index()}

b_df.reset_index():
{b_df.reset_index()}
""")

        enter_key = input(f"""\

２つのテーブルＡ、Ｂにあった No インデックスを、いったん、列にしました。

これによって、 No 列が同じ行どうしの列をくっつけることができるようになります。
次に、No 列が同じ行どうしの列をくっつけましょう。
それでは、エンター・キーを打鍵してみてください。
> """)

        print(f"""\
pd.merge(a_df.reset_index(), b_df.reset_index(), on='No'):
{pd.merge(a_df.reset_index(), b_df.reset_index(), on='No')}
""")

        enter_key = input(f"""\

これでも、２つのテーブルＡ、Ｂにあった No が同じ行どうしの列をくっつけることができました。

しかし、 No が列になっています。
No をインデックスに戻しましょう。
それでは、エンター・キーを打鍵してみてください。
> """)

        print(f"""\
pd.merge(a_df.reset_index(), b_df.reset_index(), on='No').set_index('No'):
{pd.merge(a_df.reset_index(), b_df.reset_index(), on='No').set_index('No')}
""")

        print("""\

No がインデックスになりました。""")

        print("おわり。")


    except Exception as err:
        print(f"""\
おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
