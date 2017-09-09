package database

import org.json4s.JsonAST.{JField, JObject, JString}
import org.mongodb.scala.Document
import org.mongodb.scala.model.IndexOptions

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 02/04/17.
  */
case class Region(name: String,
                  ip: String,
                  housingEnabled: Boolean,
                  regionId: Int,
                  isFrontier: Boolean,
                  expansion: Int,
                  waterLevel: Int,
                  divingEnabled: Boolean,
                  port: Int,
                  description: String)

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

  def getRegion(id: Int): Future[Seq[Region]] = {
    val doc = Document(
      "region_id" -> id
    )
    collection.find(doc)
      .map(d => {
        Region(
          d.getString("name"),
          d.getString("ip"),
          d.getBoolean("housing_enabled"),
          d.getInteger("region_id"),
          d.getBoolean("is_frontier"),
          d.getInteger("expansion"),
          d.getInteger("water_level"),
          d.getBoolean("diving_enabled"),
          d.getInteger("port"),
          d.getString("description")
        )
      })
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }
}
