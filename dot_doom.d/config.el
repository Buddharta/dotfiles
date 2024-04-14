;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!


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
 (setq doom-font (font-spec :family "JetBrainsMono" :size 14 :weight 'semi-light)
       doom-variable-pitch-font (font-spec :family "sans" :size 16))

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-monokai)

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/org/")

;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type t)


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

 ;;(setq doom-font (font-spec :family "Ubuntu Nerd Font" :size 152 :weight 'semi-light)
       ;;doom-variable-pitch-font (font-spec :family "Source Code Pro")
       ;;doom-unicode-font (font-spec :family "Monospace" :size 152)
       ;;doom-big-font (font-spec :family "Ubuntu Nerd Font" :size 260))

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
;;
;; ### Set Okular as the default PDF viewer.
(eval-after-load "tex"
  '(setcar (cdr (assoc 'output-pdf TeX-view-program-selection)) "Okular"))

(setq TeX-view-program-list '(("Okular" "okular %s")))

(add-hook 'org-mode-hook
          '(lambda ()
             (delete '("\\.pdf\\'" . default) org-file-apps) 
             (add-to-list 'org-file-apps '("\\.pdf\\'" . "okular %s"))))
(setq latex-run-command "pdflatex")
(setq tex-command "pdftex")

;; Pomodoro
(require 'org)
(setq org-clock-sound "~/org/bowl.wav")


;; org-roam
(use-package! org-roam
  :custom
  (org-roam-directory "~/roam")
  :config
  (org-roam-setup))

;; CV exporter
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
