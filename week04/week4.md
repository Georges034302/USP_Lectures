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
   5.3 [`select + case + PS3`](#53-select--case--ps3)  

Datasets used in examples (must exist in the repo):

- `animals.txt`
- `countries.txt`

---

# 1. Piping

## Definition
A **pipe** redirects the **standard output (stdout)** of one command into the **standard input (stdin)** of another command.

Pipe operator:

```bash
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
# convert animal names to lowercase, sort them, then remove duplicates
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
awk 'NR>1 {print $2}' countries.txt | sort
# extract country names from countries.txt and sort them alphabetically
```

```bash
awk 'NR>1 {print $1}' countries.txt | sort | uniq -c | sort -nr
# count how many countries belong to each continent and sort by frequency
```

## Notes
- Only **stdout** is piped by default.
- Errors (**stderr**) are **not** piped unless redirected.
- Each command in a pipeline runs as a separate process.

---

# 2. Redirection

## Definition
**Redirection** changes where a command reads input from or writes output to.

## Standard streams and file descriptors

| Stream | FD | Default |
|---|---:|---|
| STDIN | 0 | keyboard |
| STDOUT | 1 | terminal |
| STDERR | 2 | terminal |

## Common operators

| Operator | Meaning |
|---|---|
| `>` | redirect stdout to a file (overwrite) |
| `>>` | redirect stdout to a file (append) |
| `<` | read stdin from a file |
| `2>` | redirect stderr to a file |
| `2>&1` | redirect stderr to the current stdout destination |

## Examples

```bash
ls -l > out.txt
# write output to a file and overwrite its previous contents
```

```bash
ls -l >> out.txt
# append output to the end of a file
```

```bash
> out.txt
# create an empty file or clear an existing file
```

```bash
wc -l < animals.txt
# count lines by sending animals.txt into wc through stdin
```

```bash
wc -l countries.txt
# count lines in countries.txt by passing the file as a command argument
```

```bash
ls missing_file 2> errors.txt
# redirect only error messages to errors.txt
```

```bash
ls animals.txt missing_file > all.txt 2>&1
# redirect stdout and stderr to the same file
```

```bash
ls missing_file 2> /dev/null
# discard error output by sending it to the null device
```

```bash
awk 'NR>1 {print $2}' countries.txt > country_names.txt
# save extracted country names into a new file
```

---

# 3. Special Shell Parameters

## Definition
**Special shell parameters** are variables provided by the shell to expose script arguments, process information, and command status.

| Parameter | Meaning |
|---|---|
| `$0` | script name |
| `$1..$9` | positional arguments |
| `$#` | number of arguments |
| `$*` | all arguments as one string |
| `$@` | all arguments as separate strings |
| `$?` | exit status of the last command |
| `$$` | process ID of the current shell or script |

## Example

```bash
#!/usr/bin/env bash

echo "$0"   # print the script name
echo "$#"   # print how many arguments were passed
echo "$*"   # print all arguments as one combined string
echo "$@"   # print all arguments as separate words
echo "$$"   # print the process id of the current script
echo "$?"   # print the exit status of the previous command
```

## Exit status example

```bash
false
# run a command that fails

echo $?
# print the exit status of the previous command
```

---

# 4. Unix Text Processing Filters

Filters read from **stdin** or from files, process text, and write the result to **stdout**.

---

# 4.1 cut

## Definition
`cut` extracts selected **characters** or **fields** from each line of input.

## Usage

```bash
cut -c LIST file
cut -d DELIM -f LIST file
```

## Common options

| Option | Meaning |
|---|---|
| `-c LIST` | select character positions |
| `-d DELIM` | specify field delimiter |
| `-f LIST` | select fields |
| `-s` | suppress lines with no delimiter |
| `--complement` | select everything except the chosen fields or characters |

## Examples with `countries.txt`

```bash
cut -d' ' -f1 countries.txt
# extract the first field (continent column), including the header row
```

```bash
tail -n +2 countries.txt | cut -d' ' -f2
# skip the header row, then extract the country column
```

```bash
cut -d' ' -f2,3 countries.txt
# extract the country and capital columns
```

```bash
cut -d' ' -f1,4 countries.txt
# extract the continent and population columns
```

```bash
cut -c1-10 countries.txt
# extract the first 10 characters of each line as raw text
```

```bash
cut -c1-10,20-30 countries.txt
# extract two character ranges from each line
```

```bash
cut -c11- countries.txt
# extract from character 11 to the end of each line
```

```bash
cut -d' ' -f2 -s countries.txt
# extract field 2 and suppress lines without the delimiter
```

## Notes
- `cut -d' '` works best when the file is consistently space-delimited.
- `cut` works on raw character positions with `-c`, and on delimited fields with `-d` and `-f`.

---

# 4.2 awk

## Definition
`awk` is a text processing language that reads input line by line, splits each line into fields, and performs actions.

## Usage

```bash
awk 'pattern { action }' file
awk -F 'DELIM' 'pattern { action }' file
```

## Common options and features

| Option / Feature | Meaning |
|---|---|
| `-F DELIM` | set the input field separator |
| `BEGIN {}` | run code before reading input |
| `END {}` | run code after reading all input |
| `$0` | whole current line |
| `$1`, `$2`, ... | individual fields in the current line |
| `NF` | number of fields in the current line |
| `NR` | current record number (line number) |

## Examples with `countries.txt`

```bash
awk '{print}' countries.txt
# print all lines exactly as they appear
```

```bash
awk 'NR==1' countries.txt
# print only the header row
```

```bash
awk 'NR>1 {print $2}' countries.txt
# print the country column and skip the header row
```

```bash
awk 'NR>1 && $1=="Europe" {print $2}' countries.txt
# list countries where the continent is Europe
```

```bash
awk '{print NR"-", $2}' countries.txt
# print line numbering together with the second column
```

```bash
awk 'NR>1 {printf "%-10s %-15s %-12s %s\n", $1, $2, $3, $4}' countries.txt
# print a formatted table of continent, country, capital, and population
```

```bash
awk 'NR>1 {c[$1]++} END {for (k in c) printf "%-10s %2d\n", k, c[k]}' countries.txt
# count how many countries appear under each continent
```

```bash
awk 'NR>1 {g[$1]=g[$1] ? g[$1] ", " $2 : $2} END {for (k in g) print k ": " g[k]}' countries.txt
# group country names by continent
```

```bash
awk 'NR>1 {print $2}' countries.txt | sort
# extract countries and sort them alphabetically
```

```bash
awk 'NR>1 {print $1}' countries.txt | sort | uniq -c | sort -nr
# count continent frequencies and sort them in descending order
```

```bash
awk 'NR>1 && $2 ~ /^S.*/ {print $1, $2}' countries.txt
# print continents and countries whose country names start with S
```

```bash
awk 'NR>1 && $2 ~ /_/ {print $1, $2}' countries.txt
# print countries that contain underscores in their names
```

## Examples with `animals.txt`

```bash
cat animals.txt | tr 'A-Z' 'a-z' | awk '{count[$0]++} END {for (a in count) print a, count[a]}'
# count occurrences of each animal name after converting to lowercase
```

```bash
cat animals.txt | tr 'A-Z' 'a-z' | awk '$0 == "lion" {print NR, $0}'
# print line numbers for lines that exactly match lion
```

---

# 4.3 uniq

## Definition
`uniq` removes or reports **adjacent duplicate lines**.  
It usually works together with `sort` so duplicates appear next to each other.

## Usage

```bash
sort file | uniq
```

## Common options

| Option | Meaning |
|---|---|
| `-c` | prefix each line with its count |
| `-d` | show duplicated lines only |
| `-u` | show unique lines only |

## Examples

```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq
# show unique animal names ignoring case
```

```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq -c
# count how many times each animal appears
```

```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq -d
# show only animal names that appear more than once
```

```bash
cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq -u
# show only animal names that appear exactly once
```

```bash
awk 'NR>1 {print $1}' countries.txt | sort | uniq -c
# count how many rows belong to each continent
```

---

# 4.4 join

## Definition
`join` combines lines from **two sorted files** using a **common key field**.  
It is similar to a simple SQL join.

Both files **must be sorted on the join field** before using `join`.

## Usage

```bash
join [options] file1 file2
```

## Common options

| Option | Meaning |
|---|---|
| `-1 N` | join field in file1 is column N |
| `-2 N` | join field in file2 is column N |
| `-t C` | specify field delimiter |
| `-a N` | include unpaired lines from file N |

## Examples

```bash
sort animals.txt > animals_sorted.txt
# sort animals.txt so it can be used safely with join
```

```bash
uniq animals_sorted.txt > animals_unique.txt
# create a second sorted file containing unique animal names
```

```bash
join animals_sorted.txt animals_unique.txt
# join the two sorted files using column 1 as the default key
```

```bash
join -a 1 animals_sorted.txt animals_unique.txt
# include unmatched lines from animals_sorted.txt
```

```bash
join -t ' ' -1 1 -2 1 animals_sorted.txt animals_unique.txt
# explicitly join both files using field 1 with a space delimiter
```

---

# 4.5 split

## Definition
`split` breaks a file into smaller files based on a number of lines or a size limit.

## Usage

```bash
split -l LINES input [prefix]
split -b SIZE input [prefix]
```

## Common options

| Option | Meaning |
|---|---|
| `-l N` | split the file into pieces of N lines each |
| `-b SIZE` | split the file by size |
| `prefix` | prefix used for generated output files |

## Examples

```bash
split -l 5 animals.txt chunk_
# split animals.txt into files of 5 lines each using the prefix chunk_
```

```bash
split -l 4 countries.txt countries_chunk_
# split countries.txt into files of 4 lines each
```

```bash
cat chunk_* > animals_joined.txt
# reconstruct the original animals file by concatenating all chunk files
```

---

# 4.6 paste

## Definition
`paste` merges files **line by line** and places their contents side by side as columns.

## Usage

```bash
paste [options] file1 file2
```

## Common options

| Option | Meaning |
|---|---|
| `-d C` | use character C as the delimiter |
| `-s` | paste one file serially instead of in parallel |

## Examples

Examples using files produced by `split`:

```bash
paste chunk_aa chunk_ab
# merge two chunk files side by side using the default tab delimiter
```

```bash
paste -d ':' chunk_aa chunk_ab
# merge two chunk files using : as the delimiter
```

```bash
paste -d ',' chunk_aa chunk_ab
# merge two chunk files using a comma as the delimiter
```

```bash
paste countries_chunk_aa countries_chunk_ab
# merge two split country files side by side
```

```bash
paste -s animals.txt
# merge all lines of animals.txt into one line
```

---

# 4.7 tr

## Definition
`tr` translates, deletes, or squeezes characters from **stdin** and writes the result to **stdout**.

## Usage

```bash
tr 'FROM' 'TO'
tr -d 'CHARS'
tr -s 'CHARS'
```

## Common options

| Option | Meaning |
|---|---|
| `-d` | delete specified characters |
| `-s` | squeeze repeated characters into one |
| `-c` | use the complement of the given set |

## Examples

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
cat countries.txt | tr '_' ' '
# replace underscores with spaces in multi-word names
```

```bash
cat countries.txt | tr 'A-Z' 'a-z'
# convert all country data to lowercase
```

```bash
cat countries.txt | tr -d 'M'
# remove the M suffix from population values
```

```bash
cat animals.txt | tr ' ' '_'
# replace spaces with underscores
```

```bash
cat animals.txt | tr -cd 'a-zA-Z\n'
# remove everything except letters and newline characters
```

```bash
cat animals.txt | tr -s '\n'
# squeeze repeated blank lines into a single newline
```

---

# 4.8 pr

## Definition
`pr` paginates and formats text for printing by adding headers, page layout, numbering, and columns.

## Usage

```bash
pr [options] file
```

## Common options

| Option | Meaning |
|---|---|
| `-n` | number the lines |
| `-h "TITLE"` | set the page header title |
| `-l N` | set the page length to N lines |
| `-2`, `-3` | print in 2 or 3 columns |
| `-t` | omit page headers and trailers |

## Examples

```bash
pr -n animals.txt
# print animals.txt with numbered lines
```

```bash
pr -h "Animals Report" animals.txt
# print animals.txt with a custom header title
```

```bash
pr -2 animals.txt
# print animals.txt in two columns
```

```bash
pr -t animals.txt
# print animals.txt without page headers or trailers
```

```bash
pr -l 20 countries.txt
# print countries.txt using a page length of 20 lines
```

---

# 4.9 diff

## Definition
`diff` compares two files and shows the differences between them.

## Usage

```bash
diff [options] file1 file2
```

## Common options

| Option | Meaning |
|---|---|
| `-u` | show unified diff format |
| `-q` | report only whether files differ |
| `-y` | show differences side by side |

## Examples

```bash
diff animals.txt animals_joined.txt
# compare the original file with the reconstructed file
```

```bash
diff -u animals.txt animals_joined.txt
# show differences in unified format
```

```bash
diff -q animals.txt animals_joined.txt
# report only whether the two files differ
```

```bash
diff -y animals.txt animals_joined.txt
# display differences side by side
```

---

# 5. Loops and Control Structures

---

# 5.1 for Loop

## Definition
A `for` loop iterates over a list of values and runs a block of commands for each value.

## Usage

```bash
for item in list
do
  commands
done
```

## Examples

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
# generate a frequency report of animal names
```

```bash
for c in $(awk 'NR>1 {print $2}' countries.txt)
do
  echo "$c"
done
# print each country name from countries.txt
```

```bash
for f in chunk_*
do
  wc -l "$f"
done
# count the number of lines in each split file
```

---

# 5.2 while Loop

## Definition
A `while` loop repeats a block of commands while a condition remains true.

## Usage

```bash
while [ condition ]
do
  commands
done
```

## Examples

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
# read animals.txt line by line safely
```

```bash
while IFS= read -r line
do
  echo "$line" | tr 'A-Z' 'a-z'
done < animals.txt
# read each animal line and convert it to lowercase
```

```bash
while IFS= read -r line
do
  echo "$line"
done < countries.txt
# read countries.txt line by line safely
```

---

# 5.3 select + case + PS3

## Definition
- `select` creates a simple menu loop.
- `case` matches multiple patterns clearly.
- `PS3` controls the shell prompt string.

## Usage

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

## Example

```bash
#!/usr/bin/env bash

PS3="USP> "
# set a custom shell prompt

select action in "List unique animals" "Count animal occurrences" "List European countries" "Quit"
do
  case "$action" in
    "List unique animals")
      cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq
      # list unique animal names ignoring case
      ;;
    "Count animal occurrences")
      cat animals.txt | tr 'A-Z' 'a-z' | sort | uniq -c
      # count how many times each animal appears
      ;;
    "List European countries")
      awk 'NR>1 && $1=="Europe" {print $2}' countries.txt
      # print country names where continent is Europe
      ;;
    "Quit")
      break
      # exit the menu
      ;;
    *)
      echo "Invalid selection"
      # handle invalid menu choices
      ;;
  esac
done
```

---

**End of Week 4**
