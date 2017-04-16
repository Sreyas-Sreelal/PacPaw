import requests
from bs4 import BeautifulSoup
from colorama import init
init( );
from colorama import Fore, Back, Style

check = True;
wikiurl = "http://wiki.sa-mp.com/wiki/";
github_url="https://www.github.com";
function_name = "";
function_description = "";
function_parameters = "";
NeedMore = "";
plugin_name = "";
downloaded_plugin = False;
option = "";

def download_file( url ):
    filename = url.split( '/' )[ -1 ]
    
    r = requests.get( url , stream = True )
    with open( filename , 'wb' ) as f:
        for buffer in r.iter_content( chunk_size = 1024 ): 
            if buffer: 
                f.write( buffer )
                
    return filename

def GetScript( ):
	print( Fore.WHITE + "Input script name to download " );
	plugin_name = input( );
	confirm = "";
	req = requests.get( github_url  + "/search?&q=" + plugin_name + "+topic%3Asa-mp&type=Repositories" );
	soup = BeautifulSoup( req.content , "html.parser" );
	data = soup.find_all( "a" , { "class" : "v-align-middle" } );
	downloaded_plugin = False;  
	for link in data:
	     
	     if downloaded_plugin == True:
	          break;
	     req2 = requests.get( github_url + link[ 'href' ] );
	     soup2 = BeautifulSoup( req2.content , "html.parser" );
	     read_me = soup2.find( "article" , { "class" : "markdown-body entry-content" } );
	     print( Style.BRIGHT );
	     print( Fore.MAGENTA + " Description of the script \n" );
	     print( Fore.BLUE + read_me.text[ 0 : 1500 ] + "...." );
	     print( Style.NORMAL );
	     print( Fore.MAGENTA + "Press y to confirm the download or anyother key to proceed to next result");
	     confirm = input();
	     if confirm is not "y" or confirm is not "Y":
	     	continue;

	     req2 = requests.get( github_url + link[ 'href' ] + "/releases" );
	     soup2 = BeautifulSoup( req2.content , "html.parser" );
	     data2 = soup2.find( "ul" , { "class" : "release-downloads"} );
	     
	     a = data2.find( 'a' , href = True );
	     
	     if download_file( github_url + a [ 'href' ] ) is not None:
	         print( Fore.GREEN + "\nSuccessfully downloaded " + plugin_name );
	         downloaded_plugin = True;
	         break;
	
	if downloaded_plugin == False:
		print( Fore.RED + "Sorry your i can't find results " );
	     	

def GetFunction( ):
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



print( Style.NORMAL );
print( "\n\n\t\t\t\t" + Fore.WHITE + "SAMP HELPER" + Fore.MAGENTA + " PYTHON TOOL " + Fore.GREEN + "BY" + Fore.RED + " SREYAS" );

while check == True:
    print( Fore.WHITE+ "\t\tSelect your option\n\
    					1.Search for a function defintion\n\
    					2.Get a samp script\n\
    					3.Quit\n" );
    option = input( );
    if option == "1":
    	GetFunction();
    elif option == "2":
    	GetScript();
    else:
    	exit();    
    print( Fore.WHITE + "\n\n\nDo you want to do anything  more?(Y/N)" );
    NeedMore = input( );

    if NeedMore == "n" or NeedMore == "N":
        check = False;
