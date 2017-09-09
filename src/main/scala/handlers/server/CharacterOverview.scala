package handlers.server

import java.nio.ByteOrder

import database.{Characters, Classes, Races}
import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration._
import scala.concurrent.{Await, Future}

/**
  * Created by franblas on 07/04/17.
  */
class CharacterOverview(realm: Int, gameClient: GameClient) {
  private val characters = new Characters()
  private val classes = new Classes()
  private val races = new Races()

  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.characterOverview)
    val loginName = gameClient.loginName
    writer.fillString(loginName, 24)

    characters.getCharacters(loginName, realm).map(result => {
      if (result.isEmpty) {
        writer.fill(0x0, 1880)
      } else {
        val firstAccountSlot = realm match {
          case 0x01 => 100
          case 0x02 => 200
          case 0x03 => 300
        }

        for (i <- firstAccountSlot until firstAccountSlot+10) {
          var written: Boolean = false
          result.foreach(character => {
            val characterAccountSlot = character.accountSlot
            if (characterAccountSlot == i) {
              writer.fill(0x0, 4)
              writer.fillString(character.name, 24)
              writer.writeByte(0x01)
              writer.writeByte(character.eyeSize.toByte)
              writer.writeByte(character.lipSize.toByte)
              writer.writeByte(character.eyeColor.toByte)
              writer.writeByte(character.hairColor.toByte)
              writer.writeByte(character.faceType.toByte)
              writer.writeByte(character.hairStyle.toByte)
              writer.writeByte(0x0)
              writer.writeByte(0x0)
              writer.writeByte(character.customMode.toByte)
              writer.writeByte(character.moodType.toByte)
              writer.fill(0x0, 13)
              // TODO
              // Region reg = WorldMgr.GetRegion((ushort) characters[j].Region);
              // if (reg != null)
              // {
              //  var description = m_gameClient.GetTranslatedSpotDescription(reg, characters[j].Xpos, characters[j].Ypos, characters[j].Zpos);
              //  pak.FillString(description, 24);
              // }
              // else
              //   pak.Fill(0x0, 24); //No known location
              writer.fill(0x0, 24) // No known location

              // TODO: try to get rid of await
              Await.result(classes.getCharClass(character.charClass).map(result => {
                //writer.fillString(result.head.getString("char_class_name"), 24)
                writer.fillString(result.head.characterClassName, 24)
              }), 5000 millis)

              // TODO: try to get rid of await
              Await.result(races.getRace(character.race).map(result => {
                //writer.fillString(result.head.getString("race_id"), 24)
                writer.fillString(result.head.raceId, 24)
              }), 5000 millis)

              writer.writeByte(character.level.toByte)
              writer.writeByte(character.charClass.toByte)
              writer.writeByte(character.realm.toByte)
              val flag: Int = (((character.race & 0x10) << 2) + (character.race & 0x0F)) | (character.gender << 4)
              writer.writeByte(flag.toByte)
              writer.writeShort(character.creationModel.toShort, ByteOrder.LITTLE_ENDIAN)
              writer.writeByte(character.region.toByte)
              // TODO
              // if (reg == null || (int) m_gameClient.ClientType > reg.Expansion)
              //  pak.WriteByte(0x00);
              // else
              //  pak.WriteByte((byte) (reg.Expansion + 1)); //0x04-Cata zone, 0x05 - DR zone
              writer.writeByte(0x00)

              writer.writeInt(0x00) // Internal database ID
              writer.writeByte(character.strength.toByte)
              writer.writeByte(character.dexterity.toByte)
              writer.writeByte(character.constitution.toByte)
              writer.writeByte(character.quickness.toByte)
              writer.writeByte(character.intelligence.toByte)
              writer.writeByte(character.piety.toByte)
              writer.writeByte(character.empathy.toByte)
              writer.writeByte(character.charisma.toByte)


              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)
              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)
              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)

              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)

              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)
              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)
              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)
              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)

              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)

              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)

              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)

              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)

              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)

              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)

              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)

              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)

              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)
              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)
              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)
              writer.writeShort(0x0, ByteOrder.LITTLE_ENDIAN)

              writer.writeByte(0xFF.toByte)
              writer.writeByte(0xFF.toByte)
              writer.writeByte(0x00)
              writer.writeByte(character.constitution.toByte)
              written = true
            }
          })
          if (!written) writer.fill(0x0, 188)
        }
      }
      writer.fill(0x0, 94)
      writer.getFinalPacket()
    })
  }
}
