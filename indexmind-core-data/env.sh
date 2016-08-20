
##### Spark #####

# Setup spark for amazon aws s3 (need hadoop2.4 built  version, see SPARK-15965)
wget http://ftp.riken.jp/net/apache/spark/spark-2.0.0/spark-2.0.0-bin-hadoop2.4.tgz
sudo tar zxvf spark-2.0.0-bin-hadoop2.4.tgz -C /usr/local/lib/
sudo rm -r /usr/local/lib/spark
sudo ln -s /usr/local/lib/spark-2.0.0-bin-hadoop2.4 /usr/local/lib/spark

# Spark home
export SPARK_HOME=/usr/local/lib/spark
sudo echo 'export SPARK_HOME=/usr/local/lib/spark' >> /etc/profile.d/spark.sh
sudo echo 'export PATH=$SPARK_HOME/bin:$PATH' >> /etc/profile.d/spark.sh
source /etc/profile

# pyspark
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/build:~/anaconda3/bin/python3:$PYTHONPATH
export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.1-src.zip:$PYTHONPATH #py4j
export PYSPARK_PYTHON=~/anaconda3/envs/pyspark/bin/python3
# pyspark with anaconda
export PYSPARK_PYTHON=~/anaconda3/envs/pyspark/bin/python3
export PYSPARK_DRIVER_PYTHON=ipython

# aws dependency
wget http://central.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar
wget http://central.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.7.2/hadoop-aws-2.7.2.jar
sudo mv aws-java-sdk-1.7.4.jar $SPARK_HOME/lib
sudo mv hadoop-aws-2.7.2.jar $SPARK_HOME/lib
sudo echo 'spark.executor.extraClassPath	$SPARK_HOME/lib/aws-java-sdk-1.7.4.jar:$SPARK_HOME/lib/hadoop-aws-2.7.2.jar' >> $SPARK_HOME/conf/spark-defaults.conf
sudo echo 'spark.driver.extraClassPath	    $SPARK_HOME/lib/aws-java-sdk-1.7.4.jar:$SPARK_HOME/lib/hadoop-aws-2.7.2.jar' >> $SPARK_HOME/conf/spark-defaults.conf

##### Deploy #####
#TODO: creds of IAM copy to /var/creds/aws

###### IDE SETUP #######
# 1. Create Pyspark virtual env (Video to setup spark in PyCharm: https://www.youtube.com/watch?v=u-P4keLaBzc AND add ~/anaconda3/lib/python3.5/site-packages/ (already installed tushare, etc.)
# 2. Python Integrated Tools - Default test runner = unittest