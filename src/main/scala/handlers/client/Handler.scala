package handlers.client

import handlers.GameClient
import handlers.server.DoorRequest

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 26/03/17.
  */
class Handler {

  private val codePosition: Int = 9

  def handle(rawData: Array[Byte], gameClient: GameClient): Future[Array[Byte]] = {
    if (rawData == null || rawData.length < codePosition) Future { Array.emptyByteArray }

    val data = dataFormat(rawData)
    val code = codeFormat(rawData(codePosition))
    //println("RECEIVED CODE", code)

    val request: HandlerProcessor = code match {
      case 0xF4 => new CryptKeyRequest()
      case 0xA7 => new LoginRequest(gameClient)
      case 0xA3 => new PingRequest(gameClient)
      case 0x10 => new CharacterSelectRequest(gameClient)
      case 0xAC => new HandlerProcessorNoOpts()
      case 0xFC => new CharacterOverviewRequest(gameClient)
      case 0x37 => new ClientCrash()
      case 0xCB => new DuplicateNameCheckRequest(gameClient)
      case 0xFF => new CharacterCreateRequest(gameClient)
      case 0x9D => new RegionListRequest(gameClient)
      case 0xBF => new GameOpenRequest(gameClient)
      case 0xD4 => new WorldInitRequest(gameClient)
      case 0xE8 => new PlayerInitRequest(gameClient)
      case 0x99 => new DoorRequest()
      case 0xA9 => new PlayerPositionUpdate(gameClient)
      case 0xBE => new NPCCreationRequest(gameClient)
      case 0xAF => new PlayerCommandHandler()
      case 0xA5 => new ObjectUpdateRequest(gameClient)
      case 0x74 => new PlayerAttackRequest(gameClient)
      case _ => new HandlerProcessorNoOpts()
    }
    request.process(data)
  }

  def codeFormat(rawCode: Byte): Int = {
    val strCode = "%02x".format(rawCode)
    Integer.parseInt(strCode.slice(strCode.length-2, strCode.length), 16)
  }

  def dataFormat(rawData: Array[Byte]): Array[Byte] = {
    rawData.slice(codePosition+1, rawData.length)
  }
}

trait HandlerProcessor {
  def process(data: Array[Byte]): Future[Array[Byte]]
}


