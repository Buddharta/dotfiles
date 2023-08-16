
--Theme
-- setup must be called before loading the colorscheme
-- Default options:
require("gruvbox").setup({
  undercurl = true,
  underline = true,
  bold = true,
  italic = {
    strings = true,
    comments = true,
    operators = false,
    folds = true,
  },
  strikethrough = true,
  invert_selection = false,
  invert_signs = false,
  invert_tabline = false,
  invert_intend_guides = false,
  inverse = true, -- invert background for search, diffs, statuslines and errors
  contrast = "", -- can be "hard", "soft" or empty string
  palette_overrides = {},
  overrides = {},
  dim_inactive = false,
  transparent_mode = false,
})
vim.o.background = "dark"
vim.cmd("colorscheme gruvbox")
vim.api.nvim_set_hl(0, "Normal",{bg = "none"})
vim.api.nvim_set_hl(0, "NormalFloat",{bg = "none"})
vim.cmd[[ set completeopt=noinsert,menuone,noselect ]] 

--air-line
vim.cmd[[ let g:airline_powerline_fonts = 1 ]]

--if !exists('g:airline_symbols')
    --let g:airline_symbols = {}
--endif

--Airline symbols 
vim.cmd[[ let g:airline_left_sep = '' ]]
vim.cmd[[ let g:airline_left_alt_sep = '' ]]
vim.cmd[[ let g:airline_right_sep = '' ]]
vim.cmd[[ let g:airline_right_alt_sep = '' ]]
vim.cmd[[ let g:airline_symbols.branch = '' ]]
vim.cmd[[ let g:airline_symbols.readonly = '' ]]
vim.cmd[[ let g:airline_symbols.linenr = '' ]]
vim.cmd[[ let g:airline_symbols.linenr = '␤' ]]
vim.cmd[[ let g:airline_symbols.branch = '⎇' ]]
vim.cmd[[ let g:airline_symbols.paste = '∥' ]]
vim.cmd[[ let g:airline_symbols.whitespace = 'Ξ' ]]
vim.cmd[[ let g:airline_theme='base16' ]]
vim.cmd[[ let g:airline#extensions#tabline#enabled = 1 ]]
vim.cmd[[ let ayucolor="mirage" ]]
vim.cmd[[ let g:gruvbox_contrast_dark="hard" ]]
vim.cmd[[ let g:indentLine_char_list = ['|', '¦', '┆', '┊'] ]]
vim.cmd[[ set shortmess+=c ]]
