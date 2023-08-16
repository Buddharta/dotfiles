-- This file can be loaded by calling `lua require('plugins')` from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

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

	--Language Client(dont know if it conflicts with treesitter)
	--use 'autozimu/LanguageClient-neovim'

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

	--Navigator
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

