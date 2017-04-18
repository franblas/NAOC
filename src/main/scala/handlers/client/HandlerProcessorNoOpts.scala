package handlers.client

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 30/03/17.
  */
class HandlerProcessorNoOpts() extends HandlerProcessor {
  override def process(data: Array[Byte]): Future[Array[Byte]] = Future { Array.emptyByteArray }
}
