# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

# Written by Cristian Bottazzi
# 13/05/2018
# Last review: 24/05/2018
# Description: Make a backup from the selected databases on MySQL or Postgres and
# creates a dump SQL file (with creation schema)
# Currently runs on Linux.
#

from datetime import datetime, date, time, timedelta
import sys
import os.path
from subprocess import call
import platform

#PARAMS:
databases = ['DB_NAME1','DB_NAME2']
host='HOST'
username='USER'
password='PASSWORD'
port='PORT'
appMySqlDirectory = './mysqldump'
appPgDumpDirectory = './pg_dump'

if len(sys.argv) == 1:
  print("Enter database engine: 'mysql' or 'postgres'")
  print("Type -h or --help to see the documentation")
  quit()

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
  print("PERFORM A BACKUP FROM MySql OR Postgres DATABASE")
  print("This script uses the default programs to realize this job.")
  print("Args:")
  print("DbEngine   <- Database engine (can be mysql or postgres)")
  print("path       <- Path to save the SQL file")
  print("Example:")
  print("python backup.py mysql /home/my_user/backups/")
  print("to perform a backup on the backups directory")
  print("")
  quit()

OS = platform.system()
engine = sys.argv[1]

if len(sys.argv) >= 3:
  print("Using custom path to backup files")
  route = sys.argv[2]
  if not route.endswith('/') or not route.endswith('\\'):
    if (OS == 'Linux'):
      route = route + '/'
    if (OS == 'Windows'):
      route = route + '\\'
else:
    print("Missing argument for output location. Using home dir by default")
    if (OS == 'Linux'):
      route = os.getenv("HOME") + '/'
    if (OS == 'Windows'):
      route = os.path.expanduser('~') + '\\'

for database in databases:
  filename = 'backup_' + database +'_'+ datetime.now().strftime("%Y-%m-%d_%H:%M") + '.sql'
  if engine == 'mysql':
    cmd = appMySqlDirectory + ' --user='+username+' -p'+password+' --host="'+host+'" --protocol=tcp --port='+port+' --default-character-set=utf8 --single-transaction=TRUE --result-file='+route+filename+' --routines --events "'+ database +'"'
    os.system(cmd)
    print('[DONE]: Backup for [' + database + '] has finished.')

  if engine == 'postgres':
    cmd = appPgDumpDirectory + ' --dbname=postgresql://'+username+':'+password+'@'+host+':'+port+'/'+database+' > '+route+filename
    os.system(cmd)
    print('[DONE]: Backup for [' + database + '] has finished.')

if engine == 'mysql' or engine == 'postgres':
  print('[FINISHED]: Backup created on ' + route)
else:
  print('[ERROR]: Must select a correct database engine: mysql or postrges')
