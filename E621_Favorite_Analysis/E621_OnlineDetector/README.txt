      __        __   ___     __       __  ___  ___        __
|__/ |__) |  | |  \ |__     /__  \ / /__   |  |__   |\/| /__
|  \ |  \ \__/ |__/ |___    .__/  |  .__/  |  |___  |  | .__/
E621 Delta Faverite - 29Aug2024

Make sure all scripts in folder are makred as executeable and you are in the directory of the scripts. If you run into issues and you know me, contace me via discord; otherwise, idk why you have this but good luck!

This script uses E621's built in API system inorder to download JSON files for user infromation and will detect and report changes in the data!


USAGE:
One the first run, it will generate a change because it is compareing the recived data to nothing.
Once the program detects a change in the json it will notify the Discord webhook in the format of "Change Detected for <username(id)> on <$(date)>". A log will also be generated at the same time that will be stored int the log directory with the format "<username>_<date>.json"
So, you just need to set up a script, SystemD service, or a chrontab to automatically run it pereodically (or run the built script manually).
To get started run "build.sh"

INTERPRUTATION:
It is worth noteing that E621's API does not require a username for the target, just an ID number so you can technically put whatever you want in that field on build.

The long-of-the-short-of-it is that when a change was detected, the change must have occoured between the time that it was detected and logged, and the last time that the program was ran. I would recomend running it pereodically so you know just about when the last time that it was ran.

In my case this is every 10 minutes, this means that if a log is generated and I get an alert through Discord webhook, the change occoured within the last 10 minutes of that notification (unless network issues occoured).
How do I know what change was detected? Compare the difference between the latest log, and log for the same user that precedded it. This is how you can tell the difference, through the logs!
