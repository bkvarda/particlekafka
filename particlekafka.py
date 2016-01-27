import json, StringIO, time, ConfigParser
from sseclient import SSEClient
from kafka import SimpleProducer, KafkaClient

#get configuration stuff
Config = ConfigParser.ConfigParser()
Config.read('particlekafka.conf')
api_key = Config.get('Particle','ApiKey')
print_events = Config.get('Options','PrintEvents')
kafka_broker = Config.get('Options','KafkaBroker')
kafka_topic = Config.get('Options','KafkaTopic')
particle_uri = Config.get('Particle','ParticleUri')
uri = particle_uri + '?access_token=' + api_key

#Instantiate Kafka Producer
client = KafkaClient(kafka_broker)
producer = SimpleProducer(client, async=True, batch_send_every_n=1000, batch_send_every_t=10)

#Get particle public stream, send to Kafka
messages = SSEClient(uri)
for msg in messages:
    event = '"'+msg.event+'"'
    data = msg.data
    payload = {}
    if(data):
        json_out = '{"event":' + event + "," + '"data":' + data + '}'
       
        if(print_events == 'enabled'):
            print(json_out.encode('utf-8'))
       
        producer.send_messages(kafka_topic, json_out.encode('utf-8'))
 
