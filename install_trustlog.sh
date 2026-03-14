#!/bin/bash

echo "🚀 Initiating TrustLog Dynamics Enterprise Deployment..."

# Get absolute path of the directory
DIR="$(pwd)"
SERVICE_PATH="/etc/systemd/system/trustlog.service"

echo "⚙️  Forging systemd daemon architecture at $SERVICE_PATH..."

# Write the service file
sudo bash -c "cat > $SERVICE_PATH" << EOF
[Unit]
Description=TrustLog Dynamics - Financial Physics Governor
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$DIR
ExecStart=/usr/bin/python3 $DIR/trustlog_governor.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

echo "🛡️  Air-Gap established. Reloading OS daemon registry..."
sudo systemctl daemon-reload

echo "🔒 Arming TrustLog kill-switch on system boot..."
sudo systemctl enable trustlog.service

echo "⚡ Booting Physics Engine..."
sudo systemctl start trustlog.service

echo ""
echo "✅ TRUSTLOG DYNAMICS IS LIVE."
echo "To check the live heartbeat, run: sudo systemctl status trustlog.service"
