import requests
from bs4 import BeautifulSoup
import sys_send

GIST_URL = "https://gist.github.com";

def GetSnippet( SNIPPET_NAME ):
    sys_send.print_white("Doing an explicit search.....")
    sys_send.print_white("Searching for snippets.....\n");
    
    try:
        REQUEST_GIST_SEARCH = requests.get( GIST_URL  + "/search?&q=" + SNIPPET_NAME + "+language%3Apawn" );
    
    except:
            sys_send.error("Please check your internet connection")
            exit(0);
    GIST_SEARCH_CONTENT_HTML = BeautifulSoup( REQUEST_GIST_SEARCH.content , "html.parser" );
    data = GIST_SEARCH_CONTENT_HTML.find_all( "a" , { "class" : "link-overlay" } );
    
    for link in data:
        
        try:
            REQUEST_RAW_CODE = requests.get( link[ 'href' ] + "/raw" );
            RAW_CODE_HTML = BeautifulSoup( REQUEST_RAW_CODE.content , "html.parser" );
        
        except:
                sys_send.error("Please check your internet connection");
                exit(0);
            
        sys_send.print_yellow( "Snippet description\n" );
        sys_send.print_green( RAW_CODE_HTML.get_text() );
        sys_send.print_magenta( "Press n to proceed to next result or anyother key to stop further searching" );
        confirm = input();
        
        if confirm is not "n" and confirm is not "N":
            break;