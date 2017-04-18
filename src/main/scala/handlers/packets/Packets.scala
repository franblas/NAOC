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
