import akka.actor.{ActorSystem, Props}
import database.DatabaseContext

import scala.concurrent.ExecutionContext.Implicits.global

/**
  * Created by franblas on 25/03/17.
  */
object Main extends App {
  DatabaseContext
  val system = ActorSystem()
  system.actorOf(Props(new Server()))
  system.whenTerminated.onComplete(res => {
    println(res)
    DatabaseContext.closeClient()
  })
}