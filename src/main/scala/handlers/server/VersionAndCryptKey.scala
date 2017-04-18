package handlers.server

import handlers.packets.{PacketWriter, PacketsUtils}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 26/03/17.
  */
class VersionAndCryptKey(version: String) {

  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(0x22)
    writer.writeByte(0x00)
    writer.writeByte(0x32)
    writer.writeByte(PacketsUtils.parseVersion(version, true))
    writer.writeByte(PacketsUtils.parseVersion(version, false))
    writer.writeByte(0x00)
    Future {
      writer.getFinalPacket()
    }
  }
}