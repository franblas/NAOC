package handlers.server

import java.nio.ByteOrder

import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 14/04/17.
  */
class UpdatePoints {
  def process(): Future[Array[Byte]] = {
    val realmPoints = 0x00 //TODO
    val levelPermill = 0x00 //TODO
    val skillSpecialityPoints = 0x00 //TODO
    val bountyPoints = 0x00 //TODO
    val realmSpecialityPoints = 0x00 //TODO
    val championLevelPermill = 0x00 //TODO
    val experience = 0x00 //TODO
    val experienceForNextLevel = 0x32 //TODO
    val champExperience = 0x00
    val champExperienceForNextLevel = 0x00

    val writer = new PacketWriter(0x91)
    writer.writeInt(realmPoints.toInt)
    writer.writeShort(levelPermill.toShort)
    writer.writeShort(skillSpecialityPoints.toShort)
    writer.writeInt(bountyPoints.toInt)
    writer.writeShort(realmSpecialityPoints.toShort)
    writer.writeShort(championLevelPermill.toShort)
    writer.writeLong(experience.toLong, ByteOrder.LITTLE_ENDIAN)
    writer.writeLong(experienceForNextLevel.toLong, ByteOrder.LITTLE_ENDIAN)
    writer.writeLong(champExperience.toLong, ByteOrder.LITTLE_ENDIAN)
    writer.writeLong(champExperienceForNextLevel.toLong, ByteOrder.LITTLE_ENDIAN)
    Future {
      writer.getFinalPacket()
    }
  }
}
