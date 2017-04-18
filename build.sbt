name := "NAOC"

version := "1.0"

scalaVersion := "2.12.1"

libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-actor" % "2.4.17",
  "org.mongodb.scala" %% "mongo-scala-driver" % "2.0.0",
  "org.json4s" %% "json4s-native" % "3.5.1"
)