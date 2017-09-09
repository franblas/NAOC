package handlers.client

import java.nio.ByteOrder
import java.util.Date

import database.{Accounts, Characters}
import org.mongodb.scala.Document
import handlers.GameClient
import handlers.packets.PacketReader
import handlers.server.CharacterOverview

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future


case class CharacterReader(characterName: String,
                           customMode: Byte,
                           eyeSize: Byte,
                           lipSize: Byte,
                           eyeColor: Byte,
                           hairColor: Byte,
                           faceType: Byte,
                           hairStyle: Byte,
                           moodType: Byte,
                           operation: Int,
                           unk: Byte,
                           level: Byte,
                           charClass: Byte,
                           realm: Byte,
                           startRaceGender: Byte,
                           race: Int,
                           gender: Int,
                           shroudedIslesStartLocation: Boolean,
                           creationModel: Short,
                           region: Byte,
                           strength: Byte,
                           dexterity: Byte,
                           constitution: Byte,
                           quickness: Byte,
                           intelligence: Byte,
                           piety: Byte,
                           empathy: Byte,
                           charisma: Byte,
                           activeRightSlot: Byte,
                           activeLeftSlot: Byte,
                           shroudedIslesZone: Byte,
                           newConstitution: Byte)

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
    }

    currentRealm match {
      case 0x0 => Future.failed(new Exception("Unknown realm"))
      case _ =>
        var characterReaders: Seq[CharacterReader] = Seq()
        for (_ <- 0 until 10) {
          try {
            characterReaders = characterReaders :+ readIt(reader)
          } catch {
            case e: ArrayIndexOutOfBoundsException => println("Error ---> " , e.getMessage)
            case e: Throwable => println("Error ---> ", e.getMessage)
          }
        }
        val futures = for (c <- characterReaders) yield createCharacter(c)
        Future.sequence(futures).flatMap(_ => new CharacterOverview(currentRealm, gameClient).process())
    }
  }

  def readIt(reader: PacketReader): CharacterReader = {
    //if (client.Version >= GameClient.eClientVersion.Version1104)
    //	packet.ReadIntLowEndian();
    reader.readInt(ByteOrder.LITTLE_ENDIAN)
    val characterName = reader.readString(24)
    val customMode = reader.readByte()
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
    CharacterReader(
      characterName, customMode, eyeSize, lipSize, eyeColor, hairColor, faceType, hairStyle, moodType, operation,
      unk, level, charClass, realm, startRaceGender, race, gender, shroudedIslesStartLocation, creationModel, region,
      strength, dexterity, constitution, quickness, intelligence, piety, empathy, charisma, activeRightSlot, activeLeftSlot,
      shroudedIslesZone, newConstitution
    )
  }

  def createCharacter(characterReader: CharacterReader): Future[Any] = {
    // characterReader.customMode
    val customMode = 2 // if another number, does not work. I don't know why :s

    characterReader.characterName match {
      case null => Future.successful()
      case "" => Future.successful()
      case _ =>
        val loginName = gameClient.loginName
        characters.getCharacterByName(characterReader.characterName).flatMap(charSeq => {
          if (charSeq.nonEmpty) {
            Future.successful()
          } else {
            val result: Future[Any] = for {
              chars <- characters.getCharacters(loginName, characterReader.realm)
              nextAccountSlot = chars.length
              doc = Document(
                "login_name" -> loginName,
                "name" -> characterReader.characterName,
                "custom_mode" -> customMode.toInt,
                "eye_size" -> characterReader.eyeSize.toInt,
                "eye_color" -> characterReader.eyeColor.toInt,
                "hair_color" -> characterReader.hairColor.toInt,
                "lip_size" -> characterReader.lipSize.toInt,
                "face_type" -> characterReader.faceType.toInt,
                "hair_style" -> characterReader.hairStyle.toInt,
                "mood_type" -> characterReader.moodType.toInt,
                "operation" -> characterReader.operation,
                "unk" -> characterReader.unk.toInt,
                "level" -> characterReader.level.toInt,
                "char_class" -> characterReader.charClass.toInt,
                "realm" -> characterReader.realm.toInt,
                "race" -> characterReader.race,
                "gender" -> characterReader.gender,
                "shrouded_isles_start_location" -> characterReader.shroudedIslesStartLocation,
                "creation_model" -> characterReader.creationModel.toInt,
                "region" -> characterReader.region.toInt,
                "strength" -> characterReader.strength.toInt,
                "dexterity" -> characterReader.dexterity.toInt,
                "constitution" -> characterReader.constitution.toInt,
                "quickness" -> characterReader.quickness.toInt,
                "intelligence" -> characterReader.intelligence.toInt,
                "piety" -> characterReader.piety.toInt,
                "empathy" -> characterReader.empathy.toInt,
                "charisma" -> characterReader.charisma.toInt,
                "active_right_slot" -> characterReader.activeRightSlot.toInt,
                "active_left_slot" -> characterReader.activeLeftSlot.toInt,
                "shrouded_isles_zone" -> characterReader.shroudedIslesZone.toInt,
                "new_constitution" -> characterReader.newConstitution.toInt,
                "max_speed" -> 191,
                "concentration" -> 100,
                "endurance" -> 100,
                "max_endurance" -> 100,
                "account_slot" -> (nextAccountSlot + characterReader.realm.toInt * 100),
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
              res <- characters.insertCharacter(doc)
            } yield res
            result
          }
        })
    }
  }
}
