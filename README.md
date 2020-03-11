#How to use

1. Get the slack token from lastpass or generate one from a new app.
2. Put said token into the environment variable inside`local.wifislackstatus.plist`
1. `cp slack-wifi-status.py ~/Library/Application\ Support/slack-wifi-status.py`
2. `cp local.wifislackstatus.plist ~/Library/LaunchAgents/local.wifislackstatus.plist`
3. `launchctl load  ~/Library/LaunchAgents/local.wifislackstatus.plist`