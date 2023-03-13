# -*- coding: utf-8 -*-

##
# Author: bw3u <berkcan@vivaldi.net>
# Github: @bw3u
# Gitlab: @bw3u
# Reddit: @panlazy
#
# License: MIT

# Imports #
import os
import subprocess
from libqtile import qtile
from libqtile.config import (
    Group,
    KeyChord,
    Key,
    Match,
    Screen,
    EzClick as Click,
    EzDrag as Drag,
)
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentwindow is not none:
        i = qtile.groups.index(qtile.currentgroup)
        qtile.currentwindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentwindow is not none:
        i = qtile.groups.index(qtile.currentgroup)
        qtile.currentwindow.togroup(qtile.groups[i + 1].name)

##### kill all windows #####
    
@lazy.function
def kill_all_windows():
        for window in qtile.current_group.windows:
        window.kill()

@lazy.function
def kill_all_windows_minus_current():
        for window in qtile.current_group.windows:
                if window != qtile.current_window:
                        window.kill()

class pwa:
    def __init__(self):
        pass

    @staticmethod
    def notion():
        return "firefox --profile-directory=default --app=https://notion.so"

    @staticmethod
    def music():
        return "firefox --profile-directory=Default --app=https://music.youtube.com/"

    @staticmethod
    def spotify():
        return "firefox --profile-directory=Default --app=https://open.spotify.com/"

    @staticmethod
    def youtube():
        return "firefox --user-data-dir=Default --app=https://www.youtube.com"

    @staticmethod
    def calendar():
        return "firefox --profile-directory=Default --app=https://calendar.google.com/calendar/"

    @staticmethod
    def habitica():
        return "firefox --profile-directory=Default --app=https://habitica.com/"


# Defaults #
mod = "mod4"  # Setting mod key to "SUPER"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

myTerm = "alacritty"  # Setting terminal to "alacritty"
browser = "firefox"  # Setting browser to "Firefox Developer Edition"

# Keybindings #
keys = [

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod, "control"], "space", lazy.next_layout()),

# TOGGLE FLOATING LAYOUT
    Key([mod], "shift"], "space", lazy.window.toggle_floating()),

# SUPER + FUNCTION KEYS

    Key([mod], "m", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "t", lazy.spawn('xterm')),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "Space", lazy.spawn('nwggrid -p -o 0.4')),
    Key([mod], "Return", lazy.spawn('alacritty')),
    Key([mod], "KP_Enter", lazy.spawn('alacritty')),
    Key([mod], "x", lazy.shutdown()),
    Key([mod], "b", lazy.spawn('firefox')),
    Key([mod], "f", lazy.spawn('thunar')),
    Key([mod], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),

# SUPER + SHIFT KEYS

    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()), 
    Key([mod, "shift"], "x", lazy.shutdown()),
# CONTROL + ALT KEYS

    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "t", lazy.spawn('xterm')),
    Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),

# CONTROL + SHIFT KEYS

    Key([mod2, "shift"], "Escape", lazy.spawn('lxtask')),

# SCREENSHOTS

    Key([], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
    Key([mod2], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),

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
]

#Groups
groups = [
    Group(
        "1", 
        label="", 
        matches=[
            Match(wm_class=["firefox"]),
        ],
    ),
    Group(
        "2",
        label="",
        matches=[
            Match(wm_class=["Alacritty"]),
        ],
    ),
    Group(
        "3",
        label="",
        matches=[
            Match(wm_class=["Steam"]),
        ],
    ),
    Group(
        "4",
        label="﬏",
        matches=[
            Match(wm_class=["code-oss"]),
        ],
    ),
    Group(
        "5",
         label="",
         matches=[
             Match(wm_class=["Spotify"]),
         ],
    ),
    Group(
        "6",
        label="",
        matches=[
            Match(wm_class=["discord", "TelegramDesktop"])
        ]),
    Group("7", label=""),
    Group("8", label="﵂"),
    Group(
        "9",
        label="",
        matches=[
            Match(wm_class=["zoom"]),
        ],
    ),
    Group("0", label=""),
]

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

# Navy and Ivory based. (["main color", "2nd color, if diff will be gradient"])
colors = [
    #["#021b21", "#021b21"],  # 0
    ["#1e2021", "#1e2021"],  # 0
    ["#032c36", "#065f73"],  # 1
    # ["#032c36", "#61778d"],# 1 this one is bit lighter
    ["#e8dfd6", "#e8dfd6"],  # 2
    ["#c2454e", "#c2454e"],  # 3
    ["#44b5b1", "#44b5b1"],  # 4
    ["#9ed9d8", "#9ed9d8"],  # 5
    #["#f6f6c9", "#f6f6c9"],  # 6
    ["#6095c5", "#6095c5"],  # 6
    ["#61778d", "#61778d"],  # 7
    #["#e2c5dc", "#e2c5dc"],  # 8
    ["#dfe9f3", "#dfe9f3"],  # 8
    ["#5e8d87", "#5e8d87"],  # 9
    ["#032c36", "#032c36"],  # 10
    ["#2e3340", "#2e3340"],  # 11
    ["#065f73", "#065f73"],  # 12
    #["#8a7a63", "#8a7a63"],  # 13
    ["#bfd4e7", "#bfd4e7"],  # 13
    ["#A4947D", "#A4947D"],  # 14
    #["#BDAD96", "#BDAD96"],  # 15
    ["#9fbfdc", "#9fbfdc"],  # 15
    #["#a2d9b1", "#a2d9b1"],  # 16
    ["#7faad0", "#7faad0"],  # 16
    ["#ffffff", "#ffffff"],  # 17
]

layout_theme = {
    "border_width": 2,
    "margin": 4,
    "border_focus": "#6095c5",
    "border_normal": "#021b21",
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.Floating(**layout_theme),
]


# Widgets #

widget_defaults = dict(
    font="Noto Sans Font",
    fontsize=10,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[6],
                ),
                widget.TextBox(
                    #text="  ",
                    text="  ",
                    font="Iosevka Nerd Font",
                    fontsize="15",
                    background=colors[6],
                    foreground=colors[0],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('jgmenu_run')}
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",              
                    fontsize="33",
                    padding=-3,
                    background=colors[6],
                    foreground=colors[0],
                ),
                widget.GroupBox(
                    font="Ubuntu Nerd Font",
                    fontsize=13,
                    margin_y=3,
                    margin_x=6,
                    padding_y=7,
                    padding_x=-3,
                    borderwidth=4,
                    active=colors[17],
                    inactive=colors[0],
                    rounded=False,
                    highlight_color=colors[13],
                    highlight_method="text",
                    this_current_screen_border=colors[6],
                    block_highlight_text_color=colors[0],
                ),
                widget.Prompt(
                    background=colors[2],
                    foreground=colors[0],
                    font="Iosevka Nerd Font",
                    fontsize=18,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox(
                #    text="\ue0be",
                #    font="Inconsolata for powerline",
                #    fontsize=33,
                #    padding=0,
                #    background=colors[0],
                #    foreground=colors[2],
                #),
                #widget.WindowName(
                #    font="Iosevka Nerd Font",
                #    fontsize=15,
                #    background=colors[2],
                #    foreground=colors[0],
                #),
                #widget.TextBox(
                #    text="\ue0be",
                #    font="Inconsolata for powerline",
                #    fontsize="33",
                #    padding=0,
                #    background=colors[2],
                #    foreground=colors[0],
                #),
                widget.Spacer(length=1195),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background=colors[0],
                    foreground=colors[13],
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    scale=0.45,
                    padding=0,
                    background=colors[13],
                    foreground=colors[0],
                    font="Iosevka Nerd Font",
                    fontsize=14,
                ),
                widget.CurrentLayout(
                    font="Noto Sans Font",
                    fontsize=13,
                    background=colors[13],
                    foreground=colors[0],
                ),
                #widget.TextBox(
                #    text="\ue0be",
                #    font="Inconsolata for powerline",
                #    fontsize="33",
                #    padding=0,
                #    background=colors[10],
                #    foreground=colors[11],
                #),
                #widget.TextBox(
                #    text=" ",
                #    font="Iosevka Nerd Font",
                #    fontsize=18,
                #    padding=0,
                #    background=colors[11],
                #    foreground=colors[2],
                #),
                #widget.DF(
                #    fmt=" {}",
                #    font="Iosevka Nerd Font",
                #    fontsize=15,
                #    partition="/home",
                #    format="{uf}{m} ({r:.0f}%)",
                #    visible_on_warn=False,
                #    background=colors[11],
                #    foreground=colors[2],
                #    padding=5,
                #    mouse_callbacks={
                #        "Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")
                #    },
                #),
                #widget.TextBox(
                #    text="\ue0be",
                #    font="Inconsolata for powerline",
                #    fontsize="33",
                #    padding=0,
                #    background=colors[11],
                #    foreground=colors[12],
                #),
                #widget.TextBox(
                #    text=" ",
                #    font="Iosevka Nerd Font",
                #    fontsize=16,
                #    foreground=colors[2],
                #    background=colors[12],
                #    padding=0,
                #    mouse_callbacks={
                #        "Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")
                #    },
                #),
                #widget.Memory(
                #    background=colors[12],
                #    foreground=colors[2],
                #    font="Iosevka Nerd Font",
                #    fontsize=15,
                #    format="{MemUsed: .0f} MB",
                #    mouse_callbacks={
                #        "Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")
                #    },
                #),
                #widget.Sep(
                #    padding=8,
                #    linewidth=0,
                #    background=colors[12],
                #),
                #widget.TextBox(
                #    text="\ue0be",
                #    font="Inconsolata for powerline",
                #    fontsize="33",
                #    padding=0,
                #    background=colors[12],
                #    foreground=colors[7],
                #),
                #widget.Sep(
                #    padding=6,
                #    linewidth=0,
                #    background=colors[7],
                #),
                #widget.Systray(
                #    background=colors[7],
                #    foreground=colors[2],
                #    icons_size=18,
                #    padding=4,
                #),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background=colors[13],
                    foreground=colors[15],
                ),
                widget.TextBox(
                    text="墳 ",
                    font="Iosevka Nerd Font",
                    fontsize=18,
                    background=colors[15],
                    foreground=colors[0],
                ),
                widget.Systray(
                       background=colors[10],
                       icon_size=20,
                       padding = 4
                ),
                # Doesn't work with Spotify so its disabled!
                # widget.TextBox(
                #    text="\u2572",
                #    font="Inconsolata for powerline",
                #    fontsize="33",
                #    padding=0,
                #    background=colors[13],
                #    foreground=colors[0],
                # ),
                # widget.Mpd2(
                #   background=colors[13],
                #   foreground=colors[0],
                #   idle_message=" ",
                #   idle_format="{idle_message} Not Playing",
                #   status_format="  {artist}/{title} [{updating_db}]",
                #   font="Iosevka Nerd Font",
                #   fontsize=15,
                # ),
                # This one works with Spotify, enable if you want!
                # widget.Mpris2(
                #    background=colors[13],
                #    foreground=colors[0],
                #    name="spotify",
                #    objname="org.mpris.MediaPlayer2.spotify",
                #    fmt="\u2572   {}",
                #    display_metadata=["xesam:title", "xesam:artist"],
                #    scroll_chars=20,
                #    font="Iosevka Nerd Font",
                #    fontsize=15,
                # ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background=colors[15],
                    foreground=colors[16],
                ),
                #widget.KeyboardLayout(
                #    fmt=" {} הּ ",
                #    font="Iosevka Nerd Font",
                #    configured_keyboards=["us", "gb", "tr"],
                #    fontsize="14",
                #    padding=0,
                #    background=colors[14],
                #    foreground=colors[0],
                #),
                #widget.TextBox(
                #    text="\ue0be",
                #    font="Inconsolata for powerline",
                #    fontsize="33",
                 #   padding=0,
                #    background=colors[14],
                #    foreground=colors[15],
                #),
                widget.TextBox(
                    text="   ",
                    font="Iosevka Nerd Font",
                    fontsize="14",
                    padding=0,
                    background=colors[16],
                    foreground=colors[0],
                ),
                widget.Clock(
                    font="Noto Sans Font",
                    foreground=colors[0],
                    background=colors[16],
                    fontsize=13,
                    format="%A, %d %b %Y"
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[16],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="12",
                    padding=0,
                    background=colors[16],
                    foreground=colors[6],
                ),
                widget.TextBox(
                    text=" ",
                    font="Iosevka Nerd Font",
                    fontsize="18",
                    padding=0,
                    background=colors[6],
                    foreground=colors[0],
                ),
                widget.Clock(
                    font="Noto Sans Font",
                    foreground=colors[0],
                    background=colors[6],
                    fontsize=13,
                    format="%H:%M",
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=0,
                    background=colors[6],
                    foreground=colors[6],
                ),
                #widget.Sep(
                #    padding=6,
                #    linewidth=0,
                #    background=colors[6],
                #),
            ],
            22,
            opacity=1,
            background=colors[0],
            margin=[4, 4, 0, 4],
        ),
        # left=bar.Gap(5),
        # right=bar.Gap(5),
    ),
]

# Helper functions #
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


# Mod + Mouse drag -> Floating
mouse = [
    Drag("M-1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click("M-2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        # default_float_rules include: utility, notification, toolbar, splash, dialog,
        # file_progress, confirm, download and error.
        *layout.Floating.default_float_rules,
        Match(title="Confirmation"),
        Match(title="Qalculate!"),
        Match(wm_class="OBS"),
        Match(wm_class="MultiMC"),
        Match(wm_class="Tilda"),
        #Match(wm_class="Steam"),
    ]
)

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

