# 🐍 Python 3.13 Build, Install & Manage Guide

<h1 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&color=FF5733&center=true&width=600&lines=Python+3.13+Build+%26+Management" alt="Typing SVG">
</h1>

---

## 📌 Overview

इस guide में हम सीखेंगे:

1. Python 3.13 **source से build & install करना**
2. Python 3.13 **RPM package बनाकर install करना**
3. Python को **system-wide alias** और **alternatives** से default set करना
4. Old Python 3.9 के साथ coexistence और version switching
5. Python version check सिर्फ `python` command से
6. Python 3.13 को **permanently remove करना**

---

## 1️⃣ Python 3.13 Source Build & Install

```bash
# Step 1: Install development tools
sudo dnf groupinstall "Development Tools" -y
dnf install gcc gcc-c++ make zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel tk-devel libffi-devel xz-devel wget curl -y

# Step 2: Download Python 3.13 source
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.13.7/Python-3.13.7.tgz

# Step 3: Extract source
tar xzvf Python-3.13.7.tgz
cd Python-3.13.7

# Step 4: Configure and compile
sudo ./configure --enable-optimizations --prefix=/usr/local
sudo make -j$(nproc)

# Step 5: Install without replacing system python
sudo make altinstall

# Step 6: Verify installation
/usr/local/bin/python3.13 --version
```

---

## 2️⃣ Create RPM for Python 3.13

### Step A: Install RPM build tools

```bash
sudo dnf install rpm-build rpmdevtools -y
rpmdev-setuptree
```

### Step B: Move source tarball

```bash
mv /usr/src/Python-3.13.7.tgz ~/rpmbuild/SOURCES/
```

### Step C: Create SPEC file

```bash
cd ~/rpmbuild/SPECS
nano python3.13.spec
```

**Sample spec content:**

```spec
Name:           python3.13
Version:        3.13.7
Release:        1%{?dist}
Summary:        Python 3.13

License:        Python
URL:            https://www.python.org
Source0:        %{name}-%{version}.tgz
BuildRequires:  gcc make bzip2 bzip2-devel zlib-devel xz-devel

%description
Python 3.13 language interpreter.

%prep
%setup -q

%build
./configure --enable-optimizations
make -j$(nproc)

%install
make altinstall DESTDIR=%{buildroot}

%files
/usr/local/bin/python3.13
/usr/local/lib/python3.13*

%changelog
* Sat Aug 23 2025 Jyoti Swaroop <youremail@example.com> - 3.13.7-1
- Initial build
```

### Step D: Build RPM

```bash
rpmbuild -ba python3.13.spec
```

### Step E: Install RPM

```bash
sudo dnf install ~/rpmbuild/RPMS/x86_64/python3.13-3.13.7-1.el9.x86_64.rpm -y
```

✅ अब Python 3.13 system-wide RPM के माध्यम से install हो चुका है।

---

## 3️⃣ Set Python 3.13 as Default Using Alias

```bash
# Temporary (current session)
alias python='/usr/local/bin/python3.13'

# Permanent (for all sessions for one user)
echo "alias python='/usr/local/bin/python3.13'" >> ~/.bashrc

# Permanent (for all sessions for all user)
echo "alias python='/usr/local/bin/python3.13'" >> /etc/bashrc
source ~/.bashrc
# OR
siurce /etc/bashrc

# Check version
python --version
```

💡 अब आप `python` command से Python 3.13 use कर सकते हैं।

---

## 4️⃣ Set Python 3.13 as Default Using Alternatives

```bash
# Register versions
sudo alternatives --install /usr/bin/python python /usr/bin/python3.9 1
sudo alternatives --install /usr/bin/python python /usr/local/bin/python3.13 2

# Select default version
sudo alternatives --config python3

# set python as a command
alternatives --install /usr/bin/python python /usr/bin/python3 1
alternatives --config python
# Verify
python --version
```

✅ अब Python 3.13 default हो गया है, लेकिन Python 3.9 अभी भी system में available है।

---

## 5️⃣ Switch Back to Old Python 3.9 (if needed)

```bash
# Using alternatives
sudo alternatives --config python
# Select Python 3.9
python --version

# Or temporary alias override
alias python='/usr/bin/python3.9'
python --version
```

---

## 6️⃣ Permanently Remove Python 3.13

```bash
# Remove source installed files
sudo rm -rf /usr/local/bin/python3.13
sudo rm -rf /usr/local/lib/python3.13
sudo rm -rf /usr/src/Python-3.13.0

# Remove from alternatives
sudo alternatives --remove python /usr/local/bin/python3.13

# Remove RPM if installed
sudo dnf remove python3.13 -y

# Remove alias from ~/.bashrc if set
nano ~/.bashrc
# Delete line: alias python='/usr/local/bin/python3.13'
source ~/.bashrc
```

✅ अब Python 3.13 system से completely remove हो चुका है और Python 3.9 default है।

---

## 7️⃣ Verify Python Version

```bash
python --version      # Should show default version (3.13 or 3.9 based on your settings)
which python          # Shows path of python command
```

---

✅ यह **README.md** एकदम **step-by-step, future-proof, attractive GitHub-ready** guide है जो Python 3.13 build, install, alias, alternatives, version switch और removal cover करता है।

