"""
Create hex file in python
$ python create_rom.py

Verify it's content
$ hexdump -C rom.bin 
00000000  a9 ff 8d 02 60 a9 55 8d  00 60 a9 aa 8d 00 60 4c  |....`.U..`....`L|
00000010  05 80 ea ea ea ea ea ea  ea ea ea ea ea ea ea ea  |................|
00000020  ea ea ea ea ea ea ea ea  ea ea ea ea ea ea ea ea  |................|
*
00007ff0  ea ea ea ea ea ea ea ea  ea ea ea ea 00 80 ea ea  |................|
00008000
"""

code = bytearray([
    0xa9, 0xff,         # lda #$ff
    0x8d, 0x02, 0x60,   # sta $6002

    0xa9, 0x55,         # lda #$55
    0x8d, 0x00, 0x60,   # sta $6000

    0xa9, 0xaa,         # lda #$aa
    0x8d, 0x00, 0x60,   # sta $6000

    0x4c, 0x05, 0x80    # jmp $8005
 ])

rom = code + bytearray([0xea] * (32768 - len(code)))

rom[0x7ffc] = 0x00
rom[0x7ffd] = 0x80

with open("rom.bin", "wb") as fh:
    fh.write(rom)

