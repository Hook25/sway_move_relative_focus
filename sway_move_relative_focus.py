#!/usr/bin/env python3
import argparse
import json
from subprocess import check_output, check_call


def get_displays():
    return json.loads(check_output(["swaymsg", "-t", "get_outputs"]))


def set_window_position(
    selector: str,
    additional_commands: str,
    absolute_x: int,
    absolute_y: int,
    workspace: int,
):
    additional_commands = additional_commands.strip().rstrip(",")
    if additional_commands:
        additional_commands += ","
    command = (
        f"{selector} {additional_commands} "
        f"move to workspace number {workspace},"
        f"move position {absolute_x} {absolute_y},"
    )
    check_call(["swaymsg", command])


def set_window_relative_position(
    selector: str,
    additional_commands: str,
    position_x: int,
    position_y: int,
):
    displays = get_displays()
    active_display = next(filter(lambda display: display.get("focused"), displays))
    if position_x < 0:
        position_x += active_display["rect"]["width"]
    if position_y < 0:
        position_y += active_display["rect"]["height"]
    workspace = active_display["current_workspace"]
    set_window_position(
        selector, additional_commands, position_x, position_y, workspace
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description="Set window position relative to the active display."
    )
    parser.add_argument(
        "selector",
        type=str,
        help="""Sway window selector (e.g., '[class="firefox"]').""",
    )
    parser.add_argument(
        "--additional-commands",
        type=str,
        default="",
        help="Additional swaymsg commands to prepend to the move command",
    )
    parser.add_argument(
        "position_x",
        type=int,
        help="X position. If negative, relative to the right edge of the active display.",
    )
    parser.add_argument(
        "position_y",
        type=int,
        help="Y position. If negative, relative to the bottom edge of the active display.",
    )

    return parser.parse_args()


def main():
    args = parse_args()
    set_window_relative_position(
        args.selector,
        args.additional_commands,
        args.position_x,
        args.position_y,
    )


if __name__ == "__main__":
    main()
