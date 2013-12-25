syntax on
filetype indent on
filetype indent plugin on
set number
set showmatch

"" Whitespace
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
set backspace=indent,eol,start

"" Shows document path and title in the terminal title
set title
set textwidth=80

"Set mouse 
"set mouse=a

"au FileType python set omnifunc=pythoncomplete#Complete
"let g:SuperTabDefaultCompletionType = "context"

call pathogen#infect()
let g:syntastic_check_on_open = 1
let g:syntastic_python_checker = "flake8"
"let g:syntastic_python_checker_args = \"--ignore=E501"
let g:syntastic_python_flake8_args='--ignore=E501'


if !exists("autocommands_loaded")
    let autocommands_loaded = 1
        autocmd BufRead,BufNewFile,FileReadPost *.py source ~/.vim/python
    endif

" This beauty remembers where you were the last time you edited the file,and returns to the same position.
au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif
