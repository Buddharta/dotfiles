-- This file can be loaded by calling `lua require('plugins')` from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

require('remote-sshfs').setup({})
require('telescope').load_extension 'remote-sshfs'

return require('packer').startup(function(use)
  -- Packer can manage itself
	use 'wbthomason/packer.nvim'
        --Tresitter
	use {
		'nvim-treesitter/nvim-treesitter',
		run = ':TSUpdate'
	}
	use 'nvim-treesitter/playground'
        --LSP-Zero
        use {
                  'VonHeikemen/lsp-zero.nvim',
                  branch = 'v2.x',
                  requires = {
                    -- LSP Support
                    {'neovim/nvim-lspconfig'},             -- Required
                    {'williamboman/mason.nvim'},           -- Optional
                    {'williamboman/mason-lspconfig.nvim'}, -- Optional

                    -- Autocompletion
                    {'hrsh7th/nvim-cmp'},     -- Required
                    {'hrsh7th/cmp-nvim-lsp'}, -- Required
                    {'L3MON4D3/LuaSnip'},     -- Required
                  }
        }
	--Theme

	use { "ellisonleao/gruvbox.nvim" }
	use 'ayu-theme/ayu-vim'
	use 'joshdick/onedark.vim'

	--Visual
	use 'yggdroot/indentline'
        use 'vim-airline/vim-airline'
        use 'vim-airline/vim-airline-themes'
	use 'lilydjwg/colorizer'

	--sshfs: nvim over SSH basically 
    use {
      'nosduco/remote-sshfs.nvim',
      requires = { {'nvim-telescope/telescope.nvim'} } -- optional if you declare plugin somewhere else
    }
	--Completion With Java
	use 'ncm2/ncm2'
	use 'roxma/nvim-yarp'
	use 'ncm2/ncm2-bufword'    
	use 'ncm2/ncm2-path'
	use 'chun-yang/auto-pairs'
	use 'ncm2/ncm2-tagprefix'
	use 'ncm2/ncm2-ultisnips'
	use 'ncm2/ncm2-markdown-subscope'
	use 'ncm2/ncm2-rst-subscope'
	--FileTree
	use 'scrooloose/nerdtree'
	use 'Xuyuanp/nerdtree-git-plugin'
	use 'ryanoasis/vim-devicons'

	--Navigation
    use "nvim-lua/plenary.nvim"
    use {
      'nvim-telescope/telescope.nvim', tag = '0.1.5',
    -- or                            , branch = '0.1.x',
  requires = { {'nvim-lua/plenary.nvim'} }
}
	use 'christoomey/vim-tmux-navigator'
	use {
    		'junegunn/fzf.vim',
    		requires = { 'junegunn/fzf', run = ':call fzf#install()' }
 	}
	use { "ibhagwan/fzf-lua",
  	-- optional for icon support
  	requires = { "nvim-tree/nvim-web-devicons" }
	}
	
	use 'mbbill/undotree' 	
	--Snippets
	use 'SirVer/ultisnips'
	use 'honza/vim-snippets'
	--HTML
	use 'mattn/emmet-vim'

	--Typescript
	use 'leafgarland/typescript-vim'

	--Python
	use 'vim-python/python-syntax'

	--Rust
	use 'rust-lang/rust.vim'

        --Git integration
        use 'tpope/vim-fugitive'
  end)
