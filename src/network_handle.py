import requests
import sys_send
def download_file( url ):
    sys_send.print_white("Connecting to ftp server.....")
    filename = url.split( '/' )[ -1 ]
    r = requests.get( url , stream = True )
    with open( filename , 'wb' ) as f:
        for buffer in r.iter_content( chunk_size = 1024 ): 
            if buffer: 
                f.write( buffer )
                
    return filename