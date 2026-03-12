# Week 2 — Filesystem and File Control in Unix

## Table of Contents
1. [Week 2 Overview](#1-week-2-overview)  
2. [Filesystem Structure and Path Semantics](#2-filesystem-structure-and-path-semantics)  
3. [File Permissions Model](#3-file-permissions-model)  
4. [Ownership and Groups](#4-ownership-and-groups)  
5. [Changing Permissions with chmod](#5-changing-permissions-with-chmod)  
6. [Core File Operations](#6-core-file-operations)  
   6.1 [`touch` — Create Files](#61-touch--create-files)  
   6.2 [`ls` — List Files](#62-ls--list-files)  
   6.3 [`cp` — Copy Files](#63-cp--copy-files)  
   6.4 [`mv` — Move/Rename Files](#64-mv--moverename-files)  
   6.5 [`find` — Search Filesystem](#65-find--search-filesystem)  
7. [`rm` — File and Directory Removal](#7-rm--file-and-directory-removal)  
8. [`tar` and `gzip` — Archiving and Compression](#8-tar-and-gzip--archiving-and-compression)  
9. [Globbing (Metacharacters)](#9-globbing-metacharacters)  

---

# 1. Week 2 Overview

By the end of Week 2, you should be able to:

- Understand the **Unix filesystem hierarchy**
- Navigate paths using **absolute and relative paths**
- Interpret **file permissions**
- Manage **ownership and groups**
- Perform common **file operations**
- Remove files safely
- Archive and compress files
- Use **globbing patterns** to operate on multiple files

---

# 2. Filesystem Structure and Path Semantics

Unix uses a **hierarchical filesystem** starting from the root directory.

### Filesystem Architecture

```
            +------+
            |  /   |
            +------+
                |
   --------------------------------
   |        |        |            |
 /home     /etc     /var        /usr
   |
 /home/user
   |
 /home/user/project
   |
 file.txt
```

Key directories:

| Directory | Purpose |
|---|---|
| / | root filesystem |
| /home | user home directories |
| /etc | configuration files |
| /var | logs and variable data |
| /usr | system programs |

---

### Path Resolution Flow

```
User Command
     |
     v
Shell
     |
     v
Resolve Path
     |
     |-- Absolute path? → Start from /
     |
     |-- Relative path? → Start from current directory
     |
     v
Apply navigation symbols
     |
     v
Final file location
```

Examples:

```bash
ls /usr/bin
# list executables in /usr/bin
```

```bash
cp ../notes.txt ./backup/
# copy file from parent directory to backup directory
```

```bash
mv ~/Downloads/file.txt .
# move file from home downloads to current directory
```

---

# 3. File Permissions Model

Permissions determine **who can access a file or directory and what actions they can perform**.

### Permission Structure

```
User → Group → Others
```

Example permission string:

```
-rwxr-xr--
```

Breakdown:

```
|Type| User | Group | Others |
      rwx     r-x      r--
```

| Field | Meaning |
|---|---|
| Type | `-` file, `d` directory |
| User | permissions for file owner |
| Group | permissions for group members |
| Others | permissions for all other users |

---

### Permission Symbols

| Symbol | Numeric Value | Meaning |
|---|---|---|
| r | 4 | read permission |
| w | 2 | write permission |
| x | 1 | execute permission |

Permissions are **additive**.

Example calculations:

| Numeric | Calculation | Result |
|---|---|---|
| 7 | 4+2+1 | rwx |
| 6 | 4+2 | rw- |
| 5 | 4+1 | r-x |
| 4 | 4 | r-- |
| 3 | 2+1 | -wx |
| 2 | 2 | -w- |
| 1 | 1 | --x |
| 0 | 0 | --- |

---

### chmod Symbolic Operators

When using symbolic permissions with `chmod`, three operators control how permissions change.

| Operator | Meaning |
|---|---|
| `+` | add permission |
| `-` | remove permission |
| `=` | set exact permission |

Examples:

```bash
chmod u+x script.sh
# add execute permission to the owner
```

```bash
chmod g-w file.txt
# remove write permission from group
```

```bash
chmod o=r file.txt
# set others permission to read only
```

```bash
chmod u=rw file.txt
# set owner permissions exactly to read and write
```

---

### Numeric Permission Examples

```bash
chmod 755 script.sh
# owner rwx, group r-x, others r-x
```

```bash
chmod 644 file.txt
# owner rw-, group r--, others r--
```

```bash
chmod 600 private.txt
# owner read/write only
```

Teaching note:  
Explain that **numeric permissions represent the sum of r(4), w(2), and x(1)**.

---

# 4. Ownership and Groups

Every file has:

```
Owner
Group
Others
```

Example:

```bash
sudo chown alice file.txt
# change owner of file.txt to alice
```

```bash
sudo chown alice:staff file.txt
# change owner to alice and group to staff
```

```bash
sudo chown -R alice project/
# recursively change ownership of project directory
```

```bash
chgrp dev file.txt
# change group ownership to dev
```

Teaching note:  
Explain **multi-user environments and shared directories**.

---

# 5. Changing Permissions with chmod

### Definition

`chmod` modifies **file permission bits**.

### Syntax

```bash
chmod mode file
```

### Common options

| Option | Meaning |
|---|---|
| -R | recursive permission change |

### Examples

```bash
chmod 644 file.txt
# owner read/write, others read only
```

```bash
chmod 755 script.sh
# executable script with read access
```

```bash
chmod u+x script.sh
# add execute permission to owner
```

```bash
chmod g-w file.txt
# remove write permission from group
```

```bash
chmod -R 755 project/
# recursively change permissions for entire directory
```

---

# 6. Core File Operations

---

## 6.1 `touch` — Create Files

### Definition

`touch` creates empty files or updates file timestamps.

### Syntax

```bash
touch file
```

### Common options

| Option | Meaning |
|---|---|
| -c | don't create new file |
| -t | set timestamp |

### Examples

```bash
touch file.txt
# create empty file
```

```bash
touch file1 file2 file3
# create multiple files
```

```bash
touch file{1..5}.txt
# create file1.txt to file5.txt
```

```bash
touch -c existing.txt
# update timestamp without creating file
```

```bash
touch -t 202401010101 file.txt
# set custom timestamp
```

Teaching note:  
Explain timestamps **(mtime, atime, ctime)**.

---

## 6.2 `ls` — List Files

### Definition

`ls` lists directory contents.

### Syntax

```bash
ls [options]
```

### Common options

| Option | Meaning |
|---|---|
| -l | long format |
| -a | include hidden |
| -h | human readable sizes |
| -R | recursive |

### Examples

```bash
ls
# list files in current directory
```

```bash
ls -l
# show detailed file information
```

```bash
ls -la
# show hidden files and detailed listing
```

```bash
ls -lh
# display human readable file sizes
```

```bash
ls -R
# recursively list directory contents
```

```bash
ls *.txt
# list only text files
```

---

## 6.3 `cp` — Copy Files

### Definition

`cp` copies files or directories.

### Syntax

```bash
cp source destination
```

### Common options

| Option | Meaning |
|---|---|
| -r | recursive |
| -i | interactive |
| -v | verbose |

### Examples

```bash
cp file1 file2
# copy file1 to file2
```

```bash
cp *.txt docs/
# copy all text files into docs directory
```

```bash
cp -r project backup/
# copy entire directory recursively
```

```bash
cp -i file1 file2
# ask before overwriting
```

```bash
cp -v file1 backup/
# display copy operation
```

Teaching note:  
Explain **overwrite risks**.

---

## 6.4 `mv` — Move/Rename Files

### Definition

`mv` moves or renames files.

### Syntax

```bash
mv source destination
```

### Common options

| Option | Meaning |
|---|---|
| -i | interactive |
| -v | verbose |

### Examples

```bash
mv old.txt new.txt
# rename file
```

```bash
mv *.log logs/
# move log files to logs directory
```

```bash
mv report.txt ../archive/
# move file to parent directory archive
```

```bash
mv -i file dest
# ask before overwrite
```

```bash
mv -v file dest
# show move operation
```

---

## 6.5 `find` — Search Filesystem

### Definition

`find` searches directories recursively based on criteria.

### Syntax

```bash
find path condition
```

### Common options

| Option | Meaning |
|---|---|
| -name | filename pattern |
| -type | file type |
| -size | size filter |
| -exec | run command |

### Examples

```bash
find . -name "*.txt"
# find all text files in current directory tree
```

```bash
find /var/log -type f
# locate all regular files in /var/log
```

```bash
find . -size +1M
# find files larger than 1MB
```

```bash
find . -name "*.log" -exec rm {} \;
# delete all log files found
```

Teaching note:  
Explain **recursive filesystem traversal**.

---

# 7. `rm` — File and Directory Removal

### Definition

`rm` removes files and directories.

### Common options

| Option | Meaning |
|---|---|
| -r | recursive |
| -f | force |
| -i | interactive |

### Examples

```bash
rm file.txt
# delete file
```

```bash
rm -i file.txt
# ask before deletion
```

```bash
rm -r project/
# remove directory recursively
```

```bash
rm -rf build/
# force delete directory tree
```

```bash
rm *.tmp
# delete all temporary files
```

Teaching note:  
Explain why `rm -rf` is dangerous.

---

# 8. `tar` and `gzip` — Archiving and Compression

### tar

### Definition

`tar` bundles multiple files into a single archive.

### Options

| Option | Meaning |
|---|---|
| -c | create archive |
| -x | extract archive |
| -v | verbose |
| -f | filename |
| -z | gzip compression |

### Examples

```bash
tar -cvf project.tar project/
# create archive of project directory
```

```bash
tar -xvf project.tar
# extract archive
```

```bash
tar -czvf project.tar.gz project/
# create compressed archive
```

---

### gzip

### Definition

`gzip` compresses files individually.

### Options

| Option | Meaning |
|---|---|
| -d | decompress |
| -k | keep original |

### Examples

```bash
gzip file.txt
# compress file
```

```bash
gzip -k file.txt
# compress but keep original
```

```bash
gzip -d file.txt.gz
# decompress file
```

---

# 9. Globbing (Metacharacters)

Globbing allows the **shell to expand filename patterns** before executing commands.

### Architecture

```
User Command
      |
      v
Shell Expansion (Globbing)
      |
      v
Expanded File List
      |
      v
Command Execution
```

### Metacharacters

| Pattern | Meaning |
|---|---|
| * | any characters |
| ? | single character |
| [abc] | set |
| [a-z] | range |
| {a,b} | alternatives |
| {1..5} | sequence |

### Examples

```bash
ls *.txt
# list all text files
```

```bash
cp data* backup/
# copy all files starting with data
```

```bash
mv log2023*.txt archive/
# move log files from 2023 to archive
```

```bash
rm *.tmp
# delete all temporary files
```

```bash
ls file?.txt
# match file1.txt file2.txt etc
```

```bash
ls report[1-5].txt
# match report1.txt through report5.txt
```

```bash
cp file{1,2,3}.txt backup/
# copy specific files using brace expansion
```

```bash
mkdir dir{1..5}
# create dir1 dir2 dir3 dir4 dir5
```

```bash
cp *.{jpg,png} images/
# copy image files of multiple extensions
```

```bash
mv report_202[0-3].txt archive/
# move reports for years 2020–2023
```

```bash
rm file?.log
# remove files like file1.log file2.log
```

```bash
cp {a..d}.txt letters/
# copy a.txt b.txt c.txt d.txt
```

```bash
touch file{1..9..2}.txt
# create file1 file3 file5 file7 file9
```

Teaching note:  
Explain **shell expansion happens BEFORE command execution**.

---

**End of Week 2**
```
