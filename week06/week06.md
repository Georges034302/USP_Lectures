
# Week 6 — Unix Filesystem Internals

## Table of Contents
1. [Filesystem Internal Structure](#1-filesystem-internal-structure)  
   1.1 [Partition Layout](#11-partition-layout)  
   1.2 [Boot Block](#12-boot-block)  
   1.3 [Superblock](#13-superblock)  
   1.4 [Inode Table](#14-inode-table)  
   1.5 [Data Blocks](#15-data-blocks)  
2. [Inodes and File Metadata](#2-inodes-and-file-metadata)  
   2.1 [What an Inode Represents](#21-what-an-inode-represents)  
   2.2 [What an Inode Stores](#22-what-an-inode-stores)  
   2.3 [What an Inode Does Not Store](#23-what-an-inode-does-not-store)  
   2.4 [Viewing Inodes with `ls -i` and `stat`](#24-viewing-inodes-with-ls--i-and-stat)  
3. [Block Addressing and File Size](#3-block-addressing-and-file-size)  
   3.1 [Direct Pointers](#31-direct-pointers)  
   3.2 [Singly Indirect Pointer](#32-singly-indirect-pointer)  
   3.3 [Doubly Indirect Pointer](#33-doubly-indirect-pointer)  
   3.4 [Triply Indirect Pointer](#34-triply-indirect-pointer)  
   3.5 [Worked Size Calculations](#35-worked-size-calculations)  
4. [Directories and Path Resolution](#4-directories-and-path-resolution)  
   4.1 [Directories as Filename-to-Inode Maps](#41-directories-as-filename-to-inode-maps)  
   4.2 [How Path Resolution Works](#42-how-path-resolution-works)  
   4.3 [Practical Inspection Examples](#43-practical-inspection-examples)  
5. [Hard Links and Directory Link Counts](#5-hard-links-and-directory-link-counts)  
   5.1 [Hard Links](#51-hard-links)  
   5.2 [Practical Hard Link Demonstration](#52-practical-hard-link-demonstration)  
   5.3 [Removing Links and File Deletion](#53-removing-links-and-file-deletion)  
   5.4 [Directory Link Counts](#54-directory-link-counts)  
6. [Symbolic Links (Soft Links)](#6-symbolic-links-soft-links)  
   6.1 [Concept and Definition](#61-concept-and-definition)  
   6.2 [Creating Symbolic Links](#62-creating-symbolic-links)  
   6.3 [Inspecting Symbolic Links](#63-inspecting-symbolic-links)  
   6.4 [Broken Symbolic Links](#64-broken-symbolic-links)  
   6.5 [Hard Links vs Symbolic Links](#65-hard-links-vs-symbolic-links)

---

# 1. Filesystem Internal Structure

## Definition

A **Unix filesystem** is the internal on-disk structure used to store files, store metadata, allocate blocks, and retrieve file contents from a partition.

A filesystem is not just a collection of filenames. It is a set of coordinated structures that let the kernel answer questions such as:

- Where is the file’s metadata?
- Which blocks contain the file’s contents?
- Which blocks are free?
- Which inode belongs to a given filename?
- Is the filesystem in a valid state?

The classic teaching model used in Unix systems programming divides a filesystem partition into four major areas:

- boot block
- superblock
- inode table
- data blocks

## 1.1 Partition Layout

A simplified conceptual layout is:

```text
+------------------------------------------------------+
| Boot Block                                           |
| Boot code if this partition is bootable              |
+------------------------------------------------------+
| Superblock                                           |
| Global metadata about the whole filesystem           |
+------------------------------------------------------+
| Inode Table (i-list)                                 |
| Array of inodes describing files and directories     |
+------------------------------------------------------+
| Data Blocks                                          |
| File contents, directory contents, pointer blocks    |
+------------------------------------------------------+
```

Flow of lookup at a high level:

```text
filename
   ↓
directory entry
   ↓
inode number
   ↓
inode
   ↓
data block addresses
   ↓
file contents
```

That sequence is the core idea behind the Unix filesystem.

## 1.2 Boot Block

The **boot block** is relevant only if the partition can be used to boot the system.

Purpose:

- stores boot loader code
- participates in system startup
- is usually ignored for ordinary data partitions

In many practical situations in this subject, you do not interact with the boot block directly. It is part of the filesystem layout, but not part of normal daily file operations.

## 1.3 Superblock

The **superblock** stores global metadata about the filesystem as a whole.

Typical information includes:

- total filesystem size
- block size
- inode count
- free block count
- free inode count
- filesystem status information

Conceptual diagram:

```text
+----------------------------------+
| SUPERBLOCK                       |
+----------------------------------+
| filesystem size                  |
| block size                       |
| number of inodes                 |
| number of free blocks            |
| number of free inodes            |
| state / consistency information  |
+----------------------------------+
```

The superblock is critical because the kernel needs it to interpret the filesystem correctly. If the superblock is corrupted, the filesystem may not mount or may require repair.

## 1.4 Inode Table

The **inode table** is an array of inode structures.

Each inode corresponds to exactly one filesystem object, such as:

- regular file
- directory
- symbolic link
- device file
- pipe
- socket

Conceptually:

```text
inode table
+----------+
| inode 1  |
+----------+
| inode 2  |
+----------+
| inode 3  |
+----------+
| inode 4  |
+----------+
      ...
```

Important principle:

An inode identifies the file object itself, not the filename.

## 1.5 Data Blocks

**Data blocks** are the storage units used to hold actual content.

Depending on context, a data block may contain:

- regular file contents
- directory entries
- indirect pointer arrays

Typical block sizes used in teaching examples include:

```text
512 B
1 KB
4 KB
8 KB
```

The filesystem allocates blocks as files grow, and the inode stores pointers to those blocks.

---

# 2. Inodes and File Metadata

## Definition

An **inode** is the metadata structure that describes a filesystem object.

Every regular file and every directory has an inode. The inode contains the information the kernel needs to manage that object.

## 2.1 What an Inode Represents

The inode represents the file object itself.

A useful mental model is:

```text
directory entry
   ├── filename
   └── inode number
             ↓
           inode
             ↓
        file metadata
        block pointers
             ↓
         file contents
```

The filename gets you to the inode number.  
The inode number gets you to the inode.  
The inode gets you to the data blocks.

## 2.2 What an Inode Stores

A typical inode stores:

1. file type  
2. link count  
3. owner user ID  
4. group ID  
5. permissions  
6. timestamps  
7. file size  
8. pointers to data blocks  

Conceptual structure:

```text
+-------------------------------+
| inode                         |
+-------------------------------+
| file type                     |
| link count                    |
| owner UID                     |
| group GID                     |
| permissions                   |
| timestamps                    |
| file size                     |
| block pointers                |
+-------------------------------+
```

### File type

The inode identifies what kind of object this is:

- regular file
- directory
- symbolic link
- device file
- pipe
- socket

### Link count

The link count tells how many directory entries refer to this inode.

### Owner, group, permissions

These fields support access control.

### Timestamps

These record important file times, such as last access and last modification.

### File size

This records the logical size of the file in bytes.

### Block pointers

These point to the blocks containing the file’s data, or to pointer blocks used to reach those data blocks.

## 2.3 What an Inode Does Not Store

The inode does **not** store the filename.

That is one of the most important Unix filesystem facts.

The filename is stored in the **directory**, not in the inode.

Conceptually:

```text
directory
+------------------------------+
| filename        inode number |
+------------------------------+
| report.txt      672283       |
| notes.txt       672258       |
+------------------------------+
```

That is why multiple filenames can refer to the same inode: hard links.

## 2.4 Viewing Inodes with `ls -i` and `stat`

### `ls -i`

Use `ls -i` to display inode numbers.

```bash
ls -i
# show inode numbers with filenames
```

Example:

```bash
ls -i
672258 notes.txt
672283 report.txt
672253 data.csv
```

Interpretation:

```text
672258 → inode for notes.txt
672283 → inode for report.txt
672253 → inode for data.csv
```

### `stat`

Use `stat` to inspect file metadata associated with the inode.

```bash
stat report.txt
# display file metadata
```

Typical output includes fields such as:

```text
File: report.txt
Size: 1024
Blocks: 8
IO Block: 4096
regular file
Device: ...
Inode: 672283
Links: 1
Access: (0644/-rw-r--r--)
Uid: ...
Gid: ...
Access: ...
Modify: ...
Change: ...
```

Practical reading of that output:

- `Inode` identifies the inode number
- `Links` shows the hard link count
- `Size` shows the file length in bytes
- `Access` shows permissions

Practical example:

```bash
touch demo.txt
# create an empty file

ls -i demo.txt
# view its inode number

stat demo.txt
# inspect the inode-related metadata
```

---

# 3. Block Addressing and File Size

## Definition

The inode stores pointers that allow the filesystem to locate the blocks containing the file’s data.

To support both small and very large files efficiently, a traditional Unix teaching model uses:

- 12 direct pointers
- 1 singly indirect pointer
- 1 doubly indirect pointer
- 1 triply indirect pointer

Conceptual layout:

```text
+------------------------------------+
| inode                              |
+------------------------------------+
| 12 direct pointers                 |
| 1 singly indirect pointer          |
| 1 doubly indirect pointer          |
| 1 triply indirect pointer          |
+------------------------------------+
```

## 3.1 Direct Pointers

The first 12 pointers are **direct pointers**.

Each one points directly to a data block.

```text
inode
 ├── direct ptr 1  ──→ data block
 ├── direct ptr 2  ──→ data block
 ├── direct ptr 3  ──→ data block
 ├── ...
 └── direct ptr 12 ──→ data block
```

Why direct pointers matter:

- fast access for small files
- no extra pointer blocks needed
- efficient for common files such as configuration files and small directories

Example:

If block size = 4 KB, then maximum size using only direct pointers is:

```text
12 × 4 KB = 48 KB
```

## 3.2 Singly Indirect Pointer

The 13th pointer is the **singly indirect pointer**.

It does not point directly to file data.  
It points to a block that contains many block addresses.

```text
inode
   └── singly indirect ptr
            ↓
      +-------------------+
      | ptr | ptr | ptr   |
      | ptr | ptr | ptr   |
      +-------------------+
         ↓     ↓     ↓
       data  data  data blocks
```

Worked example:

Assume:

- block size = 4 KB
- pointer size = 4 bytes

Pointers that fit in one block:

```text
4096 / 4 = 1024 pointers
```

Maximum size reachable through the singly indirect pointer:

```text
1024 × 4 KB = 4 MB
```

## 3.3 Doubly Indirect Pointer

The 14th pointer is the **doubly indirect pointer**.

It points to a block of pointers, each of which points to another pointer block, which then points to data blocks.

```text
inode
   └── doubly indirect ptr
            ↓
      +-------------------+
      | ptr | ptr | ptr   |
      +-------------------+
         ↓     ↓     ↓
   +---------+  +---------+
   | ptr...  |  | ptr...  |
   +---------+  +---------+
      ↓             ↓
   data blocks   data blocks
```

Worked example:

Using:

- block size = 4 KB
- pointer size = 4 bytes
- 1024 pointers per block

Maximum size reachable:

```text
1024 × 1024 × 4 KB = 4 GB
```

## 3.4 Triply Indirect Pointer

The 15th pointer is the **triply indirect pointer**.

It adds one more level.

```text
inode
   └── triply indirect ptr
            ↓
      top-level pointer block
            ↓
      second-level pointer blocks
            ↓
      third-level pointer blocks
            ↓
           data blocks
```

Worked example:

Using the same assumptions:

- 1024 pointers per block
- 4 KB data block size

Maximum size reachable:

```text
1024 × 1024 × 1024 × 4 KB = 4 TB
```

## 3.5 Worked Size Calculations

### Example 1: direct pointers only

Assume:

- block size = 512 B

Maximum file size from direct pointers:

```text
12 × 512 B = 6144 B = 6 KB
```

### Example 2: doubly indirect pointer

Assume:

- block size = 8 KB
- pointer size = 4 B

Pointers per pointer block:

```text
8192 / 4 = 2048
```

Maximum size from doubly indirect pointer:

```text
2048 × 2048 × 8 KB = 32 GB
```

### Why this design makes sense

This structure is efficient because:

- small files are handled quickly through direct pointers
- large files are still supported through indirect levels
- the common case stays fast

---

# 4. Directories and Path Resolution

## Definition

A **directory** is a special file whose content is a list of mappings from filenames to inode numbers.

A directory entry conceptually looks like:

```text
filename → inode number
```

## 4.1 Directories as Filename-to-Inode Maps

Example conceptual directory content:

```text
+----------------------------------+
| filename          inode number   |
+----------------------------------+
| notes.txt         672258         |
| report.txt        672283         |
| data.csv          672253         |
+----------------------------------+
```

This means the directory does not store the full metadata for those files.  
It stores the names and the inode numbers that let the kernel find the actual inode structures.

Practical consequence:

To open `report.txt`, the system first searches the directory for the entry `report.txt`, obtains its inode number, loads that inode, and then follows its block pointers.

## 4.2 How Path Resolution Works

When the user accesses a pathname such as:

```text
/home/student/projects/report.txt
```

the kernel resolves it one component at a time.

Step-by-step flow:

```text
/
 ↓
home
 ↓
student
 ↓
projects
 ↓
report.txt
```

Detailed lookup model:

```text
start at /
   ↓
read root directory
   ↓
find inode for "home"
   ↓
read /home directory
   ↓
find inode for "student"
   ↓
read /home/student directory
   ↓
find inode for "projects"
   ↓
read /home/student/projects directory
   ↓
find inode for "report.txt"
   ↓
load inode for report.txt
   ↓
follow block pointers to file data
```

This is why path resolution depends on directories being readable and valid.

### Why absolute paths require multiple lookups

An absolute path is not resolved all at once.  
Each path component must be found in the directory before it.

For:

```text
/home/student/projects/report.txt
```

the kernel must resolve:

1. `/`
2. `home`
3. `student`
4. `projects`
5. `report.txt`

That is a chain of directory-based lookups.

## 4.3 Practical Inspection Examples

### Example 1: inspect inode and directory behavior

```bash
mkdir demo_dir
# create a directory

touch demo_dir/file1.txt
# create a file inside it

ls -li demo_dir
# show inode numbers for entries inside the directory
```

Possible interpretation:

- the directory contains filename-to-inode mappings
- `file1.txt` has its own inode
- the directory itself also has an inode

### Example 2: inspect the directory inode itself

```bash
ls -ldi demo_dir
# show inode information for the directory itself
```

Explanation:

- `-d` tells `ls` to list the directory entry itself
- `-i` prints the inode number
- without `-d`, `ls` lists the directory contents instead

### Example 3: compare file and directory metadata

```bash
stat demo_dir
# inspect metadata for the directory inode

stat demo_dir/file1.txt
# inspect metadata for the file inode
```

That comparison helps students see that both directories and regular files have inodes.

---

# 5. Hard Links and Directory Link Counts

## Definition

A **hard link** is an additional directory entry that refers to the same inode.

That means two or more filenames can refer to the same file object.

## 5.1 Hard Links

Conceptual model:

```text
directory A
   └── report.txt
            ↓
         inode 672283
            ↓
         data blocks

directory B
   └── archive.txt
            ↓
         inode 672283
            ↓
         same data blocks
```

Key fact:

If two names have the same inode number, they are hard links to the same file.

This is not the same as copying a file.  
A copy creates a new inode and new data blocks.  
A hard link creates a new directory entry pointing to the existing inode.

## 5.2 Practical Hard Link Demonstration

### Step 1: create a file

```bash
echo "Unix Systems Programming" > original.txt
# create a file with content
```

### Step 2: inspect its inode and link count

```bash
ls -li original.txt
# show inode number and link count
```

Example style of output:

```text
672300 -rw-r--r-- 1 student staff 25 original.txt
```

Interpretation:

- inode = 672300
- link count = 1

### Step 3: create a hard link

```bash
ln original.txt alias.txt
# create a second filename pointing to the same inode
```

### Step 4: inspect both names

```bash
ls -li original.txt alias.txt
# both names should show the same inode number
```

Expected pattern:

```text
672300 -rw-r--r-- 2 student staff 25 original.txt
672300 -rw-r--r-- 2 student staff 25 alias.txt
```

Interpretation:

- same inode number
- link count now 2
- both names refer to the same file

### Step 5: modify one name and read through the other

```bash
echo "More content" >> original.txt
# append using first name

cat alias.txt
# read through second name
```

Why this works:

Both filenames refer to the same inode, therefore the same file contents.

### Step 6: compare with copying

```bash
cp original.txt copy.txt
# create an independent copy

ls -li original.txt alias.txt copy.txt
# compare inode numbers
```

Expected interpretation:

- `original.txt` and `alias.txt` share one inode
- `copy.txt` has a different inode

That is the difference between linking and copying.

## 5.3 Removing Links and File Deletion

If you remove one filename:

```bash
rm original.txt
# remove one directory entry
```

the file is not necessarily deleted.

If `alias.txt` still exists, then:

- the inode still exists
- the data blocks still exist
- the link count decreases by one

Practical check:

```bash
ls -li alias.txt
# file still exists because one link remains
```

Only when the hard link count reaches zero can the filesystem reclaim the inode and its data blocks.

Conceptual flow:

```text
2 links
   ↓ rm one name
1 link
   ↓ rm last name
0 links
   ↓
inode and data blocks can be reclaimed
```

## 5.4 Directory Link Counts

Directories have link counts too.

Every directory contains special entries:

```text
.
..
```

Meaning:

- `.` refers to the directory itself
- `..` refers to the parent directory

### Minimum directory links

A directory normally has at least:

- one link from its name in the parent directory
- one link from `.` inside itself

That is why an empty directory typically shows link count 2.

### Subdirectories increase parent link count

Each subdirectory contains a `..` entry that points back to its parent.

Therefore, each subdirectory increases the parent directory’s link count by one.

Conceptual example:

```text
parent/
 ├── .
 ├── child1/
 │    └── ..
 └── child2/
      └── ..
```

For the parent directory, link count reflects:

- its name in its parent directory
- its own `.`
- one additional reference from each child directory via `..`

### Practical example

```bash
mkdir parent
# create parent directory

ls -ld parent
# inspect initial link count
```

Typical interpretation for an empty directory:

```text
drwxr-xr-x 2 student staff ... parent
```

Now create a subdirectory:

```bash
mkdir parent/child
# create one subdirectory
```

Inspect again:

```bash
ls -ld parent
# parent link count should increase
```

Typical interpretation:

```text
drwxr-xr-x 3 student staff ... parent
```

Why 3:

```text
1 → parent entry in its own parent directory
1 → .
1 → child/.. pointing back to parent
```

Practical check of the child directory:

```bash
ls -ld parent/child
# inspect child directory link count
```

The child itself usually starts with link count 2 because it has:

- its name in `parent`
- its own `.` entry

---

# 6. Symbolic Links (Soft Links)

## 6.1 Concept and Definition

A **symbolic link** (also called a **soft link**) is a special file whose content is a **pathname pointing to another file**.

Unlike a hard link, a symbolic link does **not refer directly to the target file’s inode**. Instead, it stores the **path of the target file**. When the symbolic link is accessed, the kernel follows the stored path and resolves the actual file.

Conceptual structure:

```text
symbolic link file
        ↓
stored path string
        ↓
target file
        ↓
target inode
        ↓
data blocks
```

Key idea:

```text
hard link      → inode directly
symbolic link  → pathname → inode
```

## 6.2 Creating Symbolic Links

Symbolic links are created with the `-s` option of the `ln` command.

```bash
ln -s target_file link_name
```

Example:

```bash
ln -s report.txt report_link.txt
# create a symbolic link pointing to report.txt
```

After this command:

- `report_link.txt` is a symbolic link
- its content is the path `report.txt`

## 6.3 Inspecting Symbolic Links

To inspect a symbolic link, use:

```bash
ls -l
```

Example output:

```text
lrwxrwxrwx 1 student staff 10 report_link.txt -> report.txt
```

Interpretation:

```text
l   → indicates a symbolic link
->  → shows the target path
```

To view inode numbers:

```bash
ls -li report.txt report_link.txt
```

Example pattern:

```text
672300 -rw-r--r-- 1 student staff 25 report.txt
672450 lrwxrwxrwx 1 student staff 10 report_link.txt -> report.txt
```

Notice:

- the symbolic link has **its own inode**
- it does **not share the inode** of the target file

## 6.4 Broken Symbolic Links

If the target file is removed, the symbolic link becomes **dangling (broken)**.

Example:

```bash
rm report.txt
# delete the target file

cat report_link.txt
```

Result:

```text
No such file or directory
```

Explanation:

The symbolic link still exists, but the path it references no longer resolves to a valid file.

Conceptual situation:

```text
symbolic link
      ↓
stored path → report.txt
      ↓
target missing
```

## 6.5 Hard Links vs Symbolic Links

| Feature | Hard Link | Symbolic Link |
|-------|-----------|---------------|
| References inode directly | Yes | No |
| References pathname | No | Yes |
| Same inode as target | Yes | No |
| Works across filesystems | No | Yes |
| Works for directories | Usually No | Yes |
| Breaks if target removed | No | Yes |

Summary:

```text
hard link:
filename → inode → data

symbolic link:
filename → path → inode → data
```

---

**End of Week 6**
