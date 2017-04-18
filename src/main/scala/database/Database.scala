package database

import org.json4s.JsonAST.JValue
import org.json4s.native.JsonMethods.parse
import org.mongodb.scala.MongoDatabase

/**
  * Created by franblas on 02/04/17.
  */
class Database {

  protected val db: MongoDatabase = DatabaseContext.database

  def loadJsonResource(filepath: String): JValue = {
    val json = io.Source.fromResource(filepath).getLines mkString "\n"
    parse(json)
  }

}
