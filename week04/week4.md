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
   4.5 [`paste`](#45-paste)  
   4.6 [`split`](#46-split)  
   4.7 [`tr`](#47-tr)  
   4.8 [`pr`](#48-pr)  
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

## Common patterns (with `animals.txt`)

Normalize case, sort, remove duplicates:
```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq
```

Count total lines:
```bash
cat animals.txt | wc -l
```

Count unique animal names (case-insensitive):
```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq | wc -l
```

Count occurrences (case-insensitive):
```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq -c
```

Pick the 3rd line of a listing (example pattern):
```bash
ls -l | head -4 | tail -1
```

## Notes
- Only **stdout** is piped by default (stderr is not).
- Each command in a pipeline runs as a **separate process**, typically in parallel.

---

# 2. Redirection

## Definition
**Redirection** changes where a command reads input from (stdin) or writes output to (stdout/stderr).

## Standard streams and file descriptors

| Stream | FD | Default |
|---|---:|---|
| STDIN | 0 | keyboard |
| STDOUT | 1 | terminal |
| STDERR | 2 | terminal |

## Output redirection

Overwrite a file:
```bash
ls -l > out.txt
```

Append to a file:
```bash
ls -l >> out.txt
```

Create/empty a file quickly:
```bash
> out.txt
```

## Input redirection

Read stdin from a file:
```bash
wc -l < animals.txt
```

Difference between “argument” vs “redirected stdin”:
```bash
wc -l animals.txt
wc -l < animals.txt
```

## Error redirection

Redirect errors (stderr) only:
```bash
ls missing_file 2> errors.txt
```

Redirect stdout and stderr to the same file:
```bash
ls animals.txt missing_file > all.txt 2>&1
```

## Explicit descriptor forms

These are equivalent to the simpler versions:
```bash
ls -l 1> out.txt
cat 0< animals.txt
ls missing_file 2> errors.txt
```

## Useful redirection combinations

Discard output (send to “null device”):
```bash
ls missing_file 2> /dev/null
```

Keep stdout on screen, send stderr to file:
```bash
ls animals.txt missing_file 2> errors.txt
```

---

# 3. Special Shell Parameters

## Definition
Special parameters are variables provided by the shell to expose script arguments, process info, and status codes.

| Parameter | Meaning |
|---|---|
| `$0` | script name |
| `$1..$9` | positional arguments |
| `$#` | number of arguments |
| `$*` | all arguments as one string |
| `$@` | all arguments as separate strings |
| `$?` | exit status of last command |
| `$$` | process ID of current shell/script |

## Example (use in a script)

```bash
#!/usr/bin/env bash

echo "$0"
echo "$#"
echo "$*"
echo "$@"
echo "$$"
echo "$?"
```

## Exit status
- `0` means **success**
- non-zero means **failure** (or a specific error code)

Example:
```bash
false
echo $?
```

---

# 4. Unix Text Processing Filters

Filters read from **stdin** (or files), transform text, and write to **stdout**.

---

## 4.1 cut

## Definition
`cut` extracts **columns** from each line of input:
- by **character position** (`-c`)
- by **field** (`-f`) with a delimiter (`-d`)

## Usage
```bash
cut -c LIST file
cut -d DELIM -f LIST file
```

## Common options
| Option | Meaning |
|---|---|
| `-c LIST` | select character positions |
| `-d DELIM` | field delimiter |
| `-f LIST` | select fields |
| `--complement` | select everything *except* LIST (GNU) |
| `-s` | suppress lines with no delimiter |

## Examples (with `list.txt`)

First 10 characters:
```bash
cut -c1-10 list.txt
```

Multiple character ranges:
```bash
cut -c1-10,20-30 list.txt
```

Everything from character 11 to end:
```bash
cut -c11- list.txt
```

Extract permissions only (first 10 chars):
```bash
cut -c1-10 list.txt
```

Extract file name (9th field, space-delimited):
```bash
cut -d' ' -f9 list.txt
```

Extract size + filename (5th and 9th fields):
```bash
cut -d' ' -f5,9 list.txt
```

Use a safer pipeline to handle multiple spaces (normalize whitespace first):
```bash
tr -s ' ' < list.txt | cut -d' ' -f5,9
```

Suppress lines without the delimiter (useful on mixed input):
```bash
cut -d' ' -f9 -s list.txt
```

Complement example (GNU systems):
```bash
tr -s ' ' < list.txt | cut -d' ' -f1-8 --complement
```

---

## 4.2 awk

## Definition
`awk` is a text processing language. It reads input line-by-line (records), splits each line into fields, and runs actions.

Field basics:
- `$0` = whole line
- `$1` = first field, `$2` = second field, ...
- `NF` = number of fields in current line
- `NR` = current line number (record number)

## Usage
```bash
awk 'pattern { action }' file
awk -F 'DELIM' 'pattern { action }' file
```

## Common options / features
| Feature | Meaning |
|---|---|
| `-F` | set field separator |
| `BEGIN {}` | run once before reading input |
| `END {}` | run once after reading input |
| `printf` | formatted output |
| `if`, `for`, `while` | control structures |
| associative arrays | counting/grouping |

## Examples (with `list.txt`)

Print file name column:
```bash
awk '{print $9}' list.txt
```

Print permissions + filename:
```bash
awk '{print $1, $9}' list.txt
```

Print line number + filename:
```bash
awk '{print NR, $9}' list.txt
```

Print “size filename” with formatting (`printf`):
```bash
awk '{printf "size=%s file=%s\n", $5, $9}' list.txt
```

Only show executable files (permission starts with `-rwx`):
```bash
awk '$1 ~ /^-rwx/ {print $9}' list.txt
```

Sum file sizes (field 5) and print total:
```bash
awk '{sum += $5} END {print "total_bytes:", sum}' list.txt
```

Show last field using `NF` (works even if field count changes):
```bash
awk '{print $NF}' list.txt
```

Loop example: print all fields with their index (per line):
```bash
awk '{
  for (i = 1; i <= NF; i++) printf "[%d]=%s ", i, $i
  print ""
}' list.txt
```

Count file extensions (simple example):
```bash
awk '{
  n = split($9, a, ".")
  ext = (n > 1) ? a[n] : "(noext)"
  count[ext]++
}
END {
  for (e in count) printf "%s %d\n", e, count[e]
}' list.txt
```

Examples (with `animals.txt`)

Normalize case, then count occurrences using awk:
```bash
cat animals.txt | tr 'A-Z' 'a-z' | awk '{count[$0]++} END {for (a in count) print a, count[a]}'
```

Print only lines that match “lion” (after case normalization):
```bash
cat animals.txt | tr 'A-Z' 'a-z' | awk '$0 == "lion" {print NR, $0}'
```

---

## 4.3 uniq

## Definition
`uniq` removes **adjacent duplicates**. It usually requires sorted input.

## Usage
```bash
sort file | uniq
```

## Common options
| Option | Meaning |
|---|---|
| `-c` | prefix lines by count |
| `-d` | show duplicated lines only |
| `-u` | show unique (non-duplicated) lines only |

## Examples (with `animals.txt`)

Case-insensitive unique list:
```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq
```

Counts:
```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq -c
```

Only duplicates:
```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq -d
```

---

## 4.4 join

## Definition
`join` combines two **sorted** files using a common key field (like a simple SQL join).

## Usage
```bash
join [options] file1 file2
```

## Common options
| Option | Meaning |
|---|---|
| `-1 N` | join field in file1 is field N |
| `-2 N` | join field in file2 is field N |
| `-t C` | field separator |
| `-a N` | also print unpaired lines from file N |
| `-o` | control output fields |

## Example template
```bash
# files must be sorted on the join field
join -1 1 -2 1 file1_sorted.txt file2_sorted.txt
```

---

## 4.5 paste

## Definition
`paste` merges files **line-by-line** as columns.

## Usage
```bash
paste [options] file1 file2
```

## Common options
| Option | Meaning |
|---|---|
| `-d C` | delimiter |
| `-s` | serial mode (merge lines from one file) |

## Examples
```bash
paste file1.txt file2.txt
paste -d ':' file1.txt file2.txt
paste -s animals.txt
```

---

## 4.6 split

## Definition
`split` breaks a file into smaller files.

## Usage
```bash
split -l LINES input [prefix]
```

## Common options
| Option | Meaning |
|---|---|
| `-l N` | split by N lines |
| `-b SIZE` | split by size (implementation-dependent) |

## Examples
Split `animals.txt` into chunks of 5 lines:
```bash
split -l 5 animals.txt chunk_
```

Reassemble:
```bash
cat chunk_* > animals_joined.txt
```

---

## 4.7 tr

## Definition
`tr` translates or deletes characters from stdin to stdout.

## Usage
```bash
tr 'FROM' 'TO'
tr -d 'CHARS'
tr -s 'CHARS'
```

## Common options
| Option | Meaning |
|---|---|
| `-d` | delete characters |
| `-s` | squeeze repeats |
| `-c` | complement (inverse set) |

## Examples (with `animals.txt`)

Uppercase → lowercase:
```bash
cat animals.txt | tr 'A-Z' 'a-z'
```

Delete all vowels:
```bash
cat animals.txt | tr -d 'aeiouAEIOU'
```

Squeeze repeated spaces (useful before `cut` on space-separated text):
```bash
tr -s ' ' < list.txt
```

---

## 4.8 pr

## Definition
`pr` paginates and formats text for printing (headers, columns, numbering).

## Usage
```bash
pr [options] file
```

## Common options
| Option | Meaning |
|---|---|
| `-n` | line numbering |
| `-h "TITLE"` | header title |
| `-l N` | page length |
| `-2`, `-3` | multi-column output (2 or 3 columns) |

## Examples

Number lines:
```bash
pr -n animals.txt
```

Add a title header:
```bash
pr -h "Animals Report" animals.txt
```

Two columns:
```bash
pr -2 animals.txt
```

---

# 5. Loops and Control Structures

---

## 5.1 for Loop

## Definition
A `for` loop iterates over a list of values.

## Usage
```bash
for item in list
do
  commands
done
```

## Examples

Iterate words from a file (simple):
```bash
for a in $(cat animals.txt)
do
  echo "$a"
done
```

Case-insensitive frequency report using a loop + pipeline:
```bash
for a in $(cat animals.txt | tr 'A-Z' 'a-z')
do
  echo "$a"
done | sort | uniq -c
```

---

## 5.2 while Loop

## Definition
A `while` loop repeats while a condition is true.

## Usage
```bash
while [ condition ]
do
  commands
done
```

## Examples

Count from 1 to 5:
```bash
n=1
while [ $n -le 5 ]
do
  echo $n
  n=$((n + 1))
done
```

Read a file line-by-line (recommended pattern):
```bash
while IFS= read -r line
do
  echo "LINE: $line"
done < animals.txt
```

---

## 5.3 select + case + PS1

## Definition
- `select` creates a simple menu loop.
- `case` matches multiple patterns cleanly.
- `PS1` controls the shell prompt string.

## Usage (menu)
```bash
select choice in A B C
do
  case "$choice" in
    A) ... ;;
    B) ... ;;
    *) ... ;;
  esac
done
```

## Example: menu tool for `animals.txt` (case-insensitive)

```bash
#!/usr/bin/env bash

PS1="USP> "

select action in "List unique (case-insensitive)" "Count occurrences" "Show only lions" "Quit"
do
  case "$action" in
    "List unique (case-insensitive)")
      cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq
      ;;
    "Count occurrences")
      cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq -c
      ;;
    "Show only lions")
      cat animals.txt | tr 'A-Z' 'a-z' | awk '$0 == "lion" {print NR, $0}'
      ;;
    "Quit")
      break
      ;;
    *)
      echo "Invalid selection"
      ;;
  esac
done
```

---

**End of Week 4**
