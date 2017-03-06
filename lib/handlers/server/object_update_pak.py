from ..packets.packet_out import *

def object_update_pak(gameclient, obj, obj_id):
    player = gameclient.player
    if not player: return

    zone = obj.get('current_zone', player.current_zone)
    if not zone: return

    # var xOffsetInZone = (ushort) (obj.X - z.XOffset);
    offset_x_in_zone = (obj['X'] - zone['offset_x']) & 0xFFFF

    # var yOffsetInZone = (ushort) (obj.Y - z.YOffset);
    offset_y_in_zone = (obj['Y'] - zone['offset_y']) & 0xFFFF

    # ushort xOffsetInTargetZone = 0;
    offset_x_in_target_zone = 0

    # ushort yOffsetInTargetZone = 0;
    offset_y_in_target_zone = 0

    # ushort zOffsetInTargetZone = 0;
    offset_z_in_target_zone = 0

    # int speed = 0;
    speed = 0

    # ushort targetZone = 0;
    target_zone = 0

    # byte flags = 0;
    flags = 0

    # int targetOID = 0;
    target_OID = 0

    # if (obj is GameNPC)
    if obj['object_type'] == 'npc':
        realm = obj.get('realm', 0)
        if not realm: realm = 0

        tmp_flags = obj.get('flags', 0)
        eflags = obj.get('eflags')
        if tmp_flags:
            new_flags = realm << 6 #tmp_flags << 6
            if tmp_flags & eflags.get('ghost') != 0: new_flags |= 0x01
            if tmp_flags & eflags.get('peace') != 0: new_flags |= 0x10
            if tmp_flags & eflags.get('flying') != 0: new_flags |= 0x20
            if tmp_flags & eflags.get('torch') != 0: new_flags |= 0x04
            flags = new_flags & 0xFF

    # pak.WriteShort((ushort) speed);
    ins = write_short(speed)
    # if (obj is GameNPC)
    # {
    # 	pak.WriteShort((ushort)(obj.Heading & 0xFFF));
    # }
    # else
    # {
    # 	pak.WriteShort(obj.Heading);
    # }
    if obj['object_type'] == 'npc':
        ins += write_short(obj['heading'] & 0xFFF)
    else:
        ins += write_short(obj['heading'])

    # pak.WriteShort(xOffsetInZone);
    ins += write_short(offset_x_in_zone)
    # pak.WriteShort(xOffsetInTargetZone);
    ins += write_short(offset_x_in_target_zone)
    # pak.WriteShort(yOffsetInZone);
    ins += write_short(offset_y_in_zone)
    # pak.WriteShort(yOffsetInTargetZone);
    ins += write_short(offset_y_in_target_zone)
    # pak.WriteShort((ushort) obj.Z);
    ins += write_short(obj['Z'])
    # pak.WriteShort(zOffsetInTargetZone);
    ins += write_short(offset_z_in_target_zone)
    # pak.WriteShort((ushort) obj.ObjectID);
    ins += write_short(obj_id)
    # pak.WriteShort((ushort) targetOID);
    ins += write_short(target_OID)
    # //health
    # if (obj is GameLiving)
    # {
    # 	pak.WriteByte((obj as GameLiving).HealthPercent);
    # }
    # else
    # {
    # 	pak.WriteByte(0);
    # }
    ins += write_byte(0)
    # //Dinberg:Instances - zoneskinID for positioning of objects clientside.
    # flags |= (byte) (((z.ZoneSkinID & 0x100) >> 6) | ((targetZone & 0x100) >> 5));
    # pak.WriteByte(flags);
    ins += write_byte(flags)
    # pak.WriteByte((byte) z.ZoneSkinID);
    ins += write_byte(zone['zone_id'])
    # //Dinberg:Instances - targetZone already accomodates for this feat.
    # pak.WriteByte((byte) targetZone);
    ins += write_byte(target_zone)

    pak = write_short(packet_length(ins))
    pak += write_byte(0xA1)
    pak += ins
    return pak


# a
# 		public virtual void SendObjectUpdate(GameObject obj)
# 		{
# 			Zone z = obj.CurrentZone;
#
# 			if (z == null ||
# 				m_gameClient.Player == null ||
# 				m_gameClient.Player.IsVisibleTo(obj) == false)
# 			{
# 				return;
# 			}
#
# 			var xOffsetInZone = (ushort) (obj.X - z.XOffset);
# 			var yOffsetInZone = (ushort) (obj.Y - z.YOffset);
# 			ushort xOffsetInTargetZone = 0;
# 			ushort yOffsetInTargetZone = 0;
# 			ushort zOffsetInTargetZone = 0;
#
# 			int speed = 0;
# 			ushort targetZone = 0;
# 			byte flags = 0;
# 			int targetOID = 0;
# 			if (obj is GameNPC)
# 			{
# 				var npc = obj as GameNPC;
# 				flags = (byte) (GameServer.ServerRules.GetLivingRealm(m_gameClient.Player, npc) << 6);
#
# 				if (m_gameClient.Account.PrivLevel < 2)
# 				{
# 					// no name only if normal player
# 					if ((npc.Flags & GameNPC.eFlags.CANTTARGET) != 0)
# 						flags |= 0x01;
# 					if ((npc.Flags & GameNPC.eFlags.DONTSHOWNAME) != 0)
# 						flags |= 0x02;
# 				}
# 				if ((npc.Flags & GameNPC.eFlags.STATUE) != 0)
# 				{
# 					flags |= 0x01;
# 				}
# 				if (npc.IsUnderwater)
# 				{
# 					flags |= 0x10;
# 				}
# 				if ((npc.Flags & GameNPC.eFlags.FLYING) != 0)
# 				{
# 					flags |= 0x20;
# 				}
#
# 				if (npc.IsMoving && !npc.IsAtTargetPosition)
# 				{
# 					speed = npc.CurrentSpeed;
# 					if (npc.TargetPosition.X != 0 || npc.TargetPosition.Y != 0 || npc.TargetPosition.Z != 0)
# 					{
# 						Zone tz = npc.CurrentRegion.GetZone(npc.TargetPosition.X, npc.TargetPosition.Y);
# 						if (tz != null)
# 						{
# 							xOffsetInTargetZone = (ushort) (npc.TargetPosition.X - tz.XOffset);
# 							yOffsetInTargetZone = (ushort) (npc.TargetPosition.Y - tz.YOffset);
# 							zOffsetInTargetZone = (ushort) (npc.TargetPosition.Z);
# 							//Dinberg:Instances - zoneSkinID for object positioning clientside.
# 							targetZone = tz.ZoneSkinID;
# 						}
# 					}
#
# 					if (speed > 0x07FF)
# 					{
# 						speed = 0x07FF;
# 					}
# 					else if (speed < 0)
# 					{
# 						speed = 0;
# 					}
# 				}
#
# 				GameObject target = npc.TargetObject;
# 				if (npc.AttackState && target != null && target.ObjectState == GameObject.eObjectState.Active && !npc.IsTurningDisabled)
# 					targetOID = (ushort) target.ObjectID;
# 			}
#
# 			using (GSUDPPacketOut pak = new GSUDPPacketOut(GetPacketCode(eServerPackets.ObjectUpdate)))
# 			{
# 				pak.WriteShort((ushort) speed);
#
# 				if (obj is GameNPC)
# 				{
# 					pak.WriteShort((ushort)(obj.Heading & 0xFFF));
# 				}
# 				else
# 				{
# 					pak.WriteShort(obj.Heading);
# 				}
# 				pak.WriteShort(xOffsetInZone);
# 				pak.WriteShort(xOffsetInTargetZone);
# 				pak.WriteShort(yOffsetInZone);
# 				pak.WriteShort(yOffsetInTargetZone);
# 				pak.WriteShort((ushort) obj.Z);
# 				pak.WriteShort(zOffsetInTargetZone);
# 				pak.WriteShort((ushort) obj.ObjectID);
# 				pak.WriteShort((ushort) targetOID);
# 				//health
# 				if (obj is GameLiving)
# 				{
# 					pak.WriteByte((obj as GameLiving).HealthPercent);
# 				}
# 				else
# 				{
# 					pak.WriteByte(0);
# 				}
# 				//Dinberg:Instances - zoneskinID for positioning of objects clientside.
# 				flags |= (byte) (((z.ZoneSkinID & 0x100) >> 6) | ((targetZone & 0x100) >> 5));
# 				pak.WriteByte(flags);
# 				pak.WriteByte((byte) z.ZoneSkinID);
# 				//Dinberg:Instances - targetZone already accomodates for this feat.
# 				pak.WriteByte((byte) targetZone);
# 				SendUDP(pak);
# 			}
#
# 			// Update Cache
# 			m_gameClient.GameObjectUpdateArray[new Tuple<ushort, ushort>(obj.CurrentRegionID, (ushort)obj.ObjectID)] = GameTimer.GetTickCount();
#
# 			if (obj is GameNPC)
# 			{
# 				(obj as GameNPC).NPCUpdatedCallback();
# 			}
# 		}
