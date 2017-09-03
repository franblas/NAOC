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

  def intChecker(a: JValue): Int = {
    a match {
      case null => 0
      case _ if a.values == null => 0
      case _ => a.values.toString.toInt
    }
  }

  def stringChecker(a: JValue): String = {
    a match {
      case null => ""
      case _ if a.values == null => ""
      case _ => a.values.toString
    }
  }

  def booleanChecker(a: JValue): Boolean = {
    a match {
      case null => false
      case _ if a.values == null => false
      case _ => a.values.toString.toBoolean
    }
  }

}
