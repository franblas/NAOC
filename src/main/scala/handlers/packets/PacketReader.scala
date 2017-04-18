package handlers.packets

import java.nio.{ByteBuffer, ByteOrder}

/**
  * Created by franblas on 26/03/17.
  */
class PacketReader(val data: Array[Byte]) extends Packets {

  var cursor: Int = 0

  def skip(a: Int): Unit = {
    cursor += a
  }

  def readByte(): Byte = {
    val res: Byte = data(cursor)
    cursor += byteSize
    res
  }

  def readShort(endian: ByteOrder = ByteOrder.BIG_ENDIAN): Short = {
    val res: Short = ByteBuffer.wrap(data.slice(cursor, cursor+shortSize)).order(endian).getShort
    cursor += shortSize
    res
  }

  def readInt(endian: ByteOrder = ByteOrder.BIG_ENDIAN): Int = {
    val res: Int = ByteBuffer.wrap(data.slice(cursor, cursor+intSize)).order(endian).getInt
    cursor += intSize
    res
  }

  def readString(size: Int): String = {
    val res: String = PacketsUtils.printableString(new String(data.slice(cursor, cursor+size)))
    cursor += size
    res
  }

}
