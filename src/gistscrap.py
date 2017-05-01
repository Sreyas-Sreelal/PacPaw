import requests
from bs4 import BeautifulSoup
import sys_send

gist_url = "https://gist.github.com";

def GetSnippet( snippet_name ):
    sys_send.print_white("Doing an explicit search.....")
    sys_send.print_white("Searching for snippets.....\n");
    
    try:
        req = requests.get( gist_url  + "/search?&q=" + snippet_name + "+language%3Apawn" );
    
    except:
            sys_send.error("Please check your internet connection")
            exit(0);
    soup = BeautifulSoup( req.content , "html.parser" );
    data = soup.find_all( "a" , { "class" : "link-overlay" } );
    
    for link in data:
        
        try:
            req2 = requests.get( link[ 'href' ] + "/raw" );
            soup2 = BeautifulSoup( req2.content , "html.parser" );
        
        except:
                sys_send.error("Please check your internet connection");
                exit(0);
            
        sys_send.print_yellow( "Snippet description\n" );
        sys_send.print_green( soup2.get_text() );
        sys_send.print_magenta( "Press n to proceed to next result or anyother key to stop further searching" );
        confirm = input();
        
        if confirm is not "n" and confirm is not "N":
            break;