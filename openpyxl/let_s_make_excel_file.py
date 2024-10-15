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
from openpyxl.styles.borders import Border, Side


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

        ws = wb['Hello'] # Worksheet
        ws['A1'].value = 'World'
        wb.save(FILE_NAME)

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

        ws['A2'].fill = PatternFill(patternType='solid', fgColor='CCFFFF')
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

        ws['A3'].value = 'Apple'
        ws['A3'].font = Font(color='FF0000')
        wb.save(FILE_NAME)

        print(f"Hello シートの A3 セルに Applet という文字を入力して赤色にし、 {FILE_NAME} ファイルを保存しました")
        time.sleep(MSG_SECS)

        print(f"{FILE_NAME} ファイルを開けて確認してみてください。")
        time.sleep(MSG_SECS)

        print(f"Hello シートの A3 セルに赤色の Applet という文字が入っていますか？")
        time.sleep(MSG_SECS)


        ############
        # MARK: 罫線
        ############

        print()
        time.sleep(MSG_SECS)

        print("次は、 B4 セルに罫線（けいせん）を引いてみましょう")
        time.sleep(MSG_SECS)

        print(f"それでは、{FILE_NAME} ファイルを閉じ、")
        time.sleep(MSG_SECS)

        enter_key = input("エンター・キーを打鍵してみてください")

        side = Side(style='thin', color='000000')
        # style に入るもの： 'thin', 'dashDot', 'dashDotDot', 'double', 'hair', 'dotted', 'mediumDashDotDot', 'dashed', 'mediumDashed', 'slantDashDot', 'thick', 'thin', 'medium', 'mediumDashDot'
        border = Border(top=side, bottom=side, left=side, right=side)
        ws['B4'].border = border
        wb.save(FILE_NAME)

        print(f"B4 セルに罫線（けいせん）を引き、 {FILE_NAME} ファイルを保存しました")
        time.sleep(MSG_SECS)

        print(f"{FILE_NAME} ファイルを開けて確認してみてください。")
        time.sleep(MSG_SECS)

        print(f"Hello シートの B4 セルに罫線（けいせん）が引かれていますか？")
        time.sleep(MSG_SECS)


        ########################
        # MARK: 列の幅、行の高さ
        ########################

        print()
        time.sleep(MSG_SECS)

        print("次は、 A, B, C 列の幅を 10, 20, 30に、 1, 2, 3 行目の行の高さを 10, 20, 30 に設定してみましょう")
        time.sleep(MSG_SECS)

        print(f"それでは、{FILE_NAME} ファイルを閉じ、")
        time.sleep(MSG_SECS)

        enter_key = input("エンター・キーを打鍵してみてください")

        # width はだいたい 'ＭＳ Ｐゴシック' サイズ11 の半角英文字の個数
        ws.column_dimensions['A'].width = 10
        ws.column_dimensions['B'].width = 20
        ws.column_dimensions['C'].width = 30

        # height の単位はポイント。昔のアメリカ人が椅子に座ってディスプレイを見たとき 1/72 インチに見える大きさが 1ポイント らしいが、そんなんワカラン。目視確認してほしい
        ws.row_dimensions[1].height = 10
        ws.row_dimensions[2].height = 20
        ws.row_dimensions[3].height = 30
        wb.save(FILE_NAME)

        print(f"A, B, C 列の幅を 10, 20, 30に、 1, 2, 3 行目の行の高さを 10, 20, 30 に設定し、 {FILE_NAME} ファイルを保存しました")
        time.sleep(MSG_SECS)

        print(f"{FILE_NAME} ファイルを開けて確認してみてください。")
        time.sleep(MSG_SECS)

        print(f"A, B, C 列の幅を 10, 20, 30に、 1, 2, 3 行目の行の高さを 10, 20, 30 になっていますか？")
        time.sleep(MSG_SECS)


        print("おわり。")


    except Exception as err:
        print(f"""\
おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
