import requests
from bs4 import BeautifulSoup
import sys_send

wiki_url = "http://wiki.sa-mp.com/wiki/";
function_name = "";
function_description = "";
function_parameters = "";

def GetFunction( function_name ) :
    
    r = requests.get( wiki_url + function_name );
    s = r.content;
    soup = BeautifulSoup( s , "html.parser" );
    
    try:
        description = soup.find_all( "div" , { "class" : "description" } );
        sys_send.print_yellow( "\nDescription\n" );
        sys_send.print_magenta( "\t" + description[0].text );

        try:
            params = soup.find_all( "div" , { "class" : "parameters" } );
            sys_send.print_yellow( "\nParameters\n" );
            sys_send.print_cyan( "\t" + params[0].text );

        except IndexError:
            sys_send.error( "Invalid Function specified" );

        try:
            example_code = soup.find_all( "pre" , { "class" : "pawn" } );
            sys_send.print_yellow( "Example code\n" );
            sys_send.code( example_code[0].text );
            

        except IndexError:
            sys_send.warning( "There is no example code available for this function" );    

    except IndexError:
        sys_send.error( "No results found check your function name (case sensitive)" );