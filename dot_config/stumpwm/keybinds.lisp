(set-prefix-key (stumpwm:kbd "s-c"))

;; Commands denfined by me for special apps

;; Alacritty
(defcommand alacritty () ()
  (run-or-raise "alacritty -e tmux" '(:class "Alacritty")))
(define-key *top-map* (stumpwm:kbd "s-RET") "alacritty")

;; Firefox
(defcommand firefox () ()
  (run-or-raise "firefox" '(:class "firefox")))
(define-key *top-map* (kbd "s-f") "firefox")
(define-key *root-map* (stumpwm:kbd "f") "exec firefox")

;; Flameshot
(defcommand flameshot ()()
  (run-or-raise "flameshot gui -p ~/Pictures/screenshots" '(:class "flameshot")))
(define-key *top-map* (kbd "SunPrint_Screen") "flameshot")

;; Rofi
(defcommand rofi-run () ()
  (run-shell-command "rofi -show run"))

(define-key *top-map* (kbd "s-x") "rofi-run")

;; Thunar
(defcommand thunar () ()
  (run-or-raise "thunar" '(:class "thunar")))
(define-key *top-map* (kbd "s-F") "thunar")
;; Dmenu
(defcommand dmenu-run () ()
  (run-shell-command "dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'JetBrains Nerd Font:bold:pixelsize=14'"))
(define-key *top-map* (kbd "s-d") "dmenu-run")

;; (define-key *top-map* (kbd "s-d") "exec")
(define-key *top-map* (kbd "s-m") "fullscreen")
(define-key *top-map* (kbd "s-w") "windowlist")
;; resize
(define-key *top-map* (kbd "C-s-l") "resize 10 0")
(define-key *top-map* (kbd "C-s-h") "resize 0 10")
;; groups
;;(define-key *top-map* (kbd "s-l") "gnext")
;;(define-key *top-map* (kbd "s-h") "gprev")
;; stump commands
(define-key *top-map* (kbd "s-;") "colon")
(define-key *top-map* (kbd "s-:") "eval")
(define-key *top-map* (kbd "s-R") "restart-hard")
;; modeline
(define-key *top-map* (kbd "s-y") "mode-line")
;; frames
(define-key *top-map* (kbd "s-b") "fclear")
(define-key *top-map* (kbd "s-|") "hsplit")
(define-key *top-map* (kbd "s--") "vsplit")
(define-key *top-map* (kbd "s-r") "remove-split")
;; navigation
(define-key *top-map* (kbd "s-SPC") "frame-windowlist")
(define-key *top-map* (kbd "s-TAB") "fnext")
(define-key *top-map* (kbd "s-h") "move-focus left")
(define-key *top-map* (kbd "s-j") "move-focus down")
(define-key *top-map* (kbd "s-k") "move-focus up")
(define-key *top-map* (kbd "s-l") "move-focus right")
;; window movement
(define-key *top-map* (kbd "s-H") "move-window left")
(define-key *top-map* (kbd "s-J") "move-window down")
(define-key *top-map* (kbd "s-K") "move-window up")
(define-key *top-map* (kbd "s-L") "move-window right")
(define-key *top-map* (kbd "s-n") "pull-hidden-next")
(define-key *top-map* (kbd "s-p") "pull-hidden-previous")
(define-key *top-map* (kbd "s-M") "exchange-direction down")
(define-key *top-map* (kbd "s-N") "exchange-direction left")
(define-key *top-map* (kbd "s-<") "exchange-direction up")
(define-key *top-map* (kbd "s->") "exchange-direction right")
(define-key *top-map* (kbd "s-q") "kill-window")
;; groups
(define-key *top-map* (kbd "s-g") "grouplist")
(define-key *top-map* (kbd "s-1") "gselect 1")
(define-key *top-map* (kbd "s-2") "gselect 2")
(define-key *top-map* (kbd "s-3") "gselect 3")
(define-key *top-map* (kbd "s-4") "gselect 4")
(define-key *top-map* (kbd "s-5") "gselect 5")
(define-key *top-map* (kbd "s-6") "gselect 6")
(define-key *top-map* (kbd "s-7") "gselect 7")
(define-key *top-map* (kbd "s-8") "gselect 8")
(define-key *top-map* (kbd "s-9") "gselect 9")
(define-key *top-map* (kbd "s-0") "gselect 0")
(define-key *top-map* (kbd "s-!") "gmove 1")
(define-key *top-map* (kbd "s-@") "gmove 2")
(define-key *top-map* (kbd "s-#") "gmove 3")
(define-key *top-map* (kbd "s-$") "gmove 4")
(define-key *top-map* (kbd "s-%") "gmove 5")
(define-key *top-map* (kbd "s-^") "gmove 6")
(define-key *top-map* (kbd "s-&") "gmove 7")
(define-key *top-map* (kbd "s-*") "gmove 8")
(define-key *top-map* (kbd "s-(") "gmove 9")
(define-key *top-map* (kbd "s-)") "gmove 0")
