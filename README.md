Usage monitor
=============
This python app monitors usage of cpu (5 min average), memory and disk and sends notification to Telegram chat on reaching predefined thresholds 

INSTALLATION
------------

Create local config:

```
cd config
cp _local.py local.py
```

Fill in local.py with Telegram bot credentials. You may also override default usage thresholds there

You may need to edit `usage_monitor.service` and replace `ExecStart` and `WorkingDirectory` pathes. Install and start `usage_monitor.service`:

```
sudo cp usage_monitor.service /etc/systemd/system/usage_monitor.service
sudo systemctl daemon-reload
sudo systemctl enable usage_monitor.service
sudo systemctl start usage_monitor.service

```