package database

import org.json4s.JsonAST.{JField, JObject, JString}
import org.mongodb.scala.Document
import org.mongodb.scala.model.IndexOptions

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 02/04/17.
  */
case class Zone(coin: Int,
                isLava: Boolean,
                name: String,
                realmPoints: Int,
                regionId: Int,
                offsetX: Int,
                offsetY: Int,
                experience: Int,
                divingFlag: Int,
                width: Int,
                height: Int,
                waterLevel: Int,
                bountyPoints: Int,
                realm: Int,
                id: Int)

class Zones extends Database {
  private val collection = db.getCollection("zones")
  private val resourceFile = "data/zones.json"

  def createIndex(): Unit = {
    collection.createIndex(Document("id" -> 1), IndexOptions().unique(true))
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Zones index created"))
  }

  def importData(): Unit = {
    val jsonData = loadJsonResource(resourceFile)
    val data: List[Document] = for {
      JObject(child) <- jsonData
      JField("Coin", JString(coin)) <- child
      JField("IsLava", JString(isLava)) <- child
      JField("Name", JString(name)) <- child
      JField("Realmpoints", JString(realmPoints)) <- child
      JField("RegionID", JString(regionId)) <- child
      JField("OffsetX", JString(offsetX)) <- child
      JField("OffsetY", JString(offsetY)) <- child
      JField("Experience", JString(experience)) <- child
      JField("DivingFlag", JString(divingFlag)) <- child
      JField("Width", JString(width)) <- child
      JField("Height", JString(height)) <- child
      JField("WaterLevel", JString(waterLevel)) <- child
      JField("Bountypoints", JString(bountyPoints)) <- child
      JField("Realm", JString(realm)) <- child
      JField("ZoneID", JString(zoneId)) <- child
    } yield Document(
      "coin" -> coin.toInt,
      "is_lava" -> isLava.toBoolean,
      "name" -> name.toString,
      "realm_points" -> realmPoints.toInt,
      "region_id" -> regionId.toInt,
      "offset_x" -> offsetX.toInt,
      "offset_y" -> offsetY.toInt,
      "experience" -> experience.toInt,
      "diving_flag" -> divingFlag.toInt,
      "width" -> width.toInt,
      "height" -> height.toInt,
      "water_level" -> waterLevel.toInt,
      "bounty_points" -> bountyPoints.toInt,
      "realm" -> realm.toInt,
      "id" -> zoneId.toInt
    )

    collection.insertMany(data)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Zones data imported"))
  }

  def documentToZone(doc: Document): Zone = Zone(
    doc.getInteger("coin"),
    doc.getBoolean("is_lava"),
    doc.getString("name"),
    doc.getInteger("realm_points"),
    doc.getInteger("region_id"),
    doc.getInteger("offset_x"),
    doc.getInteger("offset_y"),
    doc.getInteger("experience"),
    doc.getInteger("diving_flag"),
    doc.getInteger("width"),
    doc.getInteger("height"),
    doc.getInteger("water_level"),
    doc.getInteger("bounty_points"),
    doc.getInteger("realm"),
    doc.getInteger("id")
  )

  def getZone(id: Int): Future[Seq[Zone]] = {
    val doc = Document(
      "id" -> id
    )
    collection.find(doc)
      .map(documentToZone)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

  def getZoneFromRegion(regionId: Int): Future[Seq[Zone]] = {
    val doc = Document(
      "region_id" -> regionId
    )
    collection.find(doc)
      .map(documentToZone)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

}
