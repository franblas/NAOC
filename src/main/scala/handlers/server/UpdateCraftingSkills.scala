package handlers.server

import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 14/04/17.
  */
class UpdateCraftingSkills(gameClient: GameClient) {
  private val craftingSkills: Seq[Map[String, Any]] = Seq(
    Map(
      "points" -> 0x01,
      "icon" -> 0x01,
      "name" -> "Weaponcraft"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x02,
      "name" -> "Armorcraft"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x03,
      "name" -> "Siegecraft"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x04,
      "name" -> "Alchemy"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x06,
      "name" -> "Metalworking"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x07,
      "name" -> "Leathercrafting"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x08,
      "name" -> "Clothworking"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x09,
      "name" -> "Gemcutting"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x0A,
      "name" -> "Herbcraft"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x0B,
      "name" -> "Tailoring"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x0C,
      "name" -> "Fletching"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x0D,
      "name" -> "Spellcrafting"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x0E,
      "name" -> "Woodworking"
    ),
    Map(
      "points" -> 0x01,
      "icon" -> 0x0F,
      "name" -> "Basic Crafting"
    )
  )

  def process(): Future[Array[Byte]] = {
    val player = gameClient.player

    player match {
      case null => Future { Array.emptyByteArray }
      case _ => compute()
    }
  }

  private def compute(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.updateCraftingSkills)
    writer.writeByte(0x08)
    writer.writeByte(craftingSkills.length.toByte)
    writer.writeByte(0x03)
    writer.writeByte(0x00)

    craftingSkills.foreach(skill => {
      writer.writeShort(skill.getOrElse("points", 0x01).toString.toShort)
      writer.writeByte(skill.getOrElse("icon", 0x01).toString.toByte)
      writer.writeInt(0x01)
      writer.writePascalString(skill.getOrElse("name", "").toString)
    })

    writer.toFinalFuture()
  }
}
