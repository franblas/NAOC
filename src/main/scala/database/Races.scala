package database

import org.json4s.JsonAST._
import org.mongodb.scala.Document
import org.mongodb.scala.model.IndexOptions

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 02/04/17.
  */
case class Race(id: Int,
                resistCrush: Int,
                resistNatural: Int,
                resistThrust: Int,
                resistSlash: Int,
                resistSpirit: Int,
                resistMatter: Int,
                resistBody: Int,
                resistHeat: Int,
                resistEnergy: Int,
                resistCold: Int,
                raceId: String,
                name: String)

class Races extends Database {
  private val collection = db.getCollection("races")
  private val resourceFile = "data/races.json"

  def createIndex(): Unit = {
    collection.createIndex(Document("id" -> 1), IndexOptions().unique(true))
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Races index created"))
  }

  def importData(): Unit = {
    val jsonData = loadJsonResource(resourceFile)
    val data: List[Document] = for {
      JObject(child) <- jsonData
      JField("ID", JInt(id)) <- child
      JField("ResistCrush", JInt(resistCrush)) <- child
      JField("ResistNatural", JInt(resistNatural)) <- child
      JField("ResistThrust", JInt(resistThrust)) <- child
      JField("ResistSlash", JInt(resistSlash)) <- child
      JField("ResistSpirit", JInt(resistSpirit)) <- child
      JField("ResistMatter", JInt(resistMatter)) <- child
      JField("ResistBody", JInt(resistBody)) <- child
      JField("ResistHeat", JInt(resistHeat)) <- child
      JField("ResistEnergy", JInt(resistEnergy)) <- child
      JField("ResistCold", JInt(resistCold)) <- child
      JField("Race_ID", JString(raceId)) <- child
      JField("Name", JString(name)) <- child
    } yield Document(
      "id" -> id.toInt,
      "resist_crush" -> resistCrush.toInt,
      "resist_natural" -> resistNatural.toInt,
      "resist_thrust" -> resistThrust.toInt,
      "resist_slash" -> resistSlash.toInt,
      "resist_spirit" -> resistSpirit.toInt,
      "resist_matter" -> resistMatter.toInt,
      "resist_body" -> resistBody.toInt,
      "resist_heat" -> resistHeat.toInt,
      "resist_energy" -> resistEnergy.toInt,
      "resist_cold" -> resistCold.toInt,
      "race_id" -> raceId.toString,
      "name" -> name.toString
    )

    collection.insertMany(data)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Races data imported"))
  }

  def getRace(id: Int): Future[Seq[Race]] = {
    val doc = Document(
      "id" -> id
    )
    collection.find(doc)
      .map(d => {
        Race(
          d.getInteger("id"),
          d.getInteger("resist_crush"),
          d.getInteger("resist_natural"),
          d.getInteger("resist_thrust"),
          d.getInteger("resist_slash"),
          d.getInteger("resist_spirit"),
          d.getInteger("resist_matter"),
          d.getInteger("resist_body"),
          d.getInteger("resist_heat"),
          d.getInteger("resist_energy"),
          d.getInteger("resist_cold"),
          d.getString("race_id"),
          d.getString("name")
        )
      })
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

}