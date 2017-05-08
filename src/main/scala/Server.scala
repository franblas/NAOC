import java.net.InetSocketAddress
import java.util.concurrent.TimeUnit

import akka.actor.{Actor, ActorRef, Props}
import akka.io.{IO, Tcp}
import database.DatabaseBootstrap
import handlers.GameClient
import world.WorldUpdate

import scala.concurrent.duration.Duration
import scala.concurrent.ExecutionContext.Implicits.global

/**
  * Created by franblas on 25/03/17.
  */
class Server extends Actor {

  import Tcp._
  import context.system

  IO(Tcp) ! Bind(self, new InetSocketAddress("0.0.0.0", 10300))

  var gameClients: Map[Int, ActorRef] = Map.empty[Int, ActorRef]
  var sessionId: Int = 1
  val worldUpdate = new WorldUpdate()

  override def preStart(): Unit = {
    super.preStart()
    // bootstrap the database
    new DatabaseBootstrap().setup()
    // setup the npc world update job
    context.system.scheduler.schedule(
      Duration.create(0, TimeUnit.MILLISECONDS), // initial delay
      Duration.create(worldUpdate.NPC_UPDATE_INTERVAL, TimeUnit.SECONDS), // frequency
      self,
      "SendNPCsUpdates"
    )
    // setup the static objs world update job
    context.system.scheduler.schedule(
      Duration.create(0, TimeUnit.MILLISECONDS), // initial delay
      Duration.create(worldUpdate.OBJ_UPDATE_INTERVAL, TimeUnit.SECONDS), // frequency
      self,
      "SendWOsUpdates"
    )
  }

  def receive = {
    case b @ Bound(localAddress) =>
      // do some logging or setup ...
      println("Local Address", localAddress)

    case CommandFailed(_: Bind) => context stop self
      
    case "SendNPCsUpdates" => broadcast(worldUpdate.NPC_UPDATE_KEYWORD)
    case "SendWOsUpdates" => broadcast(worldUpdate.OBJ_UPDATE_KEYWORD)

    case c @ Connected(remote, local) =>
      val handler = context.actorOf(Props(new GameClient(sessionId)))
      val connection = sender()
      connection ! Register(handler)
      gameClients += sessionId -> handler
      sessionId += 1
  }

  def broadcast(message: String): Unit = gameClients.values.foreach(_ ! message)

}
