import requests
import sys_send
import sys

def download_file( url , filename):
    
    sys_send.print_white( 'Connecting to ftp server.....' )
        
    try:
        REQUEST_FTP_FILE = requests.get( url , stream = True );
        FILE_SIZE = int( REQUEST_FTP_FILE.headers.get( 'content-FILE_SIZE' ) );
        
        if FILE_SIZE < 1023:
             sys_send.print_white( "Package Size : %d Bytes" % ( FILE_SIZE ) );
        
        elif FILE_SIZE > 1023 and FILE_SIZE < 1048575 :
            sys_send.print_white( "Package Size : %d KB" % ( FILE_SIZE / 1024 ) );
        
        elif FILE_SIZE > 1048575:
            sys_send.print_white( "Package Size : %d MB" % ( FILE_SIZE / 1048576 ) );
    
    except:
           sys_send.error( "Please check your internet connection" );
           exit( 0 );
    
    RECIEVED_STATUS = int( 0 );
    sys_send.print_white( "Downloading......." );
    
    with open( filename , 'wb' ) as chunk_file:
         
        for buffer in REQUEST_FTP_FILE.iter_content( chunk_size = 1024 ):
            
            if buffer:
                RECIEVED_STATUS += len( buffer );
                chunk_file.write( buffer );
                done = int( 50 * ( RECIEVED_STATUS / FILE_SIZE ) );
                sys.stdout.write( " %s%%" % ( 2 * done ) + "\r[%s%s]" % ( '#' * done , ' ' * ( 50 - done ) ) );
                sys.stdout.flush( );
    
    return filename



			
