package database

import org.mongodb.scala.{MongoClient, MongoDatabase}

/**
  * Created by franblas on 31/03/17.
  */
object DatabaseContext {

  val host: String = "localhost"
  val port: Int = 27017
  val poolSize: Int = 50

  val client: MongoClient = MongoClient(f"mongodb://$host:$port/?maxPoolSize=$poolSize")
  val databaseName: String = "naoc"

  def database: MongoDatabase = client.getDatabase(databaseName)

  def closeClient(): Unit = client.close()

}
