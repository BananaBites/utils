#!/usr/bin/env bash
# Checks/installs the pi agent and pi-web, then makes sure pi-web is NOT
# registered as a systemd service (we start it manually).
set -e

command -v pi     >/dev/null || npm install -g @earendil-works/pi-coding-agent
command -v pi-web >/dev/null || npm install -g @jmfederico/pi-web --allow-scripts=node-pty
hash -r

# Remove any service units left behind by an earlier `pi-web install`
rm -f ~/.config/systemd/user/pi-web* ~/.local/share/systemd/user/pi-web* /etc/systemd/system/pi-web*
systemctl --user daemon-reload >/dev/null 2>&1 || true

echo "pi:     $(pi --version)"
echo "pi-web: $(pi-web --version)"
echo "Start manually: pi-web-sessiond  +  PI_WEB_PORT=8504 pi-web-server  ->  http://127.0.0.1:8504"
