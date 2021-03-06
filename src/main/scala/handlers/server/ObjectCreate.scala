package handlers.server

import database.WorldObject
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 08/05/17.
  */
class ObjectCreate(obj: WorldObject) {
  def process(): Future[Array[Byte]] = {

    val writer = new PacketWriter(ServerCodes.objectCreate)


    //pak.WriteShort((ushort)obj.ObjectID);
    writer.writeShort(obj.objectId.toShort)

    /*
    if (obj is GameStaticItem) // static_item
      pak.WriteShort((ushort)(obj as GameStaticItem).Emblem);
    else
      pak.WriteShort(0);
    */
    writer.writeShort(0)

    //pak.WriteShort(obj.Heading);
    writer.writeShort(obj.heading.toShort)

    //pak.WriteShort((ushort)obj.Z);
    writer.writeShort(obj.z.toShort)

    //pak.WriteInt((uint)obj.X);
    writer.writeInt(obj.x)

    //pak.WriteInt((uint)obj.Y);
    writer.writeInt(obj.y)

    //int flag = ((byte)obj.Realm & 3) << 4;
    val flag = (obj.realm & 3) << 4

    //ushort model = obj.Model;
    /*
    if (obj.IsUnderwater)
    {
      if (obj is GameNPC)
        model |= 0x8000;
      else
        flag |= 0x01; // Underwater
    }
    */
    //pak.WriteShort(model);
    writer.writeShort(obj.model.toShort)

    /*
    if (obj is Keeps.GameKeepBanner) // game_keep_banner
      flag |= 0x08;
    if (obj is GameStaticItemTimed && m_gameClient.Player != null && ((GameStaticItemTimed)obj).IsOwner(m_gameClient.Player))
      flag |= 0x04;
    pak.WriteShort((ushort)flag);
    */
    writer.writeShort(flag.toShort)

    /*
    if (obj is GameStaticItem) // static_item
    {
      int newEmblemBitMask = ((obj as GameStaticItem).Emblem & 0x010000) << 9;
      pak.WriteInt((uint)newEmblemBitMask);//TODO other bits
    }
    else pak.WriteInt(0);
    */
    writer.writeInt(0)

    /*
    string name = obj.Name;
    LanguageDataObject translation = null;
    if (obj is GameStaticItem) // static_item
    {
      translation = LanguageMgr.GetTranslation(m_gameClient, (GameStaticItem)obj);
      if (translation != null)
      {
        if (obj is WorldInventoryItem)
        {
          //if (!Util.IsEmpty(((DBLanguageItem)translation).Name))
          //    name = ((DBLanguageItem)translation).Name;
        }
        else
        {
          if (!Util.IsEmpty(((DBLanguageGameObject)translation).Name))
            name = ((DBLanguageGameObject)translation).Name;
        }
      }
    }
    pak.WritePascalString(name.Length > 48 ? name.Substring(0, 48) : name);
    */
    var name = obj.name
    if (name.length > 48) name = name.substring(0, 48)
    writer.writePascalString(name)

    /*
    if (obj is IDoor)
    {
      pak.WriteByte(4);
      pak.WriteInt((uint)(obj as IDoor).DoorID);
    }
    else pak.WriteByte(0x00);
    */
    writer.writeByte(0x00)

    writer.toFinalFuture()
  }
}
