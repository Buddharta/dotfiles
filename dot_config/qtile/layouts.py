from typing import List  # noqa: F401

from libqtile.config import Click, Drag, Key, Group, Match, Screen, Rule
from libqtile.command import lazy
from libqtile import layout

from functions import window_to_next_group, window_to_prev_group

#For multi-monitor
class CreateGroups:
    groups = []

    group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",] 
    group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
    #group_labels = ["", "", "", "", "", "", "", "", "", "",]
    #group_labels = ["", "", "", "", "",]
    #group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

    group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "treetab", "floating",]
    #group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Right", lazy.screen.next_group()),
        Key([mod], "Left", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

def init_groups():
    for i in range(len(group_names)):
        groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))
    return groups

class Layouts:
    
    def init_layout_theme():
    return {
            "margin":8,
            "border_width":2,
            "border_focus": "#668bd7",
            "border_normal": "1D2330"
            }
    layout_theme = init_layout_theme()

    def init_layouts():
        """
        Returns the layouts variable
        """
        layouts = [
            layout.MonadTall(margin=5, border_width=2, border_focus="#ffa00f", border_normal="#cfc2c2"),
            layout.MonadWide(margin=5, border_width=2, border_focus="#ffa00f", border_normal="#cfc2c2"),
            layout.Matrix(**layout_theme),
            layout.Bsp(**layout_theme),
            layout.Floating(**layout_theme),
            layout.RatioTile(**layout_theme),
            layout.Max(**layout_theme),
            layout.Columns(**layout_theme),
            layout.Stack(**layout_theme),
            layout.Tile(**layout_theme),
            layout.TreeTab(
                font="Ubuntu",
                fontsize=10,
                sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
                section_fontsize=10,
                border_width=2,
                bg_color="1c1f24",
                active_bg="c678dd",
                active_fg="000000",
                inactive_bg="a9a1e1",
                inactive_fg="1c1f24",
                padding_left=0,
                padding_x=0,
                padding_y=5,
                section_top=10,
                section_bottom=20,
                level_shift=8,
                vspace=3,
                panel_width=200
            ),
            layout.VerticalTile(**layout_theme),
            layout.Zoomy(**layout_theme)
        ]
        return layouts

#layout_theme = init_layout_theme()
