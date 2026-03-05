
# Week 4 — Piping, Redirection, and Shell Control Structures

## Table of Contents
1. [Piping](#1-piping)  
2. [Redirection](#2-redirection)  
3. [Special Shell Parameters](#3-special-shell-parameters)  
4. [Unix Text Processing Filters](#4-unix-text-processing-filters)  
5. [Loops and Control Structures](#5-loops-and-control-structures)  

Datasets used in examples:

- `animals.txt`
- `list.txt`

These files must exist in the repository and are used in command examples.

---

# 1. Piping

## Definition

Piping connects the **standard output of one command** to the **standard input of another command**.

The pipe operator is:

```
|
```

Commands used in pipelines behave like **filters**, receiving input, processing it, and producing output.

## Usage

```
command1 | command2
```

## Examples

Count number of lines:

```bash
cat animals.txt | wc -l
```

Sort animals:

```bash
cat animals.txt | sort
```

Count unique animals:

```bash
cat animals.txt | sort | uniq | wc -l
```

Display first three sorted animals:

```bash
cat animals.txt | sort | head -3
```

Each command in the pipeline runs as a **separate process**.

---

# 2. Redirection

## Definition

Redirection changes where a command **reads input from** or **writes output to**.

Unix commands use three standard streams:

| Stream | Descriptor | Default |
|---|---|---|
STDIN | 0 | keyboard |
STDOUT | 1 | terminal |
STDERR | 2 | terminal |

## Output Redirection

Redirect output to file:

```bash
ls > files.txt
```

Overwrite existing file.

Append output:

```bash
ls >> files.txt
```

## Input Redirection

Provide input from a file:

```bash
wc -l < animals.txt
```

Difference:

```bash
wc -l animals.txt
wc -l < animals.txt
```

The first prints filename; the second does not.

## Error Redirection

Redirect error messages:

```bash
ls missingfile 2> errors.txt
```

Redirect output and errors together:

```bash
ls animals.txt missing.txt > out.txt 2>&1
```

## Explicit File Descriptors

```
1>   redirect stdout
2>   redirect stderr
0<   redirect stdin
```

Example:

```bash
ls 1> output.txt
```

---

# 3. Special Shell Parameters

Special parameters are automatically set by the shell.

| Parameter | Meaning |
|---|---|
$0 | script name |
$1..$9 | positional parameters |
$# | number of arguments |
$* | all arguments |
$@ | all arguments separately |
$? | exit status of last command |
$$ | process ID of shell |

## Example Script

```bash
#!/usr/bin/env bash

echo $*
echo $2
echo $#
echo $$
echo $0

exit 5
```

Run:

```bash
./script.sh alpha 100
```

Check exit status:

```bash
echo $?
```

Exit status **0 means success**.

---

# 4. Unix Text Processing Filters

## cut

### Definition

Extract columns from input.

### Usage

```
cut -c LIST
cut -d DELIMITER -f FIELD
```

### Examples

Display first 10 characters:

```bash
cut -c1-10 list.txt
```

Extract file names:

```bash
cut -d' ' -f9 list.txt
```

---

## awk

### Definition

A pattern scanning and processing language.

### Usage

```
awk 'pattern { action }'
```

### Examples

Print filenames column:

```bash
awk '{print $9}' list.txt
```

Print first field:

```bash
awk '{print $1}' list.txt
```

---

## uniq

Removes duplicate lines from sorted input.

```bash
sort animals.txt | uniq
```

Count duplicates:

```bash
sort animals.txt | uniq -c
```

---

## join

Join two files by common field.

```bash
join file1.txt file2.txt
```

---

## paste

Merge files line-by-line.

```bash
paste file1.txt file2.txt
```

---

## split

Split large file into smaller files.

```bash
split -l 5 animals.txt
```

---

## tr

Translate characters.

Convert to lowercase:

```bash
cat animals.txt | tr 'A-Z' 'a-z'
```

Delete characters:

```bash
cat animals.txt | tr -d 'a'
```

---

## pr

Format text for printing.

```bash
pr animals.txt
```

Add line numbers:

```bash
pr -n animals.txt
```

---

# 5. Loops and Control Structures

## for Loop

Iterates over list of values.

```bash
for animal in $(cat animals.txt)
do
    echo $animal
done
```

---

## foreach style loop

Loop through fixed list.

```bash
for x in dog cat lion tiger
do
    echo $x
done
```

---

## while Loop

Runs while condition is true.

```bash
count=1

while [ $count -le 5 ]
do
    echo $count
    count=$((count+1))
done
```

---

## select

Creates menu selection.

```bash
select animal in dog cat lion tiger
do
    echo "You selected $animal"
    break
done
```

---

## case Statement

Used for multiple conditions.

```bash
read animal

case $animal in
dog)
    echo "Dog selected"
    ;;
cat)
    echo "Cat selected"
    ;;
*)
    echo "Unknown animal"
    ;;
esac
```

---

## PS1 Prompt

PS1 controls the shell prompt.

Example:

```bash
PS1="USP> "
```

Custom prompt example:

```bash
PS1="\u@\h:\w$ "
```

---

**End of Week 4**
