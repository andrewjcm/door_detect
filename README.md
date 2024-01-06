# Raspberry PI Door Sensor

### Turn into a service
```commandline
[Unit]
Description=Door Detect service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=username
WorkingDirectory=/home/username/door_detect
ExecStart=/home/username/door_detect/venv/bin/python /home/username/door_detect/main.py

[Install]
WantedBy=multi-user.target
```
#### Start the service

```commandline
sudo systemctl start doordetect
```

#### Enable to start on boot

```commandline
sudo systemctl enable doordetect
```