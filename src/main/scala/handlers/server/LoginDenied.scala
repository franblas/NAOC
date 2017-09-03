package handlers.server

import handlers.packets.{PacketWriter, PacketsUtils, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 26/03/17.
  */
class LoginDenied(version: String, errorCode: Byte) {

  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.loginDenied)
    writer.writeByte(errorCode)
    writer.writeByte(0x01)
    writer.writeByte(PacketsUtils.parseVersion(version, true))
    writer.writeByte(PacketsUtils.parseVersion(version, false))
    writer.writeByte(0x00)
    writer.toFinalFuture()
  }
}
