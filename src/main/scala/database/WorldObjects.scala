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
class WorldObjects extends Database {
  private val collection = db.getCollection("world_objects")
  private val resourceFile = "data/world_objects.json"

  def createIndex(): Unit = {
    collection.createIndex(Document("world_object_id" -> 1), IndexOptions().unique(true))
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("World objects index created"))
  }

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
      JField("Type", JString(wotype)) <- child
      JField("WorldObject_ID", JString(woId)) <- child
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
      "world_object_id" -> woId.toString,
      "object_id" -> (Random.nextInt((Short.MaxValue+1)*2)-(Short.MaxValue+1))
    )
    collection.insertMany(data)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("World objects data imported"))
  }

  def getWorldObjectsFromRegion(regionId: Int): Future[Seq[Document]] = {
    collection.find(and(
      equal("region", regionId),
      notEqual("x", 0),
      notEqual("y", 0),
      notEqual("z", 0),
      notEqual("model", 0)
    ))
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

}
