package handlers.packets

/**
  * Created by franblas on 26/03/17.
  */
class Packets {

  val byteSize: Int = 1
  val shortSize: Int = 2
  val intSize: Int = 4
  val longSize: Int = 8

}

object PacketsUtils {
  def versionBuilder(major: Byte, minor: Byte, build: Byte): String = {
    printableString(major.toString + minor.toString + build.toString)
  }

  def parseVersion(version: String, isMsb: Boolean): Byte = {
    var cteVersion: Int = 100
    if (version.toInt > 199) cteVersion = 1000
    if (isMsb) {
      (version.toFloat / cteVersion).toByte
    } else {
      ((version.toFloat % cteVersion) / 10).toByte
    }
  }

  def printableString(s: String): String = {
    val controlCode : (Char) => Boolean = (c: Char) => c <= 32 || c == 127
    val extendedCode : (Char) => Boolean = (c: Char) => c <= 32 || c > 127
    s.filterNot(controlCode).filterNot(extendedCode)
  }

}

object ServerCodes {
  val addFriend = 0xC5
  val attackMode = 0x74
  val characterOverview = 0xFD
  val charResistsUpdate = 0xFB
  val charStatsUpdate = 0xFB
  val concentrationList = 0x75
  val debugMode = 0x21
  val dialog = 0x81
  val doorState = 0x99
  val duplicateNameCheck = 0xCC
  val encumberance = 0xBD
  val gameOpen = 0x2D
  val livingEquipmentUpdate = 0x15
  val loginDenied = 0x2C
  val loginGranted = 0x2A
  val message = 0xAF
  val nonHybridSpellLines = 0x16
  val npcCreate = 0xDA
  val objectCreate = 0xD9
  val objectGuildId = 0xDE
  val objectUpdate = 0xA1
  val pingReply = 0x29
  val playerFreeLevelUpdate = 0x4C
  val playerInitFinished = 0x2B
  val playerPositionAndObjectId = 0x20
  val realm = 0xFE
  val regionColorScheme = 0x4C
  val regions = 0xB1
  val sessionId = 0x28
  val setControlledHorse = 0x4E
  val startedHelp = 0xF7
  val statusUpdate = 0xAD
  val time = 0x7E
  val updateCraftingSkills = 0x16
  val updateMaxSpeed = 0xB6
  val updateMoney = 0xFA
  val updatePlayer = 0x16
  val updatePlayerSkills = 0x16
  val updatePoints = 0x91
  val updateWeaponAndArmorStats = 0x16
  val versionAndCryptKey = 0x22
  val weather = 0x92
  val xFireInfo = 0x5C
}

object ClientCodes {
  val cryptKey = 0xF4
  val login = 0xA7
  val ping = 0xA3
  val characterSelect = 0x10
  val characterOverview = 0xFC
  val clientCrash = 0x37
  val duplicateNameCheck = 0xCB
  val characterCreate = 0xFF
  val regionList = 0x9D
  val gameOpen = 0xBF
  val worldInit = 0xD4
  val playerInit = 0xE8
  val door = 0x99
  val playerPositionUpdate = 0xA9
  val npcCreation = 0xBE
  val playerCommand = 0xAF
  val objectUpdate = 0xA5
  val playerAttack = 0x74
}