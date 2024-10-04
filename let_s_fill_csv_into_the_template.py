#
# python let_s_fill_csv_into_the_template.py
#
# テンプレートにCSVを流し込もう
#
import traceback
import pandas as pd


DATA_CSV_FILE_PATH = 'resources/data.csv'
TEMPLATE_TXT_FILE_PATH = 'resources/template.txt'


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
        try:
                # ファイル名の一部が入力されます
                file_path = input(f"""\
予め、データをCSV形式で {DATA_CSV_FILE_PATH} ファイルに書き込んで用意しています。

また、データを書き出す書式を書いた {TEMPLATE_TXT_FILE_PATH} ファイルを用意しています。
これはテンプレートと呼びます。

これから、テンプレートにデータを流し込むのを練習をします。

それでは、エンター・キーを打鍵してみてください。
? """)


                # テンプレート・ファイルを先に読込
                with open(TEMPLATE_TXT_FILE_PATH, 'r', encoding='utf8') as f:
                        # NOTE テキストファイルの末尾に改行が入っていると、表示時に改行されます。改行されたくない場合は、ファイルの末尾に改行を入れないようにしてください
                        template = f.read()


                # データ・ファイルを読み込んで、データ・フレームにして返す
                df = pd.read_csv(DATA_CSV_FILE_PATH, encoding="utf8")


                # データを１行ずつ見ていく
                for              person,        place in\
                        zip(df['person'], df['place']):

                        filled_text = template.replace('{{person}}', person).replace('{{place}}', place)
                        print(filled_text)


                print("おわり。")


        except Exception as err:
                print(f"""\
おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
