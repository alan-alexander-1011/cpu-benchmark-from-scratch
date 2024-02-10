"""
just dont modify the original code, pls, just play fair.

LICENSE For software code and distribution and advertising materials:
 
MIT/GU-NNoA-LF License

Copyright (c) 2023 alan-alexander-1011
(Copyright was added by the owner too :) not too much force but pls give creds 
when showing this to the public or distribute it)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

(i added in this part :)) )

After the MIT License, the name of the owner("alan-alexander-1011") *Shall Not* be used to
make money or in advertisement or to make any deals that is related to this software because
the software is *100%* free.

The program IS NOT for sale, but for normal and commercial uses.

The Distributor of this software is not needed to show the code of the program to the public. 
But the Distributor of this software may needed to give an simple explanation of what the 
Distributor added/modified to the program.
And the distributor may give the owner credits.

-----------------------------------------
Notes after the terms: LF means less force:)
-----------------------------------------


----------------------------------------------------------------
"""
import sys
try:
    import msvcrt
except ImportError:
    pass
try:
    import colorama
except ImportError:
    supports_colorama = False
else: supports_colorama = True
import curses,typing

def arrow_key_menu(options, start_message:str = ""):
    """
    Displays a menu with the given options and allows the user to navigate using arrow keys.\n
    Returns the index of the selected option.
    """
    selected_option = 0

    if sys.platform.startswith('win'):
        while True:
            # Clear the console screen
            sys.stdout.write("\033[H\033[J")
            sys.stdout.write(start_message+"\n")
            # Print the menu options
            for i, option in enumerate(options):
                if i == selected_option:
                    sys.stdout.write("-> "); sys.stdout.write(colorama.Fore.GREEN + option + colorama.Fore.RESET + "\n") if supports_colorama else sys.stdout.write(option + "\n")
                else:
                    sys.stdout.write("   "); sys.stdout.write(option + "\n")

            # Wait for user input
            key = msvcrt.getch()

            # Handle arrow key input
            if key == b'\xe0':
                key = msvcrt.getch()
                if key == b'H' and selected_option > 0:
                    # Up arrow key
                    selected_option -= 1
                elif key == b'P' and selected_option < len(options) - 1:
                    # Down arrow key
                    selected_option += 1
            elif key == b'\r':
                # Enter key
                return selected_option
    else:
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        try:
            while True:
                stdscr.clear()
                stdscr.addstr(start_message+"\n")
                # Print the menu options
                for i, option in enumerate(options):
                    if i == selected_option:
                        stdscr.addstr("-> " + option + "\n", curses.A_REVERSE)
                    else:
                        stdscr.addstr("   " + option + "\n")

                # Get user input
                key = stdscr.getch()

                # Handle arrow key input
                if key == curses.KEY_UP and selected_option > 0:
                    selected_option -= 1
                elif key == curses.KEY_DOWN and selected_option < len(options) - 1:
                    selected_option += 1
                elif key == ord('\n'):
                    # Enter key
                    return selected_option
        finally:
            # Clean up curses
            curses.nocbreak()
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()

def custom_int_counter(min:int = 1, max:int=10, start_message:str = "") -> int:
    number = min
    if sys.platform.startswith('win'):
        while True:
                # Clear the console screen
                sys.stdout.write("\033[H\033[J")
                sys.stdout.write(start_message+"\n")
                sys.stdout.write(str(number) + "\n(Press enter to choose)")
                
                # Wait for user input
                key = msvcrt.getch()

                # Handle arrow key input
                if key == b'\xe0':
                    key = msvcrt.getch()
                    if (key == b'H' and number < max) or (key == b'H' and max == -1):
                        # Up arrow key
                        number += 1
                    elif key == b'P' and number > min:
                        # Down arrow key
                        number -= 1
                elif key == b'\r':
                    # Enter key
                    return number
    else:
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        try:
            while True:
                stdscr.clear()
                stdscr.addstr(start_message + "\n")
                stdscr.addstr(str(number) + "\n(Press enter to choose)")

                # Get user input
                key = stdscr.getch()

                # Handle arrow key input
                if key == curses.KEY_UP and (number < max or max == -1):
                    number += 1
                elif key == curses.KEY_DOWN and number > min:
                    number -= 1
                elif key == ord('\n'):
                    # Enter key
                    return number
        finally:
            # Clean up curses
            curses.nocbreak()
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()
