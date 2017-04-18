package handlers.server

import java.nio.ByteOrder

import database.{Characters, Classes, Races}
import handlers.GameClient
import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.{Await, Future}
import scala.concurrent.duration._

/**
  * Created by franblas on 07/04/17.
  */
class CharacterOverview(realm: Int, gameClient: GameClient) {
  private val characters = new Characters()
  private val classes = new Classes()
  private val races = new Races()

  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(0xFD)
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
            val characterAccountSlot = character.getInteger("account_slot", -1)
            if (characterAccountSlot == i) {
              writer.fill(0x0, 4)
              writer.fillString(character.getString("name"), 24)
              writer.writeByte(0x01)
              writer.writeByte(character.getInteger("eye_size").toByte)
              writer.writeByte(character.getInteger("lip_size").toByte)
              writer.writeByte(character.getInteger("eye_color").toByte)
              writer.writeByte(character.getInteger("hair_color").toByte)
              writer.writeByte(character.getInteger("face_type").toByte)
              writer.writeByte(character.getInteger("hair_style").toByte)
              writer.writeByte(0x0)
              writer.writeByte(0x0)
              writer.writeByte(character.getInteger("custom_mode").toByte)
              writer.writeByte(character.getInteger("mood_type").toByte)
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

              Await.result(classes.getCharClass(character.getInteger("char_class")).map(result => {
                writer.fillString(result.head.getString("char_class_name"), 24)
              }), 2000 millis)

              Await.result(races.getRace(character.getInteger("race")).map(result => {
                writer.fillString(result.head.getString("race_id"), 24)
              }), 2000 millis)

              writer.writeByte(character.getInteger("level").toByte)
              writer.writeByte(character.getInteger("char_class").toByte)
              writer.writeByte(character.getInteger("realm").toByte)
              val flag: Int = (((character.getInteger("race") & 0x10) << 2) + (character.getInteger("race") & 0x0F)) | (character.getInteger("gender") << 4)
              writer.writeByte(flag.toByte)
              writer.writeShort(character.getInteger("creation_model").toShort, ByteOrder.LITTLE_ENDIAN)
              writer.writeByte(character.getInteger("region").toByte)
              // TODO
              // if (reg == null || (int) m_gameClient.ClientType > reg.Expansion)
              //  pak.WriteByte(0x00);
              // else
              //  pak.WriteByte((byte) (reg.Expansion + 1)); //0x04-Cata zone, 0x05 - DR zone
              writer.writeByte(0x00)

              writer.writeInt(0x00) // Internal database ID
              writer.writeByte(character.getInteger("strength").toByte)
              writer.writeByte(character.getInteger("dexterity").toByte)
              writer.writeByte(character.getInteger("constitution").toByte)
              writer.writeByte(character.getInteger("quickness").toByte)
              writer.writeByte(character.getInteger("intelligence").toByte)
              writer.writeByte(character.getInteger("piety").toByte)
              writer.writeByte(character.getInteger("empathy").toByte)
              writer.writeByte(character.getInteger("charisma").toByte)


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
              writer.writeByte(character.getInteger("constitution").toByte)
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
