# monpid.py

## Introduction

monpid.py checks if:
 - a pid file exists;
 - if the pid exists; and
 - if the pid associated process is not a zoombie/defunct.

It starts the script/process if any of these fail.

## How to use it

Use:
```shell
 ./monpid.py /path/to/script (or command) /path/to/pid_file
 ```

The script/process should write a pid file that nonpid.py can read.

See sleep.py for an example.

You can run monpid.py at regular intervals using cron.

Example:
```shell
crontab -e
```
```
* * * * * * /path/to/monpid.py /path/to/script (or command) /path/to/pid_file
```
Or you can edit monpid.py and change this:
```python
if __name__ == '__main__':
  main()
```
To this:
```python
if __name__ == '__main__':
  while True:
    main()
    sleep(60) #Number of seconds you want it to wait until it runs again.
```
And add `from time import sleep` at the beginning of the script with the rest of import lines.

Then want to possibly run it from the shell like this:
```shell
./monpid.py /path/to/script (or command) /path/to/pid_file &
```
The & at the end will send the process to the background where it will keep doing its thing.
Bear in mind that if you plan to use monpid.py for SysAdmin tasks, you most likely want to run monpid.py automatically instead.
