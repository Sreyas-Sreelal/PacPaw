import requests
from bs4 import BeautifulSoup
import sys_send
import network_handle

GITHUB_URL = "https://www.github.com" ;
DOWNLOADED_PACKAGE = False;
PACKAGE_DOWNLOAD_URL = "";


def GetRepo( PACKAGE_NAME , LIST_VERSIONS_AVAILABLE = False):
    
    sys_send.print_white("Searching for packages in github......\n")
    
    try:
        REQUEST_GITHUB_SEARCH = requests.get( GITHUB_URL  + "/search?&q=" + PACKAGE_NAME + "+topic%3Asa-mp&type=Repositories" );
    
    except:
            sys_send.error("Please check your internet connection");
            exit(0);
    
    GITHUB_SEARCH_CONTENT_HTML = BeautifulSoup( REQUEST_GITHUB_SEARCH.content , "html.parser" );
    SCRAPED_RESULTS = GITHUB_SEARCH_CONTENT_HTML.find_all( "a" , { "class" : "v-align-middle" } );
    DOWNLOADED_PACKAGE = False;  
	
    for link in SCRAPED_RESULTS:

        if DOWNLOADED_PACKAGE == True:
            break;
	     
        try:
            REQUEST_GITHUB_REPOSITORY = requests.get( GITHUB_URL + link[ 'href' ] );
            GITHUB_REPOSITORY_CONTENT_HTML = BeautifulSoup( REQUEST_GITHUB_REPOSITORY.content , "html.parser" );
        
        except:
            sys_send.error( "Please check your internet connection" );
            exit(0);
        
        read_me = GITHUB_REPOSITORY_CONTENT_HTML.find( "article" , { "class" : "markdown-body entry-content" } );

        sys_send.print_magenta( " Description of the script \n" );
        sys_send.print_blue( read_me.text[ 0 : 2000 ] + "...." );
         
        sys_send.print_magenta( "Press y to confirm the download or anyother key to proceed to next result" );
        confirm = input();
                 
        if confirm is not "y" and confirm is not "Y":
            continue;
        sys_send.print_white( "Searching for binaries " + PACKAGE_NAME + "....." );   
        
        try :
            REQUEST_GITHUB_REPOSITORY_RELEASES = requests.get( GITHUB_URL + link[ 'href' ] + "/releases" );

        except:
            sys_send.error("Please check your internet connection");
            exit(0);
        
        GITHUB_REPOSITORY_RELEASE_CONTENT_HTML = BeautifulSoup( REQUEST_GITHUB_REPOSITORY_RELEASES.content , "html.parser" );
        
        if LIST_VERSIONS_AVAILABLE:
            
            PACAKAGE_RELEASES = GITHUB_REPOSITORY_RELEASE_CONTENT_HTML.find_all( "ul" , { "class" : "release-downloads" } );
            
            if PACAKAGE_RELEASES is None:
                sys_send.error( "Failed to find binary release for this pacakage contact the developer" );
                exit(0);       
           
            sys_send.print_white("Versions available for this pacakge : \n")
            i = 1;
            
            for versions in PACAKAGE_RELEASES:
                
                link_to = versions.find( 'a' , href = True );
                print( "%d.)" % ( i ) + PACKAGE_NAME + link_to[ 'href' ].split( '/' )[ -1 ]  );
                i = i + 1;
                
            sys_send.print_white("Select your version : ")
            version_code = int(input())
            
            link_to = PACAKAGE_RELEASES[version_code -1 ].find( 'a' , href = True );
            PACKAGE_DOWNLOAD_URL = link_to['href'];
        
        else:
            
            PACAKAGE_RELEASES = GITHUB_REPOSITORY_CONTENT_HTML.find( "ul" , { "class" : "release-downloads" } );
            link_to = PACAKAGE_RELEASES.find( 'a' , href = True );
            PACKAGE_DOWNLOAD_URL = link_to[ 'href' ];
            
            if PACAKAGE_RELEASES is None:
                sys_send.error( "Failed to find binary release for this pacakage contact the developer" );
                exit(0)       
               
        PACKAGE_NAME = PACKAGE_NAME + " " + PACKAGE_DOWNLOAD_URL.split( '/')[ -1 ];        
        
        if network_handle.download_file( GITHUB_URL + PACKAGE_DOWNLOAD_URL ,PACKAGE_NAME ) is not None:
            sys_send.sucess(  "Successfully downloaded " + PACKAGE_NAME );
            DOWNLOADED_PACKAGE = True;
            break;

    if DOWNLOADED_PACKAGE == False:
        sys_send.error( "Failed to find package specified....." );
