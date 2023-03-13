# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.command import lazy

from libqtile.widget import Spacer

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

myTerm = "alacritty" # My terminal of choice


keys = [
# SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "t", lazy.spawn('xterm')),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "d", lazy.spawn('nwggrid -p -o 0.4')),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn('alacritty')),
    Key([mod], "KP_Enter", lazy.spawn('alacritty')),
    Key([mod], "x", lazy.shutdown()),

# SUPER + SHIFT KEYS

    Key([mod, "shift"], "Return", lazy.spawn('thunar')),
    Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
#    Key([mod, "shift"], "d", lazy.spawn(home + '/.config/qtile/scripts/dmenu.sh')),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()), Key([mod, "shift"], "x", lazy.shutdown()),
# CONTROL + ALT KEYS

    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "t", lazy.spawn('xterm')),
    Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),

# ALT + ... KEYS

    Key(["mod1"], "f", lazy.spawn('firefox')),
    Key(["mod1"], "m", lazy.spawn('thunar')),
    Key(["mod1"], "w", lazy.spawn('garuda-welcome')),


# CONTROL + SHIFT KEYS

    Key([mod2, "shift"], "Escape", lazy.spawn('lxtask')),


# SCREENSHOTS

    Key([], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
    Key([mod2], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
#    Key([mod2, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

# MULTIMEDIA KEYS

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

         ### Treetab controls
    Key([mod, "control"], "k",
        lazy.layout.section_up(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "control"], "j",
        lazy.layout.section_down(),
        desc='Move down a section in treetab'
        ),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),]

 #keys = [
 #
 ## QTILE LAYOUT KEYS
     #Key([mod], "n", lazy.layout.normalize()),
     #Key([mod], "control"], "space", lazy.next_layout()),
 #
 ## TOGGLE FLOATING LAYOUT
     #Key([mod, "shift"], "space", lazy.window.toggle_floating()),
 #
 ## SUPER + FUNCTION KEYS
 #
 ##    Key([mod], "m", lazy.toggle.Max()),
     #Key([mod], "q", lazy.window.kill()),
     #Key([mod], "t", lazy.spawn('xterm')),
     #Key([mod], "v", lazy.spawn('pavucontrol')),
     #Key([mod], "Space", lazy.spawn('nwggrid -p -o 0.4')),
     #Key([mod], "Return", lazy.spawn('alacritty')),
     #Key([mod], "KP_Enter", lazy.spawn('alacritty')),
     #Key([mod], "x", lazy.shutdown()),
     #Key([mod], "b", lazy.spawn('firefox')),
     #Key([mod], "f", lazy.spawn('thunar')),
     #Key([mod], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
 #
 ## SUPER + SHIFT KEYS
 #
     #Key([mod, "shift"], "q", lazy.window.kill()),
     #Key([mod, "shift"], "r", lazy.restart()),
     #Key([mod, "control"], "r", lazy.restart()), 
     #Key([mod, "shift"], "x", lazy.shutdown()),
 ## CONTROL + ALT KEYS
 #
     #Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
     #Key(["mod1", "control"], "t", lazy.spawn('xterm')),
     #Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),
 #
 ## CONTROL + SHIFT KEYS
 #
     #Key([mod2, "shift"], "Escape", lazy.spawn('lxtask')),
 #
 ## SCREENSHOTS
 #
     #Key([], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
     #Key([mod2], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
 #
 ## MULTIMEDIA KEYS
 #
 ## INCREASE/DECREASE BRIGHTNESS
     #Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
     #Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
 #
 ## INCREASE/DECREASE/MUTE VOLUME
     #Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
     #Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
     #Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
 #
     #Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
     #Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
     #Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
     #Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
 #
 ##    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
 ##    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
 ##    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
 ##    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),
 #
 ## CHANGE FOCUS
     #Key([mod], "Up", lazy.layout.up()),
     #Key([mod], "Down", lazy.layout.down()),
     #Key([mod], "Left", lazy.layout.left()),
     #Key([mod], "Right", lazy.layout.right()),
     #Key([mod], "k", lazy.layout.up()),
     #Key([mod], "j", lazy.layout.down()),
     #Key([mod], "h", lazy.layout.left()),
     #Key([mod], "l", lazy.layout.right()),
 #
 ## RESIZE UP, DOWN, LEFT, RIGHT
     #Key([mod, "control"], "l",
         #lazy.layout.grow_right(),
         #lazy.layout.grow(),
         #lazy.layout.increase_ratio(),
         #lazy.layout.delete(),
         #),
     #Key([mod, "control"], "Right",
         #lazy.layout.grow_right(),
         #lazy.layout.grow(),
         #lazy.layout.increase_ratio(),
         #lazy.layout.delete(),
         #),
     #Key([mod, "control"], "h",
         #lazy.layout.grow_left(),
         #lazy.layout.shrink(),
         #lazy.layout.decrease_ratio(),
         #lazy.layout.add(),
         #),
     #Key([mod, "control"], "Left",
         #lazy.layout.grow_left(),
         #lazy.layout.shrink(),
         #lazy.layout.decrease_ratio(),
         #lazy.layout.add(),
         #),
     #Key([mod, "control"], "k",
         #lazy.layout.grow_up(),
         #lazy.layout.grow(),
         #lazy.layout.decrease_nmaster(),
         #),
     #Key([mod, "control"], "Up",
         #lazy.layout.grow_up(),
         #lazy.layout.grow(),
         #lazy.layout.decrease_nmaster(),
         #),
     #Key([mod, "control"], "j",
         #lazy.layout.grow_down(),
         #lazy.layout.shrink(),
         #lazy.layout.increase_nmaster(),
         #),
     #Key([mod, "control"], "Down",
         #lazy.layout.grow_down(),
         #lazy.layout.shrink(),
         #lazy.layout.increase_nmaster(),
         #),
 #
 ## FLIP LAYOUT FOR MONADTALL/MONADWIDE
     #Key([mod, "shift"], "f", lazy.layout.flip()),
 #
 ## FLIP LAYOUT FOR BSP
     #Key([mod, "mod1"], "k", lazy.layout.flip_up()),
     #Key([mod, "mod1"], "j", lazy.layout.flip_down()),
     #Key([mod, "mod1"], "l", lazy.layout.flip_right()),
     #Key([mod, "mod1"], "h", lazy.layout.flip_left()),
 #
 ## MOVE WINDOWS UP OR DOWN BSP LAYOUT
     #Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
     #Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
     #Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
     #Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
 #
          #### Treetab controls
     #Key([mod, "control"], "k",
         #lazy.layout.section_up(),
         #desc='Move up a section in treetab'
         #),
     #Key([mod, "control"], "j",
         #lazy.layout.section_down(),
         #desc='Move down a section in treetab'
         #),
 #
 #
 ## MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
     #Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
     #Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
     #Key([mod, "shift"], "Left", lazy.layout.swap_left()),
     #Key([mod, "shift"], "Right", lazy.layout.swap_right()), 
 #]


groups = []

# FOR QWERTY KEYBOARDS

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",] 
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "treetab", "floating",]
group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]

#group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["", "", "", "", "",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Right", lazy.screen.next_group()),
        Key([mod], "Left", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


def init_layout_theme():
    return {"margin":10,
            "border_width":2,
            "border_focus": "#fe8019",
            "border_normal": "#83a598"
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(margin=16, border_width=2, border_focus="#ffa00f", border_normal="#0ac2c2"),
    layout.MonadWide(margin=16, border_width=2, border_focus="#ffa00f", border_normal="#0ac2c2"),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Stack(**layout_theme),
    layout.Tile(**layout_theme),
    layout.TreeTab(
        sections=['FIRST', 'SECOND'],
        bg_color = '#282828',
        active_bg = '#000fff',
        inactive_bg = '#458588',
        padding_y =5,
        section_top =10,
        panel_width = 280),
    layout.VerticalTile(**layout_theme),
    layout.Zoomy(**layout_theme)
]

# COLORS FOR THE BAR


def init_colors():
    return [["#282828", "#282828"],  # 0
            ["#32302f", "#32302f"],  # 1
            ["#1d2021", "#1d2021"],  # 2
            ["#3c3836", "#3c3036"],  # 3
            ["#44b5b1", "#44b5b1"],  # 4
            ["#9ed9d8", "#9ed9d8"],  # 5
            ["#6095c5", "#6095c5"],  # 6
            ["#61778d", "#61778d"],  # 7
            ["#8f3f71", "#8f3f71"],  # 8
            ["#b16286", "#b16286"],  # 9 
            ["#504945", "#504945"],  # 10
            ["#665c54", "#665c54"],  # 11
            ["#7c6f64", "#7c6f64"],  # 12
            ["#a89984", "#a89984"],  # 13
            ["#bdae93", "#bdae93"],  # 14
            ["#928374", "#928374"],  # 15
            ["#d5c4a1", "#d5c4a1"],  # 16
            ["#ebdbb2", "#ebdbb2"],  # 17
            ["#fbf1c7", "#fbf1c7"],  # 18
            ["#1d2021", "#1d2021"],  # 19
            ["#689d6a", "#689d6a"],  # 20
            ["#8ec07c", "#8ec07c"],  # 21 
            ["#cc241d", "#cc241d"],  # 22
            ["#fb4934", "#fb4934"],  # 23
            ["#458588", "#458588"],  # 24
            ["#83a598", "#83a598"],  # 25 
            ["#d65d0e", "#d65d0e"],  # 26
            ["#fe8819", "#fe8819"],  # 27
            ["#d79921", "#d79921"],  # 28
            ["#fabd3f", "#fabd2f"]]  # 29  


colors = init_colors()

def base(fg='text', bg='dark'):
    return {'foreground': colors[18],'background': colors[19]}


# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Ubuntu Nerd Font",
                fontsize = 9,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [

                 widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[15],
                        background = colors[15]
                        ),
                 widget.TextBox(
                    #text="  ",
                    text="  ",
                    font="Iosevka Nerd Font",
                    fontsize="16",
                    background=colors[15],
                    foreground=colors[19],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('jgmenu_run')}
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",              
                    fontsize="33",
                    padding=-3,
                    background=colors[15],
                    foreground=colors[19],
                ),              #
                #widget.Image(
                        #filename = "~/.config/qtile/icons/python.png",
                        #iconsize = 9,
                        #background = colors[24],
                        #mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('jgmenu_run')}
                        #),

               widget.GroupBox(

            **base(bg=colors[18]),
            font='Ubuntu Nerd Font',

                    fontsize = 12,
                    margin_y = 3,
                    margin_x = 2,
                    padding_y = 5,
                    padding_x = 4,
                    borderwidth = 3,

            active=colors[8],
            inactive=colors[6],
            rounded= True,
            highlight_method='line',
            urgent_alert_method='line',
            urgent_border=colors[22],
            this_current_screen_border=colors[9],
            this_screen_border=colors[9],
            other_current_screen_border=colors[13],
            other_screen_border=colors[9],
            disable_drag=True
                        ),
                widget.TaskList(
                    highlight_method = 'block', # or block
                    icon_size=17,
                    max_title_width=150,
                    rounded=True,
                    padding_x=0,
                    padding_y=0,
                    margin_y=0,
                    fontsize=14,
                    block=colors[4],
                    foreground=colors[18],
                    margin=2,
                    txt_floating='🗗',
                    txt_minimized='>_ ',
                    borderwidth = 1,
                    background=colors[19],
                    #unfocused_border = 'border'
                ),
              widget.TextBox(
                       text = '',
                       background = colors[19],
                       foreground = colors[23],
                       padding = 0,
                       fontsize = 37
                       ),
               widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[18],
                       background = colors[23],
                       padding = 0,
                       scale = 0.7
                       ),
               widget.CurrentLayout(
                      font = "Ubuntu Nerd Font Bold",
                      fontsize = 12,
                      foreground = colors[18],
                      background = colors[23]
                        ),
               #widget.TextBox(
                        #text = '',
                        #background = colors[22],
                        #foreground = colors[19],
                        #padding = 0,
                        #fontsize = 37
                        #),
                 #widget.Net(
                          #font="Ubuntu Nerd Font",
                          #fontsize=12,
                         ## Here enter your network name
                          #interface=["wlp6s0"],
                          #format = '{down} ↓↑ {up}',
                          #foreground=colors[18],
                          #background=colors[19],
                          #padding = 0,
                          #),
              widget.TextBox(
                       text = '',
                       background = colors[23],
                       foreground = colors[29],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.ThermalSensor(
                       font="Ubuntu Nerd Font",
                       fontsize = 12,
                       foreground = colors[18],
                       background = colors[29],
                       threshold = 90,
                       padding = 5
                       ),
               widget.Memory(
                       font="Ubuntu Nerd Font",
                        format = '{MemUsed: .0f}M/{MemTotal: .0f}M',
                        update_interval = 1,
                        fontsize = 12,
                        measure_mem = 'M',
                        foreground = colors[18],
                        background = colors[29],
                        #mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                       ),
                       widget.TextBox(
                       text = '',
                       background = colors[29],
                       foreground = colors[21],
                       padding = 0,
                       fontsize = 37,
                       ),
               widget.Clock(
                        font="Ubuntu Nerd Font",
                        format="%d-%m-%y | %H:%M",
                        foreground = colors[18],
                        background = colors[21],
                        fontsize = 12,
                        mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + 'cal')},
                        ),

                widget.TextBox(
                    text = '',
                    background=colors[21],
                    foreground=colors[24],
                    padding = 0,
                    fontsize = 37
                ),   
               widget.Systray(
                       background=colors[24],
                       icon_size=20,
                       padding = 4
                       ),
               ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=0.85, background= "000000")),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=0.85, background= "000000"))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(title='branchdialog'),
    Match(title='Open File'),
    Match(title='pinentry'),
    Match(wm_class='ssh-askpass'),
    Match(wm_class='lxpolkit'),
    Match(wm_class='Lxpolkit'),
    Match(wm_class='yad'),
    Match(wm_class='Yad'),
    Match(wm_class='Cairo-dock'),
    Match(wm_class='cairo-dock'),


],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
