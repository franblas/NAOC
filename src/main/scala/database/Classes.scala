package database

import org.json4s.JsonAST.{JField, JInt, JObject, JString}
import org.mongodb.scala.Document
import org.mongodb.scala.model.IndexOptions

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 01/04/17.
  */
case class GameClass(characterClass: Int,
                     characterClassName: String,
                     base: String,
                     profession: String)

class Classes extends Database {
  private val collection = db.getCollection("classes")
  private val resourceFile = "data/classes.json"

  def createIndex(): Unit = {
    collection.createIndex(Document("char_class" -> 1), IndexOptions().unique(true))
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Classes index created"))
  }

  def importData(): Unit = {
    val jsonData = loadJsonResource(resourceFile)
    val data: List[Document] = for {
      JObject(child) <- jsonData
      JField("CharClass", JInt(charClass)) <- child
      JField("CharClassName", JString(charClassName)) <- child
      JField("Base", JString(base)) <- child
      JField("Profession", JString(profession)) <- child
    } yield Document(
      "char_class" -> charClass.toInt,
      "char_class_name" -> charClassName.toString,
      "base" -> base.toString,
      "profession" -> profession.toString
    )

    collection.insertMany(data)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Classes data imported"))
  }


  def getCharClass(charClass: Int): Future[Seq[GameClass]] = {
    val doc = Document(
      "char_class" -> charClass
    )
    collection.find(doc)
      .map(d => {
        GameClass(
          d.getInteger("char_class"),
          d.getString("char_class_name"),
          d.getString("base"),
          d.getString("profession")
        )
      })
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }
}
