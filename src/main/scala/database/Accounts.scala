package database

import java.util.Date

import org.mongodb.scala.model.IndexOptions
import org.mongodb.scala.Document

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 31/03/17.
  */
class Accounts extends Database {
  private val collection = db.getCollection("accounts")

  def createIndex(): Unit = {
    collection.createIndex(Document("name" -> 1), IndexOptions().unique(true))
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Accounts index created"))
  }

  def newAccount(name: String, password: String): Unit = {
    val doc: Document = Document(
      "name" -> name,
      "password" -> password,
      "creationDate" -> new Date()
    )
    collection.insertOne(doc)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println(f"New account created for $name"))
  }

  def getAccount(name: String, password: String): Future[Seq[Document]] = {
    val doc = Document(
      "name" -> name,
      "password" -> password
    )
    collection.find(doc)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

  def getAccount(name: String): Future[Seq[Document]] = {
    val doc = Document(
      "name" -> name
    )
    collection.find(doc)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

}
