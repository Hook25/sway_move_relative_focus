# Sway move relative focus

This script implements negative coordinate moves for windows in sway. This is
useful because it enables the user to spawn a window to a position relative to
a corner of the currently active display.

# Installation

Download the script to a location on disk, for example `~/.local/bin`.
This script needs Python 3.8+, although it can be easily backported.
This script needs access to `swaymsg` and assumes it is in the PATH.

Run the following to download this to your `~/.local/bin` and making it executable:
```
curl https://raw.githubusercontent.com/Hook25/sway_move_relative_focus/refs/heads/master/sway_move_relative_focus.py > ~/.local/bin/sway_move_relative_focus.py
chmod +x ~/.local/bin/sway_move_relative_focus.py
```

# Example usage

Move telegram to the bottom left corner. Note the move position off screen.
This is because it seems that Sway takes a little bit of time to launch the
script. This makes the window flicker. To avoid this we float it in the
config and move it off screen. Note the 0 as X, it seems that if the move is
to a coordinate that is after the current display, the app miss-behaves (on
telegram right click on chats doesn't work anymore).
```sway
for_window [app_id="org.telegram.desktop"] border none, floating enable, move position 0 -2000, exec ~/.local/sway_move_relative_focus.py --additional-commands "resize set 400 515" '[app_id="org.telegram.desktop"]' -403 -540
```

Move pavucontrol to the bottom left corner.

```sway
for_window [app_id="org.pulseaudio.pavucontrol"] border none, floating enable, move position 0 -2000, exec ~/.local/sway_move_relative_focus.py --additional-commands "resize set 700 360" '[app_id="org.pulseaudio.pavucontrol"]' -700 -380
```
