#    _   _   _           ____ _______ _ _                         __ _       
#   | \ | (_) |         / __ \__   __(_) |                       / _(_)      
#   |  \| | | |_ ___   | |  | | | |   _| | ___    ___ ___  _ __ | |_ _  __ _ 
#   | . ` | | __/ _ \  | |  | | | |  | | |/ _ \  / __/ _ \| '_ \|  _| |/ _` |
#   | |\  | | || (_) | | |__| | | |  | | |  __/ | (_| (_) | | | | | | | (_| |
#   |_| \_|_|\__\___/   \___\_\ |_|  |_|_|\___|  \___\___/|_| |_|_| |_|\__, |
#                                                                       __/ |
#                                                                      |___/ 
						
from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

# Define mod key
mod = "mod4"

terminal = guess_terminal()


#-----------------------------------------------------------
#	KEY SHORTCUTS
#-----------------------------------------------------------

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # "Alt-tab"
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
	
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

    # Make floating window follow the layout again
    Key([mod], "f", lazy.window.toggle_floating()),

    # Spawn terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Spawn rofi
    #Key([mod], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn a command using rofi"),
    # Spawn command
    Key([mod], "p", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    # Spawn Dmenu
    #Key([mod], 'r', lazy.run_extension(extension.DmenuRun(
    #    dmenu_command = 'dmenu_run -c -l 12',
    #    dmenu_prompt="  ",
    #    #dmenu_font="Andika-8",
    #    background="#1f2322",
    #    #foreground="#9b9e9a",
    #    foreground="#cdcbcd",
    #    selected_background="#262b2a",
    #    selected_foreground="#fff",
    #    dmenu_height=24,
    #    ))),
	
    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),

    # Kill window
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # Qtile actions
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    # Screenshot using scrot
    Key([], "Print", lazy.spawn("scrot 'Arch-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$HOME/screenshots'")),

    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessnotif up"), desc="Brightness up"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessnotif down"), desc="Brightness down"),

    Key([], "XF86AudioRaiseVolume", lazy.spawn("volume-set up"), desc="Volume up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("volume-set down"), desc="Volume down"),
    Key([], "XF86AudioMute", lazy.spawn("volume-set mute"), desc="Volume toggle mute"),

    Key([], "XF86AudioPlay", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause"), lazy.spawn("musicnotif")),
    Key([], "XF86AudioStop", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop"), lazy.spawn("musicnotif")),
    Key([], "XF86AudioPrev", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous"), lazy.spawn("musicnotif")),
    Key([], "XF86AudioNext", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next"), lazy.spawn("musicnotif")),

    Key([mod], "Left", lazy.screen.prev_group()),
    Key([mod], "Right", lazy.screen.next_group()),
]



#-----------------------------------------------------------
#	GROUPS
#-----------------------------------------------------------

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


#-----------------------------------------------------------
#	LAYOUTS
#-----------------------------------------------------------

layouts = [
    layout.Max(margin=2),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4, margin=2),
]


#-----------------------------------------------------------
#	WIDGETS AND TOP BAR
#-----------------------------------------------------------

widget_defaults = dict(
    font="sans",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Colors define
colors = ['1e2120','262b2a','303635','3a403f',
	  '262b2a','5f6763','525a57','989b97',
	  'adafac','cbcdcb','d9dbd9']
black = '1e2120'
white = '9b9e9a'
backgroundColor = '1f2322'

# Powerline decorations
powerline = {"decorations": [PowerLineDecoration(path='arrow_right')]}
powerlineLeft = {"decorations": [PowerLineDecoration(path='arrow_left')]}
powerlineRoundLeft = {"decorations": [PowerLineDecoration(path='rounded_left')]}
powerlineRoundRight = {"decorations": [PowerLineDecoration(path='rounded_right')]}
powerlineBack = {"decorations": [PowerLineDecoration(path='back_slash')]}

# Top bar
screens = [
    Screen(
        top=bar.Bar(
            [
            widget.Sep(foreground = colors[10], background = colors[10], linewidth = 8, size_percent = 1),

            widget.Image(
                filename = "~/.config/qtile/icons/arch-blue.png",
                background = colors[10],
                mouse_callbacks = {"Button1": lazy.spawncmd()},
                margin = 3,
                ), 
           
            widget.Sep(foreground = colors[10], background = colors[10], linewidth = 2, size_percent = 1, **powerlineLeft),
		    
            widget.Prompt( # Fixed size not working, it resizes with text
                foreground = black,
                background = colors[9],
                prompt = ' run  ',
                **powerlineLeft
                ), 

            widget.Clock(
                format = '   %H:%M    󰃭  %d/%m/%y',
                fontsize = 14,
                foreground = black,
                background= colors[8],
		padding = 6, 
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('calendar2 curr'), 'Button5': lambda: qtile.cmd_spawn('calendar2 next'),'Button4': lambda: qtile.cmd_spawn('calendar2 prev')},
                **powerlineLeft
                ),

            widget.CurrentLayoutIcon(
                custom_icon_paths = ["/home/nito/.config/qtile/layout-icons/gruvbox-dark0"],
                scale = 0.75,
		foreground = colors[7],
		background = colors[7],
		padding = 12,
		**powerlineLeft
		),
            
            widget.Sep(foreground = colors[8], background = colors[8], linewidth = 3, size_percent = 1, **powerlineLeft),

            widget.GroupBox(
		#hide_unused=True,  Only show used ones
                disable_drag = True, # Disable dragging groups to change the order
		center_aligned = True,
		highlight_method = 'line',
                highlight_color = colors[7],
                background = colors[8],
                active = colors[4],
		padding = 8,
                **powerlineLeft,
                fontsize = 14,
                ),

            widget.Sep(foreground = colors[8], background = colors[8], linewidth = 0, size_percent = 1, **powerlineLeft),
            
            widget.Sep(foreground = backgroundColor, background = backgroundColor, linewidth = 0, size_percent = 1, padding = -2, **powerlineLeft),

            widget.TaskList(
                border = colors [8],
                highlight_method = 'border',
                rounded = False,
                ),

            widget.Sep(foreground = colors[7],background = backgroundColor,linewidth = 0,size_percent = 1,padding = 10,**powerline),
 
            widget.CPU( # Fixed width doesnt work
		format = '  : {freq_current} GHz {load_percent:5.2f}%',
                foreground = white,
                background = colors[3], 
		padding = 5,
		**powerline
                ),
	
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
                	widget.Net( # Fixed width doesnt work
                        	format = '󰛳  : {down} ↓  ↑{up} ',
                        	foreground = white,
                        	background = colors[1],
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
                        	colour_have_updates = colors[10],
                        	background = colors[1],
                        	display_format = ' : {updates} updates',
                        	n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        