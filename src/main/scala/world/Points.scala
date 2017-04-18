package world

/**
  * Created by franblas on 17/04/17.
  */
class Points {

  def getDistance(x1: Int, y1: Int, x2: Int, y2: Int): Int = {
    val dx = x1 - x2
    val dy = y1 - y2
    math.sqrt(dx*dx + dy*dy).toInt
  }

  def inRadius(centerX: Int, centerY: Int, x: Int, y: Int, radius: Int): Boolean = {
    val rSquared = radius*radius
    val dx = centerX - x
    val dy = centerY - y
    var dist = dx*dx
    if (dist > rSquared) return false
    dist += dy*dy
    if (dist > rSquared) return false
    true
  }

}
