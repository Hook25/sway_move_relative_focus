# Sway move relative focus

This script implements negative coordinate moves for windows in sway. This is
useful because it enables the user to spawn a window to a position relative to
a corner of the currently active display.

# Installation

Download the script to a location on disk, for example `~/.local/bin`.
This script needs Python 3.8+, although it can be easily backported.
This script needs access to `swaymsg` and assumes it is in the PATH.

# Example usage

Move telegram to the bottom left corner. Note the move position off screen.
This is because it seems that Sway takes a little bit of time to launch the
script. This makes the window flicker. To avoid this we float it in the
config and move it off screen.
```sway
for_window [app_id="org.telegram.desktop"] border none, floating enable, move position 6000 6000, exec ~/.local/sway_move_relative_focus.py --additional-commands "resize set 400 515" '[app_id="org.telegram.desktop"]' -403 -540
```

Move pavucontrol to the bottom left corner. Note the same move but less
drammatic. It seems that if moved too much off screen this doesn't work.

```sway
for_window [app_id="org.pulseaudio.pavucontrol"] border none, floating enable, move position 0 -1000, exec ~/.local/sway_move_relative_focus.py --additional-commands "resize set 700 360" '[app_id="org.pulseaudio.pavucontrol"]' -700 -380
```
