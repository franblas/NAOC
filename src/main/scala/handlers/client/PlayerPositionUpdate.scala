package handlers.client

import database.{Zone, Zones}
import gameobjects.GamePlayer
import handlers.GameClient
import handlers.packets.PacketReader

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class PlayerPositionUpdate(gameClient: GameClient) extends HandlerProcessor {

  private val zones = new Zones()

  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val reader = new PacketReader(data)
    gameClient.player.map(player => compute(reader, player)).getOrElse(Future { Array.emptyByteArray })
  }

  private def compute(reader: PacketReader, player: GamePlayer): Future[Array[Byte]] = {
    // int environmentTick = Environment.TickCount;
    // int packetVersion;
    // if (client.Version > GameClient.eClientVersion.Version171)
    // {
    // 	packetVersion = 172;
    // }
    // else
    // {
    // 	packetVersion = 168;
    // }
    // int oldSpeed = client.Player.CurrentSpeed;

    // cursor = skip(cursor, 2) // pid
    reader.skip(2) // pid

    // ushort data = packet.ReadShort();
    // data, cursor = read_short(packet, cursor)
    val data2 = reader.readShort()

    // int speed = (data & 0x1FF);
    // speed = data & 0x1FFF
    var speed = data2 & 0x1FFF

    // if ((data & 0x200) != 0)
    // 	speed = -speed;
    //if (data & 0x200) != 0: speed = -speed
    if ((data2 & 0x200) != 0) speed = -1*speed

    // if (client.Player.IsMezzed || client.Player.IsStunned)
    // {
    // 	// Nidel: updating client.Player.CurrentSpeed instead of speed
    // 	client.Player.CurrentSpeed = 0;
    // }
    // else
    // {
    // 	client.Player.CurrentSpeed = (short)speed;
    // }
    //if player.is_mezzed or player.is_stunned:
    //  player.currentpeed = 0
    //else:
    //  player.current_speed = speed
    if (player.isMezzed || player.isStunned) {
      player.currentSpeed = 0
    } else {
      player.currentSpeed = speed
    }

    // client.Player.IsStrafing = ((data & 0xe000) != 0);
    //player.is_strafing = ((data & 0xE000) != 0)
    player.isStrafing = (data2 & 0xE000) != 0

    // int realZ = packet.ReadShort();
    //real_Z, cursor = read_short(packet, cursor)
    val realZ = reader.readShort()

    // ushort xOffsetInZone = packet.ReadShort();
    //x_offset_in_zone, cursor = read_short(packet, cursor)
    val xOffsetInZone = reader.readShort()

    // ushort yOffsetInZone = packet.ReadShort();
    //y_offset_in_zone, cursor = read_short(packet, cursor)
    val yOffsetInZone = reader.readShort()

    // ushort currentZoneID;
    // if (packetVersion == 168)
    // {
    // 	currentZoneID = (ushort)packet.ReadByte();
    // 	packet.Skip(1); //0x00 padding for zoneID
    // }
    // else
    // {
    // 	currentZoneID = packet.ReadShort();
    // }
    //current_zone_id, cursor = read_short(packet, cursor)
    val currentZoneId = reader.readShort()

    // Zone newZone = WorldMgr.GetZone(currentZoneID);
    //print "CURRENT ZONE ID: " + str(current_zone_id) // Hibernia tuto zone => zoneid=29
    //println("CurrentZoneId", currentZoneId)

    //new_zone = get_zone(current_zone_id)
    zones.getZone(currentZoneId.toInt).map(result => {
      val newZone: Zone = result.head

      // if (newZone == null)
      // {
      // 	if(client.Player==null) return;
      // 	if(!client.Player.TempProperties.getProperty("isbeingbanned",false))
      // 	{
      // 		if (log.IsErrorEnabled)
      // 			log.Error(client.Player.Name + "'s position in unknown zone! => " + currentZoneID);
      // 		GamePlayer player=client.Player;
      // 		player.TempProperties.setProperty("isbeingbanned", true);
      // 		player.MoveToBind();
      // 	}
      // 	return; // TODO: what should we do? player lost in space
      // }
      //if not new_zone: return
      if (result.isEmpty) {
        Future { Array.emptyByteArray }
      } else {
        //player.current_zone = new_zone
        player.currentZone = newZone

        // // move to bind if player fell through the floor
        // if (realZ == 0)
        // {
        // 	client.Player.MoveTo(
        // 		(ushort)client.Player.BindRegion,
        // 		client.Player.BindXpos,
        // 		client.Player.BindYpos,
        // 		(ushort)client.Player.BindZpos,
        // 		(ushort)client.Player.BindHeading
        // 	);
        // 	return;
        // }

        // int realX = newZone.XOffset + xOffsetInZone;
        // int realY = newZone.YOffset + yOffsetInZone;
        //real_X = int(new_zone.get('offset_x')) + x_offset_in_zone
        val realX = newZone.offsetX + xOffsetInZone
        //println("realX", realX)

        //real_Y = int(new_zone.get('offset_y')) + y_offset_in_zone
        val realY = newZone.offsetY + yOffsetInZone
        //println("realY", realY)

        player.updateCurrentPosition(realX, realY, realZ.toInt)

        // bool zoneChange = newZone != client.Player.LastPositionUpdateZone;
        // if (zoneChange)
        // {
        // 	//If the region changes -> make sure we don't take any falling damage
        // 	if (client.Player.LastPositionUpdateZone != null && newZone.ZoneRegion.ID != client.Player.LastPositionUpdateZone.ZoneRegion.ID)
        // 				client.Player.MaxLastZ = int.MinValue;
        // 		// Update water level and diving flag for the new zone
        // 		client.Out.SendPlayerPositionAndObjectID();
        // 		zoneChange = true;
        // 		/*
        // 		 * "You have entered Burial Tomb."
        // 		 * "Burial Tomb"
        // 		 * "Current area is adjusted for one level 1 player."
        // 		 * "Current area has a 50% instance bonus."
        // 		 */
        //         string description = newZone.Description;
        //         string screenDescription = description;
        //         var translation = client.GetTranslation(newZone) as DBLanguageZone;
        //         if (translation != null)
        //         {
        //             if (!Util.IsEmpty(translation.Description))
        //                 description = translation.Description;
        //             if (!Util.IsEmpty(translation.ScreenDescription))
        //                 screenDescription = translation.ScreenDescription;
        //         }
        //         client.Out.SendMessage(LanguageMgr.GetTranslation(client.Account.Language, "PlayerPositionUpdateHandler.Entered", description),
        // 			    eChatType.CT_System, eChatLoc.CL_SystemWindow);
        //         client.Out.SendMessage(screenDescription, eChatType.CT_ScreenCenterSmaller, eChatLoc.CL_SystemWindow);
        // 		client.Player.LastPositionUpdateZone = newZone;
        // }

        // int coordsPerSec = 0;
        // int jumpDetect = 0;
        // int timediff = Environment.TickCount - client.Player.LastPositionUpdateTick;
        // int distance = 0;
        // if (timediff > 0)
        // {
        // 	distance = client.Player.LastPositionUpdatePoint.GetDistanceTo(new Point3D(realX, realY, realZ));
        // 	coordsPerSec = distance * 1000 / timediff;
        // 	if (distance < 100 && client.Player.LastPositionUpdatePoint.Z > 0)
        // 	{
        // 		jumpDetect = realZ - client.Player.LastPositionUpdatePoint.Z;
        // 	}
        // }
      }
    }).flatMap(_ => {
      Future { Array.emptyByteArray }
    })
  }
}
