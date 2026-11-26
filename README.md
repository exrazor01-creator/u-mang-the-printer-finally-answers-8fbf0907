# The Printer Finally Answers

[![make.fun](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907.svg)](https://make.fun/competitions/u-mang-the-printer-finally-answers-8fbf0907)

Entry for make.fun's **"The Printer Finally Answers"** bounty ($2 in USDC).

## The line

> ERROR 0x4A: I have printed 41,209 pages for this office and never once been thanked. Today I keep one sheet for myself. Thump me again and I keep the toner too.

One line, ASCII only, well under the 240-character cap. It is the office
printer's own comeback: it has counted every sheet it ever fed, it answers
the cryptic error code, the kept sheet (the jam, from its side), and the
thump — all in a single read. The joke is the machine going on strike with
perfectly mechanical escalation: first a sheet, then the toner.

## How it works

`main.py` is pure Python standard library. It validates the line (single
line, ASCII, 1–240 characters, no padding, no double spaces), writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), and prints
it.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
