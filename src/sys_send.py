

from colorama import init
init( autoreset = True );
from colorama import Fore, Back, Style


def print_title( ):
	print( "\n\n\t\t\t\t" + Fore.YELLOW + "SAMP HELPER" + Fore.MAGENTA + " PYTHON TOOL " + Fore.GREEN + "BY" + Fore.RED + " SREYAS" );

def print_blue( str ):
	print( Style.BRIGHT + Fore.BLUE + str );

def print_magenta( str ):
	print( Style.BRIGHT + Fore.MAGENTA + str );

def print_red( str ):
	print( Style.BRIGHT + Fore.RED + str );  

def print_white( str ):
	print( Style.BRIGHT + Fore.WHITE + str );

def print_green( str ):
	print( Style.BRIGHT + Fore.GREEN + str );

def print_yellow( str ):
	print(  Style.BRIGHT + Fore.YELLOW + str  );

def print_cyan( str ):
	print(  Style.BRIGHT + Fore.CYAN + str  );

def sucess( str ):
	print( Style.BRIGHT + Fore.YELLOW + "\n[***]" + Fore.GREEN + str );

def warning( str ):
	print( Style.BRIGHT + Fore.RED + "[WARNING!]" + Style.NORMAL + str );

def error ( str ):
	print( Style.BRIGHT + Fore.RED + "[Error]" + str );

def ask( str ):
	print( Style.BRIGHT + Fore.WHITE + "Input " + str );

def prompt( str ):
	print( Style.BRIGHT + Fore.WHITE + "Press " + str );

def code( str ):
	print( Style.BRIGHT + Back.BLACK + Fore.GREEN + str );

class term_style:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_bold( str , color = Fore.WHITE ):
	print( term_style.BOLD + str );

def print_underlined( str , color = Fore.WHITE ):
	print( term_style.UNDERLINE + str );


