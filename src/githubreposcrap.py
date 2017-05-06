
# ~ src/githubreposcrap.py

"""
 This module is responsible for scraping the github and finding the packages using github's 
 powerful search function.There is also a version listing task for this module if lv flag 
 is enabled.

"""

import requests
from bs4 import BeautifulSoup
import sys_send
import network_handle

GITHUB_URL = "https://www.github.com" ; # Github main site
DOWNLOADED_PACKAGE = False;
PACKAGE_DOWNLOAD_URL = "";

"""

function GetRepo(PACKAGE_NAME , LIST_VERSIONS_AVAILABLE = False )

parameters:
    PACKAGE_NAME - name of the package to be searched
    LIST_VERSIONS_AVAILABLE - boolean for listing all available version. It's state depends on lv flag.

purpose and description:
    This function mainly relies on github's website structure.It first searches for results with 
    help of newly implemented feature of github called topics.The key using will be "sa-mp".It scrapes
    versions with help of tag feature in release section.User can also view a short description about 
    repository to confirm the right package for them. 

"""
def GetRepo( PACKAGE_NAME , LIST_VERSIONS_AVAILABLE = False):
    
    sys_send.print_white("Searching for packages in github......\n")
    
    try:
        # searching in github
        
        REQUEST_GITHUB_SEARCH = requests.get( GITHUB_URL  + "/search?&q=" + PACKAGE_NAME + "+topic%3Asa-mp&type=Repositories" );
    
    except:
            
            sys_send.error("Please check your internet connection");
            exit(0);
    
    # scraping fetched result for further analysis

    GITHUB_SEARCH_CONTENT_HTML = BeautifulSoup( REQUEST_GITHUB_SEARCH.content , "html.parser" );
    SCRAPED_RESULTS = GITHUB_SEARCH_CONTENT_HTML.find_all( "a" , { "class" : "v-align-middle" } );
    DOWNLOADED_PACKAGE = False;  
	
    #iterate through them 

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

        if read_me is None:
            sys_send.print_white( "No descirption provided for this repository ");
        
        else:
            sys_send.print_magenta( " Description of the script \n" );
            sys_send.print_blue( read_me.text[ 0 : 2000 ] + "...." );
         
        sys_send.print_magenta( "Press y to confirm the download or anyother key to proceed to next result" );
        confirm = input();
                 
        if confirm is not "y" and confirm is not "Y":
            continue;
        
        sys_send.print_white( "Searching for binaries " + PACKAGE_NAME + "....." );   
        
        try:
            
            # checking for binaries
            
            REQUEST_GITHUB_REPOSITORY_RELEASES = requests.get( GITHUB_URL + link[ 'href' ] + "/releases" );

        except:
            
            sys_send.error("Please check your internet connection");
            exit(0);
        
        # fetching binaries
        
        GITHUB_REPOSITORY_RELEASE_CONTENT_HTML = BeautifulSoup( REQUEST_GITHUB_REPOSITORY_RELEASES.content , "html.parser" );
        
        if LIST_VERSIONS_AVAILABLE: # lv flag is given
            
            PACAKAGE_RELEASES = GITHUB_REPOSITORY_RELEASE_CONTENT_HTML.find_all( "ul" , { "class" : "release-downloads" } );
            
            if PACAKAGE_RELEASES is None:
                
                sys_send.error( "Failed to find binary release for this pacakage contact the developer" );
                exit(0);       
           
            sys_send.print_white("Versions available for this pacakge : \n")
            i = 1;
            
            # list available versions
            
            for versions in PACAKAGE_RELEASES:
                
                link_to = versions.find( 'a' , href = True );
                print( "%d.)" % ( i ) + PACKAGE_NAME + " " + link_to[ 'href' ].split( '/' )[ -1 ]  );
                i = i + 1;
                
            sys_send.print_white("Select your version : ")
            version_code = int(input())
            
            link_to = PACAKAGE_RELEASES[version_code -1 ].find( 'a' , href = True );
            PACKAGE_DOWNLOAD_URL = link_to['href'];
        
        else:
            
            # if lv flag is not given pacpaw downloads latest one
            
            PACAKAGE_RELEASES_LATEST = GITHUB_REPOSITORY_RELEASE_CONTENT_HTML.find( "ul" , { "class" : "release-downloads" } );
            
           
            if PACAKAGE_RELEASES_LATEST is None:
                
                sys_send.error( "Failed to find binary release for this pacakage contact the developer" );
                exit(0)       
            
            link_to = PACAKAGE_RELEASES_LATEST.find( 'a' , href = True );
            PACKAGE_DOWNLOAD_URL = link_to[ 'href' ];   
        
        PACKAGE_NAME = PACKAGE_NAME + " " + PACKAGE_DOWNLOAD_URL.split( '/')[ -1 ];        
        
        # checks for ftp source
        if network_handle.download_file( GITHUB_URL + PACKAGE_DOWNLOAD_URL ,PACKAGE_NAME ) is not None:
            
            sys_send.sucess(  "Successfully downloaded " + PACKAGE_NAME );
            DOWNLOADED_PACKAGE = True;
            break;
        
    if DOWNLOADED_PACKAGE == False:
        
        sys_send.error( "Failed to find package specified....." );




