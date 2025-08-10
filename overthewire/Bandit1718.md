# Bandit Level 17 → Level 18 Advanced SSH, remote command execution

## Previous Flag
<b>x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO</b>

## Goal
Use previous password to log in SSH with user <b>bandit18</b> on port <b>2220</b>.  Password stored in a file <b>readme</b> in the homedirectory. Unfortunately, someone has <b>modified .bashrc</b> to log you out when you log in with SSH.

## What I learned
```
.bashrc is an important shell configuration file
can execute command after ssh
log in as pseudo terminal and can modify .bashrc if wanted to
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit18@bandit.labs.overthewire.org -p 2220 ⌨️
bandit18@bandit.labs.overthewire.org's password: ⌨️
Welcome to OverTheWire!

Byebye !
Connection to bandit.labs.overthewire.org closed.
@trungdullc ➜ /workspaces/01noobHacker (main) $ whatis ssh ls cat ⌨️
ssh (1)              - OpenSSH remote login client
ls (1)               - list directory contents
cat (1)              - concatenate files and print on the standard output
@trungdullc ➜ /workspaces/01noobHacker (main) $ man ssh | grep "pseudo-terminal" --color=always ⌨️
       -T      Disable pseudo-terminal allocation.
       -t      Force pseudo-terminal allocation.  This can be used to execute arbitrary screen-based programs  on  a  remote
       If an interactive session is requested, ssh by default will only request a pseudo-terminal (pty) for interactive ses‐
       If a pseudo-terminal has been allocated, the user may use the escape characters noted below.
       If no pseudo-terminal has been allocated, the session is transparent and can be  used  to  reliably  transfer  binary
       When a pseudo-terminal has been requested, ssh supports a number of functions through the use of an escape character.
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh -t bandit18@bandit.labs.overthewire.org -p 2220 /bin/bash ⌨️
Byebye !
Connection to bandit.labs.overthewire.org closed.
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh -t bandit18@bandit.labs.overthewire.org -p 2220 /bin/sh ⌨️
bandit18@bandit.labs.overthewire.org's password: ⌨️
$ ls ⌨️
readme
$ cat readme ⌨️
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8 🔐
$ cat .bashrc ⌨️
export GAMEHOSTNAME=${GAMEHOSTNAME:-$HOSTNAME}
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
        # We have color support; assume it's compliant with Ecma-48
        # (ISO/IEC-6429). (Lack of such support is extremely rare, and such
        # a case would tend to support setf rather than setaf.)
        color_prompt=yes
    else
        color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@$GAMEHOSTNAME\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@$GAMEHOSTNAME:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@$GAMEHOSTNAME: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
echo 'Byebye !'
exit 0 🕵️‍♀️
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit18@bandit.labs.overthewire.org -p 2220 ls ⌨️
bandit18@bandit.labs.overthewire.org's password: ⌨️
readme
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme ⌨️
bandit18@bandit.labs.overthewire.org's password: ⌨️
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8 🔐
```

## Flag
<b>cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8</b>

## Continue
[Continue](./Bandit1819.md)