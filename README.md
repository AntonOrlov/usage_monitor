Usage monitor
=============
This python utility monitors usage of cpu (5 min average), memory and disk and sends notification to Telegram chat on reaching predefined thresholds 

INSTALLATION
------------

Clone repository:

```
git clone https://github.com/AntonOrlov/usage_monitor.git

```

Create local config:

```
cd usage_monitor
cp config/_local.py config/local.py
nano config/local.py
```

Fill in local.py with Telegram bot credentials. You may override default usage thresholds there

You may need to edit `usage_monitor.service` and replace `ExecStart` and `WorkingDirectory` pathes. Install and start `usage_monitor.service`:

```
sudo cp usage_monitor.service /etc/systemd/system/usage_monitor.service
sudo systemctl daemon-reload
sudo systemctl enable usage_monitor.service
sudo systemctl start usage_monitor.service

```

REQUIREMENTS
------------

The application requires python 3.6 or above