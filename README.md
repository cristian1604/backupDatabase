# backupDatabase
Script to perform a database backup using **MySQL** and **Postgres** dump utilities.

This project currently runs on Linux.


### Changelog

  - Updated README file
  - Support Windows paths


### Requirements

- [Pexpect][Pexpect] - A Python module for controlling interactive programs in a pseudo-terminal
- By default the binaries for dump the databases are provided on this repository (only for Linux). But you can set your database binaries.

To install Pexpect simply run:

    python -m pip install pexpect


### How to set parameters

Parameters:

On `backup.py` there is a list of parameters between lines 21 and 27:

    databases = ['DATABASE1', 'DATABASE2', ..., 'DATABASEn']
    host='HOST'
    username='MY_USERNAME'
    password='MY_PASSWORD'
    port='PORT'                        # 5432 (default for Postgres), 3306 (default for MySQL)
    appMySqlDirectory = './mysqldump'  # Directory to mysqldump binary (executable on Windows)
    appPgDumpDirectory = './pg_dump'   # Directory to pg_dump binary (executable on Windows)


### Example

The script support two parameters:

`engine`  -  To set the database: `mysql` or `postgres`

`outputFile`  -  Set the location to the sql dump file (by default, home dir)

With all the parameters setted correctly (and intalled dependences), simply run:

**MySQL backup**

    python backup.py mysql

**Postgres backup**

    python backup.py postgres

By default the directory of the resultant SQL file will stored on `HOME` dir. Otherwise, add a third parameter to set the dump directory:

**MySQL backup**

    python backup.py mysql /home/backups

**Postgres backup**

    python backup.py postgres /home/backups

The filename will be **`backup_DATABASENAME_DATETIME.sql`**.

### To Do:

On next versions I will go to implement:

- Execute with Pexpect commands on Windows
- Improve the documentation (this file)


### Why this script?

I was motivated by the need to perform an automatic backup of several databases on MySQL and Postgres. And the capability to perform it by remote access or automatized tasks (cron)


About
----

Written by Cristian Bottazzi


[//]: #
   [Pexpect]: <https://github.com/pexpect/pexpect>
