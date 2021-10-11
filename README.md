<p align="center">
  <img src="/gnitch.webp" title="gnitch"/>
</p>

- [Description](#desc)
- [Dependencies](#depend)
  - [Python](#python_dep)
  - [External](#ext_dep)
  - [Optional](#opt_dep)
- [Install](#install)
  - [Setuptools](#install_st)
- [Usage](#usage)
- [Default Keybinds](#def_keys)
  - [Page Navigation](#page_keys)
  - [Swap Views](#view_keys)
  - [Search](#search_keys)
  - [Quality Select](#quality_keys)
  - [Follow List](#follow_keys)
  - [Misc List](#misc_keys)
- [Configuration](#config)
  - [Config File](#conf_file)
  - [IRC](#irc)
	- [Weechat](#weechat)
	- [Irssi](#irssi)
  - [Followed List Import](#follow_import)

<a id="desc"></a>

# Description

[Reflex-Curses](https://github.com/Foldex/reflex-curses) is a TUI/CLI wrapper around streamlink, allowing for easy launching
of twitch.tv streams from your terminal.

This fork is only for testing purposes and not actively maintained. It uses GNOME apps like `totem` and `gnome-terminal` by default, apart from some other minor changes like WASD keybindings. Weechat is turned into a bare-bones read-only chat, but can open multiple instances.

<a id="depend"></a>

# Dependencies

<a id="python_dep"></a>

## Python

- Python 3.6
- python-requests

<a id="ext_dep"></a>

## External

- streamlink (launching streams)
- xclip (clipboard support)
- setsid (detach player from terminal)

<a id="opt_dep"></a>

## Optional

- firefox (default browser)
- totem (default player)
- gnome-terminal (default terminal)
- weechat (recommended) / irssi

<a id="install"></a>

# Installation

<a id="install_st"></a>

## Setuptools

System: `python setup.py install`

User: `python setup.py install --user`

<a id="usage"></a>

# Usage

```
glitch [OPTION]

OPTIONS
       NONE   Starts up the tui interface

       -a channel_name
              Add a twitch channel to your followed list

       -d channel_name
              Delete a twitch channel from your followed list

       -f     Prints out any followed streams that are online.

       -h, --help
              Print help message

       -i channel_name (--overwrite)
              Import channels followed by channel_name into your followed list.
              Default is to append to your current followed list, add --overwrite to replace it.
              NOTE: Currently limited to the results_limit (default: 75), large lists might not fully import.

       -v     Print version
```

More info available from the man page: `man glitch`

An example dmenu script is [Here](./scripts/dmenu_streams.sh)

<a id="def_keys"></a>

# Default Keybinds

<a id="page_keys"></a>

## Page Navigation

| Key       | Description                               |
|---------  |-----------------------------------------  |
| h         | Go back                                   |
| s         | Move cursor down                          |
| w         | Move cursor up                            |
| e / Enter | Enter menu or launch stream               |
| d         | Next Page                                 |
| a         | Previous page                             |
| r         | Refresh last query                        |

<a id="view_keys"></a>

## Swap Views

| Key       | Description                               |
|---------  |-----------------------------------------  |
| f         | Go to followed view                       |
| S         | Go to top streams view                    |
| G         | Go to top games view                      |
| v         | Go to VOD view                            |

<a id="search_keys"></a>

## Search

| Key       | Description                               |
|---------  |-----------------------------------------  |
| /         | General Search                            |
| g         | Search by Game Name (exact)               |

<a id="quality_keys"></a>

## Quality Selection

| Key       | Description                               |
|---------  |-----------------------------------------  |
| -         | Decrease quality                          |
| +         | Increase quality                          |

<a id="follow_keys"></a>

## Follow List

| Key       | Description                                |
|---------  |------------------------------------------  |
| A         | Add channel to followed list               |
| k         | Delete channel from followed list          |
| i         | Import follows from twitch user (limited)  |
| f         | Toggle online/all streams in followed list |

<a id="misc_keys"></a>

## Misc

| Key       | Description                               |
|---------  |-----------------------------------------  |
| c         | Open chat with chat method                |
| y         | Yank channel url                          |
| q         | Quit                                      |

<a id="config"></a>

# Configuration

Configuration files are stored in `~/.config/reflex-curses`

<a id="conf_file"></a>

## Config File

Config file is stored in `~/.config/reflex-curses/config`

Default Config Example:

```
[keys]
add = A
chat = c
delete = k
followed = f
game = g
back = h
import = i
down = s
up = w
forward = e
online = f
quit = q
refresh = r
t_stream = S
t_game = G
search = /
vods = v
yank = y
page+ = d
page- = a
qual+ = +
qual- = -

[exec]
browser = firefox --new-window
chat_method = weechat
player = totem
streamlink = streamlink --twitch-disable-hosting --twitch-disable-ads --player-passthrough hls
term = gnome-terminal --geometry=36x38 --zoom=1.2 --

[twitch]
client_id = caozjg12y6hjop39wx996mxn585yqyk
lang = en
results_limit = 75
retry_limit = 3

[ui]
default_state = followed
hl_color = red
l_win_color = white
r_win_color = green
quality = 720p
show_borders = True
show_keys = True

[irc]
address = irc.chat.twitch.tv
network = reflex
no_account = True
port = 6697
```

<a id="irc"></a>

## IRC

Glitch will by default connect to the saved network `reflex`.

To connect to twitch irc, you must either connect with the nick
`justinfanRANDOMNUMBERHERE` or use an [OAUTH Token](https://twitchapps.com/tmi/)
for your account.

For more info, see the [Twitch IRC
Documentation](https://dev.twitch.tv/docs/irc/guide)

<a id="weechat"></a>

### Weechat

Simplified, read-only chat window.

Uses `weechat -t` to create a temporary Weechat directory that will be deleted after closing.

<a id="irssi"></a>

### Irssi

Irssi unfortunately does not appear to support running commands through launch
arguments, so support is much more limited in comparison. Only the `network`
option is supported at this time. Launching chat will also only copy the join
command to your clipboard instead of automatically joining the channel.

If using an account, see the above section on getting your oauth token and add
it to your saved network.

<a id="follow_import"></a>

## Followed List Import

In addition to the -i flag, glitch can also mass import a list of channel names from a file.

Place entries (one per line) in `~/.config/reflex-curses/followed`

Glitch will resolve the Channel IDs on startup.
