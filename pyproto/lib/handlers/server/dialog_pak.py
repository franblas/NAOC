from ..packets.packet_out import *

def dialog_pak(code, data1, data2, data3, data4, dialog_type, auto_wrap_text, msg, gameclient):
  data = gameclient.selected_character
  if not data: return

  # 				pak.WriteByte(0x00);
  ins = write_byte(0x00)
  # 				pak.WriteByte((byte) code);
  ins += write_byte(code)
  # 				pak.WriteShort(data1); #data1
  ins += write_short(data1)
  # 				pak.WriteShort(data2); #data2
  ins += write_short(data2)
  # 				pak.WriteShort(data3); #data3
  ins += write_short(data3)
  # 				pak.WriteShort(data4); #data4
  ins += write_short(data4)
  # 				pak.WriteByte((byte) type);
  ins += write_byte(dialog_type)
  # 				pak.WriteByte((byte) (autoWrapText ? 0x01 : 0x00));
  ins += write_byte(0x01 if auto_wrap_text else 0x00)
  # 				if (message.Length > 0)
  # 					pak.WriteString(message, message.Length);
  if msg: ins += write_string(msg)
  # 				pak.WriteByte(0x00);
  ins += write_byte(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x81)
  pak += ins
  return pak
