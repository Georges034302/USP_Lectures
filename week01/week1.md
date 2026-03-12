# Week 1 — Introduction to Unix Systems Programming

## Table of Contents
1. [Week 1 Overview](#1-week-1-overview)  
2. [Core Concepts](#2-core-concepts)  
   2.1 [Systems Programming and Operating System Foundations](#21-systems-programming-and-operating-system-foundations)  
   2.2 [Unix Architecture: Kernel, Shell, and Interfaces (CLI vs GUI)](#22-unix-architecture-kernel-shell-and-interfaces-cli-vs-gui)  
   2.3 [Evolution of Unix and Its Variants](#23-evolution-of-unix-and-its-variants)  
   2.4 [Linux as the Modern Unix Standard (Servers, Cloud, AI)](#24-linux-as-the-modern-unix-standard-servers-cloud-ai)  
   2.5 [Linux Distributions, Virtualization, and Access Methods](#25-linux-distributions-virtualization-and-access-methods)  
   2.6 [Command Execution Workflow (Shell → Program → System Calls → Kernel → Hardware)](#26-command-execution-workflow-shell--program--system-calls--kernel--hardware)  
3. [Starter Unix Commands](#3-starter-unix-commands)  
   3.1 [`man` — Manual Pages](#31-man--manual-pages)  
   3.2 [`pwd` — Print Working Directory](#32-pwd--print-working-directory)  
   3.3 [`mkdir` — Make Directory](#33-mkdir--make-directory)  
   3.4 [`cd` — Change Directory](#34-cd--change-directory)  
   3.5 [`rmdir` — Remove Directory](#35-rmdir--remove-directory)  

---

# 1. Week 1 Overview

By the end of Week 1 you should be able to:

- Explain **what systems programming is**
- Describe **Unix layered architecture**
- Explain **how commands execute in Unix**
- Understand **why Linux dominates servers and cloud**
- Use basic **filesystem navigation commands**

---

# 2. Core Concepts

---

## 2.1 Systems Programming and Operating System Foundations

### Definition

An **Operating System (OS)** is the software layer that manages hardware and provides services to programs.

Its main responsibilities:

- CPU scheduling
- Memory management
- File systems
- Device drivers
- Networking
- Security

### Systems Programming

**Systems programming** means writing software that interacts closely with OS services.

Examples include programs that use:

- processes
- file descriptors
- system calls
- sockets
- memory management

### Comparison

| Type | Focus |
|---|---|
| Application Programming | Builds user applications |
| Systems Programming | Uses OS mechanisms directly |

Examples:

- Systems programs → `ls`, `cp`, `ssh`, `docker`
- Applications → web apps, games, editors

---

## 2.2 Unix Architecture: Kernel, Shell, and Interfaces (CLI vs GUI)

Unix uses a **layered architecture**.

### Architecture Diagram

```
+----------------------+
|      User            |
+----------------------+
          ↓
+----------------------+
|   Shell (bash,zsh)   |
|   Command Interpreter|
+----------------------+
          ↓
+----------------------+
|     System Calls     |
+----------------------+
          ↓
+----------------------+
|       Kernel         |
| Process | Memory | IO|
+----------------------+
          ↓
+----------------------+
|       Hardware       |
| CPU Disk Network GPU |
+----------------------+
```

### Kernel

The **kernel** is the core of the OS.

Responsibilities:

- process scheduling
- memory allocation
- device communication
- filesystem management
- networking

### Shell

The **shell** is a command interpreter.

Examples:

- `bash`
- `zsh`
- `sh`
- `fish`

The shell:

- reads commands
- starts programs
- manages environment variables
- supports scripting

### CLI vs GUI

| Interface | Description |
|---|---|
| CLI | text commands |
| GUI | graphical interface |

CLI advantages:

- automation
- remote access
- scripting
- reproducibility

---

## 2.3 Evolution of Unix and Its Variants

Unix began at **Bell Labs (1970s)**.

Over time many variants emerged.

### Unix Family Tree

```
Original Unix
     ↓
 BSD -------- System V
     ↓             ↓
 macOS          Solaris
     ↓
 Linux (Unix-like)
```

Modern Unix environments include:

- Linux
- macOS
- FreeBSD
- Solaris

### Important shells developed

| Shell | Description |
|---|---|
| sh | Bourne shell |
| csh | C shell |
| ksh | Korn shell |
| bash | Bourne again shell |
| zsh | modern extended shell |

---

## 2.4 Linux as the Modern Unix Standard (Servers, Cloud, AI)

Linux dominates modern computing because it is:

- open source
- stable
- scalable
- highly portable

### Where Linux dominates

| Domain | Usage |
|---|---|
| Servers | majority of internet infrastructure |
| Cloud | AWS, Azure, GCP |
| Containers | Docker and Kubernetes |
| AI | GPU training environments |

Example:

Most AI models are trained on **Linux GPU clusters**.

---

## 2.5 Linux Distributions, Virtualization, and Access Methods

### Linux Distribution

A **distribution (distro)** packages:

- Linux kernel
- system libraries
- package manager
- utilities

Examples:

| Distro | Type |
|---|---|
| Ubuntu | Debian-based |
| Debian | stable server distro |
| Fedora | RedHat family |
| Arch | rolling release |

### Running Linux

Common methods:

```
Local machine
    ↓
Virtual Machine
    ↓
Remote SSH server
    ↓
Cloud instance
```

### Example VM tools

- VirtualBox
- VMware
- Multipass
- Docker containers

---

## 2.6 Command Execution Workflow (Shell → Program → System Calls → Kernel → Hardware)

When you type a command:

```
ls
```

The system follows this sequence.

### Execution Flow

```
User
 ↓
Shell (bash)
 ↓
Executable program (/bin/ls)
 ↓
System Calls
 ↓
Kernel
 ↓
Hardware
```

### Step-by-step process

1. User enters command
2. Shell parses command
3. Shell finds executable
4. Program starts as new process
5. Program requests kernel services
6. Kernel interacts with hardware
7. Output returned to terminal

### Example

```bash
ls
# request directory listing
```

Internally:

```
ls
 ↓
open directory
 ↓
read entries
 ↓
send output to terminal
```

### Privilege levels

```
User Mode
  |
  | system calls
  v
Kernel Mode
```

User programs **cannot access hardware directly**.

---

# 3. Starter Unix Commands

---

## 3.1 `man` — Manual Pages

### Definition

`man` displays the **manual page** for a command.

### Syntax

```bash
man command
```

### Common usage

| Command | Meaning |
|---|---|
| man ls | documentation for ls |
| man mkdir | documentation for mkdir |
| man man | manual for man itself |

### Examples

```bash
man ls
# open documentation for ls command
```

```bash
man pwd
# show manual page for pwd
```

Inside `man`:

| Key | Action |
|---|---|
| q | quit |
| /word | search |
| n | next match |

---

## 3.2 `pwd` — Print Working Directory

### Definition

`pwd` prints the **absolute path of the current directory**.

### Syntax

```bash
pwd
```

### Examples

```bash
pwd
# show current directory
```

Example output:

```
/home/student
```

```bash
cd /etc
pwd
# verify the directory change
```

Output:

```
/etc
```

---

## 3.3 `mkdir` — Make Directory

### Definition

`mkdir` creates directories.

### Syntax

```bash
mkdir name
```

### Common options

| Option | Meaning |
|---|---|
| -p | create parent directories if needed |
| -v | verbose output |

### Examples

```bash
mkdir project
# create directory named project
```

```bash
mkdir week1 week2 week3
# create multiple directories
```

```bash
mkdir -p course/week1/lab
# create nested directories
```

```bash
mkdir dir{1..5}
# create dir1 dir2 dir3 dir4 dir5
```

```bash
mkdir lab{A..D}
# create labA labB labC labD
```

---

## 3.4 `cd` — Change Directory

### Definition

`cd` changes the shell's working directory.

### Syntax

```bash
cd path
```

### Path types

| Type | Example |
|---|---|
| Absolute | `/usr/bin` |
| Relative | `documents` |

### Examples

```bash
cd /etc
# move to absolute path
```

```bash
cd project
# move to project directory relative to current location
```

```bash
cd ..
# move up one directory
```

```bash
cd ../..
# move up two directories
```

```bash
cd ~
# go to home directory
```

```bash
cd -
# go to previous directory
```

Symbols:

```
.   current directory
..  parent directory
/   root filesystem
```

---

## 3.5 `rmdir` — Remove Directory

### Definition

`rmdir` removes **empty directories only**.

### Syntax

```bash
rmdir name
```

### Examples

```bash
rmdir project
# remove project directory if empty
```

```bash
rmdir week1 week2
# remove multiple directories
```

```bash
rmdir parent/child
# remove child directory
```

### Important rule

`rmdir` **fails if directory is not empty**.

Example failure:

```bash
rmdir project
# error if project contains files
```

Recursive deletion will be covered later using `rm -r`.

---

**End of Week 1**
