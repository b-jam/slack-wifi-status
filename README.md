#How to use

1. Customise the wifi config for yourself in the `slack-wifi-status.py`

2. Get the slack token from lastpass or generate one from a new app.

3. Put said token into the environment variable inside`local.wifislackstatus.plist`

4. `cp slack-wifi-status.py ~/Library/Application\ Support/slack-wifi-status.py`

5. `cp local.wifislackstatus.plist ~/Library/LaunchAgents/local.wifislackstatus.plist`

6. `launchctl load  ~/Library/LaunchAgents/local.wifislackstatus.plist`
