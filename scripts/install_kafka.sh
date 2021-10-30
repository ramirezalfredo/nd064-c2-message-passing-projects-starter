#!/usr/bin/bash

helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm upgrade --install udaconnect  bitnami/kafka

## after exec into the kafka client pod:
# kafka-topics.sh --create --topic locations  --bootstrap-server udaconnect-kafka:9092
# kafka-topics.sh --describe --topic locations --bootstrap-server udaconnect-kafka:9092
# kafka-console-producer.sh --broker-list udaconnect-kafka:9092 --topic locations
# kafka-console-consumer.sh --topic locations --from-beginning --bootstrap-server udaconnect-kafka:9092
# kafka-delete-records.sh --bootstrap-server udaconnect-kafka-headless:9092

## output from helm chart installation

# NAME: udaconnect
# LAST DEPLOYED: Wed Oct 20 00:50:29 2021
# NAMESPACE: default
# STATUS: deployed
# REVISION: 1
# TEST SUITE: None
# NOTES:
# ** Please be patient while the chart is being deployed **

# Kafka can be accessed by consumers via port 9092 on the following DNS name from within your cluster:

#     udaconnect-kafka.default.svc.cluster.local

# Each Kafka broker can be accessed by producers via port 9092 on the following DNS name(s) from within your cluster:

#     udaconnect-kafka-0.udaconnect-kafka-headless.default.svc.cluster.local:9092

# To create a pod that you can use as a Kafka client run the following commands:

#     kubectl run udaconnect-kafka-client --restart='Never' --image docker.io/bitnami/kafka:2.8.1-debian-10-r0 --namespace default --command -- sleep infinity
#     kubectl exec --tty -i udaconnect-kafka-client --namespace default -- bash

#     PRODUCER:
#         kafka-console-producer.sh \
            
#             --broker-list udaconnect-kafka-0.udaconnect-kafka-headless.default.svc.cluster.local:9092 \
#             --topic test

#     CONSUMER:
#         kafka-console-consumer.sh \
            
#             --bootstrap-server udaconnect-kafka.default.svc.cluster.local:9092 \
#             --topic test \
#             --from-beginning