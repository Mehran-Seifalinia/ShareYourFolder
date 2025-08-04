# Share Your Folder

## 📦 Description
**Share Your Folder** is a lightweight Python-based tool that lets you easily share a folder over your local network. It's ideal for quick file transfers between devices without setting up complex file servers.

This script supports both Windows and Linux platforms and can be compiled into a standalone executable.

## 🚀 Features
- ✅ **Cross-platform support**: Works on both **Windows** and **Linux**
- 🌐 **Browser-based access**: Access shared folders using your local IP and port
- 🧠 **Smart local IP detection**: Automatically shows the correct IP address, not just `127.0.0.1`
- 🎯 **Custom port selection**: Use the default or specify a different port
- 🖼️ **Graphical folder selection** (Linux only): Uses Tkinter to select folders easily
- 📛 **Friendly error handling**: Handles exceptions gracefully and provides clear messages

## 📥 Download Links
- **Windows**: [Download ShareYourFolder v2.0 for Windows](https://raw.githubusercontent.com/Mehran-Seifalinia/ShareYourFolder/refs/heads/main/ShareFolderv2.0.exe)
- **Linux**: [View Python source code](https://raw.githubusercontent.com/Mehran-Seifalinia/ShareYourFolder/main/Linux/ShareFolder.py)
- **Linux Installer Source**: [View Installer](https://raw.githubusercontent.com/pyAref/ShareYourFolder/main/Linux/sharefolder_installer.py)

## 🛠️ How to Use
1. Download the appropriate file for your system.
2. Run the script or executable.
3. Select the folder you wish to share (on Linux).
4. Enter a port number or use the default (`80`).
5. Access the shared folder via `http://your-local-ip:port` in a web browser.

## 📒 Change Log

### Windows:
- **v1.0**: Initial release.
- **v1.1**: Show real local IP; colored output.
- **v2.0.0**: GUI for folder selection; exception handling; SimpleHTTPRequestHandler for stability; better IP detection.
- **v2.0.1**: Fixed `EXE` error

### Linux:
- **v1.0.0**: Initial release.
- **v1.0.1**: Code style improvements.
- **v1.1.0**: Added installer script and `.sh` file.
- **v1.2.0**: Colored output; better IP handling.
- **v1.2.1**: Removed installer and `.sh`; bug fixes; new install workflow.
- **v2.0.0**: GUI for folder selection; exception handling; SimpleHTTPRequestHandler; better IP detection.
- **v2.0.1**: Fixed `EXE` error
- **2.1.0**: Refactored imports and exit handling for `EXE` compatibility and code clarity.

## License
Licensed under the [MIT License](https://github.com/Mehran-Seifalinia/ShareYourFolder/blob/main/LICENSE).

## 🤝 Contributing
Contributions are welcome! Open issues or submit pull requests on the [GitHub repository](https://github.com/Mehran-Seifalinia/ShareYourFolder)
