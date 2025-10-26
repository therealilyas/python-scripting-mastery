# 💻 02 - MUHIT TAYYORLASH

## Python o'rnatish va sozlash

### Tizim talablari

**Minimal:**
- 💾 RAM: 2GB
- 💿 Disk: 5GB bo'sh joy
- 🖥 OS: Windows 7+, Linux, MacOS

**Tavsiya etiladi:**
- 💾 RAM: 4GB+
- 💿 Disk: 20GB+ bo'sh joy
- 🖥 OS: Windows 10/11, Ubuntu 20.04+, MacOS 10.15+

---

## Windows uchun Python o'rnatish

### 1-qadam: Python yuklab olish

1. **Brauzerda oching:** https://www.python.org
2. **Downloads** tugmasini bosing
3. **Python 3.12.x** (eng yangi versiya) ni yuklab oling
4. **Windows installer (64-bit)** ni tanlang

### 2-qadam: O'rnatish

1. Yuklab olingan faylni ishga tushiring
2. **MUHIM:** "Add Python to PATH" ni belgilang ✅
3. "Install Now" ni bosing
4. Administratordan ruxsat so'ralsa, "Yes" deb javob bering
5. Kutamiz... (2-3 daqiqa)
6. "Setup was successful" - tugadi!

### 3-qadam: Tekshirish

**CMD ni oching:**
- Win + R
- Yozing: `cmd`
- Enter

**Tekshiramiz:**
```cmd
python --version
```

**Natija:**
```
Python 3.12.0
```

**pip ni tekshiramiz:**
```cmd
pip --version
```

**Natija:**
```
pip 23.3.1 from C:\Python312\lib\site-packages\pip (python 3.12)
```

✅ Agar versiyalar ko'rinsa - **muvaffaqiyatli!**

### 4-qadam: Python Shell

CMD da yozing:
```cmd
python
```

Python interaktiv shell ochiladi:
```python
>>>
```

Sinab ko'ramiz:
```python
>>> print("Salom Dunyo!")
Salom Dunyo!
>>> 2 + 2
4
>>> exit()
```

---

## Linux (Ubuntu/Debian) uchun

### 1-qadam: Yangilash

Terminal ni oching (Ctrl + Alt + T):

```bash
sudo apt update
sudo apt upgrade -y
```

### 2-qadam: Python o'rnatish

```bash
sudo apt install python3 python3-pip python3-venv -y
```

### 3-qadam: Tekshirish

```bash
python3 --version
pip3 --version
```

### 4-qadam: Alias qo'shish (Ixtiyoriy)

```bash
echo "alias python=python3" >> ~/.bashrc
echo "alias pip=pip3" >> ~/.bashrc
source ~/.bashrc
```

Endi `python` va `pip` ishlatishingiz mumkin.

---

## MacOS uchun

### 1-qadam: Homebrew o'rnatish

Terminal da:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2-qadam: Python o'rnatish

```bash
brew install python
```

### 3-qadam: Tekshirish

```bash
python3 --version
pip3 --version
```

---

## Code Editor o'rnatish

### Visual Studio Code (Tavsiya etiladi)

**Windows:**
1. https://code.visualstudio.com
2. Download for Windows
3. O'rnatish (Default settings)

**Linux:**
```bash
sudo snap install code --classic
```

**MacOS:**
```bash
brew install --cask visual-studio-code
```

### VS Code kengaytmalari

VS Code ni ochib, Extensions (Ctrl + Shift + X):

1. **Python** (Microsoft) - ⭐ Majburiy
2. **Pylance** - Intelligent IntelliSense
3. **Python Indent** - Auto indent
4. **autoDocstring** - Docstring generator
5. **Error Lens** - Inline errors
6. **Material Icon Theme** - Beautiful icons
7. **One Dark Pro** - Theme

---

## Virtual Environment yaratish

### Nega Virtual Environment?

```
Global Python
├── project1 (Django 3.2)
├── project2 (Django 4.0)  ❌ KONFLIKT!
└── project3 (Flask)
```

**Yechim:** Har bir loyiha uchun alohida muhit!

```
project1/
└── venv/ (Django 3.2) ✅

project2/
└── venv/ (Django 4.0) ✅

project3/
└── venv/ (Flask) ✅
```

### Virtual Environment yaratish

**Windows:**
```cmd
cd C:\Users\User\Desktop
mkdir python-projects
cd python-projects
python -m venv myenv
```

**Linux/Mac:**
```bash
cd ~/Desktop
mkdir python-projects
cd python-projects
python3 -m venv myenv
```

### Virtual Environment faollashtirish

**Windows:**
```cmd
myenv\Scripts\activate
```

**Linux/Mac:**
```bash
source myenv/bin/activate
```

**Faollashsa:**
```
(myenv) C:\Users\User\Desktop\python-projects>
```

### Virtual Environment o'chirish

```bash
deactivate
```

---

## pip - Package Manager

### pip nima?

pip - Python Package Installer  
300,000+ tayyor kutubxonalar!

### pip asosiy buyruqlar

```bash
# Kutubxona o'rnatish
pip install requests

# Versiya ko'rsatish
pip install requests==2.28.0

# Yangilash
pip install --upgrade requests

# O'chirish
pip uninstall requests

# O'rnatilgan paketlar
pip list

# Paket haqida ma'lumot
pip show requests

# requirements.txt yaratish
pip freeze > requirements.txt

# requirements.txt dan o'rnatish
pip install -r requirements.txt
```

### CyberSecurity uchun asosiy paketlar

```bash
# Network
pip install scapy
pip install paramiko
pip install impacket

# Web
pip install requests
pip install beautifulsoup4
pip install selenium

# Cryptography
pip install cryptography
pip install pycryptodome

# Utilities
pip install colorama
pip install python-nmap
pip install pexpect
```

---

## Git o'rnatish

### Windows

1. https://git-scm.com/download/win
2. Download
3. Install (Default settings)

### Linux

```bash
sudo apt install git -y
```

### MacOS

```bash
brew install git
```

### Git sozlash

```bash
git config --global user.name "Ismingiz"
git config --global user.email "email@example.com"
```

---

## Terminal/CMD dan foydalanish

### Asosiy buyruqlar

**Windows CMD:**
```cmd
dir              # Fayllarni ko'rish
cd papka         # Papkaga kirish
cd ..            # Orqaga
mkdir yangi      # Papka yaratish
del fayl.txt     # Fayl o'chirish
cls              # Ekranni tozalash
```

**Linux/Mac Terminal:**
```bash
ls               # Fayllarni ko'rish
cd papka         # Papkaga kirish
cd ..            # Orqaga
mkdir yangi      # Papka yaratish
rm fayl.txt      # Fayl o'chirish
clear            # Ekranni tozalash
pwd              # Joriy papka
```

---

## Birinchi Python fayl yaratish

### VS Code da

1. VS Code ni oching
2. File → Open Folder
3. `python-projects` papkasini tanlang
4. Yangi fayl: `salom.py`

```python
print("Salom Dunyo!")
print("Men Python o'rganyapman!")
```

5. Saqlang (Ctrl + S)
6. Ishga tushirish (F5 yoki Ctrl + F5)

### Terminal orqali

```bash
cd python-projects
python salom.py
```

**Natija:**
```
Salom Dunyo!
Men Python o'rganyapman!
```

✅ **Tabriklaymiz! Birinchi dasturingiz ishladi!**

---

## Muammolarni bartaraf etish

### Python topilmadi

**Windows:**
- PATH ga qo'shilganini tekshiring
- CMD ni qayta oching
- Kompyuterni qayta ishga tushiring

**Linux/Mac:**
- `python3` ni ishlating
- Alias qo'shing

### pip ishlamayapti

```bash
python -m pip install --upgrade pip
```

### Virtual Environment aktivatsiyalanmayapti

**Windows:**
```cmd
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### VS Code Python ni taniмayapti

1. Ctrl + Shift + P
2. "Python: Select Interpreter"
3. Python versiyasini tanlang

---

## Keyingi qadam

✅ Python o'rnatildi  
✅ VS Code sozlandi  
✅ Virtual Environment yaratildi  
✅ Birinchi dastur yozildi  
