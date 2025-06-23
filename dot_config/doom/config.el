;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!

;; Here are some additional functions/macros that could help you configure Doom:
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.

;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets.
(setq user-full-name "Carlos Martinez"
      user-mail-address "cmartineza@ciencias.com")

;; Doom exposes five (optional) variables for controlling fonts in Doom. Here
;; are the three important ones:
;;
;; + `doom-font'
;; + `doom-variable-pitch-font'
;; + `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;;
;; They all accept either a font-spec, font string ("Input Mono-12"), or xlfd
;; font string. You generally only need these two:

(setq doom-font
      (cl-find-if #'doom-font-exists-p
                  '("JetBrainsMonoNerdFont:pixelsize=16"
                    "SourceCodePro:pixelsize=16"
                    "FiraCode:pixelsize=16"
                    "UbuntuNerdFont:pixelsize=16")))

;;(setq doom-font (font-spec :family "JetBrainsMono" :size 14 :weight 'semi-light)
;;       doom-variable-pitch-font (font-spec :family "sans" :size 16))

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-gruvbox)


;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type t)

;(use-package! fira-code-mode
;  :custom (fira-code-mode-disabled-ligatures '("[]" "x"))  ; ligatures you don't want
;  :hook prog-mode)                                         ; mode to enable fira-code-mode in

;;   ____  ____  ______      __  _______  ____  ______
;;  / __ \/ __ \/ ____/     /  |/  / __ \/ __ \/ ____/
;; / / / / /_/ / / ________/ /|_/ / / / / / / / __/
;;/ /_/ / _, _/ /_/ /_____/ /  / / /_/ / /_/ / /___
;;\____/_/ |_|\____/     /_/  /_/\____/_____/_____/
;;
;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/org/")
(setq org-default-notes-file (concat org-directory "/notes.org"))
(setq org-hide-emphasis-markers t)

(font-lock-add-keywords 'org-mode
                          '(("^ *\\([-]\\) "
                             (0 (prog1 () (compose-region (match-beginning 1) (match-end 1) "•"))))))

(let* ((variable-tuple
          (cond ((x-list-fonts "ETBembo")         '(:font "ETBembo"))
                ((x-list-fonts "Source Sans Pro") '(:font "Source Sans Pro"))
                ((x-list-fonts "Lucida Grande")   '(:font "Lucida Grande"))
                ((x-list-fonts "Verdana")         '(:font "Verdana"))
                ((x-family-fonts "Sans Serif")    '(:family "Sans Serif"))
                (nil (warn "Cannot find a Sans Serif Font.  Install Source Sans Pro."))))
         (base-font-color     (face-foreground 'default nil 'default))
         (headline           `(:inherit default :weight bold :foreground ,base-font-color)))

    (custom-theme-set-faces
     'user
     `(org-level-8 ((t (,@headline ,@variable-tuple))))
     `(org-level-7 ((t (,@headline ,@variable-tuple))))
     `(org-level-6 ((t (,@headline ,@variable-tuple))))
     `(org-level-5 ((t (,@headline ,@variable-tuple))))
     `(org-level-4 ((t (,@headline ,@variable-tuple :height 1.1))))
     `(org-level-3 ((t (,@headline ,@variable-tuple :height 1.25))))
     `(org-level-2 ((t (,@headline ,@variable-tuple :height 1.5))))
     `(org-level-1 ((t (,@headline ,@variable-tuple :height 1.75))))
     `(org-document-title ((t (,@headline ,@variable-tuple :height 2.0 :underline nil))))))

(add-hook 'org-mode-hook 'variable-pitch-mode)
(add-hook 'org-mode-hook 'visual-line-mode)

;; This is for exporting CV from org I dont know if it works.
;;  CV exporter
;;(use-package ox-altacv
;;    :load-path "/home/buddharta/org/org-cv/"
;;    :init (require 'ox-altacv))
;;
;;(use-package ox-moderncv
;;    :load-path "/home/buddharta/org/org-cv/"
;;    :init (require 'ox-moderncv))
;;
;;(use-package ox-hugocv
;;    :load-path "/home/buddharta/org/org-cv/"
;;    :init (require 'ox-hugocv))
;;
;;(after! org
;;  (use-package! ox-extra
;;    :config
;;    (ox-extras-activate '(latex-header-blocks ignore-headlines))))
;;
;;
;;(after! org
;;  ;; Import ox-latex to get org-latex-classes and other funcitonality
;;  ;; for exporting to LaTeX from org
;;  (use-package! ox-latex
;;    :init
;;    ;; code here will run immediately
;;    :config
;;    ;; code here will run after the package is loaded
;;    (setq org-latex-pdf-process
;;          '("pdflatex -interaction nonstopmode -output-directory %o %f"
;;            "bibtex %b"
;;            "pdflatex -interaction nonstopmode -output-directory %o %f"
;;            "pdflatex -interaction nonstopmode -output-directory %o %f"))
;;    (setq org-latex-with-hyperref nil) ;; stop org adding hypersetup{author..} to latex export
;;    ;; (setq org-latex-prefer-user-labels t)
;;
;;    ;; deleted unwanted file extensions after latexMK
;;    (setq org-latex-logfiles-extensions
;;          (quote ("lof" "lot" "tex~" "aux" "idx" "log" "out" "toc" "nav" "snm" "vrb" "dvi" "fdb_latexmk" "blg" "brf" "fls" "entoc" "ps" "spl" "bbl" "xmpi" "run.xml" "bcf" "acn" "acr" "alg" "glg" "gls" "ist")))
;;
;;    (unless (boundp 'org-latex-classes)
;;      (setq org-latex-classes nil)))

; Clojure configuration
;(load! "+clojure")

;: Clojure LSP Configuration
;(load! "+lsp")

;;(with-eval-after-load 'ox-latex
;;(add-to-list 'org-latex-classes
;;             '("org-plain-latex"
;;               "\\documentclass{article}
;;           [NO-DEFAULT-PACKAGES]
;;           [PACKAGES]
;;           [EXTRA]"
;;               ("\\section{%s}" . "\\section*{%s}")
;;               ("\\subsection{%s}" . "\\subsection*{%s}")
;;               ("\\subsubsection{%s}" . "\\subsubsection*{%s}")
;;               ("\\paragraph{%s}" . "\\paragraph*{%s}")
;;               ("\\subparagraph{%s}" . "\\subparagraph*{%s}"))))



;; ### Set Okular as the default PDF viewer.
(eval-after-load "tex"
  '(setcar (cdr (assoc 'output-pdf TeX-view-program-selection)) "Okular"))

(setq TeX-view-program-list '(("Okular" "okular %s")))

(setq TeX-evince-sync-view '(("Okular" "okular %s")))

(add-hook 'org-mode-hook
          (lambda()
             (delete '("\\.pdf\\'" . default) org-file-apps)
             (add-to-list 'org-file-apps '("\\.pdf\\'" . "okular %s"))))
(setq latex-run-command "pdflat frex")
(setq tex-command "pdftex")

;; org-roam
(use-package! org-roam
  :custom
  (org-roam-directory "~/roam")
  :config
  (org-roam-setup))

(setq tramp-defaut-method "ssh")
(setq python-shell-interpreter "~/miniconda3/bin/python3")
(setq conda-anaconda-home (expand-file-name "~/miniconda3"))
(setq conda-env-home-directory (expand-file-name "~/miniconda3"))

;; JULIA CONFIG
(use-package! julia-repl
  :hook (julia-mode . julia-repl-mode)
  :init (setenv "JULIA_NUM_THREADS" "8")
  :config
  ;; Set the terminal backend
  (julia-repl-set-terminal-backend 'vterm)
  ;; Keybindings for quickly sending code to the REPL
  (define-key julia-repl-mode-map (kbd "<C-RET>") 'my/julia-repl-send-cell)
  (define-key julia-repl-mode-map (kbd "<M-RET>") 'julia-repl-send-line))


(setq lsp-julia-package-dir "~/.julia/packages")
(setq lsp-julia-flags `("-J ~/.julia/packages/LanguageServer"))

(add-hook 'julia-mode-hook 'julia-repl-mode)
(add-hook 'julia-mode-hook 'company-mode)
(add-hook 'julia-mode-hook 'eglot-jl-init)
(add-hook 'julia-mode-hook 'eglot-ensure)

(setq eldoc-box-max-pixel-width 450)
(setq eldoc-idle-delay 2)
(setq eldoc-box-cleanup-interval 1)

(after! eglot-jl
  (setq eglot-jl-language-server-project eglot-jl-base))
