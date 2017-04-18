package database

import org.json4s.JsonAST.{JField, JObject, JString}
import org.mongodb.scala.Document
import org.mongodb.scala.model.IndexOptions

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 02/04/17.
  */
class Regions extends Database {
  private val collection = db.getCollection("regions")
  private val resourceFile = "data/regions.json"

  def createIndex(): Unit = {
    collection.createIndex(Document("name" -> 1), IndexOptions().unique(true))
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Regions index created"))
  }

  def importData(): Unit = {
    val jsonData = loadJsonResource(resourceFile)
    val data: List[Document] = for {
      JObject(child) <- jsonData
      JField("Name", JString(name)) <- child
      JField("IP", JString(ip)) <- child
      JField("HousingEnabled", JString(housingEnabled)) <- child
      JField("RegionID", JString(regionId)) <- child
      JField("IsFrontier", JString(isFrontier)) <- child
      JField("Expansion", JString(expansion)) <- child
      JField("WaterLevel", JString(waterLevel)) <- child
      JField("DivingEnabled", JString(divingEnabled)) <- child
      JField("Port", JString(port)) <- child
      JField("Description", JString(description)) <- child
    } yield Document(
      "name" -> name.toString,
      "ip" -> ip.toString,
      "housing_enabled" -> housingEnabled.toBoolean,
      "region_id" -> regionId.toInt,
      "is_frontier" -> isFrontier.toBoolean,
      "expansion" -> expansion.toInt,
      "water_level" -> waterLevel.toInt,
      "diving_enabled" -> divingEnabled.toBoolean,
      "port" -> port.toInt,
      "description" -> description.toString
    )

    collection.insertMany(data)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Regions data imported"))
  }

  def getRegion(id: Int): Future[Seq[Document]] = {
    val doc = Document(
      "region_id" -> id
    )
    collection.find(doc)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }
}
