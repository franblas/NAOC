package handlers.client

import handlers.GameClient
import handlers.packets.ClientCodes

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 26/03/17.
  */
class Handler {

  private val codePosition: Int = 9

  def handle(rawData: Array[Byte], gameClient: GameClient): Future[Array[Byte]] = {
    rawData match {
      case null => Future { Array.emptyByteArray }
      case _ if rawData.length < codePosition => Future { Array.emptyByteArray }
      case _ =>
        val data = dataFormat(rawData)
        val code = codeFormat(rawData(codePosition))
        //println("RECEIVED CODE", code)

        val request: HandlerProcessor = code match {
          case ClientCodes.cryptKey => new CryptKeyRequest()
          case ClientCodes.login => new LoginRequest(gameClient)
          case ClientCodes.ping => new PingRequest(gameClient)
          case ClientCodes.characterSelect => new CharacterSelectRequest(gameClient)
          case ClientCodes.characterOverview => new CharacterOverviewRequest(gameClient)
          case ClientCodes.clientCrash => new ClientCrash()
          case ClientCodes.duplicateNameCheck => new DuplicateNameCheckRequest(gameClient)
          case ClientCodes.characterCreate => new CharacterCreateRequest(gameClient)
          case ClientCodes.regionList => new RegionListRequest(gameClient)
          case ClientCodes.gameOpen => new GameOpenRequest(gameClient)
          case ClientCodes.worldInit => new WorldInitRequest(gameClient)
          case ClientCodes.playerInit => new PlayerInitRequest(gameClient)
          case ClientCodes.door => new DoorRequest()
          case ClientCodes.playerPositionUpdate => new PlayerPositionUpdate(gameClient)
          case ClientCodes.npcCreation => new NPCCreationRequest(gameClient)
          case ClientCodes.playerCommand => new PlayerCommandHandler()
          case ClientCodes.objectUpdate => new ObjectUpdateRequest(gameClient)
          case ClientCodes.playerAttack => new PlayerAttackRequest(gameClient)
          case 0xAC => new CharacterSelectRequest(gameClient)
          case _ => new HandlerProcessorNoOpts()
        }
        request.process(data)
    }
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


