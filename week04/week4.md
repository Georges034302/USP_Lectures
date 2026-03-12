
# Week 4 — Piping, Redirection, and Shell Control Structures

## Table of Contents
1. [Piping](#1-piping)  
2. [Redirection](#2-redirection)  
3. [Special Shell Parameters](#3-special-shell-parameters)  
4. [Unix Text Processing Filters](#4-unix-text-processing-filters)  
   4.1 [`cut`](#41-cut)  
   4.2 [`awk`](#42-awk)  
   4.3 [`uniq`](#43-uniq)  
   4.4 [`join`](#44-join)  
   4.5 [`split`](#45-split)  
   4.6 [`paste`](#46-paste)  
   4.7 [`tr`](#47-tr)  
   4.8 [`pr`](#48-pr)  
   4.9 [`diff`](#49-diff)  
5. [Loops and Control Structures](#5-loops-and-control-structures)  
   5.1 [`for`](#51-for-loop)  
   5.2 [`while`](#52-while-loop)  
   5.3 [`select + case + PS1`](#53-select--case--ps1)  

Datasets used in examples (must exist in the repo):

- `animals.txt`
- `list.txt`

---

# 1. Piping

## Definition
A **pipe** redirects the **standard output (stdout)** of one command into the **standard input (stdin)** of another command.

Pipe operator:

```
|
```

A **pipeline** is one or more commands separated by `|`.

## Usage

```bash
command1 | command2 | command3
```

## Examples

```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq
# convert all names to lowercase, sort them, then remove duplicates
```

```bash
cat animals.txt | wc -l
# count the total number of lines in animals.txt
```

```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq | wc -l
# count how many unique animal names exist
```

```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq -c
# count occurrences of each animal name
```

```bash
ls -l | head -4 | tail -1
# extract the third line from an ls listing
```

---

# 2. Redirection

## Definition
Redirection changes where a command reads input from or writes output to.

| Stream | FD | Default |
|---|---|---|
| STDIN | 0 | keyboard |
| STDOUT | 1 | terminal |
| STDERR | 2 | terminal |

## Examples

```bash
ls -l > out.txt
# write output to a file (overwrite)
```

```bash
ls -l >> out.txt
# append output to a file
```

```bash
> out.txt
# create or empty a file quickly
```

```bash
wc -l < animals.txt
# count lines using input redirection
```

```bash
ls missing_file 2> errors.txt
# redirect only error messages to a file
```

```bash
ls animals.txt missing_file > all.txt 2>&1
# redirect stdout and stderr to the same file
```

```bash
ls missing_file 2> /dev/null
# discard error output
```

---

# 3. Special Shell Parameters

| Parameter | Meaning |
|---|---|
| `$0` | script name |
| `$1..$9` | positional arguments |
| `$#` | number of arguments |
| `$*` | all arguments as one string |
| `$@` | all arguments individually |
| `$?` | exit status of last command |
| `$$` | process ID |

Example:

```bash
#!/usr/bin/env bash

echo "$0"   # print script name
echo "$#"   # print number of arguments
echo "$*"   # print arguments as a single string
echo "$@"   # print arguments individually
echo "$$"   # print process id of script
echo "$?"   # print exit status of previous command
```

---

# 4. Unix Text Processing Filters

Filters read from **stdin**, process the text, and write to **stdout**.

---

# 4.1 cut

```bash
cut -c1-10 list.txt
# extract the first 10 characters of each line
```

```bash
cut -c1-10,20-30 list.txt
# extract two character ranges from each line
```

```bash
cut -d' ' -f9 list.txt
# extract the 9th field (filename column)
```

```bash
tr -s ' ' < list.txt | cut -d' ' -f5,9
# normalize spaces then extract size and filename fields
```

---

# 4.2 awk

```bash
awk '{print $9}' list.txt
# print filename column
```

```bash
awk '{print $1, $9}' list.txt
# print permissions and filename
```

```bash
awk '{print NR, $9}' list.txt
# print line number and filename
```

```bash
awk '{sum += $5} END {print sum}' list.txt
# sum all file sizes
```

---

# 4.3 uniq

```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq
# show unique animal names ignoring case
```

```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq -c
# show counts of each animal
```

```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq -d
# show only duplicated animals
```

---

# 4.4 join

```bash
join -1 1 -2 1 file1_sorted.txt file2_sorted.txt
# join two sorted files using the first column as key
```

---

# 4.5 split

```bash
split -l 5 animals.txt chunk_
# split animals.txt into files of 5 lines each
```

```bash
cat chunk_* > animals_joined.txt
# reconstruct the original file by concatenating chunks
```

---

# 4.6 paste

Examples using files produced by `split`.

```bash
paste chunk_aa chunk_ab
# merge two chunk files side by side
```

```bash
paste -d ':' chunk_aa chunk_ab
# merge files using ':' as delimiter
```

```bash
paste -d ',' chunk_aa chunk_ab
# merge files using comma delimiter
```

---

# 4.7 tr

```bash
cat animals.txt | tr 'A-Z' 'a-z'
# convert uppercase letters to lowercase
```

```bash
cat animals.txt | tr 'a-z' 'A-Z'
# convert lowercase letters to uppercase
```

```bash
cat animals.txt | tr -d 'aeiouAEIOU'
# delete all vowels from the input
```

```bash
tr -s ' ' < list.txt
# squeeze repeated spaces into one space
```

```bash
cat animals.txt | tr ' ' '_'
# replace spaces with underscores
```

```bash
cat animals.txt | tr -cd 'a-zA-Z\n'
# remove all characters except letters and newline
```

---

# 4.8 pr

```bash
pr -n animals.txt
# print file with numbered lines
```

```bash
pr -h "Animals Report" animals.txt
# print file with a header title
```

```bash
pr -2 animals.txt
# print output in two columns
```

```bash
pr -t animals.txt
# print file without page headers or formatting
```

---

# 4.9 diff

## Definition

`diff` compares two files and shows the differences between them.

## Examples

```bash
diff file1.txt file2.txt
# show differences between two files
```

```bash
diff -u file1.txt file2.txt
# show unified diff format (used in patches and git)
```

```bash
diff animals.txt animals_joined.txt
# compare original file and reconstructed file
```

---

# 5. Loops and Control Structures

---

# 5.1 for Loop

```bash
for a in $(cat animals.txt)
do
  echo "$a"
done
# print each word from animals.txt
```

```bash
for a in $(cat animals.txt | tr 'A-Z' 'a-z')
do
  echo "$a"
done | sort | uniq -c
# generate a frequency report of animals
```

---

# 5.2 while Loop

```bash
n=1
while [ $n -le 5 ]
do
  echo $n
  n=$((n + 1))
done
# count from 1 to 5
```

```bash
while IFS= read -r line
do
  echo "LINE: $line"
done < animals.txt
# read file line by line safely
```

---

# 5.3 select + case + PS1

```bash
select action in "List unique" "Count occurrences" "Quit"
do
  case "$action" in
    "List unique")
      cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq
      ;;
    "Count occurrences")
      cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq -c
      ;;
    "Quit")
      break
      ;;
    *)
      echo "Invalid option"
      ;;
  esac
done
# simple interactive menu
