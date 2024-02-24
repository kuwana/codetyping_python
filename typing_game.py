import curses
import time

def main(stdscr):
    # Cursesの初期化
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    stdscr.keypad(True)
    curses.noecho()

    # 問題の読み込み
    with open("questions/sample.txt", "r") as file:
        content = file.read().splitlines()

    # ゲーム開始時間
    start_time = time.time()
    # ゲーム終了時間
    end_time = 0
    # ミスタイプ数
    mistakes = 0

    # カーソルの位置
    cursor_x = 0
    cursor_y = 0

    # メインループ
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # 問題を描画
        for i, line in enumerate(content):
            stdscr.addstr(i, 0, line)

        # カーソルを描画
        stdscr.move(cursor_y, cursor_x)

        # 入力を取得
        c = stdscr.getch()
        stdscr.addstr(height - 2, 0, "Key pressed: {}".format(c))

        # ウィンドウの高さと幅を取得
        height, width = stdscr.getmaxyx()

        # カーソルの移動
        if c == curses.KEY_RIGHT:
            cursor_x = min(cursor_x + 1, len(content[cursor_y]))
        elif c == curses.KEY_LEFT:
            cursor_x = max(cursor_x - 1, 0)
        elif c == curses.KEY_DOWN:
            cursor_y = min(cursor_y + 1, len(content) - 1)
            cursor_x = min(cursor_x, len(content[cursor_y]))
        elif c == curses.KEY_UP:
            cursor_y = max(cursor_y - 1, 0)
            cursor_x = min(cursor_x, len(content[cursor_y]))

        # 全ての文字をタイプし終えたかどうかを確認
        if cursor_y == len(content) - 1 and cursor_x == len(content[-1]):
            end_time = time.time()
            break

    # 結果を表示
    stdscr.clear()
    stdscr.addstr(0, 0, "Total Characters: {}".format(sum(len(line) for line in content)))
    stdscr.addstr(1, 0, "Mistakes: {}".format(mistakes))
    stdscr.addstr(2, 0, "Total Time: {:.2f} seconds".format(end_time - start_time))
    stdscr.addstr(3, 0, "Average Typing Speed: {:.2f} characters per second".format(sum(len(line) for line in content) / (end_time - start_time)))

    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)

