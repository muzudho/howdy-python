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
from openpyxl.styles import PatternFill, Font


FILE_NAME = 'hello.xlsx'
MSG_SECS = 0.1     # メッセージ送りの長さ（秒）


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    try:
        ########################
        # MARK: ワークブック作成
        ########################

        print()             # 空行
        time.sleep(MSG_SECS)     # メッセージが少しずつ進むようにウェイトを入れます
        
        print("空のシートを１つ持つエクセルファイルを新規作成しましょう。")
        time.sleep(MSG_SECS)

        print("ファイル名は hello.xlsx とします。")
        time.sleep(MSG_SECS)

        print("ファイルが既存の場合は上書きします")
        time.sleep(MSG_SECS)

        enter_key = input(f"""\
それでは、エンター・キーを打鍵してみてください
> """)

        wb = xl.Workbook()
        wb.save(FILE_NAME)  # 既存のファイルがあれば上書きになる

        print(f"{FILE_NAME} ファイルを作成しました")
        time.sleep(MSG_SECS)

        print(f"{FILE_NAME} ファイルを開けてみてください。")
        time.sleep(MSG_SECS)

        print(f"デフォルトで Sheet という名前のシートがありますか？")
        time.sleep(MSG_SECS)


        ####################
        # MARK: シート名変更
        ####################

        print()
        time.sleep(MSG_SECS)

        print("この Sheet シートの名前を Hello に変えましょう")
        time.sleep(MSG_SECS)

        print(f"それでは、{FILE_NAME} ファイルを閉じ、")
        time.sleep(MSG_SECS)

        enter_key = input("エンター・キーを打鍵してみてください")

        wb['Sheet'].title = 'Hello'
        wb.save(FILE_NAME)

        print(f"Sheet シートの名前を Hellow に変えて {FILE_NAME} ファイルを保存しました")
        time.sleep(MSG_SECS)

        print(f"{FILE_NAME} ファイルを開けてみてください。")
        time.sleep(MSG_SECS)

        print("Hello という名前のシートがありますか？")
        time.sleep(MSG_SECS)


        ################
        # MARK: 文字入力
        ################

        print()
        time.sleep(MSG_SECS)

        print("この Sheet シートの A1 セルに World と文字を入れてみましょう")
        time.sleep(MSG_SECS)

        print(f"それでは、{FILE_NAME} ファイルを閉じ、")
        time.sleep(MSG_SECS)

        enter_key = input("エンター・キーを打鍵してみてください")

        sheet = wb['Hello']
        sheet['A1'].value = 'World'
        wb.save(FILE_NAME)

        print()
        time.sleep(MSG_SECS)

        print(f"Hello シートの A1 セルに World と入力して {FILE_NAME} ファイルを保存しました")
        time.sleep(MSG_SECS)

        print(f"{FILE_NAME} ファイルを開けて確認してみてください。")
        time.sleep(MSG_SECS)

        print(f"Hello シートの A1 セルに World と入力されていますか？")
        time.sleep(MSG_SECS)


        ##############
        # MARK: 背景色
        ##############

        print()
        time.sleep(MSG_SECS)

        print("次は、 A2 セルの背景に色を付けてみましょう")
        time.sleep(MSG_SECS)

        print(f"それでは、{FILE_NAME} ファイルを閉じ、")
        time.sleep(MSG_SECS)

        enter_key = input("エンター・キーを打鍵してみてください")

        sheet['A2'].fill = PatternFill(patternType='solid', fgColor='CCFFFF')
        wb.save(FILE_NAME)

        print(f"Hello シートの A2 セルの背景に色を付けて {FILE_NAME} ファイルを保存しました")
        time.sleep(MSG_SECS)

        print(f"{FILE_NAME} ファイルを開けて確認してみてください。")
        time.sleep(MSG_SECS)

        print(f"Hello シートの A2 セルの背景に色が付いていますか？")
        time.sleep(MSG_SECS)


        ##################
        # MARK: フォント色
        ##################

        print()
        time.sleep(MSG_SECS)

        print("次は、 A3 セルに Apple という文字を入力して赤色にしてみましょう")
        time.sleep(MSG_SECS)

        print(f"それでは、{FILE_NAME} ファイルを閉じ、")
        time.sleep(MSG_SECS)

        enter_key = input("エンター・キーを打鍵してみてください")

        sheet['A3'].value = 'Apple'
        sheet['A3'].font = Font(color='FF0000')
        wb.save(FILE_NAME)

        print(f"Hello シートの A3 セルに Applet という文字を入力して赤色にし、 {FILE_NAME} ファイルを保存しました")
        time.sleep(MSG_SECS)

        print(f"{FILE_NAME} ファイルを開けて確認してみてください。")
        time.sleep(MSG_SECS)

        print(f"Hello シートの A2 セルの背景に色が付いていますか？")
        time.sleep(MSG_SECS)


        print("おわり。")


    except Exception as err:
        print(f"""\
おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
