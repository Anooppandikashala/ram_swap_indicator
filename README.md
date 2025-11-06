## ram_swap_indicator

How to autostart this script at login.

1. Download this script and Install dependencies
    ```bash
   sudo apt install python3-gi gir1.2-appindicator3-0.1
    ```
2. Move your script to a safe location <br>
    Place your script somewhere stable (so it won’t get deleted accidentally):
   ```bash
   mkdir -p ~/.local/bin
   mv ~/Downloads/ram_swap_indicator.py ~/.local/bin/
   chmod +x ~/.local/bin/ram_swap_indicator.py 
   ```
3. Create a .desktop autostart entry
    ```bash
   mkdir -p ~/.config/autostart
   nano ~/.config/autostart/ram_swap_indicator.desktop
   ```
   Paste the following content:
    ```bash
   [Desktop Entry]
    Type=Application
    Exec=/usr/bin/python3 /home/username/.local/bin/ram_swap_indicator.py
    Hidden=false
    NoDisplay=false
    X-GNOME-Autostart-enabled=true
    Name=RAM & SWAP Indicator
    Comment=Shows RAM and swap usage in system tray
   ```
   replace your username 
4. Copy your autostart file to your local applications directory
   ```bash
    mkdir -p ~/.local/share/applications
    cp ~/.config/autostart/ram_swap_indicator.desktop ~/.local/share/applications/
    update-desktop-database ~/.local/share/applications/ 
   ```
5. Test manually
    ```bash
   gtk-launch ram_swap_indicator
   ```