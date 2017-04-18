package handlers.packets

import java.nio.{ByteBuffer, ByteOrder}

/**
  * Created by franblas on 26/03/17.
  */
class PacketWriter(val packetCode: Int) extends Packets {

  var packet: Array[Byte] = Array.emptyByteArray

  def writeByte(code: Byte): Unit = {
    packet ++= ByteBuffer.allocate(byteSize).put(code).array
  }

  def writeShort(code: Short, endian: ByteOrder = ByteOrder.BIG_ENDIAN): Unit = {
    packet ++= ByteBuffer.allocate(shortSize).order(endian).putShort(code).array
  }

  def writeInt(code: Int, endian: ByteOrder = ByteOrder.BIG_ENDIAN): Unit = {
    packet ++= ByteBuffer.allocate(intSize).order(endian).putInt(code).array
  }

  def writeLong(code: Long, endian: ByteOrder = ByteOrder.BIG_ENDIAN): Unit = {
    packet ++= ByteBuffer.allocate(longSize).order(endian).putLong(code).array
  }

  def writeString(str: String): Unit = {
    if (str.isEmpty) {
      writeByte(0x0)
    } else {
      packet ++= str.getBytes
    }
  }

  def writePascalString(str: String): Unit = {
    if (str.isEmpty) {
      writeByte(0x0)
    } else {
      val bytes = str.getBytes
      packet :+= bytes.length.toByte
      packet ++= bytes
    }
  }

  def fill(code: Byte, n: Int): Unit = {
    for (_ <- 0 until n) { writeByte(code) }
  }

  def fillString(str: String, n: Int): Unit = {
    val bytes = str.getBytes()
    if (n <= bytes.length) {
      writeString(str)
    } else {
      writeString(str)
      fill(0x00, n - bytes.length)
    }
  }

  def getFinalPacket(): Array[Byte] = {
    // maybe prepend to array better ?
    var finalPacket: Array[Byte] = Array.emptyByteArray
    finalPacket ++= ByteBuffer.allocate(shortSize).order(ByteOrder.BIG_ENDIAN).putShort(packet.length.toShort).array
    finalPacket :+= packetCode.toByte
    finalPacket ++= packet
    finalPacket
  }

}
