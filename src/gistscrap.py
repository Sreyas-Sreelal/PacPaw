import requests
from bs4 import BeautifulSoup
import sys_send

gist_url = "https://gist.github.com";

def GetSnippet( snippet_name ):
    
    req = requests.get( gist_url  + "/search?&q=" + snippet_name + "+language%3Apawn" );
    soup = BeautifulSoup( req.content , "html.parser" );
    data = soup.find_all( "a" , { "class" : "link-overlay" } );
    
    for link in data:
        
        req2 = requests.get( link[ 'href' ] + "/raw" );
        soup2 = BeautifulSoup( req2.content , "html.parser" );
        sys_send.print_yellow( "Snippet description\n" );
        sys_send.print_green( soup2.get_text() );
        sys_send.print_magenta( "Press N to proceed to next result" );
        confirm = input();
        
        if confirm is not "n" and confirm is not "N":
            break;