# Dyna

<img width="1473" height="551" alt="image" src="https://github.com/user-attachments/assets/c09f014d-564a-4bb7-b30b-008c58fa9e01" />

A terminal-based utility for managing Discord webhooks via Discord's public API. Features include sending messages, editing webhook details, deleting webhooks, and retrieving webhook metadata.

⚠️ **Warning:** This project is for educational and personal use only. Misuse of Discord’s API or this tool (such as spamming or exploiting webhooks) is a violation of Discord's [Terms of Service](https://discord.com/terms) and can result in account termination or legal action.

Tool Showcase: coming soon

---

## 💡 Features

- ✅ Send messages to a webhook (with optional embeds)
- 🧹 Delete webhook
- ✏️ Rename webhook
- 🔎 Retrieve webhook & user metadata
- 🖼️ Change webhook avatar
- 🧩 Apply style presets (username + avatar)
- 💥 Optional multithreaded message spam (⚠️ use responsibly!)

---

## 🔧 Requirements

- Python 3.8+
- pip modules:
  - `requests`
  - `colorama`
  - `pystyle`

Install dependencies with:

```bash
pip install -r requirements.txt
````

---

## 🚀 Usage

Run the tool:

```bash
python webhook-utils.py
```

Follow the terminal prompts to interact with your webhook.

---

## 📁 File Structure

* `webhook-utils.py` - Main script
* `Data/Config.json` - Message presets
* `Data/Style.json` - Style presets for avatar & name

---

## 📜 License

This project is released under the MIT License. Use at your own risk.

---

## ❗ Disclaimer

This tool is for **educational purposes** only. The developer is **not responsible** for any misuse. Abusing Discord's webhook features can lead to your IP being rate-limited or permanently banned.

---

## 🔐 Safety Reminder

Do **not** share webhook URLs publicly. They are essentially passwords to post to specific channels.

````

📄 Example `requirements.txt`

```txt
requests
colorama
pystyle
````

---

If you’re intending to use or publish this tool **ethically**, and avoid violating platform rules, I can help you refactor it or add CLI argument parsing, error handling, or permission checks. Let me know!
