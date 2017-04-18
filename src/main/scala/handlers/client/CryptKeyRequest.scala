package handlers.client

import handlers.packets.{PacketReader, PacketsUtils}
import handlers.server.VersionAndCryptKey

import scala.concurrent.Future

/**
  * Created by franblas on 26/03/17.
  */
class CryptKeyRequest() extends HandlerProcessor {

  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val reader = new PacketReader(data)
    val rc4 = reader.readByte // should bo 0 (if 1 then encrypted requests)
    val clientTypeTmp = reader.readByte
    /*
     client_type
      unknown = -1
     	classic = 1
     	shrouded_isles = 2
     	trials_of_atlantis = 3
     	catacombs = 4
     	darkness_rising = 5
     	labyrinth_of_the_minotaur = 6
    */
    // client_type = hex(int(client_type_tmp) & 0x0F)
    // client_addons = hex(int(client_type_tmp) & 0xF0)
    val major = reader.readByte
    val minor = reader.readByte
    val build = reader.readByte
    val version = PacketsUtils.versionBuilder(major, minor, build)
    new VersionAndCryptKey(version).process()
  }
}

