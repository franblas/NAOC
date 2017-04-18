package handlers.client

import java.nio.ByteOrder
import java.util.Date

import database.{Accounts, Characters}
import org.mongodb.scala.Document
import handlers.GameClient
import handlers.packets.PacketReader
import handlers.server.CharacterOverview

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.{Await, Future}
import scala.concurrent.duration._
import scala.util.Try


/**
  * Created by franblas on 08/04/17.
  */
class CharacterCreateRequest(gameClient: GameClient) extends HandlerProcessor {

  val characters = new Characters()
  val account = new Accounts()

  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val reader = new PacketReader(data)
    val accountName = reader.readString(24)

    var currentRealm: Int = 0x0
    if (accountName.contains("-S")) {
      println("new chara Albion")
      currentRealm = 0x01
    } else if (accountName.contains("-N")) {
      println("new chara Midgard")
      currentRealm = 0x02
    } else if (accountName.contains("-H")) {
      println("new chara Hibernia")
      currentRealm = 0x03
    } else {
      println("new chara Unknown realm")
      return Future.failed(new Exception("Unknown realm"))
    }

    Future {
      for (_ <- 0 until 10) {
        Try(createCharacter(reader))
      }
    }.map(_ => {
      return new CharacterOverview(currentRealm, gameClient).process()
    })
  }

  def createCharacter(reader: PacketReader): Unit = {
    //if (client.Version >= GameClient.eClientVersion.Version1104)
    //	packet.ReadIntLowEndian();
    reader.readInt(ByteOrder.LITTLE_ENDIAN)
    val characterName = reader.readString(24)
    var customMode = reader.readByte()
    val eyeSize = reader.readByte()
    val lipSize = reader.readByte()
    val eyeColor = reader.readByte()
    val hairColor = reader.readByte()
    val faceType = reader.readByte()
    val hairStyle = reader.readByte()
    reader.skip(3)
    val moodType = reader.readByte()
    reader.skip(8)
    val operation = reader.readInt()
    val unk = reader.readByte()
    reader.skip(72)
    val level = reader.readByte()
    val charClass = reader.readByte()
    val realm = reader.readByte()
    val startRaceGender = reader.readByte()
    val race = (startRaceGender & 0x0F) + ((startRaceGender & 0x40) >> 2)
    val gender = (startRaceGender >> 4) & 0x01
    val shroudedIslesStartLocation = (startRaceGender >> 7) != 0
    val creationModel = reader.readShort(ByteOrder.LITTLE_ENDIAN)
    val region = reader.readByte()
    reader.skip(5)
    val strength = reader.readByte()
    val dexterity = reader.readByte()
    val constitution = reader.readByte()
    val quickness = reader.readByte()
    val intelligence = reader.readByte()
    val piety = reader.readByte()
    val empathy = reader.readByte()
    val charisma = reader.readByte()
    reader.skip(40)
    val activeRightSlot = reader.readByte() // 0x9C
    val activeLeftSlot = reader.readByte() // 0x9D
    val shroudedIslesZone = reader.readByte() // 0x9E
    // skip 4 bytes added in 1.99
    //if (client.Version >= GameClient.eClientVersion.Version199 && client.Version < GameClient.eClientVersion.Version1104)
    //	packet.Skip(4);
    val newConstitution = reader.readByte() // 0x9F

    customMode = 2 // if another number, does not work. I don't know why :s

    if (characterName == null || characterName == "") return

    val loginName = gameClient.loginName

    Await.result(characters.getCharacterByName(characterName).map(result => {
      if(result.nonEmpty) return
    }), 2000 millis)

    account.getAccount(loginName).map(accountResult => {
      val loginId = accountResult.head.get("_id")
      characters.getCharacters(loginName, realm).map(result => {
        val nextAccountSlot = result.length
        val doc = Document(
          "login_id" -> loginId,
          "name" -> characterName,
          "custom_mode" -> customMode.toInt,
          "eye_size" -> eyeSize.toInt,
          "eye_color" -> eyeColor.toInt,
          "hair_color" -> hairColor.toInt,
          "lip_size" -> lipSize.toInt,
          "face_type" -> faceType.toInt,
          "hair_style" -> hairStyle.toInt,
          "mood_type" -> moodType.toInt,
          "operation" -> operation,
          "unk" -> unk.toInt,
          "level" -> level.toInt,
          "char_class" -> charClass.toInt,
          "realm" -> realm.toInt,
          "race" -> race,
          "gender" -> gender,
          "shrouded_isles_start_location" -> shroudedIslesStartLocation,
          "creation_model" -> creationModel.toInt,
          "region" -> region.toInt,
          "strength" -> strength.toInt,
          "dexterity" -> dexterity.toInt,
          "constitution" -> constitution.toInt,
          "quickness" -> quickness.toInt,
          "intelligence" -> intelligence.toInt,
          "piety" -> piety.toInt,
          "empathy" -> empathy.toInt,
          "charisma" -> charisma.toInt,
          "active_right_slot" -> activeRightSlot.toInt,
          "active_left_slot" -> activeLeftSlot.toInt,
          "shrouded_isles_zone" -> shroudedIslesZone.toInt,
          "new_constitution" -> newConstitution.toInt,
          "max_speed" -> 191,
          "concentration" -> 100,
          "endurance" -> 100,
          "max_endurance" -> 100,
          "account_slot" -> (nextAccountSlot + realm.toInt * 100),
          "creation_date" -> new Date(),
          "guild_id" -> "",
          "realm_level" -> 1,
          "is_cloak_hood_up" -> false,
          "is_cloak_insisible" -> false,
          "is_helm_invisible" -> false,
          "spell_queue" -> false,
          "copper" -> 0,
          "silver" -> 0,
          "gold" -> 0,
          "platinium" -> 0,
          "mithril" -> 0,
          "x" -> 0,
          "y" -> 0,
          "z" -> 0,
          "bind_x" -> 0,
          "bind_y" -> 0,
          "bind_z" -> 0,
          "bind_region" -> 0,
          "bind_heading" -> 0,
          "bind_house_x" -> 0,
          "bind_house_y" -> 0,
          "bind_house_z" -> 0,
          "bind_house_region" -> 0,
          "bind_house_heading" -> 0,
          "death_count" -> 0,
          "constitution_lost_at_death" -> 0,
          "has_gravestone" -> false,
          "gravestone_region" -> 0,
          "direction" -> 0,
          "is_level_second_stage" -> false,
          "used_level_command" -> false,
          "abilities" -> "",
          "specs" -> "",
          "realm_abilities" -> "",
          "crafting_skills" -> "",
          "disabled_spells" -> "",
          "disabled_abilities" -> "",
          "friend_list" -> "",
          "ignore_list" -> "",
          "player_title_type" -> "",
          "flag_class_name" -> true,
          "guild_rank" -> 1,
          "respec_amount_all_skill" -> -1,
          "respec_amount_single_skill" -> -1,
          "respec_amount_realm_skill" -> -1,
          "respec_amount_dol" -> -1,
          "respec_amount_champion_skill" -> -1,
          "is_level_respec_used" -> false,
          "respec_bought" -> -1,
          "safety_flag" -> false,
          "crafting_primary_skill" -> 0,
          "cancel_style" -> false,
          "is_anonymous" -> false,
          "gain_xp" -> false,
          "gain_rp" -> false,
          "roleplay" -> false,
          "autoloot" -> false,
          "last_free_level" -> new Date(),
          "last_free_leveled" -> new Date(),
          "last_played" -> new Date(),
          "show_xfire_info" -> false,
          "no_help" -> false,
          "show_guild_login" -> false,
          "guild_note" -> "",
          "cl" -> true,
          "cl_level" -> 1,
          "ml_level" -> 1,
          "ml_granted" -> false,
          "ignore_statistics" -> true,
          "exp" -> 1,
          "bnty_pts" -> 0,
          "realm_pts" -> 0,
          "active_weapon_slot" -> 0,
          "played_time" -> 0,
          "death_time" -> 0,
          "customisation_step" -> 1,
          "cl_exp" -> 0,
          "ml" -> 0,
          "ml_exp" -> 0,
          "not_displayed_in_herald" -> 0,
          "active_saddle_bags" -> 0
        )
        characters.insertCharacter(doc)
      })
    })
  }
}
