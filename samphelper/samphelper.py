import requests
from bs4 import BeautifulSoup
import sys_send

check = True;
wiki_url = "http://wiki.sa-mp.com/wiki/";
github_url="https://www.github.com";
gist_url = "https://gist.github.com";
function_name = "";
function_description = "";
function_parameters = "";
NeedMore = "";
script_name = "";
downloaded_script = False;
option = "";


def GetSnippet( ):
    
    sys_send.ask( "name of the code snippet you want " );
    snippet_name = input();
    confirm = "";
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

        
def download_file( url ):
    
    filename = url.split( '/' )[ -1 ]
    r = requests.get( url , stream = True )
    with open( filename , 'wb' ) as f:
        for buffer in r.iter_content( chunk_size = 1024 ): 
            if buffer: 
                f.write( buffer )
                
    return filename

def GetScript( ):
    
    sys_send.ask( "script's name to download " );
    script_name = input( );
    confirm = "";
    req = requests.get( github_url  + "/search?&q=" + script_name + "+topic%3Asa-mp&type=Repositories" );
    soup = BeautifulSoup( req.content , "html.parser" );
    data = soup.find_all( "a" , { "class" : "v-align-middle" } );
    downloaded_script = False;  
	
    for link in data:

        if downloaded_script == True:
            break;
	     
        req2 = requests.get( github_url + link[ 'href' ] );
        soup2 = BeautifulSoup( req2.content , "html.parser" );
        read_me = soup2.find( "article" , { "class" : "markdown-body entry-content" } );

        sys_send.print_magenta( " Description of the script \n" );
        sys_send.print_blue( read_me.text[ 0 : 1500 ] + "...." );
         
        sys_send.print_magenta( "Press y to confirm the download or anyother key to proceed to next result" );
        confirm = input();
                 
        if confirm is not "y" and confirm is not "Y":
            continue;

        req2 = requests.get( github_url + link[ 'href' ] + "/releases" );
        soup2 = BeautifulSoup( req2.content , "html.parser" );
        data2 = soup2.find( "ul" , { "class" : "release-downloads"} );
                 
        a = data2.find( 'a' , href = True );
                 
        if download_file( github_url + a [ 'href' ] ) is not None:
            sys_send.sucess(  "Successfully downloaded " + script_name );
            downloaded_script = True;
            break;

    if downloaded_script == False:
        sys_send.error( "Sorry  can't find more results " );
	     	

def GetFunction( ):
    
    sys_send.ask( "function name to search in wiki" );
    function_name  = input( );
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

sys_send.print_title( );

while check == True:
    sys_send.print_white( "\t\tSelect your option\n\
    					       1.Search for a function defintion\n\
    					       2.Get a samp script\n\
                               3.Search for snippet\n\
    					       4.Quit\n" );
    option = input( );
    if option == "1":
    	GetFunction( );
    elif option == "2":
    	GetScript( );
    elif option == "3":
        GetSnippet( );
    else:
    	exit( );    
    sys_send.print_white( "\n\n\nDo you want to do anything  more?(Y/N)" );
    NeedMore = input( );

    if NeedMore == "n" or NeedMore == "N":
        check = False;
