from ..packets.packet_in import *

def player_position_update_handler(packet,gameclient):
    player = gameclient.player #TODO check player state
    cursor = 0

    # int environmentTick = Environment.TickCount;
	# int packetVersion;
	# if (client.Version > GameClient.eClientVersion.Version171)
	# {
	# 	packetVersion = 172;
	# }
	# else
	# {
	# 	packetVersion = 168;
	# }
	# int oldSpeed = client.Player.CurrentSpeed;

    cursor = skip(cursor, 2) # pid
    # ushort data = packet.ReadShort();
    data, cursor = read_short(packet, cursor)
    # int speed = (data & 0x1FF);
    speed = data & 0x1FFF
	# if ((data & 0x200) != 0)
	# 	speed = -speed;
    if (data & 0x200) != 0: speed = -speed
	# if (client.Player.IsMezzed || client.Player.IsStunned)
	# {
	# 	// Nidel: updating client.Player.CurrentSpeed instead of speed
	# 	client.Player.CurrentSpeed = 0;
	# }
	# else
	# {
	# 	client.Player.CurrentSpeed = (short)speed;
	# }
    if player.is_mezzed or player.is_stunned:
        player.current_speed = 0
    else:
        player.current_speed = speed
	# client.Player.IsStrafing = ((data & 0xe000) != 0);
    player.is_strafing = ((data & 0xE000) != 0)
	# int realZ = packet.ReadShort();
    real_Z, cursor = read_short(packet, cursor)
	# ushort xOffsetInZone = packet.ReadShort();
    x_offset_in_zone, cursor = read_short(packet, cursor)
	# ushort yOffsetInZone = packet.ReadShort();
    y_offset_in_zone, cursor = read_short(packet, cursor)
	# ushort currentZoneID;
	# if (packetVersion == 168)
	# {
	# 	currentZoneID = (ushort)packet.ReadByte();
	# 	packet.Skip(1); //0x00 padding for zoneID
	# }
	# else
	# {
	# 	currentZoneID = packet.ReadShort();
	# }
    current_zone_id, cursor = read_short(packet, cursor)

	# Zone newZone = WorldMgr.GetZone(currentZoneID);
	# TODO
    # into data/zones.json
    available_zones = [{
      "Coin": "0",
      "IsLava": "false",
      "Name": "Constantine's Sound",
      "Realmpoints": "0",
      "RegionID": "27",
      "OffsetX": "8",
      "OffsetY": "8",
      "Experience": "0",
      "DivingFlag": "0",
      "LastTimeRowUpdated": "2014-12-09T17:40:23.9775794Z",
      "Width": "8",
      "Height": "8",
      "WaterLevel": "0",
      "Bountypoints": "0",
      "Realm": "0",
      "ZoneID": "27"
    },
    {
      "Coin": "0",
      "IsLava": "false",
      "Name": "Grenlock's Sound",
      "Realmpoints": "0",
      "RegionID": "27",
      "OffsetX": "24",
      "OffsetY": "24",
      "Experience": "0",
      "DivingFlag": "0",
      "LastTimeRowUpdated": "2014-12-09T17:40:23.9775794Z",
      "Width": "8",
      "Height": "8",
      "WaterLevel": "0",
      "Bountypoints": "0",
      "Realm": "0",
      "ZoneID": "28"
    },
    {
      "Coin": "0",
      "IsLava": "false",
      "Name": "Lamfhota's Sound",
      "Realmpoints": "0",
      "RegionID": "27",
      "OffsetX": "40",
      "OffsetY": "40",
      "Experience": "0",
      "DivingFlag": "0",
      "LastTimeRowUpdated": "2014-12-09T17:40:23.9775794Z",
      "Width": "8",
      "Height": "8",
      "WaterLevel": "0",
      "Bountypoints": "0",
      "Realm": "0",
      "ZoneID": "29"
    }]
    # Hibernia tuto zone => zoneid=29
    print "CURRENT ZONE ID: " + str(current_zone_id)
    new_zone = dict()
    for a in available_zones:
        if a.get('ZoneID') == int(current_zone_id):
            new_zone = a

    # if (newZone == null)
	# {
	# 	if(client.Player==null) return;
	# 	if(!client.Player.TempProperties.getProperty("isbeingbanned",false))
	# 	{
	# 		if (log.IsErrorEnabled)
	# 			log.Error(client.Player.Name + "'s position in unknown zone! => " + currentZoneID);
	# 		GamePlayer player=client.Player;
	# 		player.TempProperties.setProperty("isbeingbanned", true);
	# 		player.MoveToBind();
	# 	}
	# 	return; // TODO: what should we do? player lost in space
	# }
    if not new_zone: return

	# // move to bind if player fell through the floor
	# if (realZ == 0)
	# {
	# 	client.Player.MoveTo(
	# 		(ushort)client.Player.BindRegion,
	# 		client.Player.BindXpos,
	# 		client.Player.BindYpos,
	# 		(ushort)client.Player.BindZpos,
	# 		(ushort)client.Player.BindHeading
	# 	);
	# 	return;
	# }

	# int realX = newZone.XOffset + xOffsetInZone;
	# int realY = newZone.YOffset + yOffsetInZone;
    real_X = new_zone.get('OffsetX') + x_offset_in_zone
    real_Y = new_zone.get('OffsetY') + y_offset_in_zone

	# bool zoneChange = newZone != client.Player.LastPositionUpdateZone;
	# if (zoneChange)
	# {
	# 	//If the region changes -> make sure we don't take any falling damage
	# 	if (client.Player.LastPositionUpdateZone != null && newZone.ZoneRegion.ID != client.Player.LastPositionUpdateZone.ZoneRegion.ID)
	# 				client.Player.MaxLastZ = int.MinValue;
	# 		// Update water level and diving flag for the new zone
	# 		client.Out.SendPlayerPositionAndObjectID();
	# 		zoneChange = true;
	# 		/*
	# 		 * "You have entered Burial Tomb."
	# 		 * "Burial Tomb"
	# 		 * "Current area is adjusted for one level 1 player."
	# 		 * "Current area has a 50% instance bonus."
	# 		 */
    #         string description = newZone.Description;
    #         string screenDescription = description;
    #         var translation = client.GetTranslation(newZone) as DBLanguageZone;
    #         if (translation != null)
    #         {
    #             if (!Util.IsEmpty(translation.Description))
    #                 description = translation.Description;
    #             if (!Util.IsEmpty(translation.ScreenDescription))
    #                 screenDescription = translation.ScreenDescription;
    #         }
    #         client.Out.SendMessage(LanguageMgr.GetTranslation(client.Account.Language, "PlayerPositionUpdateHandler.Entered", description),
	# 			    eChatType.CT_System, eChatLoc.CL_SystemWindow);
    #         client.Out.SendMessage(screenDescription, eChatType.CT_ScreenCenterSmaller, eChatLoc.CL_SystemWindow);
	# 		client.Player.LastPositionUpdateZone = newZone;
	# }

	# int coordsPerSec = 0;
	# int jumpDetect = 0;
	# int timediff = Environment.TickCount - client.Player.LastPositionUpdateTick;
	# int distance = 0;
	# if (timediff > 0)
	# {
	# 	distance = client.Player.LastPositionUpdatePoint.GetDistanceTo(new Point3D(realX, realY, realZ));
	# 	coordsPerSec = distance * 1000 / timediff;
	# 	if (distance < 100 && client.Player.LastPositionUpdatePoint.Z > 0)
	# 	{
	# 		jumpDetect = realZ - client.Player.LastPositionUpdatePoint.Z;
	# 	}
	# }
