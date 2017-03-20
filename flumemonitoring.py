#!/usr/bin/env python
import os
import subprocess
import re
import smtplib
import socket
import sys
from email.mime.text import MIMEText

def get_lock(process_name):
    global lock_socket
    lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        lock_socket.bind('\0' + process_name)
        print 'Lock Monitoring flume'
    except socket.error:
        print 'lock exists'
        sys.exit()

def sendAlert(pesan):
       s = smtplib.SMTP('(isi alamat ip smtp servernya)')
       msg = MIMEText(""" %s """ % pesan)
       sender = '(isi alamat sendernya)'
       recipients = ['isi alamat si penerimanya']
       msg['Subject'] = "Flume " + sys.argv[2] + " error " 
       msg['From'] = sender
       msg['To'] = ", ".join(recipients)
       s.sendmail(sender, recipients, msg.as_string())


def main():
      f = subprocess.Popen(['tail','-n','30',sys.argv[1]],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
      get_lock(sys.argv[2])
      print sys.argv[2]

      string = f.stdout.read()
      re_str = r'Error'
      re_pattern = re.compile(re_str, re.IGNORECASE)
      match = re_pattern.findall(string)
      pattern1 = ''.join(match)
      if pattern1 != '':
          print 'Found System Error'
	  sendAlert(string)
	  subprocess.call(['/usr/bin/systemctl', 'restart', sys.argv[2]])
	  sys.exit(0)
      else:
          print 'tidak ada error'
          sys.exit(0)

if __name__ == "__main__":
  main()


