package database

import org.mongodb.scala.Document
import org.mongodb.scala.model.IndexOptions

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 07/04/17.
  */
class Characters extends Database {
  private val collection = db.getCollection("characters")
  private val account = new Accounts()

  def createIndex(): Unit = {
    collection.createIndex(Document("name" -> 1), IndexOptions().unique(true))
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("Characters index created"))
  }

  def insertCharacter(doc: Document): Unit = {
    collection.insertOne(doc)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
      .onComplete(_ => println("New character has been inserted"))
  }

  def getCharacterByName(charName: String): Future[Seq[Document]] = {
    val doc = Document(
      "name" -> charName
    )
    collection.find(doc)
      .toFuture
      .recoverWith { case e: Throwable => Future.failed(e) }
  }

  def getCharacter(loginName: String, charName: String): Future[Seq[Document]] = {
    account.getAccount(loginName)
      .recoverWith { case e: Throwable => Future.failed(e) }
      .flatMap(result => {
        val doc = Document(
          "name" -> charName,
          "login_id" -> result.head.get("_id")
        )
        collection.find(doc)
          .toFuture
          .recoverWith { case e: Throwable => Future.failed(e) }
      })
  }

  def getCharacters(loginName: String, realm: Int): Future[Seq[Document]] = {
    account.getAccount(loginName)
      .recoverWith { case e: Throwable => Future.failed(e) }
      .flatMap(result => {
        val doc = Document(
          "realm" -> realm,
          "login_id" -> result.head.get("_id")
        )
        collection.find(doc)
          .toFuture
          .recoverWith { case e: Throwable => Future.failed(e) }
      })
  }
}
