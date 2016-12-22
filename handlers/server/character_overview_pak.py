from ..packets.packet_out import *
import json

def character_overview_pak(realm):
  ins = fill_string_pak('pacobro', 24) # TODO: replace with account name
  characters = [] #TODO: get characters from the db
  try:
    with open('character_test.json', 'r') as f:
      characters.append(json.load(f))
  except Exception as e:
    print e

  if not characters:
    ins += fill_pak(0x0, 1880)
  else:
    if realm == 0x01:
      first_account_slot = 100
    elif realm == 0x02:
      first_account_slot = 200
    elif realm == 0x03:
      first_account_slot = 300
    else:
      return # should throw an error or something else

    for i in range(first_account_slot, first_account_slot + 10):
      written = False
      # print i
      for character in characters:
        character_account_slot = character.get('account_slot', -1)
        if character_account_slot != i: break
        print 'Into loop char'
        # TODO
        #for (int j = 0; j < characters.Length && written == false; j++)
        #  if (characters[j].AccountSlot == i)
        #{
        ins += fill_pak(0x0, 4)
        ins += fill_string_pak(character['name'], 24)

        ins += write_byte(0x01)
        ins += write_byte(character['eye_size'])
        ins += write_byte(character['lip_size'])
        ins += write_byte(character['eye_color'])
        ins += write_byte(character['hair_color'])
        ins += write_byte(character['face_type'])
        ins += write_byte(character['hair_style'])
        ins += write_byte(0x0) # pak.WriteByte((byte)((extensionBoots << 4) | extensionGloves));
        ins += write_byte(0x0) # pak.WriteByte((byte)((extensionTorso << 4) | (c.IsCloakHoodUp ? 0x1 : 0x0)));
        ins += write_byte(character['custom_mode'])
        ins += write_byte(character['mood_type'])
        ins += fill_pak(0x0, 13)

        #TODO
        # Region reg = WorldMgr.GetRegion((ushort) characters[j].Region);
        # if (reg != null)
        # {
        #   var description = m_gameClient.GetTranslatedSpotDescription(reg, characters[j].Xpos, characters[j].Ypos, characters[j].Zpos);
        #   pak.FillString(description, 24);
        # }
        # else
        #   pak.Fill(0x0, 24); //No known location
        ins += fill_pak(0x0, 24) # No known location
        ins += fill_string_pak("", 24); # Class name

        #TODO
        #//pak.FillString(GamePlayer.RACENAMES[characters[j].Race], 24);
        #pak.FillString(m_gameClient.RaceToTranslatedName(characters[j].Race, characters[j].Gender), 24);
        # ins += fill_string_pak('Elf', 24) # Race name
        with open("data/races.json", "r") as f:
          data = json.load(f)
        plop = ""
        for d in data:
          if d.get('ID') == character['race']:
            plop = d.get('Race_ID')
            break
        ins += fill_string_pak(plop, 24) # Race name

        ins += write_byte(character['level'])
        ins += write_byte(character['char_class'])
        ins += write_byte(character['realm'])
        ins += write_byte((((character['race'] & 0x10) << 2) + (character['race'] & 0x0F)) | (character['gender'] << 4))
        ins += write_short(character['creation_model'], endian='little')
        ins += write_byte(character['region'])

        #TODO
        #if (reg == null || (int) m_gameClient.ClientType > reg.Expansion)
        #  pak.WriteByte(0x00);
        #else
        #  pak.WriteByte((byte) (reg.Expansion + 1)); //0x04-Cata zone, 0x05 - DR zone
        ins += write_byte(0x00)

        ins += write_int(0x00) # Internal database ID
        ins += write_byte(character['strength'])
        ins += write_byte(character['dexterity'])
        ins += write_byte(character['constitution'])
        ins += write_byte(character['quickness'])
        ins += write_byte(character['intelligence'])
        ins += write_byte(character['piety'])
        ins += write_byte(character['empathy'])
        ins += write_byte(character['charisma'])

        #TODO
        # pak.WriteShortLowEndian((ushort)(helmet != null ? helmet.Model : 0));
        # pak.WriteShortLowEndian((ushort)(gloves != null ? gloves.Model : 0));
        # pak.WriteShortLowEndian((ushort)(boots != null ? boots.Model : 0));
        ins += write_short(0x00, endian='little')
        ins += write_short(0x00, endian='little')
        ins += write_short(0x00, endian='little')

        #TODO
        # ushort rightHandColor = 0;
        # if (rightHandWeapon != null)
        # {
        #   rightHandColor = (ushort)(rightHandWeapon.Emblem != 0 ? rightHandWeapon.Emblem : rightHandWeapon.Color);
        # }
        # pak.WriteShortLowEndian(rightHandColor);
        ins += write_short(0x00, endian='little')

        # pak.WriteShortLowEndian((ushort)(torso != null ? torso.Model : 0));
        # pak.WriteShortLowEndian((ushort)(cloak != null ? cloak.Model : 0));
        # pak.WriteShortLowEndian((ushort)(legs != null ? legs.Model : 0));
        # pak.WriteShortLowEndian((ushort)(arms != null ? arms.Model : 0));
        ins += write_short(0x00, endian='little')
        ins += write_short(0x00, endian='little')
        ins += write_short(0x00, endian='little')
        ins += write_short(0x00, endian='little')

        #TODO
        # ushort helmetColor = 0;
        # if (helmet != null)
        # {
        #   helmetColor = (ushort)(helmet.Emblem != 0 ? helmet.Emblem : helmet.Color);
        # }
        # pak.WriteShortLowEndian(helmetColor);
        ins += write_short(0x00, endian='little')

        # ushort glovesColor = 0;
        # if (gloves != null)
        # {
        #   glovesColor = (ushort)(gloves.Emblem != 0 ? gloves.Emblem : gloves.Color);
        # }
        # pak.WriteShortLowEndian(glovesColor);
        ins += write_short(0x00, endian='little')

        # ushort bootsColor = 0;
        # if (boots != null)
        # {
        #   bootsColor = (ushort)(boots.Emblem != 0 ? boots.Emblem : boots.Color);
        # }
        # pak.WriteShortLowEndian(bootsColor);
        ins += write_short(0x00, endian='little')

        # ushort leftHandWeaponColor = 0;
        # if (leftHandWeapon != null)
        # {
        #   leftHandWeaponColor = (ushort)(leftHandWeapon.Emblem != 0 ? leftHandWeapon.Emblem : leftHandWeapon.Color);
        # }
        # pak.WriteShortLowEndian(leftHandWeaponColor);
        ins += write_short(0x00, endian='little')

        # ushort torsoColor = 0;
        # if (torso != null)
        # {
        #   torsoColor = (ushort)(torso.Emblem != 0 ? torso.Emblem : torso.Color);
        # }
        # pak.WriteShortLowEndian(torsoColor);
        ins += write_short(0x00, endian='little')

        # ushort cloakColor = 0;
        # if (cloak != null)
        # {
        #   cloakColor = (ushort)(cloak.Emblem != 0 ? cloak.Emblem : cloak.Color);
        # }
        # pak.WriteShortLowEndian(cloakColor);
        ins += write_short(0x00, endian='little')

        # ushort legsColor = 0;
        # if (legs != null)
        # {
        #   legsColor = (ushort)(legs.Emblem != 0 ? legs.Emblem : legs.Color);
        # }
        # pak.WriteShortLowEndian(legsColor);
        ins += write_short(0x00, endian='little')

        # ushort armsColor = 0;
        # if (arms != null)
        # {
        #   armsColor = (ushort)(arms.Emblem != 0 ? arms.Emblem : arms.Color);
        # }
        # pak.WriteShortLowEndian(armsColor);
        ins += write_short(0x00, endian='little')

        # pak.WriteShortLowEndian((ushort)(rightHandWeapon != null ? rightHandWeapon.Model : 0));
        # pak.WriteShortLowEndian((ushort)(leftHandWeapon != null ? leftHandWeapon.Model : 0));
        # pak.WriteShortLowEndian((ushort)(twoHandWeapon != null ? twoHandWeapon.Model : 0));
        # pak.WriteShortLowEndian((ushort)(distanceWeapon != null ? distanceWeapon.Model : 0));
        ins += write_short(0x00, endian='little')
        ins += write_short(0x00, endian='little')
        ins += write_short(0x00, endian='little')
        ins += write_short(0x00, endian='little')

        #TODO
        # if (characters[j].ActiveWeaponSlot == (byte) GameLiving.eActiveWeaponSlot.TwoHanded)
        # {
        #   pak.WriteByte(0x02);
        #   pak.WriteByte(0x02);
        # }
        # else if (characters[j].ActiveWeaponSlot == (byte) GameLiving.eActiveWeaponSlot.Distance)
        # {
        #   pak.WriteByte(0x03);
        #   pak.WriteByte(0x03);
        # }
        # else
        # {
        #   byte righthand = 0xFF;
        #   byte lefthand = 0xFF;
        #   foreach (InventoryItem item in items)
        #   {
        #     if (item.SlotPosition == (int) eInventorySlot.RightHandWeapon)
        #       righthand = 0x00;
        #     if (item.SlotPosition == (int) eInventorySlot.LeftHandWeapon)
        #       lefthand = 0x01;
        #   }
        #   if (righthand == lefthand)
        #   {
        #     if (characters[j].ActiveWeaponSlot == (byte) GameLiving.eActiveWeaponSlot.TwoHanded)
        #       righthand = lefthand = 0x02;
        #     else if (characters[j].ActiveWeaponSlot == (byte) GameLiving.eActiveWeaponSlot.Distance)
        #       righthand = lefthand = 0x03;
        #   }
        #   pak.WriteByte(righthand);
        #   pak.WriteByte(lefthand);
        # }
        ins += write_byte(0xFF)
        ins += write_byte(0xFF)

        #TODO
        # if (reg == null || reg.Expansion != 1)
        #   pak.WriteByte(0x00);
        # else
        #   pak.WriteByte(0x01); //0x01=char in ShroudedIsles zone, classic client can't "play"
        # //pak.WriteByte(0x00);
        # pak.WriteByte((byte) characters[j].Constitution);
        # //pak.Fill(0x00,2);
        # written = true;
        ins += write_byte(0x00)
        ins += write_byte(character['constitution'])
        written = True

      if not written:
        ins += fill_pak(0x00, 188)

  ins += fill_pak(0x00, 94)

  print 'packet_length: ' + str(packet_length(ins))
  pak = write_short(packet_length(ins))
  pak += write_byte(0xFD)
  pak += ins
  return pak
