from commands import *

def configure(link):
    link.do_command(SetSoftwareEncoding(Encoding.MANCHESTER))
    link.set_base_frequency(433910000)
    link.update_register(Register.PKTCTRL1, 0x20)
    link.update_register(Register.PKTCTRL0, 0x00)
    link.update_register(Register.FSCTRL1, 0x06)
    link.update_register(Register.PKTCTRL1, 0x20)
    link.update_register(Register.MDMCFG4, 0xCA)
    link.update_register(Register.MDMCFG3, 0xBC)
    link.update_register(Register.MDMCFG2, 0x06)
    link.update_register(Register.MDMCFG1, 0x10)
    link.update_register(Register.MDMCFG0, 0x11)
    link.update_register(Register.DEVIATN, 0x47)
    link.update_register(Register.MCSM0, 0x18)
    link.update_register(Register.FOCCFG, 0x17)
    link.update_register(Register.FSCAL3, 0xE9)
    link.update_register(Register.FSCAL2, 0x2A)
    link.update_register(Register.FSCAL1, 0x00)
    link.update_register(Register.FSCAL0, 0x1F)
    link.update_register(Register.TEST1, 0x31)
    link.update_register(Register.TEST0, 0x09)
    link.update_register(Register.PATABLE0, 0x84)
    link.update_register(Register.SYNC1, 0xA5)
    link.update_register(Register.SYNC0, 0x5A)
