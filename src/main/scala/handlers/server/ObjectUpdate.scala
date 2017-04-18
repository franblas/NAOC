package handlers.server

import handlers.GameClient
import handlers.packets.PacketWriter
import org.mongodb.scala.Document

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future
import scala.util.Random

/**
  * Created by franblas on 17/04/17.
  */
class ObjectUpdate(obj: Document, gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player
    val zone =  player.currentZone
    if (player == null || obj.isEmpty || zone.isEmpty) {
      return Future { Array.emptyByteArray }
    }

    val writer = new PacketWriter(0xA1)

    //# var xOffsetInZone = (ushort) (obj.X - z.XOffset);
    //offset_x_in_zone = (obj.X - zone['offset_x']) & 0xFFFF
    val offsetXInZone = obj.getInteger("x") - zone.getInteger("offset_x")

    //# var yOffsetInZone = (ushort) (obj.Y - z.YOffset);
    //offset_y_in_zone = (obj.Y - zone['offset_y']) & 0xFFFF
    val offsetYInZone = obj.getInteger("y") - zone.getInteger("offset_y")

    //# ushort xOffsetInTargetZone = 0;
    //offset_x_in_target_zone = 0
    val offsetXInTargetZone = 0

    //# ushort yOffsetInTargetZone = 0;
    //offset_y_in_target_zone = 0
    val offsetYInTargetZone = 0

    //# ushort zOffsetInTargetZone = 0;
    //offset_z_in_target_zone = 0
    val offsetZInTargetZone = 0

    //# int speed = 0;
    //speed = obj.speed
    //val speed = obj.getInteger("speed")
    val speed = 0

    //# ushort targetZone = 0;
    //target_zone = 0
    val targetZone = 0

    //# byte flags = 0;
    //flags = 0
    val flags = 0

    //# int targetOID = 0;
    //target_OID = 0
    val targetOID = 0

    /*
    # if (obj is GameNPC)
      if obj.object_type == 'npc':
    realm = obj.realm
    if not realm: realm = 0

    tmp_flags = obj.flags
    eflags = obj.eflags
    if tmp_flags:
      new_flags = realm << 6 #tmp_flags << 6
    if tmp_flags & eflags.get('ghost') != 0: new_flags |= 0x01
    if tmp_flags & eflags.get('peace') != 0: new_flags |= 0x10
    if tmp_flags & eflags.get('flying') != 0: new_flags |= 0x20
    if tmp_flags & eflags.get('torch') != 0: new_flags |= 0x04
    flags = new_flags & 0xFF
    */

    //# pak.WriteShort((ushort) speed);
    //ins = write_short(speed)
    writer.writeShort(speed.toShort)

    /*
    # if (obj is GameNPC)
    # {
      # 	pak.WriteShort((ushort)(obj.Heading & 0xFFF));
      # }
    # else
    # {
      # 	pak.WriteShort(obj.Heading);
      # }
    if obj.object_type == 'npc':
    ins += write_short(obj.heading & 0xFFF)
    else:
    ins += write_short(obj.heading)
    */
    writer.writeShort((obj.getInteger("heading") & 0xFFF).toShort)

    //# pak.WriteShort(xOffsetInZone);
    //ins += write_short(offset_x_in_zone)
    writer.writeShort(offsetXInZone.toShort)

    //# pak.WriteShort(xOffsetInTargetZone);
    //ins += write_short(offset_x_in_target_zone)
    writer.writeShort(offsetXInTargetZone.toShort)

    //# pak.WriteShort(yOffsetInZone);
    //ins += write_short(offset_y_in_zone)
    writer.writeShort(offsetYInZone.toShort)

    //# pak.WriteShort(yOffsetInTargetZone);
    //ins += write_short(offset_y_in_target_zone)
    writer.writeShort(offsetYInTargetZone.toShort)

    //# pak.WriteShort((ushort) obj.Z);
    //ins += write_short(obj.Z)
    writer.writeShort(obj.getInteger("z").toShort)

    //# pak.WriteShort(zOffsetInTargetZone);
    //ins += write_short(offset_z_in_target_zone)
    writer.writeShort(offsetZInTargetZone.toShort)

    //# pak.WriteShort((ushort) obj.ObjectID);
    //ins += write_short(obj.object_id)
    writer.writeShort(obj.getInteger("object_id").toShort)

    //# pak.WriteShort((ushort) targetOID);
    //ins += write_short(target_OID)
    writer.writeShort(targetOID.toShort)

    /*
    # #health
    # if (obj is GameLiving)
    # {
      # 	pak.WriteByte((obj as GameLiving).HealthPercent);
      # }
    # else
    # {
      # 	pak.WriteByte(0);
      # }
    ins += write_byte(0)
    */
    writer.writeByte(0x00)

    /*
    # #Dinberg:Instances - zoneskinID for positioning of objects clientside.
    # flags |= (byte) (((z.ZoneSkinID & 0x100) >> 6) | ((targetZone & 0x100) >> 5));
    # pak.WriteByte(flags);
    ins += write_byte(flags)
    */
    writer.writeByte(flags.toByte)

    //# pak.WriteByte((byte) z.ZoneSkinID);
    //ins += write_byte(zone['zone_id'])
    writer.writeByte(zone.getInteger("id").toByte)

    //# #Dinberg:Instances - targetZone already accomodates for this feat.
    //# pak.WriteByte((byte) targetZone);
    //ins += write_byte(target_zone)
    writer.writeByte(targetZone.toByte)

    Future {
      writer.getFinalPacket()
    }
  }
}
