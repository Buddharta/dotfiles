(set-font "-*-JetBrainsMonoNerdFont-*-*-*-*-14-*-*-*-*-*-*-*")
;;;
;; Colors
;;;
;;;GRUVBOX
(defvar buddha-black "#282828")
(defvar buddha-red  "#CC241D")
(defvar buddha-softred  "#FB4934")
(defvar buddha-green  "#98971A")
(defvar buddha-softgreen  "#B8BB26")
(defvar buddha-yellow  "#D79921")
(defvar buddha-softyellow  "#FABD2F")
(defvar buddha-blue  "#458588")
(defvar buddha-softblue  "#83A598")
(defvar buddha-purple  "#B16286")
(defvar buddha-softpurple  "#D3869B")
(defvar buddha-aqua  "#689D6A")
(defvar buddha-softaqua  "#8EC07C")
(defvar buddha-orange  "#D65D0E")
(defvar buddha-softorange  "#FE8019")
(defvar buddha-white  "#fbf1c7")
(defvar buddha-gray  "#928374")


;;;NORD
(defvar buddha-nord0 "#2e3440")
(defvar buddha-nord1 "#3b4252")
(defvar buddha-nord2 "#434c5e")
(defvar buddha-nord3 "#4c566a")
(defvar buddha-nord4 "#d8dee9")
(defvar buddha-nord5 "#e5e9f0")
(defvar buddha-nord6 "#eceff4")
(defvar buddha-nord7 "#8fbcbb")
(defvar buddha-nord8 "#88c0d0")
(defvar buddha-nord9 "#81a1c1")
(defvar buddha-nord10 "#5e81ac")
(defvar buddha-nord11 "#bf616a")
(defvar buddha-nord12 "#d08770")
(defvar buddha-nord13 "#ebcb8b")
(defvar buddha-nord14 "#a3be8c")
(defvar buddha-nord15 "#b48ead")

(setq *colors*
      `(,buddha-black   ;; 0 black
        ,buddha-red  ;; 1 red
        ,buddha-green  ;; 2 green
        ,buddha-yellow  ;; 3 yellow
        ,buddha-blue  ;; 4 blue
        ,buddha-softpurple  ;; 5 magenta
        ,buddha-softblue   ;; 6 cyan
        ,buddha-white)) ;; 7 white

(when *initializing*
  (update-color-map (current-screen)))

(defparameter *foreground-color* "#FBF1C7")
(defparameter *background-color* "#1D2021")
(defparameter *border-color* "#EBDBB2")
(set-frame-outline-width 0)
(setf *normal-border-width* 2)
(setf *maxsize-border-width* 4)
(setf *transient-border-width* 2)
(set-focus-color *border-color*)
(set-unfocus-color *background-color*)
