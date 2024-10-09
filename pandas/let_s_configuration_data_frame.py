#
# cd pandas
# python let_s_configuration_data_frame.py
#
# pandas のデータフレームを設定しよう
#
# 参考：
# * 📖 [pandasのインデックス指定で行・列を抽出](https://note.nkmk.me/python-pandas-index-row-column/)
#
import traceback
import datetime
import pandas as pd


DATA_CSV_FILE_PATH = '../resources/number_of_shoe_sizes.csv'


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    try:
        enter_key = input(f"""\
予め、データをCSV形式で {DATA_CSV_FILE_PATH} ファイルに書き込んで用意しています。
これを読み込んでみます。

それでは、エンター・キーを打鍵してみてください。
> """)

        # データ・ファイルを読み込んで、データ・フレームにして返す
        df = pd.read_csv(DATA_CSV_FILE_PATH, encoding="utf8")


        # データを１行ずつ見ていく
        for         shoe_size,       number in\
            zip(df['shoe_size'], df['number']):
            print(f"[{datetime.datetime.now()}] {shoe_size=}  {number=}")


        enter_key = input(f"""\
shoe_size 列をインデックスにしてみましょう。

それでは、エンター・キーを打鍵してみてください。
> """)


        df.set_index(
                ['shoe_size'],
                inplace=True)   # NOTE インプレースを真にすることで、インデックスを設定したデータフレームを戻り値として返すのではなく、このデータフレーム自身にインデックスを設定します

        enter_key = input(f"""\
{df}

shoe_size 列をインデックスにしました。

このレコードを１行ずつ読み込んでみます。
それでは、エンター・キーを打鍵してみてください。
> """)

        try:
            # データを１行ずつ見ていく
            for         shoe_size,       number in\
                zip(df['shoe_size'], df['number']):
                print(f"[{datetime.datetime.now()}] {shoe_size=}  {number=}")
                raise ValueError("ここには来ません")

        except KeyError as e:
            print(e)
        

        enter_key = input(f"""\
インデックスに変更した列はテーブルから削除され、列名としてアクセスできなくなりました。
列名を使わずアクセスすることになります。

それでは、エンター・キーを打鍵してみてください。
> """)

        print(f"""\
{df['number'][30]=}
{df['number'][30.5]=}
{df['number'][31]=}
{df['number'][31.5]=}
{df['number'][32]=}
{df['number'][32.5]=}
{df['number'][33]=}
{df['number'][33.5]=}
{df['number'][34]=}
{df['number'][34.5]=}
{df['number'][35]=}
{df['number'][35.5]=}
{df['number'][36]=}
{df['number'][36.5]=}
{df['number'][37]=}
{df['number'][37.5]=}
{df['number'][38]=}
{df['number'][38.5]=}
{df['number'][39]=}
{df['number'][39.5]=}
{df['number'][40]=}
""")

        enter_key = input(f"""\
インデックスの値を使って、データ行へアクセスできました。

次に指定のインデックスの値が存在するかどうか確認してみましょう。
それでは、エンター・キーを打鍵してみてください。
> """)

        print(f"""\
{(29.5 in df['number'])=}
{(30 in df['number'])=}
""")

        print("おわり。")


    except Exception as err:
        print(f"""\
おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
