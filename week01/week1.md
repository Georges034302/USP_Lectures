# Week 1 — Introduction to Unix Systems Programming

## Table of Contents
1. [Week 1 Overview](#1-week-1-overview)  
2. [Core Concepts](#2-core-concepts)  
   2.1 [Systems Programming and Operating System Foundations](#21-systems-programming-and-operating-system-foundations)  
   2.2 [Unix Architecture: Kernel, Shell, and Interfaces (CLI vs GUI)](#22-unix-architecture-kernel-shell-and-interfaces-cli-vs-gui)  
   2.3 [Evolution of Unix and Its Variants](#23-evolution-of-unix-and-its-variants)  
   2.4 [Linux as the Modern Unix Standard (Servers, Cloud, AI)](#24-linux-as-the-modern-unix-standard-servers-cloud-ai)  
   2.5 [Linux Distributions, Virtualization, and Access Methods](#25-linux-distributions-virtualization-and-access-methods)  
3. [Starter Unix Commands](#3-starter-unix-commands)  
   3.1 [`man` — Manual Pages](#31-man--manual-pages)  
   3.2 [`pwd` — Print Working Directory](#32-pwd--print-working-directory)  
   3.3 [`mkdir` — Make Directory](#33-mkdir--make-directory)  
   3.4 [`cd` — Change Directory](#34-cd--change-directory)  
   3.5 [`rmdir` — Remove Directory](#35-rmdir--remove-directory)  

---

## 1. Week 1 Overview

By the end of Week 1, you should be able to:
- Explain what *systems programming* means (and how it differs from application programming).
- Describe Unix’s layered architecture (hardware → kernel → shell → user interfaces).
- Explain why Unix/Linux dominates modern servers, cloud platforms, and AI environments.
- Navigate the filesystem and manage directories using a small set of essential commands.

---

## 2. Core Concepts

### 2.1 Systems Programming and Operating System Foundations

An **operating system (OS)** is the foundational software that makes a computer usable. It:
- **Controls hardware** (CPU scheduling, memory management, device I/O).
- **Provides services** to programs (files, processes, networking, security).
- **Creates abstractions** so software doesn’t need to handle raw hardware details.

**Systems programming** focuses on software that is *aware of OS features* and uses them deliberately. Typical concerns include:
- **Processes and concurrency** (how programs start, run, communicate, and terminate).
- **File and directory management** (permissions, paths, file descriptors, I/O).
- **Resource control** (CPU, memory, storage, sockets).
- **Security and access control** (users, groups, privileges).

In contrast, **application programming** usually assumes the OS “just works” and does not require deep awareness of OS mechanisms.

---

### 2.2 Unix Architecture: Kernel, Shell, and Interfaces (CLI vs GUI)

Unix is often described using a layered (“onion”) model:

- **Hardware / Devices**: physical components (CPU, disk, network, peripherals).
- **Kernel**: the OS core that manages hardware and provides system services.
- **Shell (CLI / interpreter)**: a program that accepts user commands and runs them.
- **GUI (optional)**: graphical desktop environments layered above the OS.

**Kernel (core idea):**
- Runs with high privileges.
- Manages processes, memory, filesystems, devices, and networking.
- Exposes system services via system calls (the interface that programs rely on).

**Shell (core idea):**
- A command interpreter (e.g., `sh`, `bash`, `zsh`).
- Lets you run programs, combine tools, automate tasks, and write scripts.

**CLI vs GUI (core idea):**
- **GUI** is convenient for one-off, visual tasks (clicking, dragging, browsing).
- **CLI** is powerful for repeated work, automation, remote administration, and reproducible workflows.
- In DevOps and cloud operations, CLI usage becomes essential because automation and scripting are non-negotiable.

---

### 2.3 Evolution of Unix and Its Variants

Unix is not a single “mono-brand” OS. Over time:
- Multiple **Unix families and variants** emerged (commercial and community-driven).
- Many different **shells** were created (`sh`, `csh`, `ksh`, `bash`, `zsh`, etc.).
- Even when the command name is the same, behavior can differ between systems or shells.

To reduce fragmentation, standards exist (e.g., the **Single UNIX Specification**), but real-world differences still appear—especially across older Unix systems and modern Linux environments.

Key takeaway for this subject:
- You focus on concepts that transfer across systems.
- You also learn to confirm behavior using documentation (`man`) and experimentation.

---

### 2.4 Linux as the Modern Unix Standard (Servers, Cloud, AI)

Linux has become the practical standard Unix-like environment because it is:
- **Free** to use and widely available.
- **Open source**, enabling rapid fixes and community improvements.
- **Highly portable**, running on servers, desktops, embedded devices, and cloud infrastructure.

This is why Linux dominates:
- **Servers and cloud** (most production workloads run on Linux).
- **DevOps tooling** (CI/CD runners, containers, Kubernetes nodes).
- **AI/ML platforms** (common base OS for GPU-enabled training and inference stacks).

In other words: learning Unix/Linux CLI skills is not “optional”—it’s foundational for modern software engineering and cloud operations.

---

### 2.5 Linux Distributions, Virtualization, and Access Methods

Linux is built around the **Linux kernel**, but what you use day-to-day is usually a **distribution (distro)**:
- A distro packages the kernel with system tools, libraries, package managers, and (optionally) a desktop environment.
- Examples: Debian-based (Ubuntu), Red Hat-based (Fedora), and many others.

To run Linux, you commonly use:
- **Remote Linux environments** (e.g., university servers).
- **Online terminal environments** (browser-based shells; limited persistence).
- **Virtual machines (VMs)** on your own computer (Linux as a guest OS).
- Later in the course context: **containers** (lightweight runtime environments).

The key idea is that you should be able to operate Linux regardless of where it runs—local VM, remote server, or cloud-hosted environment.

---

## 3. Starter Unix Commands

This section introduces foundational commands used to navigate and manage directories.

### 3.1 `man` — Manual Pages

**Purpose:** View official documentation for a command.

**Basic syntax:**
```bash
man command_name
```

**Examples:**
```bash
man ls
```
Shows the manual page for `ls` (options, usage, notes).

```bash
man mkdir
```
Shows how `mkdir` behaves and what flags are available.

```bash
man man
```
Shows documentation about the manual system itself.

**Inside `man`:**
- Search: type `/keyword` then press Enter
- Next match: `n`
- Quit: `q`

---

### 3.2 `pwd` — Print Working Directory

**Purpose:** Show your current directory as an **absolute path**.

**Syntax:**
```bash
pwd
```

**Examples:**
```bash
pwd
```
Example output:
```bash
/home/student
```

```bash
cd /etc
pwd
```
Example output:
```bash
/etc
```

---

### 3.3 `mkdir` — Make Directory

**Purpose:** Create directories.

**Syntax:**
```bash
mkdir name
```

**Examples:**
```bash
mkdir project
```
Creates a directory called `project`.

```bash
mkdir week1 week2 week3
```
Creates multiple directories in one command.

```bash
mkdir -p parent/child/grandchild
```
Creates nested directories; `-p` creates missing parents.

**Brace expansion (sequence creation):**
```bash
mkdir dir{1..5}
```
Creates: `dir1 dir2 dir3 dir4 dir5`

```bash
mkdir week{1..10}
```
Creates: `week1` through `week10`

```bash
mkdir lab{A..D}
```
Creates: `labA labB labC labD`

**Note:** `{m..n}` is performed by **Bash** (shell expansion), not by `mkdir` itself.

---

### 3.4 `cd` — Change Directory

**Purpose:** Move between directories (change the shell’s working context).

**Syntax:**
```bash
cd path
```

#### Absolute vs Relative Paths

**Absolute path**
- Starts at the root `/`
- Does not depend on where you currently are

Example:
```bash
cd /var/log
```

**Relative path**
- Depends on your current directory
- Does not start with `/`

Example (from `/home/student`):
```bash
cd project
```
Moves to `/home/student/project`

#### Multi-level browsing examples

Move up:
```bash
cd ..
```
Up one level.

```bash
cd ../..
```
Up two levels.

Move down multiple levels:
```bash
cd parent/child/grandchild
```

Shortcuts:
```bash
cd ~
```
Go to home directory.

```bash
cd -
```
Go back to the previous directory.

Core symbols:
- `.` current directory
- `..` parent directory
- `/` filesystem root

---

### 3.5 `rmdir` — Remove Directory

**Purpose:** Remove **empty** directories only.

**Syntax:**
```bash
rmdir name
```

**Examples:**
```bash
rmdir project
```
Removes `project` if it is empty.

```bash
rmdir week1 week2
```
Removes multiple empty directories.

```bash
rmdir parent/child
```
Removes `child` if it is empty.

**Important rule:** If a directory contains files/subdirectories, `rmdir` will fail.  
(Recursive removal using `rm -r` is covered later.)

---

**End of Week 1**
