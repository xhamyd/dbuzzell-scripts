# dbuzzell-scripts

_dbuzzell-scripts_ is my public repo that holds all of my personally useful scripts. These scripts are shared freely for
use if helpful for others (only attributions/credits requested). However, these scripts have only been lightly validated
for my personal applications, so use these scripts at your own risk.

## Table of Contents

This textual listing is provided for quick reference, and may be out-of-date at any time.

### chroot/

These files were personally edited Bash scripts that I used to personalize my
[chroot](https://github.com/dnschneid/crouton) files. While I no longer use a Chromebook/Chrome OS environment, there's
some good Bash scripting that may be useful to reference.

### csv_filesort/

This was a proof-of-concept project to sort a bunch of CSV files in nested directories. As a PoC, this script has only
been tested with the provided `test_dir/`. I would not recommended running this on actual CSVs full of data without your
own testing and backups!

### pylint-research/

This is an unsorted collection of my notes when researching all of the errors flagged by pylint. This was run on version
1.9, but the provided script should be able to provide the messages for your installed pylint package.

### tutorial-materials/

While I was learning functionalities in Bash/Python/etc., I kept a local copy of each file used to demonstrate the
feature. These files should be used as a quick reference (instead of direct importing or the like).

### Loose files

Below is a consise description of each loose file at the root directory:

- aupdate.sh: Executable script to automate Ubuntu update calls (i.e. `apt`, `pip`, `snap`)
- bash_aliases: Copiable `.bash_aliases` file for general use (requires compatible `.bashrc` installed as well)
- bashrc_add: A Bash addendum for `.bashrc` for general use (run `cat bashrc_add >> ~/.bashrc`)
- delete_local_branches.sh: Executable script to delete local git branches no longer on origin
    - There's 3 different options to delete branches with different effects
    - Refer to in-code comments for more details
- emacs-customizations: Copiable `.emacs` file for Emacs customizations (featured for reference, not for direct copy)
- gupdate.sh: Executable script to automate all Git repo updates
    - `$GIT_DIR` needs to be defined in `.bashrc`
    - All repos should be inside of `$GIT_DIR` for full effect
- MarkdownViewer.sh: Executable script to export `*.md` files to local viewing
    - Ideal for Linux users (requires `grip` pip package and `firefox` installed)
- pokemon_types.py: Proof-of-concept script for providing best Pokémon type matches (up to Gen 7), for both offensive
and defensive.
- project-euler.py: Draft script for my attempt at [Project Euler](https://projecteuler.net/) problems.
- README.md: This file!
- update.sh: Executable script to run daily update operations (i.e. `aupdate.sh` and `gupdate.sh`).
