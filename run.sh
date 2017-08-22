
# spark　所需目录
input_dir=data/sogou
website_top10_dir=output/sogou/website_top10_dir
rank_1_top10_dir=output/sogou/rank_1_top10_dir
sequence_1_top10_dir=output/sogou/sequence_1_top10_dir

hadoop fs -rm -r $website_top10_dir $rank_1_top10_dir $sequence_1_top10_dir

# spark 任务
spark-submit \
  --master yarn \
  --class com.cmcc.spark.SogouAnalysis target/scala-2.10/sogouanalysis_2.10-1.0.0.jar $input_dir $website_top10_dir $rank_1_top10_dir $sequence_1_top10_dir


rm *.dat
# 获取分析结果
hadoop fs -getmerge $website_top10_dir website_top10.dat
hadoop fs -getmerge $rank_1_top10_dir rank_1_top10.dat
hadoop fs -getmerge $sequence_1_top10_dir sequence_1_top10.dat


# 自动生成图表并导出
py2 save_images.py website_top10.dat 1
py2 save_images.py rank_1_top10.dat 2
py2 save_images.py sequence_1_top10.dat 3
