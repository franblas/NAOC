package database

import org.json4s.JsonAST._
import org.mongodb.scala.Document
import org.mongodb.scala.model.Filters._
import org.mongodb.scala.model.IndexOptions

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future
import scala.util.Random

/**
  * Created by franblas on 15/04/17.
  */
case class Mob(strength: Int,
               constitution: Int,
               translationId: String,
               speed: Int,
               quickness: Int,
               aggroRange: Int,
               guild: String,
               level: Int,
               respawnInterval: Int,
               region: Int,
               x: Int,
               y: Int,
               z: Int,
               heading: Int,
               dexterity: Int,
               bodyType: Int,
               suffix: String,
               messageArticle: String,
               factionId: Int,
               houseNumber: Int,
               size: Int,
               realm: Int,
               itemsListTemplateId: String,
               charisma: Int,
               aggroLevel: Int,
               empathy: Int,
               name: String,
               piety: Int,
               gender: Int,
               examineArticle: String,
               equipmentTemplateId: String,
               meleeDamageType: Int,
               race: Int,
               flags: Int,
               visibleWeaponSlots: Int,
               model: Int,
               npcTemplateId: Int,
               roamingRange: Int,
               intelligence: Int,
               pathId: String,
               isCloakHoodUp: Boolean,
               maxDistance: Int,
               objectId: Int)

class Mobs extends Database {
  private val collection = db.getCollection("mobs")
  val resourceFile = "data/all_mobs.json"
  //val resourceFile2 = "data/mobs_bis_2.json"

  /*def createIndex(): Unit = {
    collection.createIndex(Document("mob_id" -> 1), IndexOptions().unique(true))
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Mobs index created"))
  }*/

  def importData(file: String): Unit = {
    val jsonData = loadJsonResource(file)
    val data: List[Document] = for {
      JObject(child) <- jsonData
      ("Strength", strength) <- child
      ("Constitution", constitution) <- child
      ("TranslationId", translationId) <- child
      ("Speed", speed) <- child
      ("Quickness", quickness) <- child
      ("AggroRange", aggroRange) <- child
      ("Guild", guild) <- child
      ("Level", level) <- child
      ("RespawnInterval", respawnInterval) <- child
      ("Region", region) <- child
      ("X", x) <- child
      ("Y", y) <- child
      ("Z", z) <- child
      ("Heading", heading) <- child
      ("Dexterity", dexterity) <- child
      ("BodyType", bodyType) <- child
      ("Suffix", suffix) <- child
      ("MessageArticle", messageArticle) <- child
      ("FactionID", factionId) <- child
      ("HouseNumber", houseNumber) <- child
      ("Size", size) <- child
      ("Realm", realm) <- child
      ("ItemsListTemplateID", itemsListTemplateId) <- child
      ("Charisma", charisma) <- child
      ("AggroLevel", aggroLevel) <- child
      ("Empathy", empathy) <- child
      ("Name", name) <- child
      ("Piety", piety) <- child
      ("Gender", gender) <- child
      ("ExamineArticle", examineArticle) <- child
      ("EquipmentTemplateID", equipmentTemplateId) <- child
      ("MeleeDamageType", meleeDamageType) <- child
      ("Race", race) <- child
      ("Flags", flags) <- child
      ("VisibleWeaponSlots", visibleWeaponSlots) <- child
      ("Model", model) <- child
      ("NPCTemplateID", npcTemplateId) <- child
      ("RoamingRange", roamingRange) <- child
      ("Intelligence", intelligence) <- child
      ("PathID", pathId) <- child
      ("IsCloakHoodUp", isCloakHoodUp) <- child
      ("MaxDistance", maxDistance) <- child
      ("Object_ID", objectId) <- child
    } yield Document(
      "strength" -> intChecker(strength),
      "constitution" -> intChecker(constitution),
      "translation_id" -> stringChecker(translationId),
      "speed" -> intChecker(speed),
      "quickness" -> intChecker(quickness),
      "aggro_range" -> intChecker(aggroRange),
      "guild" -> stringChecker(guild),
      "level" -> intChecker(level),
      "respawn_interval" -> intChecker(respawnInterval),
      "region" -> intChecker(region),
      "x" -> intChecker(x),
      "y" -> intChecker(y),
      "z" -> intChecker(z),
      "heading" -> intChecker(heading),
      "dexterity" -> intChecker(dexterity),
      "body_type" -> intChecker(bodyType),
      "suffix" -> stringChecker(suffix),
      "message_article" -> stringChecker(messageArticle),
      "faction_id" -> intChecker(factionId),
      "house_number" -> intChecker(houseNumber),
      "size" -> intChecker(size),
      "realm" -> intChecker(realm),
      "items_list_template_id" -> stringChecker(itemsListTemplateId),
      "charisma" -> intChecker(charisma),
      "aggro_level" -> intChecker(aggroLevel),
      "empathy" -> intChecker(empathy),
      "name" -> stringChecker(name),
      "piety" -> intChecker(piety),
      "gender" -> intChecker(gender),
      "examine_article" -> stringChecker(examineArticle),
      "equipment_template_id" -> stringChecker(equipmentTemplateId),
      "melee_damage_type" -> intChecker(meleeDamageType),
      "race" -> intChecker(race),
      "flags" -> intChecker(flags),
      "visible_weapon_slots" -> intChecker(visibleWeaponSlots),
      "model" -> intChecker(model),
      "npc_template_id" -> intChecker(npcTemplateId),
      "roaming_range" -> intChecker(roamingRange),
      "intelligence" -> intChecker(intelligence),
      "path_id" -> stringChecker(pathId),
      "is_cloak_hood_up" -> booleanChecker(isCloakHoodUp),
      "max_distance" -> intChecker(maxDistance),
      "object_id" -> intChecker(objectId)
    )

    collection.insertMany(data)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Mobs data imported (" + file + ")"))
  }

  def getMobsFromRegion(regionId: Int): Future[Seq[Mob]] = {
    collection.find(and(
      equal("region", regionId),
      notEqual("x", 0),
      notEqual("y", 0),
      notEqual("z", 0),
      notEqual("model", 0),
      notEqual("size", 0)
    ))
      .map(documentToMob)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

  def getSingleMobFromRegion(objectId: Int, regionId: Int): Future[Seq[Mob]] = {
    val doc = Document(
      "object_id" -> objectId,
      "region" -> regionId
    )
    collection.find(doc)
      .map(documentToMob)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

  def documentToMob(doc: Document): Mob = Mob(
    doc.getInteger("strength"),
    doc.getInteger("constitution"),
    doc.getString("translation_id"),
    doc.getInteger("speed"),
    doc.getInteger("quickness"),
    doc.getInteger("aggro_range"),
    doc.getString("guild"),
    doc.getInteger("level"),
    doc.getInteger("respawn_interval"),
    doc.getInteger("region"),
    doc.getInteger("x"),
    doc.getInteger("y"),
    doc.getInteger("z"),
    doc.getInteger("heading"),
    doc.getInteger("dexterity"),
    doc.getInteger("body_type"),
    doc.getString("suffix"),
    doc.getString("message_article"),
    doc.getInteger("faction_id"),
    doc.getInteger("house_number"),
    doc.getInteger("size"),
    doc.getInteger("realm"),
    doc.getString("items_list_template_id"),
    doc.getInteger("charisma"),
    doc.getInteger("aggro_level"),
    doc.getInteger("empathy"),
    doc.getString("name"),
    doc.getInteger("piety"),
    doc.getInteger("gender"),
    doc.getString("examine_article"),
    doc.getString("equipment_template_id"),
    doc.getInteger("melee_damage_type"),
    doc.getInteger("race"),
    doc.getInteger("flags"),
    doc.getInteger("visible_weapon_slots"),
    doc.getInteger("model"),
    doc.getInteger("npc_template_id"),
    doc.getInteger("roaming_range"),
    doc.getInteger("intelligence"),
    doc.getString("path_id"),
    doc.getBoolean("is_cloak_hood_up"),
    doc.getInteger("max_distance"),
    doc.getInteger("object_id")
  )
}

