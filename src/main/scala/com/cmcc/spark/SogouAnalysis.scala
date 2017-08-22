package com.cmcc.spark

import org.apache.spark.{SparkConf, SparkContext}

/**
  * 自定义需求：
  *  1. 点击数最多的网站top10
  *  2.搜索结果排名排在１的网站top10
  *  3.点击顺序排名排在１的网站top10
  *  4.将结果生成图表格导出
  *
  */

object SogouAnalysis {

  // 表属性
  case class Log(visit_time:String, user_id:String, vocabulary:String, rank: Int,   sequence:Int, website:String)

  //　将列名初始化
  def format_columns(record: String):Array[String] = {
    val cols = record.split("\t")
    val visit_time = cols(0)
    val user_id = cols(1)
    val vocabulary = cols(2)
    val rank = cols(3)
    val sequence = cols(4)
    //　获取网站
    val website = cols(5).replace("http://","").split("/")(0)
    Array(visit_time, user_id, vocabulary, rank, sequence, website)
  }


  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("SogouAnalysis")
    val sc = new SparkContext(conf)
    val sqlContext = new org.apache.spark.sql.SQLContext(sc)
    import sqlContext.implicits._
    
    //　输入目录
    val inputDir = args(0)
    //三个结果的输出目录
    val  website_top10_dir = args(1)
    val  rank_1_top10_dir = args(2)
    val sequence_1_top10_dir = args(3)

    //　从HDFS上获取数据
    val inputRdd = sc.textFile(inputDir)

    // 格式化每一条记录
    val log = inputRdd.map(format_columns).map(x=>Log(x(0),x(1),x(2),x(3).toInt,x(4).toInt,x(5))).toDF()
    // 创建表
    log.registerTempTable("log")

    // 点击率top10的网站
    val website_top10 = sqlContext.sql("select  website, count(website)  as sum from log group by website order by sum desc limit 10")

    // 搜索结果排名排在１的网站ｔｏｐ１０
    val rank_1_top10 = sqlContext.sql("select  website, count(website)  as sum from log where rank=1 group by website order by sum desc limit 10")

    // 点击顺序排名排在１的网站ｔｏｐ１０
    val sequence_1_top10 = sqlContext.sql("select  website, count(website)  as sum from log where sequence=1 group by website order by sum desc limit 10")

    //　存储结果
    website_top10.rdd.saveAsTextFile(website_top10_dir)
    rank_1_top10.rdd.saveAsTextFile(rank_1_top10_dir)
    sequence_1_top10.rdd.saveAsTextFile(sequence_1_top10_dir)


  }

}

