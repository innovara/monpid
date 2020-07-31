#!/usr/bin/env python3
import os.path
import sys
import syslog
import subprocess
import psutil
from time import sleep


def check_pid(pid):
  '''Checks if a given Unix pid exists.'''
  try:
    p = psutil.Process(pid)
    if p.status() == psutil.STATUS_ZOMBIE or p.status() == psutil.STATUS_DEAD:
      p.send_signal(9)
      return False
  except psutil.NoSuchProcess:
    return False
  else:
    return True


def main():
  '''Checks if a pid file exists and if the Unix pid within it exists and it is running.
  It starts a script if any of these fail.
  
  Use:
      ./monpid.py /path/to/script /path/to/pid_file
  
  Your script should write a pid file that nonpid.py can read. See sleep.py for an example.

  You can run this regularly with cron using crontab -e.
  '''
  script = sys.argv[1]
  pidfile = sys.argv[2]
  try:
    with open(pidfile, "r") as pidtxt:
      pid = int(pidtxt.readline())
  except FileNotFoundError:
    syslog.syslog(syslog.LOG_ERR, pidfile + " doesn't exist. " + script + " started.")
    subprocess.Popen([script])
  else:
    status = check_pid(pid)
    if status == True:
      pass
    elif status == False:
      syslog.syslog(syslog.LOG_ERR, script + " PID " + str(pid) + " doesn't exist. " + script + " started.")
      subprocess.Popen([script])


if __name__ == '__main__':
  main()
