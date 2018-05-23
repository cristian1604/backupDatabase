# backupDatabase
Script to perform a database backup using **MySQL** and **Postgres** dump utilities.

With this script you can backup several databases from a DB engine at the same time.

**This project currently runs on Linux.**


### Changelog

  - Clean up the code to make it more readable (Work in progress)
  - Test with sevearl Postgres databases


### Requirements

- [Pexpect][Pexpect] - A Python module for controlling interactive programs in a pseudo-terminal (this dependence soon will be going removed)
- By default the binaries for dump the databases are provided on this repository (only for Linux). But you can set your database binaries.

If you have `pip`, to install Pexpect simply run:

    python -m pip install pexpect


### How to set parameters

Parameters:

On `backup.py` there is a list of parameters between lines 21 and 27:

    databases = ['DATABASE1', 'DATABASE2', ..., 'DATABASEn']
    host='HOST'                        # URL or IP to the database server
    username='MY_USERNAME'             # For security reasons I recommend a backup user only
    password='MY_PASSWORD'
    port='PORT'                        # 5432 (default for Postgres), 3306 (default for MySQL)
    appMySqlDirectory = './mysqldump'  # Directory to mysqldump binary (executable on Windows)
    appPgDumpDirectory = './pg_dump'   # Directory to pg_dump binary (executable on Windows)

Note: On this repository I've uploaded the `mysqldump` and `pg_dump` utilities. But I recommend to use the binaries provided on your database engine.


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

- Clean up the code
- Autodetect if the dump script is avaiable on the system before use the included on repository
- Test on Windows (with Python 3.6.5)
- Remove Pexpect as dependence due several issues on Windows


### Why this script?

I was motivated by the need to perform an automatic backup of several databases on MySQL and Postgres. And the capability to perform it by remote access or automatized tasks (cron)


About
----

Written by Cristian Bottazzi


[//]: #
   [Pexpect]: <https://github.com/pexpect/pexpect>
