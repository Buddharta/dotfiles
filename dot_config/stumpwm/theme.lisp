(set-font "-*-JetBrainsMono Nerd Font-*-*-*-*-13-*-*-*-*-*-*-*")
(setf *colors*
      '("#2E3440"                       ; black
        "#BF616A"                       ; red
        "#A3BE8C"                       ; green
        "#EBCB8B"                       ; yellow
        "#5E81AC"                       ; blue
        "#B48EAD"                       ; magenta
        "#88C0D0"                       ; cyan
        "#ECEFF4"                       ; white
        "#A3BE8C"                       ; spring-green
        "#D8DEE9"                       ; gray9
        ))

(update-color-map (current-screen))

(defparameter *foreground-color* "#ECEFF4")
 (defparameter *background-color* "#2E3440")
(defparameter *background-color* "#272C36")
(defparameter *border-color* "#5E81AC")
(set-frame-outline-width 1)
(setf *normal-border-width* 2)
(setf *maxsize-border-width* 4)
(setf *transient-border-width* 2)
(set-focus-color *border-color*)
(set-unfocus-color *background-color*)
