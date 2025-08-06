import time
import sys

# Warna ANSI
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

# Fungsi efek ketik per huruf
def ketik(teks, warna=RESET, delay_huruf=0.06):
    for huruf in teks:
        sys.stdout.write(warna + huruf + RESET)
        sys.stdout.flush()
        time.sleep(delay_huruf)
    print()

# Lirik dramatis versi kamu
lirik = [
    (RED, " ♪ You can fight it, you can't breathe ♪", 1.0),
    (RED, " ♪ You say something so loving, but... ♪", 1.2),
    (YELLOW, " ♪ Now I gotta let you go... ♪", 1.3),

    (MAGENTA, " ♪ You'll be better off in someone new... ♪", 1.5),
    (CYAN, " ♪ I don't wanna be alone... ♪", 1.0),
    (CYAN, " ♪ You know it hurts me too... ♪", 1.2),

    (GREEN, " ♪ You look so broken when you cry... ♪", 1.3),
    (GREEN, " ♪ One more and then I'll say goodbye... ♪", 1.5),

    (RED, " ", 0.5),
    (RED, " ♪ Sometimes, all I think about is... ♪", 1.8),
    (MAGENTA, " ♪ YOU ♪", 2.0),
]

# Menjalankan lirik
for warna, baris, delay_baris in lirik:
    ketik(baris, warna)
    time.sleep(delay_baris)