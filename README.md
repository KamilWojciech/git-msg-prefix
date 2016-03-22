#Git msg-prefix
This is subcommand to git which allows you to set commit message prefix for specific branch. It is very useful when working with jira. You can sepcify prefix i.e AB-1 which represents jira issue number.

# Installation
You can set it up via [Homebrew](http://brew.sh/)

Run the following commands:

```bash
brew tap kamilwojciech/tap
```
```bash
brew install git-msg-prefix
```

# Usage
## Set prefix
```bash
git msg-prefix set prefix [branch]
```
You don't have to specify branch name, by default it is current branch which you are working on. If prefix is already set for specific branch it will replace it.

## List
```bash
git msg-prefix list
```
This command shows all prefixes 
