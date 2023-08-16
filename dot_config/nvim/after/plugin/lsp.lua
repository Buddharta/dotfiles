local lsp = require('lsp-zero').preset({})

lsp.on_attach(function(client, bufnr)
  -- see :help lsp-zero-keybindings
  -- to learn the available actions
  lsp.default_keymaps({buffer = bufnr})
end)

-- When you don't have mason.nvim installed
-- You'll need to list the servers installed in your system
lsp.setup_servers({'tsserver', 'eslint'})

-- (Optional) Configure lua language server for neovim
require('lspconfig').lua_ls.setup(lsp.nvim_lua_ls())
lsp.ensure_installed({
        'tsserver',
        'eslint',
        'rust_analyzer'
})
--[[
local cmp = require( 'cmp' )
local cmp_select = {behavior = cmp.SelectBehavior.Select}
local cmp_mappings = lsp.defaults.cmp_mappings({
       ['<C-b>'] = cmp.mappings.select_prev_item(cmp_select), 
       ['<C-n>'] = cmp.mappings.select_next_item(cmp_select), 
       ['<C-y>'] = cmp.mappings.confirm({select = true}), 
       ['<C-Space>'] = cmp.mappings.complete(), 
})
]]
lsp.setup()

