#!/bin/bash

nohup python3 server.py &
# Check if main.py is already in the cron job
if ! crontab -l | grep -q "main.py"; then
    (crontab -l 2>/dev/null; echo "0 1 * * * python3 /home/mrink/scraper-server/main.py") | crontab -
    echo "main.py added to the cron job."
else
    echo "main.py already exists in the cron job. No changes made."
fi