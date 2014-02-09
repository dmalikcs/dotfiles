# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

if [ -f $HOME/.dotfiles/.mainrc ]; then
    . $HOME/.dotfiles/.mainrc
fi
