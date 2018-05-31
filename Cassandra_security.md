Title: Cassandra Security
Date: 2018-01-02 11:46
Category: Spark Processing, Spark Streaming
Tags: Spark Processing, Spark Streaming
Slug: Cassandra Security
Author: Mohcine Madkour
Illustration: data-lake-background.png

# Securing Cassandra

Security is always at odds with usability, particularly in the context of operations and development. More so when dealing with a distributed system such as Apache Cassandra. This presentation will cover the steps required to completely secure a Cassandra cluster to meet most regulatory and compliance guidelines. Specific topics include:
- considerations and recommendations for encrypting Cassandra data at rest 
- how and why to secure client to server and server to server communications
- authentication and access control best practices
- limiting access to management and tooling
- what to expect when enabling security features in production

## SSL Ecyption 

Cassandra provides secure communication between a client and a database cluster, and between nodes in a cluster. Enabling SSL encryption ensures that data in flight is not compromised and is transferred securely. Client-to-node and node-to-node encryption are independently configured. Cassandra tools (cqlsh, nodetool, DevCenter) can be configured to use SSL encryption. The DataStax drivers can be configured to secure traffic between the driver and Cassandra.

### Encrypting Cassandra with SSL

Briefly, SSL works in the following manner. Two entities, either software or hardware, that are communicating with one another. The entities an be a client and node or peers in a cluster. These entities must exchange information to set up trust between them. Each entity that will provide such information must have a generated key that consists of a private key that only the entity stores and a public key that can be exchanged with other entities. If the client wants to connect to the server, the client requests the secure connection and the server sends a certificate that includes its public key. The client checks the validity of the certificate by exchanging information with the server, which the server validates with its private key. If a two-way validation is desired, this process must be carried out in both directions. Private keys and certificates are stored in the keystore and public keys are stored in the truststore. For systems using a Certificate Authority (CA), the truststore can store certificates signed by the CA for verification. Both keystores and truststores have passwords assigned, referred to as the keypass and storepass.

Apache Cassandra provides these SSL encryption features for . 

#### Client-to-node encrypted communication


Client-to-node encryption protects data in flight from client machines to a database cluster using SSL (Secure Sockets Layer). It establishes a secure channel between the client and the coordinator node.

https://docs.datastax.com/en/cassandra/3.0/cassandra/configuration/secureSSLIntro.html



