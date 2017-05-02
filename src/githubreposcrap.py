import requests
from bs4 import BeautifulSoup
import sys_send
import network_handle

github_url = "https://www.github.com" ;
script_name = "";
downloaded_script = False;
download_url = "";


def GetRepo( script_name , listversion = False):
    sys_send.print_white("Searching for packages in github......\n")
    
    try:
        req = requests.get( github_url  + "/search?&q=" + script_name + "+topic%3Asa-mp&type=Repositories" );
    
    except:
            sys_send.error("Please check your internet connection");
            exit(0);
    
    soup = BeautifulSoup( req.content , "html.parser" );
    data = soup.find_all( "a" , { "class" : "v-align-middle" } );
    downloaded_script = False;  
	
    for link in data:

        if downloaded_script == True:
            break;
	     
        try:
            req2 = requests.get( github_url + link[ 'href' ] );
            soup2 = BeautifulSoup( req2.content , "html.parser" );
        
        except:
            sys_send.error( "Please check your internet connection" );
            exit(0);
        
        read_me = soup2.find( "article" , { "class" : "markdown-body entry-content" } );

        sys_send.print_magenta( " Description of the script \n" );
        sys_send.print_blue( read_me.text[ 0 : 2000 ] + "...." );
         
        sys_send.print_magenta( "Press y to confirm the download or anyother key to proceed to next result" );
        confirm = input();
                 
        if confirm is not "y" and confirm is not "Y":
            continue;
        sys_send.print_white( "Searching for binaries " + script_name + "....." );   
        
        try :
            req2 = requests.get( github_url + link[ 'href' ] + "/releases" );

        except:
            sys_send.error("Please check your internet connection");
            exit(0);
        
        soup2 = BeautifulSoup( req2.content , "html.parser" );
        
        if listversion:
            
            data2 = soup2.find_all( "ul" , { "class" : "release-downloads" } );
            
            if data2 is None:
                sys_send.error( "Failed to find binary release for this pacakage contact the developer" );
                exit(0);       
           
            sys_send.print_white("Versions available for this pacakge : \n")
            i = 1;
            
            for versions in data2:
                
                a = versions.find( 'a' , href = True );
                print( "%d.)" % ( i ) + script_name + a[ 'href' ].split( '/' )[ -1 ]  );
                i = i + 1;
                
            sys_send.print_white("Select your version : ")
            version_code = int(input())
            
            a = data2[version_code -1 ].find( 'a' , href = True );
            download_url = a['href'];
        
        else:
            
            data2 = soup2.find( "ul" , { "class" : "release-downloads" } );
            a = data2.find( 'a' , href = True );
            download_url = a[ 'href' ];
            
            if data2 is None:
                sys_send.error( "Failed to find binary release for this pacakage contact the developer" );
                exit(0)       
               
        script_name = script_name + " " + download_url.split( '/')[ -1 ];        
        
        if network_handle.download_file( github_url + download_url ,script_name ) is not None:
            sys_send.sucess(  "Successfully downloaded " + script_name );
            downloaded_script = True;
            break;

    if downloaded_script == False:
        sys_send.error( "Failed to find package specified....." );
