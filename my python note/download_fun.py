# -*- coding:utf8 -*-
import os, sys
import urllib, time, threading

download_url = ''
downlload_path = ''

def download(url,path):
    urllib.urlretrieve(url,path)

def sss(url,path):
    time.sleep(0.5)
    response = urllib.urlopen(url)
    Header = response.info()
    total_size = int(Header.getheaders("Content-Length")[0])
    out = 'DownLoad:[______________________________]'
    while True:
        size = os.path.getsize(path)
        rate = round((size*1.0)/total_size, 5)
        per = rate*100

        if rate != 1:
            out = 'DownLoad:[' + int(rate*40)*'>' + (40-int(rate*40))*' '+ ']'
        else:
            sys.stdout.write('\r%s\r' % ' '*60)
            sys.stdout.flush()
            print 'DownLoad:[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>] 100%          '
            break
        
        sys.stdout.write('\r%s %.2f%s\r'% (out,per,'%'))
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r%s\r' % ' '*60)
        sys.stdout.flush()

def main():
    threads = []
    t1 = threading.Thread(target=download, args=(download_url, download_path))
    t2 = threading.Thread(target=sss, args=(download_url, download_path))
    threads.append(t1)
    threads.append(t2)

    for i in threads:
        i.start()

if __name__ == '__main__':
    main()
