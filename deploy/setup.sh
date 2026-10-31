#!/usr/bin/env bash
# Runs inside the Proxmox CT as root. Idempotent. Installs the Arsenal MCP server as a systemd
# service on port 8810 with a bearer token generated on first run.
set -euo pipefail

APP=/opt/arsenal
apt-get update -qq
DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3-venv python3-pip openssl ca-certificates >/dev/null

id arsenal &>/dev/null || useradd -r -d "$APP" -s /usr/sbin/nologin arsenal
mkdir -p "$APP"

python3 -m venv "$APP/venv"
"$APP/venv/bin/pip" install -q --upgrade pip
"$APP/venv/bin/pip" install -q -r "$APP/requirements-mcp.txt"

if [ ! -f "$APP/.env" ]; then
  {
    echo "ARSENAL_MCP_TOKEN=$(openssl rand -hex 24)"
    echo "ARSENAL_MCP_PORT=8810"
  } > "$APP/.env"
  chmod 600 "$APP/.env"
fi
chown -R arsenal:arsenal "$APP"

cat > /etc/systemd/system/arsenal-mcp.service <<'UNIT'
[Unit]
Description=Kitsune Arsenal MCP server
After=network-online.target
Wants=network-online.target

[Service]
User=arsenal
WorkingDirectory=/opt/arsenal
EnvironmentFile=/opt/arsenal/.env
ExecStart=/opt/arsenal/venv/bin/python /opt/arsenal/arsenal_mcp.py
Restart=on-failure
RestartSec=3

[Install]
WantedBy=multi-user.target
UNIT

systemctl daemon-reload
systemctl enable --now arsenal-mcp
sleep 3
systemctl is-active arsenal-mcp
echo "TOKEN=$(grep ARSENAL_MCP_TOKEN "$APP/.env" | cut -d= -f2)"
