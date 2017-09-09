package database

import java.util.Date

import org.mongodb.scala.{Completed, Document}
import org.mongodb.scala.model.IndexOptions

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 07/04/17.
  */
case class Character(loginName: String,
                     name: String,
                     customMode: Int,
                     eyeSize: Int,
                     eyeColor: Int,
                     hairColor: Int,
                     lipSize: Int,
                     faceType: Int,
                     hairStyle: Int,
                     moodType: Int,
                     operation: Int,
                     unk: Int,
                     level: Int,
                     charClass: Int,
                     realm: Int,
                     race: Int,
                     gender: Int,
                     shroudedIslesStartLocation: Boolean,
                     creationModel: Int,
                     region: Int,
                     strength: Int,
                     dexterity: Int,
                     constitution: Int,
                     quickness: Int,
                     intelligence: Int,
                     piety: Int,
                     empathy: Int,
                     charisma: Int,
                     activeRightSlot: Int,
                     activeLeftSlot: Int,
                     shroudedIslesZone: Int,
                     newConstitution: Int,
                     maxSpeed: Int,
                     concentration: Int,
                     endurance: Int,
                     maxEndurance: Int,
                     accountSlot: Int,
                     creationDate: Date,
                     guildId: String,
                     realmLevel: Int,
                     isCloakHoodUp: Boolean,
                     isCloakInvisible: Boolean,
                     isHelmInvisible: Boolean,
                     spellQueue: Boolean,
                     copper: Int,
                     silver: Int,
                     gold: Int,
                     platinium: Int,
                     mithril: Int,
                     x: Int,
                     y: Int,
                     z: Int,
                     bindX: Int,
                     bindY: Int,
                     bindZ: Int,
                     bindRegion: Int,
                     bindHeading: Int,
                     bindHouseX: Int,
                     bindHouseY: Int,
                     bindHouseZ: Int,
                     bindHouseRegion: Int,
                     bindHouseHeading: Int,
                     deathCount: Int,
                     constitutionLostAtDeath: Int,
                     hasGravestone: Boolean,
                     gravestoneRegion: Int,
                     direction: Int,
                     isLevelSecondStage: Boolean,
                     usedLevelCommand: Boolean,
                     abilities: String,
                     specs: String,
                     realmAbilities: String,
                     craftingSkills: String,
                     disabledSpells: String,
                     disabledAbilities: String,
                     friendList: String,
                     ignoreList: String,
                     playerTitleType: String,
                     flagClassName: Boolean,
                     guildRank: Int,
                     respecAmountAllSkill: Int,
                     respecAmountSingleSkill: Int,
                     respecAmountRealmSkill: Int,
                     respecAmountDol: Int,
                     respecAmountChampionSkill: Int,
                     isLevelRespecUsed: Boolean,
                     respecBought: Int,
                     safetyFlag: Boolean,
                     craftingPrimarySkill: Int,
                     cancelStyle: Boolean,
                     isAnonymous: Boolean,
                     gainXp: Boolean,
                     gainRp: Boolean,
                     roleplay: Boolean,
                     autoloot: Boolean,
                     lastFreeLevel: Date,
                     lastFreeLeveled: Date,
                     lastPlayed: Date,
                     showXfireInfo: Boolean,
                     noHelp: Boolean,
                     showGuildLogin: Boolean,
                     guildNote: String,
                     cl: Boolean,
                     clLevel: Int,
                     mlLevel: Int,
                     mlGranted: Boolean,
                     ignoreStatistics: Boolean,
                     exp: Int,
                     bntyPts: Int,
                     realmPts: Int,
                     activeWeaponSlot: Int,
                     playedTime: Int,
                     deathTime: Int,
                     customisationStep: Int,
                     clExp: Int,
                     ml: Int,
                     mlExp: Int,
                     notDisplayedInHerald: Int,
                     activeSaddleBags: Int)

class Characters extends Database {
  private val collection = db.getCollection("characters")

  def createIndex(): Unit = {
    collection.createIndex(Document("name" -> 1), IndexOptions().unique(true))
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Characters index created"))
  }

  def insertCharacter(doc: Document): Future[Any] = {
    collection.insertOne(doc).toFuture
  }

  def getCharacterByName(charName: String): Future[Seq[Character]] = {
    val doc = Document(
      "name" -> charName
    )
    collection.find(doc)
      .map(documentToCharacter)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

  def getCharacter(loginName: String, charName: String): Future[Seq[Character]] = {
    val doc = Document(
      "name" -> charName,
      "login_name" -> loginName
    )
    collection.find(doc)
      .map(documentToCharacter)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

  def getCharacters(loginName: String, realm: Int): Future[Seq[Character]] = {
    val doc = Document(
      "realm" -> realm,
      "login_name" -> loginName
    )
    collection.find(doc)
      .map(documentToCharacter)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

  def documentToCharacter(doc: Document): Character = Character(
    doc.getString("login_name"),
    doc.getString("name"),
    doc.getInteger("custom_mode"),
    doc.getInteger("eye_size"),
    doc.getInteger("eye_color"),
    doc.getInteger("hair_color"),
    doc.getInteger("lip_size"),
    doc.getInteger("face_type"),
    doc.getInteger("hair_style"),
    doc.getInteger("mood_type"),
    doc.getInteger("operation"),
    doc.getInteger("unk"),
    doc.getInteger("level"),
    doc.getInteger("char_class"),
    doc.getInteger("realm"),
    doc.getInteger("race"),
    doc.getInteger("gender"),
    doc.getBoolean("shrouded_isles_start_location"),
    doc.getInteger("creation_model"),
    doc.getInteger("region"),
    doc.getInteger("strength"),
    doc.getInteger("dexterity"),
    doc.getInteger("constitution"),
    doc.getInteger("quickness"),
    doc.getInteger("intelligence"),
    doc.getInteger("piety"),
    doc.getInteger("empathy"),
    doc.getInteger("charisma"),
    doc.getInteger("active_right_slot"),
    doc.getInteger("active_left_slot"),
    doc.getInteger("shrouded_isles_zone"),
    doc.getInteger("new_constitution"),
    doc.getInteger("max_speed"),
    doc.getInteger("concentration"),
    doc.getInteger("endurance"),
    doc.getInteger("max_endurance"),
    doc.getInteger("account_slot"),
    doc.getDate("creation_date"),
    doc.getString("guild_id"),
    doc.getInteger("realm_level"),
    doc.getBoolean("is_cloak_hood_up"),
    doc.getBoolean("is_cloak_insisible"),
    doc.getBoolean("is_helm_invisible"),
    doc.getBoolean("spell_queue"),
    doc.getInteger("copper"),
    doc.getInteger("silver"),
    doc.getInteger("gold"),
    doc.getInteger("platinium"),
    doc.getInteger("mithril"),
    doc.getInteger("x"),
    doc.getInteger("y"),
    doc.getInteger("z"),
    doc.getInteger("bind_x"),
    doc.getInteger("bind_y"),
    doc.getInteger("bind_z"),
    doc.getInteger("bind_region"),
    doc.getInteger("bind_heading"),
    doc.getInteger("bind_house_x"),
    doc.getInteger("bind_house_y"),
    doc.getInteger("bind_house_z"),
    doc.getInteger("bind_house_region"),
    doc.getInteger("bind_house_heading"),
    doc.getInteger("death_count"),
    doc.getInteger("constitution_lost_at_death"),
    doc.getBoolean("has_gravestone"),
    doc.getInteger("gravestone_region"),
    doc.getInteger("direction"),
    doc.getBoolean("is_level_second_stage"),
    doc.getBoolean("used_level_command"),
    doc.getString("abilities"),
    doc.getString("specs"),
    doc.getString("realm_abilities"),
    doc.getString("crafting_skills"),
    doc.getString("disabled_spells"),
    doc.getString("disabled_abilities"),
    doc.getString("friend_list"),
    doc.getString("ignore_list"),
    doc.getString("player_title_type"),
    doc.getBoolean("flag_class_name"),
    doc.getInteger("guild_rank"),
    doc.getInteger("respec_amount_all_skill"),
    doc.getInteger("respec_amount_single_skill"),
    doc.getInteger("respec_amount_realm_skill"),
    doc.getInteger("respec_amount_dol"),
    doc.getInteger("respec_amount_champion_skill"),
    doc.getBoolean("is_level_respec_used"),
    doc.getInteger("respec_bought"),
    doc.getBoolean("safety_flag"),
    doc.getInteger("crafting_primary_skill"),
    doc.getBoolean("cancel_style"),
    doc.getBoolean("is_anonymous"),
    doc.getBoolean("gain_xp"),
    doc.getBoolean("gain_rp"),
    doc.getBoolean("roleplay"),
    doc.getBoolean("autoloot"),
    doc.getDate("last_free_level"),
    doc.getDate("last_free_leveled"),
    doc.getDate("last_played"),
    doc.getBoolean("show_xfire_info"),
    doc.getBoolean("no_help"),
    doc.getBoolean("show_guild_login"),
    doc.getString("guild_note"),
    doc.getBoolean("cl"),
    doc.getInteger("cl_level"),
    doc.getInteger("ml_level"),
    doc.getBoolean("ml_granted"),
    doc.getBoolean("ignore_statistics"),
    doc.getInteger("exp"),
    doc.getInteger("bnty_pts"),
    doc.getInteger("realm_pts"),
    doc.getInteger("active_weapon_slot"),
    doc.getInteger("played_time"),
    doc.getInteger("death_time"),
    doc.getInteger("customisation_step"),
    doc.getInteger("cl_exp"),
    doc.getInteger("ml"),
    doc.getInteger("ml_exp"),
    doc.getInteger("not_displayed_in_herald"),
    doc.getInteger("active_saddle_bags")
  )
}
