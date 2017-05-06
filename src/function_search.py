# ~ src/function_search.py

"""

This module is responsible for scrapnig wiki of samp. This is just a helping module for scripters.

"""

import requests
from bs4 import BeautifulSoup
import sys_send

WIKI_URL = "http://wiki.sa-mp.com/wiki/";
FUNCTION_DESCRIPTION = "";
FUNCTION_PARAMETER = "";
EXAMPLE_CODE = "";
def GetFunction( FUNCTION_NAME ) :
    
    try:
        request_to_wiki = requests.get( WIKI_URL + FUNCTION_NAME );
        WIKI_CONTENT_HTML = BeautifulSoup( request_to_wiki.content , "html.parser" );
    
    except:
            sys_send.error("Please check your internet connection");
            exit(0);
    
    sys_send.print_white("Fetching results from wiki.......\n")
    
    try:
        
        FUNCTION_DESCRIPTION = WIKI_CONTENT_HTML.find_all( "div" , { "class" : "description" } );
        sys_send.print_yellow( "\nDescription\n" );
        sys_send.print_magenta( "\t" + FUNCTION_DESCRIPTION[0].text );

        try:
            FUNCTION_PARAMETER = WIKI_CONTENT_HTML.find_all( "div" , { "class" : "parameters" } );
            sys_send.print_yellow( "\nParameters\n" );
            sys_send.print_cyan( "\t" + FUNCTION_PARAMETER[0].text );

        except IndexError:
            sys_send.error( "Invalid Function specified no result found" );

        try:
            EXAMPLE_CODE = WIKI_CONTENT_HTML.find_all( "pre" , { "class" : "pawn" } );
            sys_send.print_yellow( "Example code\n" );
            sys_send.code( EXAMPLE_CODE[0].text );
            

        except IndexError:
            sys_send.warning( "There is no example code available for this function" );    

    except IndexError:
        sys_send.error( "No results found check your function name (case sensitive)" );






        