package handlers

import akka.actor.{Actor, ActorRef}
import akka.util.ByteString
import akka.pattern.pipe
import database.Characters
import org.mongodb.scala.Document
import gameobjects.GamePlayer
import handlers.client.Handler
import world.WorldUpdate

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 25/03/17.
  */
class GameClient(session: Int) extends Actor {
  import akka.io.Tcp._

  val handler: Handler = new Handler()
  val worldUpdate = new WorldUpdate()
  val sessionId: Int = session
  var loginName: String = ""
  var requestCounter: Int = 0
  var theRef: ActorRef = _
  var player: Option[GamePlayer] = Some(new GamePlayer(new Characters().documentToCharacter(Document())))

  case class ProcessedMessage(ref: ActorRef, data: Array[Byte])

  def sendPacket(f: Future[Array[Byte]]): Unit = {
    f.map(data => ProcessedMessage(theRef, data)).pipeTo(self)
  }

  def receive = {
    case Received(data) =>
      val s = sender() // please do not remove or inline !
      theRef = s
      handler.handle(data.toArray, this)
        .map(data => ProcessedMessage(s, data))
        .pipeTo(self)
    case ProcessedMessage(ref, data) =>
      this.requestCounter += 1
      ref ! Write(ByteString.apply(data))
    case worldUpdate.NPC_UPDATE_KEYWORD => worldUpdate.updateNPCs(this)
    case worldUpdate.OBJ_UPDATE_KEYWORD => worldUpdate.updateWorldObjects(this)
    case PeerClosed => context stop self
  }
}
