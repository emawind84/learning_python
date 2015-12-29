#!/usr/bin/env python

import curses

screen = curses.initscr()
screen.keypad(True)
curses.cbreak()
curses.noecho()

game_over = False

while not game_over:
    key = screen.getch()
    print key
