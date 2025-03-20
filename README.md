# Share Your Folder

## Description
Share Your Folder is an enhanced Python script that allows you to easily share any folder on your local network. With improved security, better error handling, and an intuitive interface, this script works seamlessly on both Windows and Linux.

## Features
- **Cross-platform support**: Runs on both Windows and Linux.
- **Improved security**: Uses `SimpleHTTPRequestHandler` for better performance and security.
- **Easy setup**: Choose the folder you want to share using a graphical interface (Linux only).
- **Automatic IP detection**: Displays your local IP address without requiring external dependencies.
- **User-friendly error handling**: Prevents crashes and provides clear messages.
- **Browser-based access**: Other devices can access the shared folder by entering the host IP and port in a web browser.

## Download Links
- **Windows**: [Download ShareYourFolder v2.0 for Windows]([https://github.com/Mehran-Seifalinia/ShareYourFolder/raw/main/Windows/ShareYourFolder%20v1.1.exe](https://raw.githubusercontent.com/Mehran-Seifalinia/ShareYourFolder/refs/heads/main/ShareFolderv2.0.exe))
- **Linux**: [View Python source code](https://raw.githubusercontent.com/Mehran-Seifalinia/ShareYourFolder/main/Linux/ShareFolder.py)
- **Linux Installer Source**: [View](https://raw.githubusercontent.com/pyAref/ShareYourFolder/main/Linux/sharefolder_installer.py)

## How to Use
1. Download the appropriate file for your operating system.
2. Run the script and select the folder you want to share (Linux only) or place the script in the desired folder.
3. Enter the port number or use the default (8080).
4. Access the shared folder via `http://your-local-ip:port` in any web browser.

## Change Log
### Windows:
- [v1.0](https://github.com/Mehran-Seifalinia/ShareYourFolder/commit/2972152713597a4fcc41db57674af63c425a8545)
  - Initial release.
- [v1.1](https://github.com/Mehran-Seifalinia/ShareYourFolder/commit/e18f701ac8173f1f328fc6a69fb0efccb3868ab2)
  - Added colors for IP:PORT.
  - Show local IP address instead of 127.0.0.1.
- [v2.0.0](https://github.com/Mehran-Seifalinia/ShareYourFolder/commit/db3201fedab0c12955d0f34e89c96506c7e543be)
  - Added a graphical folder selection (Tkinter).
  - Improved exception handling and cleaner shutdown process.
  - Switched to `SimpleHTTPRequestHandler` for stability and security.
  - Optimized module installation workflow.
  - Enhanced local IP detection without using external modules.

### Linux:
- [v1.0.0](https://github.com/Mehran-Seifalinia/ShareYourFolder/commit/a6d872fe0165ef6f66f8918c243bf2884558cf0b)
  - Initial release.
- [v1.0.1](https://github.com/Mehran-Seifalinia/ShareYourFolder/commit/f220973ade7f7f07f1b28e68b44e3087a8b35dba)
  - Changed programming style from Basic to Professional.
- [v1.1.0](https://github.com/Mehran-Seifalinia/ShareYourFolder/commit/f220973ade7f7f07f1b28e68b44e3087a8b35dba#diff-5f8b34a0a255b67a1623b5e000b9eb1c16020346eb68df13896e123a0f94081b)
  - Added a Linux installer.
  - Added .sh file.
- [v1.2.0](https://github.com/Mehran-Seifalinia/ShareYourFolder/commit/1b34e1365de0c442a38acb578aad8c36e7d43bcb)
  - Added color for IP.
  - Show local IP address instead of 127.0.0.1.
- [v1.2.1](https://github.com/Mehran-Seifalinia/ShareYourFolder/commit/a990f12acf43aeafd082c3c7e621d4ffa9e6d73b)
  - Remove a Linux installer.
  - Remove .sh file.
  - Change the module install workflow.
  - Add except when the user stopped the server.
  - Fix minor bugs.
- [v2.0.0](https://github.com/Mehran-Seifalinia/ShareYourFolder/commit/db3201fedab0c12955d0f34e89c96506c7e543be)
  - Added a graphical folder selection (Tkinter).
  - Improved exception handling and cleaner shutdown process.
  - Switched to `SimpleHTTPRequestHandler` for stability and security.
  - Optimized module installation workflow.
  - Enhanced local IP detection without using external modules.

## License
This project is licensed under the [MIT License](https://github.com/Mehran-Seifalinia/ShareYourFolder/blob/main/LICENSE).

## Contributing
Contributions are welcome! Feel free to open issues and submit pull requests on the [GitHub repository](https://github.com/Mehran-Seifalinia/ShareYourFolder).
