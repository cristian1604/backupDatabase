# backupDatabase
This is a *wrapper-script* to perform a database backup using **MySQL** and **Postgres** dump utilities.

With this script you can backup several databases from a DB engine at the same time.

**This project currently runs on Linux.** I'm improving the script to run on Windows (on next updates)


### Changelog

  - Improve documentation
  - Tested on multiple MySQL and Postgres databases (one script to call each DB engine)
  - Comment code


### Requirements

- By default only the pgdump binary (for linux) is provided on this repository. But if you run this script on the database server, I recommend strongly use the provided binaries by the database engine.


### How to set parameters

Parameters:

On `backup.py` there is a list of parameters between lines 21 and 28:

    databases = ['DATABASE1', 'DATABASE2', ..., 'DATABASEn']
    host='HOST'                        # URL or IP to the database server
    port='PORT'                        # 5432 (default for Postgres), 3306 (default for MySQL)
    username='MY_USERNAME'             # For security reasons I recommend a backup user only
    password='MY_PASSWORD'
    appMySqlDirectory = './mysqldump'  # Directory to mysqldump binary (executable on Windows)
    appPgDumpDirectory = './pg_dump'   # Directory to pg_dump binary (executable on Windows)

Note: On this repository I've uploaded the `mysqldump` and `pg_dump` utilities. But I recommend to use the binaries provided on your database engine.


### Example

The script support two parameters:

`engine`  -  To set the database: `mysql` or `postgres` (or `pg` to abbreviate)

`outputFile`  -  Set the location to the sql dump file (if this field is empty, by default, home dir)

With all the parameters setted correctly, simply run:

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

- Autodetect if the dump script is avaiable on the system before use the included on repository
- Test on Windows (with Python 3.6.5)


### Why this script?

I was motivated by the need to perform an automatic backup of several databases on MySQL and Postgres. And the capability to perform it by remote access or automatized tasks (cron)


About
----

Written by Cristian Bottazzi


[//]: #
   [Pexpect]: <https://github.com/pexpect/pexpect>
