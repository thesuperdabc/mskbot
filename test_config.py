#!/usr/bin/env python3
"""
MSK Chess Bot Configuration Test Script
This script verifies that the bot is properly configured for MSK Chess
"""

import os
import sys
from pathlib import Path

def print_status(message, status):
    """Print a status message with color"""
    if status == "OK":
        print(f"✅ {message}")
    elif status == "WARNING":
        print(f"⚠️  {message}")
    elif status == "ERROR":
        print(f"❌ {message}")
    else:
        print(f"ℹ️  {message}")

def check_python_version():
    """Check if Python version is 3.10+"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 10:
        print_status(f"Python version: {version.major}.{version.minor}.{version.micro}", "OK")
        return True
    else:
        print_status(f"Python version: {version.major}.{version.minor}.{version.micro} (3.10+ required)", "ERROR")
        return False

def check_config_file():
    """Check if config.yml exists and contains MSK Chess settings"""
    if not os.path.exists("config.yml"):
        print_status("config.yml not found", "ERROR")
        return False
    
    with open("config.yml", "r") as f:
        content = f.read()
        
    # Check for MSK Chess token
    if "mEDe1IjWUIktMSrp" in content:
        print_status("MSK Chess token found in config.yml", "OK")
    else:
        print_status("MSK Chess token not found in config.yml", "WARNING")
    
    return True

def check_engines():
    """Check if chess engines exist and are executable"""
    engines_dir = Path("engines")
    
    if not engines_dir.exists():
        print_status("engines/ directory not found", "ERROR")
        return False
    
    print_status("engines/ directory exists", "OK")
    
    # Check for stockfish
    stockfish = engines_dir / "stockfish"
    if stockfish.exists():
        if os.access(stockfish, os.X_OK):
            print_status("Stockfish engine found and executable", "OK")
        else:
            print_status("Stockfish found but not executable (run: chmod +x engines/stockfish)", "WARNING")
    else:
        print_status("Stockfish engine not found", "WARNING")
    
    # Check for fairy-stockfish
    fsf = engines_dir / "fsf"
    if fsf.exists():
        if os.access(fsf, os.X_OK):
            print_status("Fairy-Stockfish engine found and executable", "OK")
        else:
            print_status("Fairy-Stockfish found but not executable (run: chmod +x engines/fsf)", "WARNING")
    else:
        print_status("Fairy-Stockfish engine not found (needed for variants)", "WARNING")
    
    return True

def check_dependencies():
    """Check if required Python packages are installed"""
    required_packages = [
        "aiohttp",
        "yaml",
        "chess",
        "tenacity"
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package)
            print_status(f"Package '{package}' installed", "OK")
        except ImportError:
            print_status(f"Package '{package}' not installed", "ERROR")
            missing.append(package)
    
    if missing:
        print()
        print("To install missing packages, run:")
        print("  pip3 install -r requirements.txt")
        return False
    
    return True

def check_books():
    """Check if opening books exist"""
    books_dir = Path("books")
    masterbooks_dir = Path("masterbooks")
    
    if books_dir.exists():
        book_count = len(list(books_dir.glob("*.bin")))
        print_status(f"Found {book_count} opening books in books/", "OK" if book_count > 0 else "WARNING")
    else:
        print_status("books/ directory not found", "WARNING")
    
    if masterbooks_dir.exists():
        master_count = len(list(masterbooks_dir.glob("*.bin")))
        print_status(f"Found {master_count} master books in masterbooks/", "OK" if master_count > 0 else "WARNING")
    else:
        print_status("masterbooks/ directory not found", "WARNING")

def check_config_py():
    """Check if config.py has MSK Chess URL"""
    if not os.path.exists("config.py"):
        print_status("config.py not found", "ERROR")
        return False
    
    with open("config.py", "r") as f:
        content = f.read()
    
    if "mskchess.ru" in content:
        print_status("config.py configured for MSK Chess", "OK")
        return True
    elif "lichess.org" in content:
        print_status("config.py still configured for Lichess (should be mskchess.ru)", "ERROR")
        return False
    else:
        print_status("config.py URL configuration unclear", "WARNING")
        return True

def main():
    print("=" * 60)
    print("MSK Chess Bot Configuration Test")
    print("=" * 60)
    print()
    
    all_ok = True
    
    print("Checking Python version...")
    all_ok &= check_python_version()
    print()
    
    print("Checking configuration files...")
    all_ok &= check_config_file()
    all_ok &= check_config_py()
    print()
    
    print("Checking dependencies...")
    all_ok &= check_dependencies()
    print()
    
    print("Checking chess engines...")
    all_ok &= check_engines()
    print()
    
    print("Checking opening books...")
    check_books()
    print()
    
    print("=" * 60)
    if all_ok:
        print("✅ Configuration test PASSED")
        print()
        print("Your bot is ready to run!")
        print("Start it with: python3 user_interface.py")
        print("Or use the launcher: ./start_bot.sh")
    else:
        print("❌ Configuration test FAILED")
        print()
        print("Please fix the errors above before running the bot.")
    print("=" * 60)
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
