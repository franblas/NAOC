package database

import scala.concurrent.ExecutionContext.Implicits.global

/**
  * Created by franblas on 01/04/17.
  */
class DatabaseBootstrap {

  def accounts(): Unit = {
    val ac = new Accounts()
    ac.createIndex()
    ac.newAccount("pacobro", "bropaco")
  }

  def classes(): Unit = {
    val c = new Classes()
    c.createIndex()
    c.importData()
  }

  def races(): Unit = {
    val r = new Races()
    r.createIndex()
    r.importData()
  }

  def regions(): Unit = {
    val r = new Regions()
    r.createIndex()
    r.importData()
  }

  def zones(): Unit = {
    val z = new Zones()
    z.createIndex()
    z.importData()
  }

  def startupLocations(): Unit = {
    val sl = new StartupLocations()
    sl.createIndex()
    sl.importData()
  }

  def mobs(): Unit = {
    val m = new Mobs()
    //m.createIndex()
    m.countMobs().map(nb => {
      if (nb < 90000) {
        println("Loading mobs, can take some time ...")
        m.importData(m.resourceFile)
        //m.importData(m.resourceFile2)
      }
    })
  }

  def worldObjects(): Unit = {
    val wo = new WorldObjects()
    //wo.createIndex()
    wo.countWorldObjects().map(nb => {
      if (nb < 900) {
        wo.importData()
      }
    })
  }

  def setup(): Unit = {
    println("Bootstrap the database ...")
    accounts()
    classes()
    races()
    regions()
    zones()
    startupLocations()
    mobs()
    worldObjects()
  }

}
