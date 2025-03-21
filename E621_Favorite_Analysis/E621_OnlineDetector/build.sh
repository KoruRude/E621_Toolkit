#! /bin/bash
echo "      __        __   ___     __       __  ___  ___        __ "
echo "|__/ |__) |  | |  \ |__     /__  \ / /__   |  |__   |\/| /__ "
echo "|  \ |  \ \__/ |__/ |___    .__/  |  .__/  |  |___  |  | .__/"
echo "E621 Delta Faverite - 29Aug2024"
echo ""
echo "Make sure all scripts in folder are makred as executeable and you are in the directory of the scripts. If you run into issues and you know me, contace me via discord; otherwise, idk why you have this but good luck!"
echo ""
echo "This script uses E621's built in API system inorder to download JSON files for user infromation and will detect and report changes in the data!"
echo ""
echo "Generator Running now..."
python3 generator.py
chmod +x runner*
echo "Build Complete! All you need is to run the built script!"
