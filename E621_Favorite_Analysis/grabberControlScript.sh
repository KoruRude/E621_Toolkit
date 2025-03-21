#! /bin/bash
echo "      __        __   ___     __       __  ___  ___        __ "
echo "|__/ |__) |  | |  \ |__     /__  \ / /__   |  |__   |\/| /__ "
echo "|  \ |  \ \__/ |__/ |___    .__/  |  .__/  |  |___  |  | .__/"
echo "E621 JSON Favorites Scraper - 29Aug2024"
echo ""
echo "Make sure all scripts in folder are makred as executeable and you are in the directory of the scripts. If you run into issues and you know me, contace me via discord; otherwise, idk why you have this but good luck!"
echo ""
echo "This script uses E621's built in API system inorder to download JSON files for the pages of someone's E621 favorites. If you are wanting to do a buld download of media, I recomend 'https://github.com/McSib/e621_downloader'"
echo ""
echo "Generator Running now..."
rm jsonGrabber.sh
python3 generateGrabber.py
chmod +x jsonGrabber.sh
sh jsonGrabber.sh
