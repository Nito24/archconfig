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
#import os
#import subprocess
from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    #Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    

    Key([mod], "p", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn a command using rofi"),

    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),

    Key([], "Print", lazy.spawn("scrot 'Arch-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$HOME/screenshots'")),

    Key([mod], "f", lazy.window.toggle_floating()),
]

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Max(margin=2),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4, margin=2),
    #layout.Floating(),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()




colors = ["1e2120","262b2a","303635","3a403f","262b2a",'5f6763',"525a57",'989b97','adafac','cbcdcb','d9dbd9']
black = '1e2120'
white = '9b9e9a'
backgroundColor = '1f2322'


powerline = {"decorations": [PowerLineDecoration(path='arrow_right')]}
powerlineLeft = {"decorations": [PowerLineDecoration(path='arrow_left')]}
powerlineRoundLeft = {"decorations": [PowerLineDecoration(path='rounded_left')]}
powerlineRoundRight = {"decorations": [PowerLineDecoration(path='rounded_right')]}
powerlineBack = {"decorations": [PowerLineDecoration(path='back_slash')]}


screens = [
    Screen(
        top=bar.Bar(
            [
            widget.Sep(
		        foreground = colors[10],
                background = colors[10],
		        linewidth = 8,
                size_percent = 1,
		        ),

            widget.Image(
                filename = "~/.config/qtile/icons/arch-blue.png",
                background = colors[10],
                #mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(dmenu_run)},
                mouse_callbacks = {"Button1": lazy.spawncmd()},
                margin = 3,
                #**powerlineLeft
                ), 
           
            widget.Sep(
		        foreground = colors[10],
                background = colors[10],
		        linewidth = 2,
                size_percent = 1,
                **powerlineLeft
		        ),

            widget.Prompt(
                foreground = black,
                background = colors[9],
                #scroll = True, 
                #scroll_fixed_width = True,
                #scroll_clear = True,
                #width = 100,
                prompt = ' run  ',
                **powerlineLeft
                ),

		    #widget.CurrentLayoutIcon(
		    #    scale = 0.75,
		    #    foreground = colors[7],
		    #    background = colors[7],
		    #    padding = 12,
		    #    **powerlineLeft
		    #    ),

            widget.Clock(
                format = '   %H:%M    󰃭  %d/%m/%y',
                fontsize = 14,
                foreground = black,
                background= colors[8],
		        padding = 6, 
                mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn('alacritty -o font.size=9 -e calendar')},
                **powerlineLeft
                ),

            widget.CurrentLayoutIcon(
		        #custom_icon_paths = ["/home/nito/.config/qtile/layout-icons/gruvbox-dark0"],
                custom_icon_paths = ["/home/nito/.config/qtile/layout-icons/gruvbox-dark0"],
                scale = 0.75,
		        foreground = colors[7],
		        background = colors[7],
		        padding = 12,
		        **powerlineLeft
		        ),
            
            widget.Sep(
		        foreground = colors[8],
                background = colors[8],
		        linewidth = 3,
                size_percent = 1,
                **powerlineLeft
		        ),

            widget.GroupBox(
                disable_drag = True,
		        center_aligned = True,
		        highlight_method = 'line',
                highlight_color = colors[7],
                background = colors[8],
                active = colors[4],
		        padding = 8,
                **powerlineLeft,
                fontsize = 14,
                ),

            widget.Sep(
		        foreground = colors[8],
                background = colors[8],
		        linewidth = 0,
                size_percent = 1,
                **powerlineLeft
		        ),
            
            widget.Sep(
		        foreground = backgroundColor,
                background = backgroundColor,
		        linewidth = 0,
                size_percent = 1,
                padding = -2,
                **powerlineLeft
		        ),

            widget.TaskList(
                border = colors [8],
                highlight_method = 'border',
                #title_width_method = 'uniform',
                #max_title_width = 10,
                #padding = -1,
                rounded = False,
                #**powerline,
                ),

            widget.Sep(foreground = colors[7],background = backgroundColor,linewidth = 0,size_percent = 1,padding = 10,**powerline),


            #widget.Prompt(
            #    foreground = black,
            #    background = colors[9],
            #    **powerlineLeft
            #    ),

            #widget.Spacer(**powerlineRoundRight),

		    #widget.Clock(
                #format = '%H:%M %d/%m/%y',
                #fontsize = 14,
                #foreground = black,
                #background= colors[7],
		        #padding = -1,
                #**powerlineRoundLeft
                #),
            #widget.Spacer(),
		    #widget.Spacer(**powerline),

            #widget.OpenWeather(
                #location = "Coimbatore",
                #format = '{weather_details}',
                #update_interval = 1,
                #background = colors[5],
                #foreground = white,
                #**powerline
                #),

            #widget.CurrentLayout(
               #foreground = white,
               #background = colors[6],
               #**powerline
               #),

            #widget.CheckUpdates(
               # distro='Arch', 
               #no_update_string = 'No Updates',
               #display_format = '{updates}',
               #foreground = white,
               #background = colors[4],
               #**powerline
               #),
 
            widget.CPU(
                #format = '{load_percent}% ',
		        format = '  : {freq_current} GHz {load_percent:5.2f}%',
                foreground = white,
                background = colors[3], 
		        padding = 5,
		        **powerline
                ),
		
            #widget.ThermalSensor(
	            #format = 'Temp: {temp:.0f}{unit}',
                #foreground = white,
	            #background = colors [3],
	            #**powerline,
	            #),

            widget.Memory(
                format = '  : {MemUsed: .0f}{mm} ',
                background = colors[2],
                foreground = white,
        		padding = 5,
                mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn('alacritty -e htop')},
                **powerline
                ),
            
            widget.WidgetBox(
                    background = colors[1],
                    text_open = '',
                    text_closed = ' ',
                    widgets=[
                        #widget.TextBox(text="This widget is in the box"),
                        widget.Net(
                            format = '󰛳  : {down} ↓  ↑{up} ',
                            foreground = white,
                            background = colors[1],
                            #**powerline
                            ),

                        widget.Sep(foreground = colors[7],background = colors[1],linewidth = 1,size_percent = 55,padding = 10,),

                        widget.ThermalSensor(
                            foreground = white,
                            background = colors[1],
                            format = ' : {temp:.1f}{unit}  ',
                            ),

                        widget.Sep(foreground = colors[7],background = colors[1],linewidth = 1,size_percent = 55,padding = 10,),

                        widget.CheckUpdates(
                            colour_no_updates = white,
                            colour_have_updates = white,
                            background = colors[1],
                            display_format = ' : {updates} updates',
                            no_update_string='No updates',
                            update_interval = 1800,
                            ),
                        ],
                    **powerline
                ),

            #widget.Net(
            #    format = '󰛳  : {down} ↓  ↑{up} ',
            #    foreground = white,
            #    background = colors[1],
            #    **powerline
            #    ),

            widget.Systray(
                foreground = white,
                background = colors[0],
                ),

	        widget.Sep(
		        foreground = colors[0],
		        linewidth = 10,
                size_percent = 1,
		        ),
            ],
            24,
            background = backgroundColor,
            margin = 2,
        ),
    ),
]



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry

        Match(title='Volume Control'),#volume
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"