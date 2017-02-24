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

Now configure your git with templates directory
```bash 
 git config --global init.templatedir ~/.git-templates
 ```

# Usage
## Branch name
You can use one of 2 naming conventions to set commit message prefix. If you use jira for issue tracking you can name your branch like `ab-12-branch-name`, the prefix will be `AB-12`.
For github use `g12-branch-name`, the prefix will be `#12`. You can also replace `-` with `_`. 

## Set prefix
You can always specify custom prefix for brunch.

```bash
git msg-prefix set prefix [branch]
```
You don't have to specify branch name, by default it is current branch which you are working on. If prefix is already set for specific branch it will replace it.

## List
```bash
git msg-prefix list
```
This command shows all prefixes 
