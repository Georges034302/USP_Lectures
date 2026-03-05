
# USP Lectures

Unix Systems Programming lecture materials and demos.

This repository contains **lecture notes, examples, and scripts** used in the subject **32547 – Unix Systems Programming**.

The material introduces Unix fundamentals, command-line tools, file systems, and Bash scripting.

---

# Lecture Structure

## Week 01 — Introduction to Unix Systems Programming

Topics covered:

- Overview of Unix Systems Programming
- Operating system fundamentals
- Unix architecture (Kernel, Shell, CLI vs GUI)
- Linux and Unix environments
- Basic command-line navigation

Commands introduced:

- `man`
- `pwd`
- `mkdir`
- `cd`
- `rmdir`

---

## Week 02 — Filesystem and File Control

Topics covered:

- Unix filesystem structure
- Absolute vs relative paths
- File permissions model
- Ownership and groups
- Managing files and directories

Commands introduced:

- `touch`
- `ls`
- `cp`
- `mv`
- `find`
- `rm`
- `tar`
- `gzip`

Concepts:

- File permissions
- Ownership
- Globbing patterns

---

## Week 03 — Text Processing and Bash Scripting

Topics covered:

- Processing text files with Unix tools
- Viewing and inspecting files
- Combining commands in Bash
- Shell variables and environment variables
- Conditional statements
- Writing simple Bash scripts

Commands introduced:

- `cat`
- `less`
- `more`
- `head`
- `tail`
- `sort`
- `wc`
- `echo`
- `read`

Concepts:

- Command chaining
- Command substitution
- Shell aliases
- PATH environment variable
- Bash scripting basics

Scripts included:

- `preview_cities.sh`
- `check_capital.sh`
- `slice_cities.sh`

---

# Repository Structure

```
USP_Lectures/
│
├── week1.md
├── week2.md
├── week3.md
│
├── datasets/
│   └── cities.txt
│
└── scripts/
    ├── preview_cities.sh
    ├── check_capital.sh
    └── slice_cities.sh
```

---

# Requirements

To run the examples you need:

- Linux / macOS terminal or WSL
- Bash shell
- Basic Unix utilities installed (standard on Unix systems)

---

# Subject

**32547 – Unix Systems Programming**
