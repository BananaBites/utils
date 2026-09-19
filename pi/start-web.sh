#!/usr/bin/env bash
# Starts pi-web (session daemon + web server). Ctrl+C stops both.
set -e

pi-web-sessiond &
trap 'kill $(jobs -p) 2>/dev/null' EXIT

PI_WEB_PORT="${PI_WEB_PORT:-8504}" pi-web-server
