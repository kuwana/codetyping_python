import curses

def main(stdscr):
    # カーソルを表示にする
    curses.curs_set(1)
    # キー入力を非ブロッキングモードに設定
    stdscr.nodelay(True)

    # メインループ
    while True:
        # キー入力を取得
        key = stdscr.getch()
        # キーが押されたら、そのキーを表示
        if key != -1:
            stdscr.addch(key)
            # 画面を更新
            stdscr.refresh()

if __name__ == "__main__":
    # cursesモードを初期化
    curses.wrapper(main)

