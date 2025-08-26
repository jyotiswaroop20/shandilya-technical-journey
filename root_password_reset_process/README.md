# Reset Forgotten Root Password — RHEL-8 / AlmaLinux 9 / 10

> **भाषा:** हिन्दी

## सार (Summary)
यह README दस्तावेज़ RHEL-8 / AlmaLinux 9/10 पर `root` पासवर्ड भूल जाने की स्थिति में सुरक्षित और समर्थित तरीकों से पासवर्ड रीसेट करने का step‑by‑step तरीका बताता है। इसमें `rd.break` (initramfs break) method, rescue ISO method, और cloud/VM specific विकल्प शामिल हैं।

**महत्वपूर्ण सुरक्षा नोट:** यह गाइड केवल उन सिस्टम्स के लिए है जिनके आप मालिक/अधिकारिता (authorized) हैं। बिना अनुमति किसी सिस्टम का पासवर्ड बदलना अवैध और अनैतिक है।

---

## prerequisites (ज़रूरी शर्तें)
- आपके पास सर्वर/VM का physical/console या hypervisor/host-level access होना चाहिए ताकि आप GRUB मेनू edit कर सकें।
- अगर डिस्क LUKS से encrypted है तो आपको LUKS passphrase चाहिए होगा।
- अगर मशीन cloud instance है (AWS/GCP/Azure/Proxmox आदि), तो provider के rescue / serial console सुविधा का उपयोग करें।
- महत्वपूर्ण डेटा का backup हमेशा रखें (यदि संभव हो)।

---

## Method A — (Recommended) `rd.break` / initramfs break (RHEL/AlmaLinux standard way)
यह विधि खासकर systemd + dracut आधारित RHEL/AlmaLinux पर सबसे भरोसेमंद और साफ़ तरीका है।

### Step‑by‑step
1. सिस्टम को reboot करें और GRUB मेनू पर पहुँचें।
   - सामान्यतः reboot पर GRUB दिखेगा; नहीं दिखे तो BIOS/UEFI के समय `Esc`/`Shift`/`F8`/`F12` (VM/hypervisor पर अलग) दबाएँ।
2. जिस kernel entry से boot करना है उस पर जाएँ और `e` दबाकर edit मोड खोलें।
3. `linux`/`linux16`/`linuxefi` लाइन खोजें (जिसमें `ro crashkernel` आदि होते हैं)।
   - उसी line के अंत में space देकर **`rd.break enforcing=0`** जोड़ दें। (उदाहरण: `... rhgb quiet rd.break and can do SeLinix Permissive by enforcing=0`)
4. Ctrl+X (या `F10`) दबाकर boot करें — यह आपको dracut-shell / initramfs prompt पर छोड़ेगा, prompt आम तौर पर `switch_root:/#` होगा।

5. initramfs में नीचे के commands चलाएँ:

```bash
# sysroot को read-write पर remount करें because now our file systems have been mounted in read-only.
mount -o remount,rw /sysroot
mount | grep /sysroot (verify it has been mounted in read-write mode or not)
# sysroot के अंदर chroot करें
chroot /sysroot

# अब root का पासवर्ड बदलें
passwd root
# (नई पासवर्ड दो बार दें)

# SELinux enabled systems के लिए relabel करवाने हेतु marker बनाएं
# (यह जरूरी है वरना SELinux context mismatch से बूट में समस्या हो सकती है)
touch /.autorelabel

# chroot से बाहर निकलें
exit

# initramfs shell से बाहर होकर continue करने के लिए एक और exit करें
exit
```

6. सिस्टम normal boot करेगा और (`/.autorelabel` होने पर) SELinux contexts relabel होंगे — यह थोड़ी देर ले सकता है।

**नोट्स / common errors:**
- अगर `passwd` पर `Authentication token manipulation error` आता है तो सम्भव है `/sysroot` रीड-ओनली है — फिर से `mount -o remount,rw /sysroot` चलाएँ।
- यदि मशीन encrypted है (LUKS), तो boot के दौरान आपसे LUKS passphrase माँगा जाएगा; वह पास करके आगे बढ़ें।

---

## Method B — `rescue.target` / `init=/bin/sh` (alternate, उपयोगी कभी‑कभी)
- `systemd.unit=rescue.target` जोड़ने से systemd rescue mode आता है लेकिन अक्सर root password माँगा जा सकता है, इसलिए यह तरीका हर बार काम नहीं करता।
- `init=/bin/sh` जोड़ने से आप single shell पर पहुँचते हैं, पर filesystem read-only मिल सकता है; remount rw करना और फिर `/usr/sbin/passwd root` चलाना पड़ता है।

> मैं आमतौर पर **`rd.break`** को प्राथमिकता देता हूँ क्योंकि यह predictable और dracut compatible है।

---

## Method C — Rescue ISO / Live CD method
यदि GRUB नहीं खुल रहा या कोई और समस्या है (या physical access नहीं पर rescue-media उपलब्ध है):
1. RHEL/AlmaLinux installer ISO से boot करें और **Troubleshooting → Rescue a RHEL system** चुनें।
2. rescue environment में root shell लीजिए और root partition mount करें — उदाहरण:

```bash
# उदाहरण — actual device नाम अलग हो सकता है
mount /dev/mapper/rhel-root /mnt/sysimage
# या
mount /dev/sda2 /mnt/sysimage

# अब chroot करें
chroot /mnt/sysimage

# passwd बदलें
passwd root

touch /.autorelabel

exit
reboot
```

---

## Method D — Cloud / VPS specific steps
- **Serial console / Rescue image:** अधिकांश cloud providers (AWS EC2, GCP, Azure, DigitalOcean, Hetzner) rescue environment या serial console देते हैं। सबसे सुरक्षित तरीका provider का rescue image या disk detach‑attach करके helper VM के साथ chroot करना है।
- **Disk detach method:** Disk को helper instance में attach करें, mount करें, chroot करके passwd चलाएँ और disk वापस attach करें।

---

## SELinux और `.autorelabel` का महत्त्व
RHEL/AlmaLinux पर SELinux enabled रहता है। जब आप emergency में `chroot` कर के `passwd` बदलते हैं, तो कई बार SELinux labels mismatch हो सकते हैं — इसलिए `touch /.autorelabel` करना ज़रूरी है ताकि अगले बूट पर system automatic relabel कर दे। अगर यह नहीं किया तो SELinux denials से लॉगिन न हो या services fail कर सकती हैं।

---

## Boot‑loop या बूट में इश्यू (Troubleshooting)
यदि रीबूट के बाद system boot loop में चला जाए या login failure हो तो:
1. Rescue ISO से boot कर के `/var/log/messages`, `journalctl -b -1` या `journalctl -xe` देखें और error trace पढ़ें।
2. SELinux से संबंधित हो तो `/etc/selinux/config` में `SELINUX=permissive` कर के reboot करके चेक करें (यदि आवश्यक हो)।
   - **Warning:** SELINUX=disabled/permissive security को कम करता है — सिर्फ troubleshooting के लिए।
3. GRUB में जो जोड़े गए parameter (जैसे `rd.break` / `init=`) को हटा कर normal boot करें।
4. अगर `/etc/fstab` में कोई गलत entry है तो rescue mode में उसे comment कर दें और reboot करें।

---

## Verification (जाँच)
- रीबूट के बाद `root` से login कर के `id`, `whoami`, `getenforce` (SELinux mode) चेक करें।
- `/var/log/secure` और `journalctl -b` देखें कि root login और passwd change के events सही हैं।

---

## FAQ / Common scenarios
- **अगर GRUB password set है:** GRUB password होने पर GRUB edit तभी संभव होगा जब आपके पास GRUB password हो। अन्यथा hypervisor/console से rescue mode का उपयोग करें।
- **अगर remote headless VM है और serial console नहीं है:** Cloud provider से rescue या disk‑attach method ही विकल्प होगा।
- **Password complexity:** RHEL systems में PAM rules के कारण strong password policies हो सकती हैं; नया पासवर्ड PAM policy के अनुरूप रखें।

---

## अंतिम सुरक्षा और audit सुझाव
- पासवर्ड बदलने के बाद root access घटाकर sudo‑based access पर जाएँ यदि संभव हो।
- change का record रखें और stakeholders को inform करें।
- unauthorized access का शक हो तो सम्पूर्ण system audit करें (Cron jobs, authorized_keys, /etc/sudoers, installed packages)।

---

## Quick cheatsheet (कमांड सार)
> **ध्यान दें:** नीचे दिए गए कमांड का उपयोग केवल authorized systems पर ही करें।

```bash
# GRUB edit -> append rd.break enforcing=0-> boot
# initramfs shell:
mount -o remount,rw /sysroot
mount | grep /sysroot (verify it has been mounted in read-write mode or not)
chroot /sysroot
passwd root
touch /.autorelabel
exit
exit
```

---
