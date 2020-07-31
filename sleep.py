#!/usr/bin/env python3
from os import getpid, remove
from time import sleep

def main():
  '''Dummy script to test monpid.py'''
  pid = getpid()
  with open("sleep.pid", "w") as pidfile:
    pidfile.write(str(pid))
  sleep(30)
  try:
    remove("sleep.pid")
  except FileNotFoundError:
    pass

if __name__ == '__main__':
  main()
