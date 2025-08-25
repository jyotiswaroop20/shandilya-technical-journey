
# 🐧 Kdump + Early Kdump — A-to-Z Step‑by‑Step (Hindi)

ये README **पूरी तरह practical** है: Kdump enable → Early Kdump enable → Runtime crash test → **Boot‑time crash (boot‑loop) के 2 तरीके** → Recovery → Dump analysis (bt समझना) → Common errors का सही fix.  
**Production पर सावधानी**: ये सारे tests केवल **lab/maintenance window** में करें।

---

## 🔎 Kdump / Early Kdump एक नज़र में
- **Kdump**: Kernel crash होते ही एक छोटा **capture kernel** boot होकर RAM का snapshot (**vmcore**) save कर देता है।
- **Early Kdump**: अगर crash **boot के बहुत शुरू में** हो जाए, तब भी dump मिल जाए — इसके लिए initramfs में earlykdump जोड़ते हैं, और cmdline पर `rd.earlykdump` flag देते हैं।

Dump आमतौर पर: **`/var/crash/<HOST>-<DATE>/`** में आता है (`vmcore`, `vmcore-dmesg.txt`).

---

## 🧰 A) ज़रूरी Packages (with debuginfo fixes)

### Quick (जब debuginfo repo पहले से enabled हो)
```bash
dnf install -y crash kernel-debuginfo-$(uname -r)
```

### Robust (Alma/Rocky/RHEL 9 — अगर ऊपर वाली command से “No match for argument” error आए)
```bash
# Plugins + CRB enable
dnf install -y dnf-plugins-core
dnf config-manager --set-enabled crb

# Matching debuginfo install (symbols crash के लिए ज़रूरी)
dnf debuginfo-install -y kernel-core-$(uname -r)

# crash tool
dnf install -y crash
```

**RHEL** पर (subscription वाले):
```bash
subscription-manager repos --enable=rhel-*-debuginfo-rpms
dnf install -y dnf-plugins-core
dnf debuginfo-install -y kernel-core-$(uname -r)
dnf install -y crash
rpm -qa | grep kernel-debuginfo
rpm -qa | grep crash
```

✅ Verify:
```bash
uname -r
rpm -qa | grep -E 'crash|kernel-debuginfo|kernel-core-debuginfo'
```

> क्यों? `crash` utility को **matching kernel symbols** चाहिए होते हैं, जो `kernel-debuginfo`/`kernel-core-debuginfo` में मिलते हैं।

---

## 💾 B) crashkernel reserve (must-have)

Check:
```bash
cat /proc/cmdline | tr ' ' '\n' | grep -i crashkernel || echo "crashkernel missing"
```
- अगर कुछ ऐसा दिखे: `crashkernel=1G-4G:192M,4G-64G:256M,64G-:512M` → **already set** ✅  
- अगर missing हो:
```bash
grubby --update-kernel=ALL --args="crashkernel=auto"
reboot
```

---

## 🚀 C) Kdump service enable + basic config

```bash
systemctl enable --now kdump
kdumpctl status        # "Kdump is operational" ideally
```
Optional: `/etc/kdump.conf` में target/collector set करें (space ensure करें):
```conf
path /var/crash
core_collector makedumpfile -c --message-level 1
```

---

## ⚡ D) Early Kdump enable (initramfs method)

1) **initramfs में earlykdump जोड़ें**  
```bash
dracut -f --add earlykdump
```

2) **Kernel cmdline पर flag दें**  
```bash
grubby --update-kernel=/boot/vmlinuz-$(uname -r) --args="rd.earlykdump"
reboot
```

3) **Verify**  
```bash
cat /proc/cmdline | grep -o rd.earlykdump || echo "missing rd.earlykdump"
journalctl -b -k | egrep -i 'earlykdump|early-kdump|kdump'
kdumpctl status
```

> अब boot के very-early phase वाले crashes भी capture होने चाहिए।

---

## 🧨 E) Runtime crash test (normal)

> ⚠️ तुरंत reboot होगा; पहले सब सेव करें.

```bash
# SysRq on (persistent)
sysctl -w kernel.sysrq=1
echo 'kernel.sysrq = 1' > /etc/sysctl.d/99-sysrq.conf

# Trigger crash
echo c > /proc/sysrq-trigger
```
Reboot के बाद dump: `ls -lh /var/crash/*`
# आमतौर पर:
```
vmcore            -> RAM snapshot (binary)
vmcore-dmesg.txt  -> crash के समय के kernel logs (text file)

---

## 🌀 F) Early‑boot crash test — **दो तरीके**

### तरीका‑1 (One‑shot | GRUB से rd.break + panic)
1) GRUB menu पर entry चुनें → `e` दबाएँ → kernel cmdline के अंत में जोड़ें:
```
rd.break=initqueue
```
2) Boot करें (dracut emergency shell मिलेगा), फिर:
```bash
echo 1 > /proc/sys/kernel/sysrq
echo c > /proc/sysrq-trigger
```
→ **very early** panic होगा; earlykdump से dump capture होना चाहिए। Next boot normal रहेगा (loop नहीं बनेगा).

---

### तरीका‑2 (Persistent boot‑loop | systemd unit + cmdline flag)

> ये method **हर boot** पर early stage में panic करवाता है ताकि real boot‑loop बने — practice/recovery सीखने के लिए best.

**(a) Crash script** → `/usr/local/early-kdump-test.sh`
```bash
cat >/usr/local/early-kdump-test.sh <<'EOF'
#!/bin/bash
echo 1 > /proc/sys/kernel/sysrq
echo c > /proc/sysrq-trigger
EOF
chmod +x /usr/local/early-kdump-test.sh
```

**(b) Systemd unit** → `/etc/systemd/system/sysrq.service`
```ini
[Unit]
Description=Trigger early kernel panic for kdump testing
DefaultDependencies=no
Before=basic.target
# केवल तब चले जब cmdline में early_panic=1 हो
ConditionKernelCommandLine=early_panic=1

[Service]
Type=oneshot
ExecStart=/usr/local/early-kdump-test.sh

[Install]
WantedBy=basic.target
```

**(c) Enable + flag add**
```bash
systemctl daemon-reload
systemctl enable sysrq.service
grubby --update-kernel=ALL --args="early_panic=1"
reboot
```
→ अब **हर boot** पर panic → dump capture → reboot → panic… यानी **boot‑loop**.

---

## 🛟 G) Boot‑loop से Recovery

### अस्थायी (one boot)
- GRUB menu पर `e` दबाएँ → cmdline से `early_panic=1` **हटा दें** then Ctrl+X → boot करें.

### स्थायी
```bash
# सेवा बंद + flag हटाएँ + सफाई
systemctl disable sysrq.service
grubby --update-kernel=ALL --remove-args="early_panic=1"
rm -f /etc/systemd/system/sysrq.service /usr/local/early-kdump-test.sh
systemctl daemon-reload
```
→ अब loop खत्म; system normal.

---

## 🧠 H) Dump कहाँ? कैसे पढ़ें?

**Location** (default): `/var/crash/<HOST>-<DATE>/`  
Files:
- `vmcore` (binary RAM snapshot)
- `vmcore-dmesg.txt` (crash के समय के kernel logs)

**Analyze (crash utility):**
> ध्यान दें: crash को **उसी kernel version** का debuginfo चाहिए जिससे dump बना था।

```bash
# Example (current kernel version से):
crash /usr/lib/debug/lib/modules/$(uname -r)/vmlinux /var/crash/*/vmcore

# अगर dump पुराने kernel से है, उस version का vmlinux दें:
crash /usr/lib/debug/lib/modules/<crashed-version>/vmlinux /var/crash/<DIR>/vmcore
```

Crash के अंदर काम के commands:
```
log           # kernel message buffer (vmcore-dmesg जैसा)
bt            # backtrace (panic कहाँ हुआ)
ps            # उस समय के processes
kmem -i       # memory summary
help          # सभी commands
q             # बाहर निकलें
```

---

## 🔍 I) `bt` (Backtrace) को आसान भाषा में समझना

आपके sample bt:
```
PID: 1555     TASK: ...  CPU: 1    COMMAND: "bash"
 #0 machine_kexec
 #1 __crash_kexec
 #2 panic
 #3 sysrq_handle_crash
 #4 __handle_sysrq.cold
 #5 write_sysrq_trigger
 #6 proc_reg_write
 #7 vfs_write
 #8 ksys_write
 #9 do_syscall_64
#10 entry_SYSCALL_64_after_hwframe
```
**मतलब:**
- `bash` से `echo c > /proc/sysrq-trigger` चला → syscall के ज़रिए kernel तक गया (`ksys_write`/`do_syscall_64`).  
- Kernel ने `/proc/sysrq-trigger` में **'c'** देखा → `sysrq_handle_crash` → `panic()` → `__crash_kexec`/`machine_kexec` ⇒ kdump capture kernel.  
- यानी ये **manual test crash** है, bug नहीं।

**Real‑life analogy (Black Box):**
- Kernel = पायलट, Crash kernel = co‑pilot (backup).  
- Accident (panic) होते ही co‑pilot control लेता है और **Black Box** (vmcore) save करता है.  
- आप `crash` tool से Black Box खोलकर पता लगाते हैं कि क्या हुआ।

---

## 🧩 J) Troubleshooting (तेज़)

- **`No match for argument: kernel-debuginfo-$(uname -r)`**  
  → `dnf config-manager --set-enabled crb` + `dnf-plugins-core` + `dnf debuginfo-install -y kernel-core-$(uname -r)` फिर `dnf install -y crash` (RHEL पर debuginfo repos enable करें).

- **`kdumpctl status` not operational**  
  → `crashkernel` सेट है? `/proc/cmdline` देखें; space/path OK? `/etc/kdump.conf` जाँचें; reboot के बाद फिर चेक करें.

- **Dump नहीं बन रहा**  
  → `/var/crash` में space दें; `core_collector makedumpfile -c` use करें; `journalctl -b -k | egrep -i 'kdump|kexec|early'` से logs देखें.

- **Mismatch vmlinux**  
  → वही kernel version का debuginfo/vmlinux दें जिससे dump बना था (older/newer mismatch मत करें).

---

## ♻️ K) Undo / Clean‑up (सब कुछ वापस)

```bash
# Early kdump flag हटाएँ
grubby --update-kernel=ALL --remove-args="rd.earlykdump"

# Boot‑loop demo हटाएँ (अगर बनाया था)
systemctl disable sysrq.service || true
grubby --update-kernel=ALL --remove-args="early_panic=1"
rm -f /etc/systemd/system/sysrq.service /usr/local/early-kdump-test.sh
systemctl daemon-reload

# Optional: kdump बंद
systemctl disable --now kdump
```

---

## ✅ Quick Checklist (Pocket)

- [ ] crash + debuginfo installed (with CRB/debuginfo fixes)  
- [ ] `crashkernel` present in `/proc/cmdline`  
- [ ] `kdump` service enabled & operational  
- [ ] Early kdump: `dracut -f --add earlykdump` + `rd.earlykdump`  
- [ ] Runtime test: `echo c > /proc/sysrq-trigger`  
- [ ] Boot‑loop test (systemd unit + `early_panic=1`) and recovery steps known  
- [ ] Dump analyzed with `crash vmlinux vmcore` (bt/log/ps/kmem -i)

---

**Author**: *Jyotiswaroop Tripathi* — Linux/DevOps  
**Language**: Simple Hindi (with commands)  
**Use**: Lab‑friendly, production‑safe (with caution)  

