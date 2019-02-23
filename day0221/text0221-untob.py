import ftplib
def ftpconnect(host,username,passwad):
    ftp =ftplib.FTP(host=host,user=username,passwd=passwad)
    return ftp
def upload(ftp,localfile,remotefile):
    buffersize=1024
    file=open(localfile,"rd")
    ftp.storbinary("STOR"+remotefile,file,buffersize)
    file.close()
def download(ftp,localfile,remotefile):
    buffersize=1024
    file=open(localfile,"wb")
    ftp.retrbinary("RETR"+remotefile,file.write,buffersize)
    file.close()
if __name__=="__main":
    ftp=ftpconnect("192.168.15.33","ftpzzy","123456")
    download(ftp,"d:ubuntu.txt","ubuntu.txt")
    ftp.quit()
