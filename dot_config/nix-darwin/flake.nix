{
  description = "Buddha's Darwin system flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    nix-darwin.url = "github:LnL7/nix-darwin";
    nix-darwin.inputs.nixpkgs.follows = "nixpkgs";
    nix-homebrew.url = "github:zhaofengli-wip/nix-homebrew";
    #mac-app-util.url = "github:hraban/mac-app-util";
  };

  outputs = inputs@{ 
  		self, 
  		nix-darwin, 
		nixpkgs, 
		nix-homebrew, 
		#home-manager, 
		#mac-app-util, 
		... }:
  let
    configuration = { pkgs, config, ... }: {
	nixpkgs.config.allowUnfree = true;
	nixpkgs.config.allowUnsupportedSystem = true;
      # List packages installed in system profile. To search by name, run:
      # $ nix-env -qaP | grep wget
      environment.systemPackages =
        [
	pkgs.ecl
        pkgs.wget
        pkgs.btop
        pkgs.zlib
	pkgs.zig
	pkgs.ncurses
	pkgs.vim
	pkgs.mkalias
	pkgs.neovim
	pkgs.tmux
	pkgs.yazi
	pkgs.fzf
	pkgs.eza
	pkgs.jq
	pkgs.emacs
	pkgs.gimp
	pkgs.alacritty
	pkgs.wezterm
	pkgs.git
	pkgs.shellcheck
	pkgs.chezmoi
	pkgs.ripgrep
	pkgs.fd
	pkgs.findutils
	pkgs.vscodium
	pkgs.texliveFull
	pkgs.neofetch
	pkgs.fastfetch
        pkgs.zoxide
        pkgs.python314
        pkgs.pyenv
        pkgs.nodejs_22
        pkgs.starship
        pkgs.clojure
        pkgs.clojure-lsp
        pkgs.sbcl
	pkgs.rlwrap
        pkgs.opam
        pkgs.lean4
        pkgs.coq
	pkgs.guile
	pkgs.chez
	pkgs.julia-bin
        ];
	#Homebrew packages
	homebrew = {
	enable = true;
	brews = [
		"mas"
		"powerlevel10k"
	];
	casks = [
		  "processing"
		  "ghostty"
		  "racket"
		  "hammerspoon"
		  "firefox"
		  "iina"
		  "the-unarchiver"
		  "font-hack-nerd-font"
		  "font-3270-nerd-font"
		  "font-fira-mono-nerd-font"
		  "font-inconsolata-go-nerd-font"
		  "font-inconsolata-lgc-nerd-font"
		  "font-inconsolata-nerd-font"
		  "font-monofur-nerd-font"
		  "font-overpass-nerd-font"
		  "font-ubuntu-mono-nerd-font"
		  "font-agave-nerd-font"
		  "font-arimo-nerd-font"
		  "font-anonymice-nerd-font"
		  "font-aurulent-sans-mono-nerd-font"
		  "font-bigblue-terminal-nerd-font"
		  "font-bitstream-vera-sans-mono-nerd-font"
		  "font-blex-mono-nerd-font"
		  "font-caskaydia-cove-nerd-font"
		  "font-code-new-roman-nerd-font"
		  "font-cousine-nerd-font"
		  "font-daddy-time-mono-nerd-font"
		  "font-dejavu-sans-mono-nerd-font"
		  "font-droid-sans-mono-nerd-font"
		  "font-fantasque-sans-mono-nerd-font"
		  "font-fira-code-nerd-font"
		  "font-go-mono-nerd-font"
		  "font-gohufont-nerd-font"
		  "font-hack-nerd-font"
		  "font-hasklug-nerd-font"
		  "font-heavy-data-nerd-font"
		  "font-hurmit-nerd-font"
		  "font-im-writing-nerd-font"
		  "font-iosevka-nerd-font"
		  "font-jetbrains-mono-nerd-font"
		  "font-lekton-nerd-font"
		  "font-liberation-nerd-font"
		  "font-meslo-lg-nerd-font"
		  "font-monoid-nerd-font"
		  "font-mononoki-nerd-font"
		  "font-mplus-nerd-font"
		  "font-noto-nerd-font"
		  "font-open-dyslexic-nerd-font"
		  "font-profont-nerd-font"
		  "font-proggy-clean-tt-nerd-font"
		  "font-roboto-mono-nerd-font"
		  "font-sauce-code-pro-nerd-font"
		  "font-shure-tech-mono-nerd-font"
		  "font-space-mono-nerd-font"
		  "font-terminess-ttf-nerd-font"
		  "font-tinos-nerd-font"
		  "font-ubuntu-nerd-font"
		  "font-victor-mono-nerd-font"
		];
	masApps = {
		"Telegram" = 747648890;
		"WhatsApp" = 310633997;
		"HP Smart" = 1474276998;
	};
	onActivation.cleanup = "zap";	
	onActivation.autoUpdate = true;	
	onActivation.upgrade = true;	
	};

      # nix.package = pkgs.nix;

      # Necessary for using flakes on this system.
      nix.settings.experimental-features = "nix-command flakes";

      # Enable alternative shell support in nix-darwin.
      # programs.fish.enable = true;

      # Set Git commit hash for darwin-version.
      system.configurationRevision = self.rev or self.dirtyRev or null;
      system.primaryUser = "cmartineza";
      # Used for backwards compatibility, please read the changelog before changing.
      # $ darwin-rebuild changelog
      system.stateVersion = 5;

      # The platform the configuration will be used on.
      nixpkgs.hostPlatform = "x86_64-darwin";
    };
  in
  {
    # Build darwin flake using:
    # $ darwin-rebuild build --flake .#simple
    darwinConfigurations."macos-air" = nix-darwin.lib.darwinSystem {
      modules = [ 
	configuration
        nix-homebrew.darwinModules.nix-homebrew
	#mac-app-util.darwinModules.default
        {
          nix-homebrew = {
            # Install Homebrew under the default prefix
            enable = true;

            # User owning the Homebrew prefix
            user = "cmartineza";

          };
	}
      ];
    };

    # Expose the package set, including overlays, for convenience.
    darwinPackages = self.darwinConfigurations."macos-air".pkgs;
  };
}
