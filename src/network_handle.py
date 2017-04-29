import requests
import sys_send
import sys

def download_file(url):
    sys_send.print_white('Connecting to ftp server.....')
    filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    length = int(r.headers.get('content-length'))
    downloaded = int(0)
    sys_send.print_white("Downloading.......")
    with open(filename, 'wb') as f:
        for buffer in r.iter_content(chunk_size=1024):
            if buffer:
                downloaded += len(buffer)
                f.write(buffer)
                done = int(50 * (downloaded / length))
                sys.stdout.write(" %s%%" % (2 * done) + "\r[%s%s]" % ('#' * done, ' ' * (50 - done)))
                sys.stdout.flush()
    return filename



			
