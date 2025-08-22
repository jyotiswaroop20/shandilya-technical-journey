#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <linux/mm.h>
#include <linux/sched/loadavg.h>
#include <linux/jiffies.h>
#include <linux/utsname.h>
#include <linux/timekeeping.h>

#define PROC_NAME "sysinfo_kmod"

static int sysinfo_show(struct seq_file *m, void *v)
{
    struct sysinfo i;
    si_meminfo(&i);

    // uptime in seconds
    unsigned long uptime = jiffies_to_msecs(get_jiffies_64()) / 1000;

    seq_printf(m,
        "===== System Information =====\n"
        "Uptime: %lu seconds\n"
        "Total RAM: %lu MB\n"
        "Free RAM : %lu MB\n"
        "Load Avg : %lu.%02lu %lu.%02lu %lu.%02lu\n"
        "Kernel   : %s\n"
        "==============================\n",
        uptime,
        (i.totalram * i.mem_unit) / (1024 * 1024),
        (i.freeram * i.mem_unit) / (1024 * 1024),
        LOAD_INT(avenrun[0]), LOAD_FRAC(avenrun[0]),
        LOAD_INT(avenrun[1]), LOAD_FRAC(avenrun[1]),
        LOAD_INT(avenrun[2]), LOAD_FRAC(avenrun[2]),
        utsname()->release
    );
    return 0;
}

static int sysinfo_open(struct inode *inode, struct file *file)
{
    return single_open(file, sysinfo_show, NULL);
}

static const struct proc_ops sysinfo_fops = {
    .proc_open    = sysinfo_open,
    .proc_read    = seq_read,
    .proc_lseek   = seq_lseek,
    .proc_release = single_release,
};

static int __init sysinfo_init(void)
{
    proc_create(PROC_NAME, 0, NULL, &sysinfo_fops);
    pr_info("sysinfo_kmod loaded\n");
    return 0;
}

static void __exit sysinfo_exit(void)
{
    remove_proc_entry(PROC_NAME, NULL);
    pr_info("sysinfo_kmod unloaded\n");
}

module_init(sysinfo_init);
module_exit(sysinfo_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Jyoti Swaroop");
MODULE_DESCRIPTION("System Information Kernel Module");

