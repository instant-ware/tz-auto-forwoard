# TZ AUTO FORWARD - Telegram Auto File Forwarder

A Python-based Telegram automation tool developed by **INSTANTWARE** under the **TZSMX** branding.

TZ AUTO FORWARD is designed to automatically forward existing and new media files between Telegram channels. Using the Telethon library, this tool allows users to transfer photos, videos, documents, audio, and voice messages from a source channel to a destination channel.

The tool supports old file forwarding, automatic new message forwarding, batch processing, Telegram API authentication, session management, and a colorful terminal interface.

<p align="center">
  <img src="https://img.shields.io/badge/PROJECT-TZSMX-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/DEVELOPER-INSTANTWARE-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/PYTHON-3.8%2B-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/STATUS-OPEN%20SOURCE-success?style=for-the-badge" />
</p>---

**Developer:** INSTANTWARE  
**GitHub:** https://github.com/instant-ware  
**Telegram:** https://t.me/InstantWare_dev

---

## ⚠️ Disclaimer

This tool is intended for legitimate Telegram channel management and authorized file forwarding purposes.

Do not use this tool for spam, harassment, unauthorized distribution, or malicious activities. Always respect Telegram's Terms of Service and content ownership.

The developer is not responsible for any misuse of this software. Use responsibly and only with proper authorization.

---

## 🚀 Features

- **Old File Forwarding:** Forward previously existing media files from a source channel.
- **Automatic New File Forwarding:** Automatically forward new incoming media messages.
- **Photo Support:** Forward Telegram photos.
- **Video Support:** Forward Telegram videos.
- **Document Support:** Forward documents and other supported files.
- **Audio Support:** Forward audio files.
- **Voice Support:** Forward voice messages.
- **Batch Processing:** Forward existing media files in batches.
- **API Configuration:** Configure Telegram API ID and API HASH.
- **Session Management:** Maintain Telegram login sessions locally.
- **Colorized Output:** Easy-to-read terminal output with color coding.
- **Error Handling:** Handle network, channel, and forwarding errors.
- **Simple Interface:** Easy source and destination channel configuration.

---

## 📋 Requirements

- Python 3.8 or higher
- Telegram account
- Telegram API credentials (api_id and api_hash)
- Internet connection
- Access to source and destination Telegram channels

---

## 🛠️ Installation

### Termux (Android)

**1. Update Packages**

```bash
pkg update && pkg upgrade -y
```

**2. Install Python and Git**

```bash
pkg install python git -y
```

**3. Clone Repository**

```bash
git clone https://github.com/instant-ware/tz-auto-forwoard.git
```

**4. Open Project Directory**

```bash
cd tz-auto-forwoard
```

**5. Install Dependencies**

```bash
pip install telethon python-dotenv
```

**6. Run Project**

```bash
python tz-auto-forwoard.py
```

### Linux (Ubuntu/Debian)

**1. Update System**

```bash
sudo apt update && sudo apt upgrade -y
```

**2. Install Python and Git**

```bash
sudo apt install python3 python3-pip git -y
```

**3. Clone Repository**

```bash
git clone https://github.com/instant-ware/tz-auto-forwoard.git
```

**4. Open Project Directory**

```bash
cd tz-auto-forwoard
```

**5. Install Dependencies**

```bash
pip3 install telethon python-dotenv
```

**6. Run Project**

```bash
python3 tz-auto-forwoard.py
```

### Windows

1. Install Python 3.8+ from [python.org](https://www.python.org/downloads/).
2. Install Git from [git-scm.com](https://git-scm.com/).
3. Open Command Prompt or PowerShell.
4. Clone the repository:

```bash
git clone https://github.com/instant-ware/tz-auto-forwoard.git
```

5. Open the project directory:

```bash
cd tz-auto-forwoard
```

6. Install dependencies:

```bash
pip install telethon python-dotenv
```

7. Run the script:

```bash
python tz-auto-forwoard.py
```

---

## 🔧 Setup

### 1. Get Telegram API Credentials

- Go to [my.telegram.org](https://my.telegram.org).
- Log in using your Telegram phone number.
- Open "API Development Tools".
- Create a new application.
- Copy your `api_id` and `api_hash`.

### 2. Configure API Credentials

Run the script:

```bash
python tz-auto-forwoard.py
```

On the first run, the tool will ask for your API credentials:

```text
Enter API_ID:
Enter API_HASH:
```

Enter your Telegram API ID and API HASH.

The configuration will be saved locally in:

```text
tzsmx_api_config.json
```

### 3. Telegram Login

After entering your API credentials:

- Enter your Telegram login code when requested.
- Enter your two-step verification password if required.
- Complete the authentication process.

### 4. Configure Source and Destination

Enter your source and destination channel IDs or usernames:

```text
TZSMX CHANNEL SETUP

Enter SOURCE channel ID:
Enter DESTINATION channel ID:
```

Make sure your account has the necessary access to both channels.

---

## 📖 Usage

### Starting the Tool

```bash
python tz-auto-forwoard.py
```

### Forwarding Old and New Files

After configuring the channels, the tool will display a confirmation prompt:

```text
Start TZSMX Forwarding (Old + New)? (y/n):
```

To start forwarding:

```text
y
```

The tool will:

1. Connect to Telegram.
2. Resolve source and destination channels.
3. Scan existing channel messages.
4. Forward supported old media files.
5. Start listening for new messages.
6. Automatically forward supported new media files.

### Stopping the Tool

Press:

```text
CTRL + C
```

---

## 📦 Supported Media Types

| Media Type | Support |
|---|---|
| Photos | Yes |
| Videos | Yes |
| Documents | Yes |
| Audio | Yes |
| Voice Messages | Yes |

---

## ⚙️ Configuration Files

The tool automatically creates configuration and session files locally.

| File | Description |
|---|---|
| `tzsmx_api_config.json` | Stores Telegram API credentials |
| `my_session.session` | Stores Telegram login session |

**Important:** Never upload your API configuration or session files to a public GitHub repository.

---

## 📁 Project Structure

```text
tz-auto-forwoard/
│
├── tz-auto-forwoard.py
├── README.md
├── tzsmx_api_config.json
└── my_session.session
```

Configuration and session files are generated locally when required.

---

## 🔒 Security Notes

- Keep your Telegram API ID and API HASH private.
- Never share your Telegram session files.
- Do not upload private credentials to GitHub.
- Use only channels where you have proper authorization.
- Protect your Telegram account with two-step verification.
- Keep your login information secure.

---

## 🐛 Troubleshooting

### Invalid API ID

- Check whether your API ID is correct.
- Make sure you copied it from [my.telegram.org](https://my.telegram.org).
- Enter numbers only.

### Invalid API HASH

- Verify your API HASH.
- Make sure there are no extra spaces.
- Check your Telegram API credentials.

### Channel Resolve Failed

- Check the channel ID or username.
- Make sure your Telegram account has joined the required channels.
- Verify that you have permission to access both channels.

### Connection Errors

- Check your internet connection.
- Make sure Telegram is accessible.
- Try again after a few minutes.

### Module Not Found

Install the required packages again:

```bash
pip install telethon python-dotenv
```

### Forwarding Errors

- Verify source and destination channel access.
- Check Telegram forwarding restrictions.
- Make sure you have permission to send messages in the destination channel.

---

## 👨‍💻 Developer Information

- **Developer:** INSTANTWARE
- **Project Name:** TZ AUTO FORWARD
- **Brand:** TZSMX
- **GitHub:** [instant-ware](https://github.com/instant-ware)
- **Repository:** [tz-auto-forwoard](https://github.com/instant-ware/tz-auto-forwoard)
- **Telegram Channel:** [@InstantWare_dev](https://t.me/InstantWare_dev)

---

## 📜 License

This project is provided as-is for educational and authorized automation purposes.

Users are responsible for complying with applicable laws, Telegram's Terms of Service, and content ownership requirements.

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a Pull Request.

Please ensure contributions maintain the legitimate purpose of this project.

---

## ⭐ Support

If you find this project useful, please consider giving this repository a Star ⭐ on GitHub.

Your support motivates us to improve and maintain this project.

---

**Developed with ❤️ by INSTANTWARE**

**TZ AUTO FORWARD | TZSMX**

**Telegram:** [@InstantWare_dev](https://t.me/InstantWare_dev)

**© 2026 INSTANTWARE. All Rights Reserved.**
