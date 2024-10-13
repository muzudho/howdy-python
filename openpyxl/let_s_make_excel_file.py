#
# cd openpyxl
# python let_s_make_excel_file.py
#
# （pandas）エクセルファイルを作ろう
#
import traceback
import time
import datetime
import openpyxl as xl


FILE_NAME = 'hello.xlsx'


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    try:
        print()             # 空行
        time.sleep(0.2)     # メッセージが少しずつ進むようにウェイトを入れます
        
        print("空のシートを１つ持つエクセルファイルを新規作成しましょう。")
        time.sleep(0.2)

        print("ファイル名は hello.xlsx とします。")
        time.sleep(0.2)

        print("ファイルが既存の場合は上書きします")
        time.sleep(0.2)

        enter_key = input(f"""\
それでは、エンター・キーを打鍵してみてください
> """)

        wb = xl.Workbook()
        wb.save(FILE_NAME)  # 既存のファイルがあれば上書きになる

        print()
        time.sleep(0.2)

        print(f"{FILE_NAME} ファイルを作成しました")
        time.sleep(0.2)

        print(f"{FILE_NAME} ファイルを開けてみてください。")
        time.sleep(0.2)

        print(f"デフォルトで Sheet という名前のシートがあります。")
        time.sleep(0.2)

        print("この Sheet シートの名前を Hello に変えましょう")
        time.sleep(0.2)

        print(f"それでは、{FILE_NAME} ファイルを閉じ、")
        time.sleep(0.2)

        enter_key = input("エンター・キーを打鍵してみてください")

        wb['Sheet'].title = 'Hello'
        wb.save(FILE_NAME)

        print()
        time.sleep(0.2)

        print(f"Sheet シートの名前を Hellow に変えて {FILE_NAME} ファイルを保存しました")
        time.sleep(0.2)

        print(f"{FILE_NAME} ファイルを開けてみてください。")
        time.sleep(0.2)

        print("Hello という名前のシートがあります。")
        time.sleep(0.2)

        print("この Sheet シートの A1 セルに World と文字を入れてみましょう")
        time.sleep(0.2)

        print(f"それでは、{FILE_NAME} ファイルを閉じ、")
        time.sleep(0.2)

        enter_key = input("エンター・キーを打鍵してみてください")

        sheet = wb['Hello']
        sheet['A1'].value = 'World'
        wb.save(FILE_NAME)

        print()
        time.sleep(0.2)

        print(f"Hello シートの A1 セルに World と入力して {FILE_NAME} ファイルを保存しました")
        time.sleep(0.2)

        print(f"{FILE_NAME} ファイルを開けて確認してみてください。")
        time.sleep(0.2)

        print("おわり。")


    except Exception as err:
        print(f"""\
おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
