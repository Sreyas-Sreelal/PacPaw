import requests
import sys_send
import sys

def download_file( url , filename):
    
    sys_send.print_white( 'Connecting to ftp server.....' )
        
    try:
        r = requests.get( url , stream = True );
        length = int( r.headers.get( 'content-length' ) );
        
        if length < 1023:
             sys_send.print_white( "Package Size : %d Bytes" % ( length ) );
        
        elif length > 1023 and length < 1048575 :
            sys_send.print_white( "Package Size : %d KB" % ( length / 1024 ) );
        
        elif length > 1048575:
            sys_send.print_white( "Package Size : %d MB" % ( length / 1048576 ) );
    
    except:
           sys_send.error( "Please check your internet connection" );
           exit( 0 );
    
    downloaded = int( 0 );
    sys_send.print_white( "Downloading......." );
    
    with open( filename , 'wb' ) as f:
         
        for buffer in r.iter_content( chunk_size = 1024 ):
            
            if buffer:
                downloaded += len( buffer );
                f.write( buffer );
                done = int( 50 * ( downloaded / length ) );
                sys.stdout.write( " %s%%" % ( 2 * done ) + "\r[%s%s]" % ( '#' * done , ' ' * ( 50 - done ) ) );
                sys.stdout.flush( );
    
    return filename



			
