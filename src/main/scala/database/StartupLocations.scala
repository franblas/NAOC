package database

import org.json4s.JsonAST.{JField, JObject, JString}
import org.mongodb.scala.Document
import org.mongodb.scala.model.IndexOptions

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 02/04/17.
  */
case class StartupLocation(clientRegionId: Int,
                           region: Int,
                           raceId: Int,
                           classId: Int,
                           x: Int,
                           y: Int,
                           z: Int,
                           heading: Int,
                           realmId: Int,
                           minVersion: Int)

class StartupLocations extends Database {
  private val collection = db.getCollection("startup_locations")
  private val resourceFile = "data/startup_locations.json"

  def createIndex(): Unit = {
    collection.createIndex(Document(
      "x" -> 1,
      "y" -> 1,
      "z" -> 1
    ), IndexOptions().unique(true))
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Startup locations index created"))
  }

  def importData(): Unit = {
    val jsonData = loadJsonResource(resourceFile)
    val data: List[Document] = for {
      JObject(child) <- jsonData
      JField("ClientRegionID", JString(clientRegionId)) <- child
      JField("Region", JString(region)) <- child
      JField("RaceID", JString(raceId)) <- child
      JField("ClassID", JString(classId)) <- child
      JField("XPos", JString(x)) <- child
      JField("YPos", JString(y)) <- child
      JField("ZPos", JString(z)) <- child
      JField("Heading", JString(heading)) <- child
      JField("RealmID", JString(realmId)) <- child
      JField("MinVersion", JString(minVersion)) <- child
    } yield Document(
      "client_region_id" -> clientRegionId.toInt,
      "region" -> region.toInt,
      "race_id" -> raceId.toInt,
      "class_id" -> classId.toInt,
      "x" -> x.toInt,
      "y" -> y.toInt,
      "z" -> z.toInt,
      "heading" -> heading.toInt,
      "realm_id" -> realmId.toInt,
      "min_version" -> minVersion.toInt
    )

    collection.insertMany(data)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Startup locations data imported"))
  }

  def getStartupLocation(regionId: Int, realmId: Int): Future[Seq[StartupLocation]] = {
    val doc = Document(
      "region" -> regionId,
      "realm_id" -> realmId
    )
    collection.find(doc)
      .map(d => {
          StartupLocation(
            d.getInteger("client_region_id"),
            d.getInteger("region"),
            d.getInteger("race_id"),
            d.getInteger("class_id"),
            d.getInteger("x"),
            d.getInteger("y"),
            d.getInteger("z"),
            d.getInteger("heading"),
            d.getInteger("realm_id"),
            d.getInteger("min_version")
          )
      })
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }
}
