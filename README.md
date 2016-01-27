###ParticleKafka

####Purpose


####Prerequisites
* CDH5.5.x
* Kafka
* Flume
* Python


####Setup
Install pip

Install python script dependencies:
```
pip install sseclient
pip install kafka-python
```
Create your kafka topic:
```
kafka-topics --create --zookeeper bkvarda-flume-3.vpc.cloudera.com:2181 --replication-factor 1 --partitions 1 --topic particle
```
Configure the particlekafka.conf file with your settings:
```

```
Start the particlekafka.py script and validate that a kafka consumer can see the messages:
```
python particlekafka.py
kafka-console-consumer --zookeeper bkvarda-flume-3.vpc.cloudera.com:2181 --topic particle
```
You should see events streaming on the python script side, and batching on the kafka consumer side

Exit that

Configure the flume.conf
```

```
Start the flume agent
```
flume-ng agent --conf conf --conf-file flume.conf --name flume1 -Dflume.root.logger=INFO,console
```
