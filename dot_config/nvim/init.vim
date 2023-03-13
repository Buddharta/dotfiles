        syntax on

set number
set mouse=a
set noerrorbells
set expandtab
set smartindent
set rnu
set numberwidth=1
set nowrap
set ignorecase
set clipboard=unnamedplus
set encoding=utf-8
set cursorline
set termguicolors

set colorcolumn=120
highlight ColoColumn ctermbg=0 guibg=lightgrey

call plug#begin('$HOME/.local/share/nvim/plugged')

        "Theme
        Plug 'morhetz/gruvbox'
        Plug 'ayu-theme/ayu-vim'
        Plug 'joshdick/onedark.vim'

        "Visual
        Plug 'yggdroot/indentline'
        Plug 'vim-airline/vim-airline'
        Plug 'vim-airline/vim-airline-themes'
        Plug 'lilydjwg/colorizer'
        
        "Java
        Plug 'autozimu/LanguageClient-neovim'
        
        "Completion With Java
        Plug 'ncm2/ncm2'
        Plug 'roxma/nvim-yarp'
        Plug 'ncm2/ncm2-bufword'    
        Plug 'ncm2/ncm2-path'
        Plug 'chun-yang/auto-pairs'
        Plug 'ncm2/ncm2-bufword'
        Plug 'ncm2/ncm2-tagprefix'
        Plug 'ncm2/ncm2-ultisnips'
        Plug 'ncm2/ncm2-markdown-subscope'
        Plug 'ncm2/ncm2-rst-subscope'
        "FileTree
        Plug 'scrooloose/nerdtree'
        Plug 'Xuyuanp/nerdtree-git-plugin'
        Plug 'ryanoasis/vim-devicons'

        "Navigator
        Plug 'christoomey/vim-tmux-navigator'
        Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
        Plug 'junegunn/fzf'

        "Snippets
        Plug 'SirVer/ultisnips'
        Plug 'honza/vim-snippets'

        "HTML
        Plug 'mattn/emmet-vim'
        
        "Typescript
        Plug 'leafgarland/typescript-vim'

        "Python
        Plug 'vim-python/python-syntax'

        "Rust
        Plug 'rust-lang/rust.vim'

call plug#end()

let g:colorizer_maxlines=1000
let g:pyhon_highlight_all=1

"For JAVA
let g:LanguageClient_autoStart = 1
" Use the location list instead of the quickfix list to show linter warnings
let g:LanguageClient_diagnosticsList = "Location"
let g:LanguageClient_rootMarkers = {
    \ 'java': ['.git']
    \ }
let g:LanguageClient_serverCommands = {
    \ 'java': ['java-lsp.sh']
    \ }
"Rebinds for JAVA
set hidden
nnoremap <buffer> <silent> F5 :call LanguageClient_contextMenu()<CR>
nnoremap <buffer> <silent> K :call LanguageClient_textDocument_hover()<CR>
nnoremap <buffer> <silent> gd :call LanguageClient_textDocument_definition()<CR>
nnoremap <buffer> <silent> gr :call LanguageClient_textDocument_references()<CR>
nnoremap <buffer> <silent> <leader>fs :call LanguageClient_textDocument_documentSymbol()<CR>
nnoremap <buffer> <silent> crr :call LanguageClient_textDocument_rename()<CR>
nnoremap <buffer> <silent> <a-CR> :call LanguageClient_textDocument_codeAction()<CR>


"For faster commands (SPACE)
let mapleader = " "
set concealcursor=""


"Opening configuration
autocmd BufEnter * call ncm2#enable_for_buffer()
autocmd VimEnter * NERDTree | wincmd p
autocmd BufEnter * if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

"source init.vim
nnoremap <F4> :source $MYVIMRC<CR> 

"Completion ncm2
inoremap <c-c> <ESC>
inoremap <expr> <CR> (pumvisible() ? "\<c-y>\<cr>" : "\<CR>")
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

"NERDTree
nnoremap <leader>f :NERDTreeFocus<CR>
nnoremap <leader>t :NERDTree<CR>
nnoremap <leader><tab> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>

"With the arrow keys you can resize your splits
nnoremap <c-right> :vertical resize +5<CR>
nnoremap <c-left> :vertical resize -5<CR>
nnoremap <c-up> :resize +5<CR>
nnoremap <c-down> :resize -5<CR>

"with leader w you save the file if it have a name set. The second command
"open your config file
nnoremap <leader>w :w<CR>

"you split a terminal with a size of 15
vnoremap <c-t> :split<CR>:ter<CR>:resize 15<CR>
nnoremap <c-t> :split<CR>:ter<CR>:resize 15<CR>
vnoremap <C-\> :split<CR>:ter<CR>:resize 15<CR>
nnoremap <C-\> :split<CR>:ter<CR>:resize 15<CR>

" Move to the next buffer
" Move to the prevoius buffer
nnoremap <leader>l :bnext<CR>
nnoremap <leader>h :bprevious<CR>

" Close the current buffer
"create a new tab
nnoremap <leader>qq :bdelete<CR>
nnoremap <leader>n :tabe<CR>

"vertical split
"horizontal split
nnoremap <leader>vs :vsp<CR>
nnoremap <leader>sp :sp<CR>

" clear search results
nnoremap <silent> // :noh<CR>

"Themes
set background=dark
set completeopt=noinsert,menuone,noselect
" air-line
let g:airline_powerline_fonts = 1

if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif

"Airline symbols 
let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
let g:airline_symbols.branch = ''
let g:airline_symbols.readonly = ''
let g:airline_symbols.linenr = ''
let g:airline_symbols.linenr = '␤'
let g:airline_symbols.branch = '⎇'
let g:airline_symbols.paste = '∥'
let g:airline_symbols.whitespace = 'Ξ'
let g:airline_theme='base16'
let g:airline#extensions#tabline#enabled = 1

let ayucolor="mirage"
let g:gruvbox_contrast_dark="hard"
colorscheme gruvbox

let g:indentLine_char_list = ['|', '¦', '┆', '┊']
set shortmess+=c
"Spelling
set spelllang=en,cjk
set spellsuggest=best,9
nnoremap <silent> <F11> :set spell!<cr>
inoremap <silent> <F11> <C-O>:set spell!<cr>
