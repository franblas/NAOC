package handlers.server

import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}
import org.mongodb.scala.Document

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 17/04/17.
  */
class LivingEquipmentUpdate(npc: Document, gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player

    player match {
      case null => Future { Array.emptyByteArray }
      case _ => compute()
    }
  }

  private def compute(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.livingEquipmentUpdate)
    //# pak.WriteShort((ushort)living.ObjectID);
    //ins = write_short(mobs)
    writer.writeShort(npc.getInteger("object_id").toShort)

    //# pak.WriteByte((byte)living.VisibleActiveWeaponSlots);
    //ins += write_byte(0x00)
    writer.writeByte(0x00)

    //# pak.WriteByte((byte)living.CurrentSpeed); # new in 189b+, speed
    //ins += write_byte(0x00)
    writer.writeByte(0x00)

    //# pak.WriteByte((byte)((living.IsCloakInvisible ? 0x01 : 0x00) | (living.IsHelmInvisible ? 0x02 : 0x00))); # new in 189b+, cloack/helm visibility
    //  ins += write_byte(0x00)
    writer.writeByte(0x00)

    //# pak.WriteByte((byte)((living.IsCloakHoodUp ? 0x01 : 0x00) | (int)living.ActiveQuiverSlot)); #bit0 is hood up bit4 to 7 is active quiver
    //  ins += write_byte(0x00)
    writer.writeByte(0x00)

    /*items = npc.inventory['visible_items']
    if items:
      print 'Get items'
    #TODO
    else:
    ins += write_byte(0x00)
    */
    writer.writeByte(0x00)

    writer.toFinalFuture()
  }
}

