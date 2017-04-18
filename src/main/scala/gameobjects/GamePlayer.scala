package gameobjects

import database.{Regions, StartupLocations, Zones}
import org.mongodb.scala.Document

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future
import scala.util.Random

/**
  * Created by franblas on 09/04/17.
  */
class GamePlayer(charData: Document) {

  val region = new Regions()
  val startupLocation = new StartupLocations()
  val zone = new Zones()

  var enteredGame = false
  var dbCharacter: Document = _
  var race = ""
  //ability_bonus = list()
  //item_bonus = list()
  //total_constitution_lost_at_death = -1
  // CharacterClass.ManaStat
  // CharacterClass.Name
  // CharacterClass.Profession
  // level = 1
  // max_health = -1
  // concentration_effects = list()
  // max_encumberance = -1
  // encumberance = -1
  val objectId: Int = Random.nextInt(Short.MaxValue+1) //TODO
  var currentPosition: Document = _
  var currentZone: Document = _
  var currentRegion: Document = _
  // is_underwater = False
  // guild = dict()
  // has_horse, active_horse = False, dict()
  // crafting_skills = list()
  // is_turning_disabled = False
  // max_speed = -1
  var currentSpeed: Int = 0
  var money: Document = _
  var isMezzed: Boolean = false
  var isStunned: Boolean = false
  var isStrafing: Boolean = false
  // last_position_update_tick = -1
  /*last_position_update_point = {
    'X': -1,
    'Y': -1,
    'Z': -1
  }*/

  def init(): Future[Unit] = {
    this.dbCharacter = charData
    initCurrentRegion().flatMap(result => {
      this.currentRegion = result.head
      println(this.currentRegion)
      initCurrentPosition()
    }).flatMap(_ => {
      initCurrentZone()
    }).map(_ => {
      initMoney()
    })
  }

  def initCurrentRegion(): Future[Seq[Document]] = {
    val regionId = dbCharacter.getInteger("region")
    region.getRegion(regionId)
  }

  def initCurrentPosition(): Future[Unit] = {
    this.currentPosition = Document(
      "x" -> this.dbCharacter.getInteger("x").toInt,
      "y" -> this.dbCharacter.getInteger("y").toInt,
      "z" -> this.dbCharacter.getInteger("z").toInt,
      "heading" -> 0
    )

    Future {
      if (this.currentPosition.getInteger("x") == 0 || this.currentPosition.getInteger("y") == 0 || this.currentPosition.getInteger("z") == 0) {
        startupLocation.getStartupLocation(this.currentRegion.getInteger("region_id"), this.dbCharacter.getInteger("realm")).map(result => {
          if (result.nonEmpty) {
            val doc = result.head
            this.currentPosition = Document(
              "x" -> doc.getInteger("x").toInt,
              "y" -> doc.getInteger("y").toInt,
              "z" -> doc.getInteger("z").toInt,
              "heading" -> doc.getInteger("heading").toInt
            )
            println(this.currentPosition)
          }
        })
      }
    }
  }

  def inZone(x: Int, y: Int, zone: Document): Boolean = {
    val offsetX = zone.getInteger("offset_x")
    val offsetY = zone.getInteger("offset_y")
    val width = zone.getInteger("width")
    val height = zone.getInteger("height")
    val startX = 8192*offsetX
    val startY = 8192*offsetY
    val endX = startX + height * 8192
    val endY = startY + width * 8192
    if ((startX <= x && x <= endX) && (startY <= y && y <= endY)) return true
    false
  }

  def initCurrentZone(): Future[Unit] = {
    zone.getZoneFromRegion(this.currentRegion.getInteger("region_id")).map(result => {
      result.foreach(zone => {
        if (inZone(this.currentPosition.getInteger("x"), this.currentPosition.getInteger("y"), zone)) {
          this.currentZone = zone
        }
      })
    })
  }

  def initMoney() = {
    this.money = Document(
      "copper" -> this.dbCharacter.getInteger("copper").toInt,
      "silver" -> this.dbCharacter.getInteger("silver").toInt,
      "gold" -> this.dbCharacter.getInteger("gold").toInt,
      "platinium" -> this.dbCharacter.getInteger("platinium").toInt,
      "mithril" -> this.dbCharacter.getInteger("mithril").toInt
    )
  }

}
