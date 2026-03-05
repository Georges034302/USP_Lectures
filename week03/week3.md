
# Week 3 — Text Processing and Bash Scripting

## Table of Contents
1. [Week 3 Overview](#1-week-3-overview)  
2. [Dataset Used in Examples](#2-dataset-used-in-examples)  
3. [Working with Text Streams (Core Commands)](#3-working-with-text-streams-core-commands)  
   3.1 [`cat` — Display File Content](#31-cat--display-file-content)  
   3.2 [`less` — Interactive File Viewer](#32-less--interactive-file-viewer)  
   3.3 [`more` — Basic Pager](#33-more--basic-pager)  
   3.4 [`head` — Display Beginning of File](#34-head--display-beginning-of-file)  
   3.5 [`tail` — Display End of File](#35-tail--display-end-of-file)  
   3.6 [`sort` — Sort Lines of Text](#36-sort--sort-lines-of-text)  
   3.7 [`wc` — Word, Line, and Character Count](#37-wc--word-line-and-character-count)  
   3.8 [`echo` — Print Text Output](#38-echo--print-text-output)  
   3.9 [`read` — Read User Input](#39-read--read-user-input)  
4. [Combining Commands in Bash](#4-combining-commands-in-bash)  
   4.1 [Command Chaining](#41-command-chaining)  
   4.2 [Conditional Chaining](#42-conditional-chaining)  
   4.3 [Command Substitution](#43-command-substitution)  
   4.4 [Command Alias](#44-command-alias)  
5. [Shell Variables](#5-shell-variables)  
6. [Environment Variables](#6-environment-variables)  
7. [The PATH Environment Variable](#7-the-path-environment-variable)  
8. [Shell Configuration Files](#8-shell-configuration-files)  
9. [Conditional Statements](#9-conditional-statements)  
10. [Bash Scripting](#10-bash-scripting)  
11. [Script Examples](#11-script-examples)  

---

# 1. Week 3 Overview

Week 3 introduces **text processing commands and Bash scripting basics**.  
Unix commands are designed to work together through text streams, allowing powerful data manipulation and automation.

By the end of this week you should be able to:

- Inspect and process text files using Unix tools.
- Combine commands into workflows.
- Use shell variables and environment variables.
- Configure the shell environment using `.bashrc`.
- Write simple Bash scripts.

---

# 2. Dataset Used in Examples

All examples use the dataset **cities.txt** that exists in the repository.

Example usage:

```bash
cat cities.txt
sort cities.txt
wc cities.txt
```

The dataset contains:

- duplicated cities
- mixed uppercase and lowercase text
- multiple Australian cities

This makes it useful for demonstrating sorting, counting, and text analysis.

---

# 3. Working with Text Streams (Core Commands)

Unix utilities typically follow the pattern:

```
File → Command → Output
```

Commands read **text input**, process it, and produce **text output**.

---

## 3.1 `cat` — Display File Content

### Definition

`cat` (concatenate) reads one or more files and prints their contents to standard output.

It is commonly used to:

- quickly inspect file contents
- combine multiple files
- pass file contents into other commands

### Usage

```bash
cat filename
```

Multiple files:

```bash
cat file1 file2
```

### Common Options

| Option | Meaning |
|---|---|
| `-n` | number all lines |
| `-b` | number non-empty lines |
| `-s` | squeeze repeated blank lines |

### Examples

Display cities dataset:

```bash
cat cities.txt
```

Number lines:

```bash
cat -n cities.txt
```

Combine files:

```bash
cat cities.txt cities.txt
```

---

## 3.2 `less` — Interactive File Viewer

### Definition

`less` is an interactive pager that allows scrolling through files forward and backward.

Unlike `cat`, it is suitable for **large files**.

### Usage

```bash
less filename
```

### Controls

| Key | Action |
|---|---|
| Space | next page |
| b | previous page |
| /pattern | search |
| q | quit |

Example:

```bash
less cities.txt
```

---

## 3.3 `more` — Basic Pager

### Definition

`more` displays file contents one screen at a time.

It is an older pager compared to `less`.

### Usage

```bash
more filename
```

Example:

```bash
more cities.txt
```

---

## 3.4 `head` — Display Beginning of File

### Definition

`head` prints the first lines of a file.

### Usage

```bash
head filename
```

### Options

| Option | Meaning |
|---|---|
| `-n` | specify number of lines |

### Examples

First lines:

```bash
head cities.txt
```

First five lines:

```bash
head -n 5 cities.txt
```

---

## 3.5 `tail` — Display End of File

### Definition

`tail` prints the last lines of a file.

### Usage

```bash
tail filename
```

### Options

| Option | Meaning |
|---|---|
| `-n` | specify number of lines |
| `-f` | follow file updates |

### Examples

Last lines:

```bash
tail cities.txt
```

Follow log file:

```bash
tail -f logfile.txt
```

---

## 3.6 `sort` — Sort Lines of Text

### Definition

`sort` reads lines of text and outputs them in sorted order.

### Usage

```bash
sort filename
```

### Options

| Option | Meaning |
|---|---|
| `-r` | reverse order |
| `-u` | unique lines |
| `-f` | ignore case |

### Examples

Sort cities:

```bash
sort cities.txt
```

Reverse order:

```bash
sort -r cities.txt
```

Unique cities:

```bash
sort -u cities.txt
```

Ignore case:

```bash
sort -f cities.txt
```

---

## 3.7 `wc` — Word, Line, and Character Count

### Definition

`wc` counts lines, words, and characters.

### Usage

```bash
wc filename
```

### Options

| Option | Meaning |
|---|---|
| `-l` | line count |
| `-w` | word count |
| `-c` | character count |

### Examples

Count lines:

```bash
wc -l cities.txt
```

Count words:

```bash
wc -w cities.txt
```

Count characters:

```bash
wc -c cities.txt
```

---

## 3.8 `echo` — Print Text Output

### Definition

`echo` prints text to standard output.

### Usage

```bash
echo text
```

### Options

| Option | Meaning |
|---|---|
| `-e` | interpret escape characters |
| `-n` | suppresses the newline character |

### Examples

```bash
echo Hello
```

New line example:

```bash
echo -e "Line1\nLine2\nLine3"
```

---

## 3.9 `read` — Read User Input

### Definition

`read` reads user input and stores it in a variable.

### Usage

```bash
read VARIABLE
```

### Example

```bash
echo -n "Enter a city: "
read CITY
echo $CITY
```

Example interaction:

```
Input: Sydney
Output: Sydney
```

---

# 4. Combining Commands in Bash

## 4.1 Command Chaining

Run multiple commands sequentially.

```bash
echo Hello; echo Goodbye
```

---

## 4.2 Conditional Chaining

Run next command if previous succeeds:

```bash
mkdir test && cd test
```

Run next command if previous fails:

```bash
mkdir test || echo "Directory exists"
```

---

## 4.3 Command Substitution

Use output of a command inside another command.

```bash
echo "User: $(whoami)"
```

---

## 4.4 Command Alias

Create shortcuts.

```bash
alias ll='ls -la'
```

---

# 5. Shell Variables

Create variable:

```bash
CITY=Sydney
```

Use variable:

```bash
echo $CITY
```

Remove variable:

```bash
unset CITY
```

---

# 6. Environment Variables

Display environment variables:

```bash
env
```

Example:

```bash
echo $HOME
```

---

# 7. The PATH Environment Variable

`PATH` determines where the system searches for commands.

```bash
echo $PATH
```

Add directory:

```bash
PATH=$PATH:$HOME/bin
```

---

# 8. Shell Configuration Files

Common configuration files:

| File | Purpose |
|---|---|
| `.bashrc` | interactive shell settings |
| `.profile` | login shell configuration |
| `.bash_logout` | executed on logout |

Add alias to `.bashrc`:

```bash
alias ll='ls -la'
```

Reload configuration:

```bash
source ~/.bashrc
```

---

# 9. Conditional Statements

Conditional statements allow scripts to make decisions.

The most common conditional statement in Bash is **if–else**.

## if Statement

```bash
if [ condition ]
then
   command
fi
```

## if–else Statement

```bash
if [ condition ]
then
   command1
else
   command2
fi
```

### Example

```bash
NUMBER=10

if [ $NUMBER -gt 5 ]
then
   echo "Number is greater than 5"
else
   echo "Number is 5 or less"
fi
```

### Explanation of `[ condition ]`

`[ ]` is a **test command** used to evaluate expressions.

Examples:

```bash
[ 5 -gt 3 ]                →  test 5 -gt 3
[ "$CITY" = "Sydney" ]     →  test "$CITY" = "Sydney"
[ -f file.txt ]            →  test -f file.txt
```

Common comparison operators:

| Operator | Meaning |
|---|---|
| `=` | strings are equal (POSIX `[ ]`) |
| `==` | strings are equal (Bash `[[ ]]`) |
| `!=` | strings are not equal |
| `-gt` | greater than (numbers) |
| `-lt` | less than (numbers) |
| `-ge` | greater than or equal (numbers) |
| `-le` | less than or equal (numbers) |
| `-eq` | equal (numbers) |
| `-ne` | not equal (numbers) |
| `>` | greater than (strings) |
| `<` | less than (strings) |
| `-f` | file exists |
| `-d` | directory exists |

**POSIX:** a Unix standard that defines portable shell behavior so scripts run consistently across different Unix systems.

---

# 10. Bash Scripting

A Bash script is a file containing commands executed by the shell.

Example script:

```bash
#!/usr/bin/env bash
echo Hello
```

Make executable:

```bash
chmod +x script.sh
```

Run:

```bash
./script.sh
```

---

# 11. Script Examples

### Script with Arguments (short + useful): `preview_cities.sh`

Shows first N cities (default 10) and then prints total line count.

```bash
#!/usr/bin/env bash

N=${1:-10}   # If $1 not provided, default to 10

echo "First $N lines from cities.txt"
head -n "$N" cities.txt

echo
echo "Total lines:"
wc -l cities.txt
```

Run:

```bash
./preview_cities.sh
./preview_cities.sh 5
```

---

### Script with Conditional: `check_capital.sh`

```bash
#!/usr/bin/env bash

read -p "Enter city: " CITY

if [ "$CITY" = "Canberra" ]
then
   echo "Capital city"
else
   echo "Other city"
fi
```

Run:

```bash
./check_capital.sh
Enter city: Sydney
Other city
```

---

### Script with User Input and conditional select: `slice_cities.sh`

User selects h or t, then enters N.

```bash
#!/usr/bin/env bash

echo -n "Head or Tail? (h/t): "
read MODE

echo -n "How many lines? "
read N

[ "$MODE" = "h" ] && head -n "$N" cities.txt
[ "$MODE" = "t" ] && tail -n "$N" cities.txt
```

Run:

```bash
./slice_cities.sh
```

---

**End of Week 3**
