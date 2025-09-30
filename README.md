# MSK Chess Bot

Enhanced version of [BotLi](https://github.com/Torom/BotLi) converted to work with **MSK Chess** (https://mskchess.ru/).

## 🎯 Quick Start

This bot has been fully configured to work with MSK Chess using token: `mEDe1IjWUIktMSrp`

### Prerequisites
- Python 3.10+
- Chess engine (Stockfish) in `./engines/` directory
- MSK Chess BOT account

### Installation & Run

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Make engines executable:**
```bash
chmod +x ./engines/stockfish
chmod +x ./engines/fsf
```

3. **Run the bot:**
```bash
python3 user_interface.py
```

4. **Start matchmaking:**
```bash
python3 user_interface.py matchmaking
```

## 📚 Documentation

**📖 [MSK Chess Setup Guide](MSK_CHESS_SETUP.md)** - Complete setup and configuration guide

**🚀 [GitHub Actions Setup Guide](GITHUB_SETUP.md)** - 24/7 free hosting (may need adaptation for MSK Chess)

## ⚙️ Configuration

The bot is pre-configured in `config.yml` with:
- ✅ MSK Chess token: `mEDe1IjWUIktMSrp`
- ✅ Base URL: `https://mskchess.ru`
- ✅ Stockfish engine with optimized settings
- ✅ Opening books for various time controls
- ✅ Challenge acceptance criteria

## 🎮 Features

- ♟️ Plays standard chess and variants
- 📖 Opening book support (master player books included)
- 🤖 Automatic matchmaking
- 💬 Chat commands
- 🔄 Rematch functionality
- 🏆 Tournament participation
- ⚡ Configurable time controls and rating ranges

## 🛠️ Key Changes from Lichess

- Base URL changed to `https://mskchess.ru`
- Token updated for MSK Chess authentication
- Lichess-specific features disabled (Opening Explorer)
- API endpoints adapted for MSK Chess compatibility

## 📝 Available Commands

Once running, use these commands:
- `matchmaking` - Start automatic matchmaking
- `challenge USERNAME` - Challenge a specific player
- `stop` - Stop matchmaking
- `quit` - Exit the bot
- `help` - Show all commands

## 🔧 Troubleshooting

**Connection issues?**
- Verify MSK Chess is accessible
- Check token validity
- Ensure API compatibility

**Engine errors?**
- Check engine exists: `ls -la ./engines/`
- Verify execute permissions
- Test manually: `./engines/stockfish`

See [MSK_CHESS_SETUP.md](MSK_CHESS_SETUP.md) for detailed troubleshooting.

## 📄 Credits

- Based on [BotLi](https://github.com/Torom/BotLi) by Torom
- Converted for MSK Chess by Ramanayake
- Chess engines: Stockfish and Fairy-Stockfish teams
- Original framework: Lichess Bot API interface
