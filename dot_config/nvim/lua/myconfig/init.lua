require("myconfig.remap")
require("myconfig.plugins")

--Numberlines and cursor
vim.opt.nu = true
vim.opt.relativenumber = true

--Tabs and indenting
vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.smartindent = true

vim.opt.mouse = 'a' 

vim.opt.numberwidth = 1 
vim.opt.wrap = false
vim.opt.ignorecase = true
vim.opt.clipboard = 'unnamedplus' 
vim.opt.encoding = "utf-8" 
vim.opt.termguicolors = true 
vim.opt.colorcolumn = "120" 
vim.opt.errorbells = false

vim.cmd[[ set cursorline ]] 
vim.cmd[[ highlight ColoColumn ctermbg=0 guibg=lightgrey ]]
vim.cmd[[ let g:colorizer_maxlines=1000 ]]
vim.cmd[[ let g:pyhon_highlight_all=1 ]]

--Spelling
vim.cmd[[ set spelllang=en,cjk ]]
vim.cmd[[ set spellsuggest=best,9 ]]

print("Loaded myconfig...")

