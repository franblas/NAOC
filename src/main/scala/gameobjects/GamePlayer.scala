package gameobjects

import database._

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future
import scala.util.Random

/**
  * Created by franblas on 09/04/17.
  */
case class Position(x: Int, y: Int, z: Int, heading: Int)
case class Money(copper: Int, silver: Int, gold: Int, platinium: Int, mithril: Int)

class GamePlayer(charData: Character) {

  val region = new Regions()
  val startupLocation = new StartupLocations()
  val zone = new Zones()

  var enteredGame = false
  var dbCharacter: Character = _
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
  var currentPosition: Position = _
  var currentZone: Zone = _
  var currentRegion: Region = _
  // is_underwater = False
  // guild = dict()
  // has_horse, active_horse = False, dict()
  // crafting_skills = list()
  // is_turning_disabled = False
  // max_speed = -1
  var currentSpeed: Int = 0
  var money: Money = _
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
      initCurrentPosition()
    }).flatMap(_ => {
      initCurrentZone()
    }).map(_ => {
      initMoney()
    })
  }

  def initCurrentRegion(): Future[Seq[Region]] = {
    val regionId = dbCharacter.region
    region.getRegion(regionId)
  }

  def initCurrentPosition(): Future[Unit] = {
    this.currentPosition = Position(this.dbCharacter.x, this.dbCharacter.y, this.dbCharacter.z, 0)

    Future {
      if (this.currentPosition.x == 0 || this.currentPosition.y == 0 || this.currentPosition.z == 0) {
        startupLocation.getStartupLocation(this.currentRegion.regionId, this.dbCharacter.realm).map(result => {
          if (result.nonEmpty) {
            val startupLocation = result.head
            this.currentPosition = Position(
              startupLocation.x,
              startupLocation.y,
              startupLocation.z,
              startupLocation.heading
            )
          }
        })
      }
    }
  }

  def updateCurrentPosition(x: Int, y: Int, z: Int): Unit = {
    this.currentPosition = Position(x, y, z, this.currentPosition.heading)
  }

  def inZone(x: Int, y: Int, zone: Zone): Boolean = {
    val offsetX = zone.offsetX
    val offsetY = zone.offsetY
    val width = zone.width
    val height = zone.height
    val startX = 8192*offsetX
    val startY = 8192*offsetY
    val endX = startX + height * 8192
    val endY = startY + width * 8192
    if ((startX <= x && x <= endX) && (startY <= y && y <= endY)) true
    else false
  }

  def initCurrentZone(): Future[Unit] = {
    zone.getZoneFromRegion(this.currentRegion.regionId).map(result => {
      result.foreach(zone => {
        if (inZone(this.currentPosition.x, this.currentPosition.y, zone)) {
          this.currentZone = zone
        }
      })
    })
  }

  def initMoney() = {
    this.money = Money(
      this.dbCharacter.copper,
      this.dbCharacter.silver,
      this.dbCharacter.gold,
      this.dbCharacter.platinium,
      this.dbCharacter.mithril
    )
  }

}
