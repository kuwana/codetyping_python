import curses

def main(stdscr):
    # カーソルを非表示にする
    curses.curs_set(0)
    # ウィンドウにテキストを表示
    stdscr.addstr(0, 0, "Hello, world!")
    # 画面を更新
    stdscr.refresh()
    # キー入力を待機
    stdscr.getch()
    # 新しい行にテキストを追加
    stdscr.addstr(1, 0, "This is a new line!")
    # 画面を更新
    stdscr.refresh()
    # キー入力を待機
    stdscr.getch()

if __name__ == "__main__":
    # cursesモードを初期化
    curses.wrapper(main)

