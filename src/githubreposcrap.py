import requests
from bs4 import BeautifulSoup
import sys_send
import network_handle

github_url = "https://www.github.com" ;
script_name = "";
downloaded_script = False;

def GetRepo( script_name ):
    
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
                 
        if network_handle.download_file( github_url + a [ 'href' ] ) is not None:
            sys_send.sucess(  "Successfully downloaded " + script_name );
            downloaded_script = True;
            break;

    if downloaded_script == False:
        sys_send.error( "Sorry  can't find more results " );