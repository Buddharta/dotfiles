--For faster commands (SPACE)
vim.g.mapleader = " "

--Cool rempas
vim.keymap.set("n", "<leader>ex", vim.cmd.Ex)

vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

--NERDTree
vim.keymap.set("n", "<leader>f", vim.cmd.NERDTreeFocus)
vim.keymap.set("n", "<leader>t", vim.cmd.NERDTree)
vim.keymap.set("n", "<leader><tab>", vim.cmd.NERDTreeToggle)
vim.keymap.set("n", "<C-f>", vim.cmd.NERDTreeFind)

--with leader w you save the file if it have a name set. The second command
vim.keymap.set("n", "<leader>w", vim.cmd.w)

--Move to the next buffer
vim.keymap.set("n", "<leader>l", vim.cmd.bnext)

--Move to the prevoius buffer
vim.keymap.set("n", "<leader>h", vim.cmd.bprevious)

--Close the current buffer
vim.keymap.set("n", "<leader>qq", vim.cmd.bdelete)

--create a new tab
vim.keymap.set("n", "leader>n", vim.cmd.tabe)

--vertical split
vim.keymap.set("n", "<leader>vs", vim.cmd.vsp)

--horizontal split
vim.keymap.set("n", "<leader>sp", vim.cmd.sp)

--clear search results
vim.keymap.set("n", "<leader><leader>", vim.cmd.noh)

--Spell Check
--vim.keymap.set("i", "<leader>sc", vim.cmd.spell!)

-- source init.vim
--vim.keymap.set("n" ,"<leader>so", vim.cmd.source("$MYVIMRC")) 

--Completion ncm2
--[[No sé pasar esto a lua:
vim.keyremap.set("i", "<C-c>", <ESC>)
vim.keyremap.set("i", "<expr>", (pumvisible() ? "\<c-y>\<cr>" : "\<CR>")
vim.keyremap.set("i", "<expr> <Tab>", pumvisible() ? "\<C-n>" : "\<Tab>")
vim.keyremap.set("i", "<expr> <S-Tab>", pumvisible() ? "\<C-p>" : "\<S-Tab>")
]]

--Toggle TSPlaygroundToggle
vim.keymap.set("n", "<leader>p", vim.cmd.TSPlaygroundToggle)

--Undotree
vim.keymap.set("n", "<leader>u", vim.cmd.UndotreeToggle)

--Git integration
vim.keymap.set("n", "<leader>gs", vim.cmd.Git)
