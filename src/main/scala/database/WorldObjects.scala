package database

import org.json4s.JsonAST.{JField, JInt, JObject, JString}
import org.mongodb.scala.Document
import org.mongodb.scala.model.Filters.{and, equal, notEqual}
import org.mongodb.scala.model.IndexOptions

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future
import scala.util.Random

/**
  * Created by franblas on 08/05/17.
  */
case class WorldObject(realm: Int,
                       name: String,
                       respawnInterval: Int,
                       examineArticle: String,
                       x: Int,
                       y: Int,
                       z: Int,
                       heading: Int,
                       model: Int,
                       region: Int,
                       emblem: Int,
                       translationId: String,
                       `type`: String,
                       objectId: Int)

class WorldObjects extends Database {
  private val collection = db.getCollection("world_objects")
  private val resourceFile = "data/world_objects.json"

  /*def createIndex(): Unit = {
    collection.createIndex(Document("world_object_id" -> 1), IndexOptions().unique(true))
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("World objects index created"))
  }*/

  def countWorldObjects(): Future[Long] = collection.count().toFuture

  def importData(): Unit = {
    val jsonData = loadJsonResource(resourceFile)
    val data: List[Document] = for {
      JObject(child) <- jsonData
      ("Realm", realm) <- child
      JField("Name", JString(name)) <- child
      ("RespawnInterval", respawnInterval) <- child
      JField("ExamineArticle", JString(examineArticle)) <- child
      JField("X", JInt(x)) <- child
      JField("Y", JInt(y)) <- child
      JField("Z", JInt(z)) <- child
      JField("Heading", JInt(heading)) <- child
      JField("Model", JInt(model)) <- child
      JField("Region", JInt(region)) <- child
      ("Emblem", emblem) <- child
      JField("TranslationId", JString(translationId)) <- child
      JField("ClassType", JString(wotype)) <- child
      JField("Object_ID", JInt(objectId)) <- child
    } yield Document(
      "realm" -> intChecker(realm),
      "name" -> name.toString,
      "respawn_interval" -> intChecker(respawnInterval),
      "examine_article" -> examineArticle.toString,
      "x" -> x.toInt,
      "y" -> y.toInt,
      "z" -> z.toInt,
      "heading" -> heading.toInt,
      "model" -> model.toInt,
      "region" -> region.toInt,
      "emblem" -> intChecker(emblem),
      "translation_id" -> translationId.toString,
      "type" -> wotype.toString,
      "object_id" -> objectId.toInt
    )
    collection.insertMany(data)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("World objects data imported"))
  }

  def getWorldObjectsFromRegion(regionId: Int): Future[Seq[WorldObject]] = {
    collection.find(and(
      equal("region", regionId),
      notEqual("x", 0),
      notEqual("y", 0),
      notEqual("z", 0),
      notEqual("model", 0)
    ))
      .map(d => {
        WorldObject(
          d.getInteger("realm"),
          d.getString("name"),
          d.getInteger("respawn_interval"),
          d.getString("examine_article"),
          d.getInteger("x"),
          d.getInteger("y"),
          d.getInteger("z"),
          d.getInteger("heading"),
          d.getInteger("model"),
          d.getInteger("region"),
          d.getInteger("emblem"),
          d.getString("translation_id"),
          d.getString("type"),
          d.getInteger("object_id")
        )
      })
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

}
