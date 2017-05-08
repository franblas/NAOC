package world

/**
  * Created by franblas on 17/04/17.
  */
class Point(x: Int, y: Int) {

  def getDistance(x2: Int, y2: Int): Int = {
    val dx = x - x2
    val dy = y - y2
    math.sqrt(dx*dx + dy*dy).toInt
  }

  def inRadius(centerX: Int, centerY: Int, radius: Int): Boolean = {
    val radius2 = radius*radius
    val dx = x - centerX
    val dy = y - centerY
    val dist = dx*dx + dy*dy
    if (dist > radius2) false
    else true
  }

}
