
# Week 6 --- Unix Filesystem Internals

## Table of Contents

1.  [Filesystem Internal Structure](#1-filesystem-internal-structure)
2.  [Inodes and File Metadata](#2-inodes-and-file-metadata)
3.  [Block Addressing and File Size](#3-block-addressing-and-file-size)
4.  [Directories and Path
    Resolution](#4-directories-and-path-resolution)
5.  [Hard Links and Directory Link Counts](#5-hard-links-and-directory-link-counts)

------------------------------------------------------------------------

# 1. Filesystem Internal Structure

## Definition

A **Unix filesystem** stores data inside a partition using a structured
layout that allows the operating system to locate files, manage
metadata, and allocate storage efficiently.

Inside a partition, the filesystem is organized into several major
components.

## Filesystem Layout

    +----------------------+
    | Boot Block           |
    | (used if bootable)   |
    +----------------------+
    | Superblock           |
    | filesystem metadata  |
    +----------------------+
    | Inode Table (i-list) |
    | metadata for files   |
    +----------------------+
    | Data Blocks          |
    | actual file content  |
    +----------------------+

### Components

**Boot Block**\
Contains boot loader information if the partition is bootable.

**Superblock**\
Stores filesystem-wide information such as:

-   filesystem size
-   block size
-   number of inodes
-   free block information

**Inode Table (i-list)**\
Array containing metadata entries for every file and directory.

**Data Blocks**\
Blocks used to store the actual contents of files.

### Block

A **block** is the smallest allocation unit on disk.

Typical block sizes:

    512 bytes
    1024 bytes
    4096 bytes
    8192 bytes

Blocks are used to store:

-   file contents
-   directory entries
-   pointer structures

------------------------------------------------------------------------

# 2. Inodes and File Metadata

## Definition

An **inode (index node)** is the data structure that stores **metadata
about a file**.

Every file and directory in a Unix filesystem has exactly one inode.

Important:\
The **inode does not store the filename**.

The filename exists only inside a directory entry.

## Information Stored in an Inode

Typical inode fields include:

1.  file type
2.  link count
3.  owner user ID
4.  group ID
5.  access permissions
6.  timestamps
7.  file size
8.  pointers to data blocks

### Inode Architecture

    +---------------------+
    | inode               |
    +---------------------+
    | file type           |
    | link count          |
    | user ID             |
    | group ID            |
    | permissions         |
    | timestamps          |
    | file size           |
    | block pointers      |
    +---------------------+

## Viewing Inode Numbers

Command:

``` bash
ls -i
# display inode numbers
```

Example:

``` bash
ls -i
# sample output
672258 food1.txt
672283 report.txt
672253 notes.txt
```

Explanation:

    inode number   filename

To inspect inode metadata:

``` bash
stat food1.txt
# show detailed inode metadata
```

Example output (simplified):

    File: food1.txt
    Size: 120
    Links: 1
    Access: rw-r--r--
    Uid: student
    Gid: student

------------------------------------------------------------------------

# 3. Block Addressing and File Size

## Definition

The inode stores **pointers to disk blocks** where the file data is
stored.

Unix filesystems typically use **15 block pointers**.

### Pointer Structure

    +------------------------+
    | inode                  |
    +------------------------+
    | 12 direct pointers     |
    | 1 singly indirect      |
    | 1 doubly indirect      |
    | 1 triply indirect      |
    +------------------------+

## Direct Pointers

The first **12 pointers** point directly to file blocks.

    inode
     ├─ block1
     ├─ block2
     ├─ block3
     ...
     └─ block12

### Example

Assume:

    block size = 4 KB
    direct pointers = 12

Maximum size supported by direct pointers:

    12 × 4 KB = 48 KB

This is efficient for small files.

------------------------------------------------------------------------

## Singly Indirect Pointer

The 13th pointer refers to a block containing **addresses of file
blocks**.

    inode
      └─ indirect block
           ├─ block1
           ├─ block2
           ├─ block3
           ...

### Example Calculation

Assume:

    block size = 4 KB
    pointer size = 4 bytes

Pointers per block:

    4096 / 4 = 1024 pointers

Maximum file size from singly indirect pointer:

    1024 × 4 KB = 4 MB

------------------------------------------------------------------------

## Doubly Indirect Pointer

The 14th pointer references a block containing pointers to **other
pointer blocks**.

    inode
      └─ double indirect block
           ├─ pointer block
           │    ├─ block
           │    ├─ block
           │    └─ block
           └─ pointer block

Example size:

    1024 × 1024 × 4 KB ≈ 4 GB

------------------------------------------------------------------------

## Triply Indirect Pointer

The 15th pointer adds a third level of indirection.

    inode
     └─ triple indirect block
          └─ double indirect block
               └─ pointer blocks
                    └─ data blocks

Example maximum size:

    1024 × 1024 × 1024 × 4 KB ≈ 4 TB

The triply indirect pointer dominates the total maximum file size.

------------------------------------------------------------------------

# 4. Directories and Path Resolution

## Definition

A **directory** is a file that stores mappings between filenames and
inode numbers.

Directory entries contain pairs:

    filename → inode number

Example directory content:

    food1.txt      8235
    report.txt     8229
    notes.txt      8269

## Directory Lookup Process

When accessing a file using an absolute path:

    /home/student/docs/file.txt

The system resolves the path step by step.

### Path Resolution Flow

    /
     ↓
    home
     ↓
    student
     ↓
    docs
     ↓
    file.txt

Each step requires reading the directory to find the inode number of the
next component.

Example:

    directory entry
    filename → inode number

Then:

    inode → data blocks

------------------------------------------------------------------------

# 5. Hard Links and Directory Link Counts

## Definition

A **hard link** is an additional filename that references the same
inode.

Multiple filenames can therefore refer to the same underlying file.

### Architecture

    directory A
       |
       ├── file1.txt ──┐
                       │
    directory B        │
       │               │
       └── file2.txt ──┘
              ↓
            same inode
              ↓
            data blocks

Both filenames refer to the **same inode and data blocks**.

## Creating a Hard Link

``` bash
ln file1.txt file2.txt
# create second name pointing to same inode
```

Check using:

``` bash
ls -l
```

Example output:

    -rw-r--r-- 2 student staff 120 file1.txt
    -rw-r--r-- 2 student staff 120 file2.txt

Explanation:

    2 = number of hard links to the inode

## Behavior Example

Modify the file through one name:

``` bash
echo "extra data" >> file1.txt
# append text to file1
```

Now read using the second name:

``` bash
cat file2.txt
# displays same content because both names reference same inode
```

## Removing Links

Removing one name only removes that directory entry.

``` bash
rm file1.txt
# removes one link
```

The file still exists because `file2.txt` still references the inode.

The inode and data blocks are removed only when:

    link count = 0

------------------------------------------------------------------------

## Directory Link Counts

Directories contain automatic entries:

    .
    ..

Meaning:

    .   current directory
    ..  parent directory

These entries affect the directory's link count.

Example:

``` bash
ls -l
```

Output example:

    drwxr-xr-x 2 student staff 4096 docs

The value **2** represents:

    docs directory entry
    .

Each subdirectory adds an additional `..` reference.

------------------------------------------------------------------------

**End of Week 6**
