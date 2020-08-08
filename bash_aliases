alias emacs="emacs -nw"
alias shutdown="shutdown now"
alias ping="ping -c 4"
alias save="echo 'Sourcing ~/.bashrc and its dependencies' && . ~/.bashrc"

alias aupdate="${DBUZZELL_SCRIPTS}/aupdate.sh"
alias gupdate="${DBUZZELL_SCRIPTS}/gupdate.sh"
alias update="${DBUZZELL_SCRIPTS}/update.sh"

alias mdview="${DBUZZELL_SCRIPTS}/MarkdownViewer.sh"

function gacp {
    git add "$1"
    git commit -m "$2"
    git push
}
