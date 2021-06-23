str = "こんにちは！"

sjis_byte = str.encode("shift_jis")
print(sjis_byte)
utf8_byte = str.encode("utf-8")
print(utf8_byte)

sjis_str = sjis_byte.decode("shift_jis")
print(sjis_str)
utf8_str = utf8_byte.decode("utf-8")
print(utf8_str)