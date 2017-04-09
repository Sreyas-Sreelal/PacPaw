import requests
from bs4 import BeautifulSoup
from colorama import init
init( );
from colorama import Fore, Back, Style

check = True;
wikiurl = "http://wiki.sa-mp.com/wiki/";
function_name = "";
function_description = "";
function_parameters = "";
NeedMore = "";
print( Style.NORMAL );
print( "\n\n\t\t\t\t" + Fore.WHITE + "SAMP HELPER" + Fore.MAGENTA + " PYTHON TOOL " + Fore.GREEN + "BY" + Fore.RED + " SREYAS" );

while check == True:
    print( Style.BRIGHT );
    print( Fore.WHITE + "\nInput function name to search in wiki" );
    function_name  = input( );
    r = requests.get( wikiurl + function_name );
    s = r.content;
    soup = BeautifulSoup( s , "html.parser" );

    try:
        description = soup.find_all( "div" , { "class" : "description" } );
        print( Fore.YELLOW + "\nDescription\n" );
        print( Fore.MAGENTA + "\t" + description[0].text );

        try:
            params = soup.find_all( "div" , { "class" : "parameters" } );
            print( Fore.YELLOW + "\nParameters\n" );
            print( Fore.CYAN + "\t" + params[0].text );

        except IndexError:
            print( "\nInvalid Function specified" );

        try:
            example_code = soup.find_all( "pre" , { "class" : "pawn" } );
            print( Fore.YELLOW + "\nExample code\n" );
            print( Back.BLACK + Fore.GREEN + example_code[0].text );
            print( Back.RESET );

        except IndexError:
            print( Fore.RED + "There is no example code available for this function" );    

    except IndexError:
        print( Fore.RED + "No results found check your function name (case sensitive)" );
    
    print( Fore.WHITE + "\n\n\nDo you want to search more?(Y/N)" );
    NeedMore = input( );

    if NeedMore == "n" or NeedMore == "N":
        check = False;
