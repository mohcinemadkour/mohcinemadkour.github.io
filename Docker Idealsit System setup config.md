Title:Docke Idealsit System setup configuration 
Date: 2018-01-02 11:46
Category: Docker
Tags: Idealist
Slug: Docker- System setup config
Author: Mohcine Madkour
Illustration: data-lake-background.png



1. First, download and install Cmder terminal, then  you need to log in to the Docker container hosting the platform. Use these commands in a linux terminal: ssh username@anest-dl02.ahc.ufl.edu (Your username in the command should just be your gatorlink id. You will be prompted for a password, which should be your gatorlink password.). Let me know if you don’t have access yet.

2. Once inside the server, enter the docker container using this command:
docker exec -it 948d3255da22 /bin/bash

3. From there, enter the cassandra bin directory:
cd /apps/apache-cassandra-3.9/bin

3. Now type:./cqlsh

5. You are now inside of cassandra. From here, type the following:
use prisma1;
desc tables;

6. You may view any table using the following command:
select * from table_name;

# apache server running inside docker.

For running the apache inside docker the command is
    /opt/lampp/lampp restart

# Server

http://anest-dl02.ahc.ufl.edu:81/prisma/

# FTP Work flow

1. We need a FTP server can be accessed by IDR, they will send their data
to the directory of "/prismap" every day.

2. Then we are able to load the data from this directory to the component
in the Docker.

3. About the file transfer service you talked like GlobalScape FTP, does it
work like the usual FTP or SFTP service can be accessed by python FTP API?
I never used it before.

 One information may be useful
this FTP service will only be accessible in Shands domain.

GlobalScape FTP

3) Is authentication required?
Yes, the account and password are:
Account: eS2E*a0G
Password: 8iKU8sGD


If you can provide some of this information and a description /diagram
of how you need the FTP server to communicate with the other parts of you
application it would be very helpful.
 
The data comes from IDR, they will dump their data every day under the directory of "/prismap". Then the data loader in the Docker will load the data from the directory of "/prismap" and do the following process.

#How to install a SSL Certificate for GlobalScape Secure FTP Server?

Please follow these instructions to install your SSL certificate on GlobalScape Secure FTP Server:

1. Once you received your SSL certificate by e-mail, please copy and paste it into a text file and save the file with the .crt extension. (Include the tags -----BEGIN CERTIFICATE----- and -----END CERTIFICATE-----).

2. In the Secure FTP Administrator, select the Server tab.

3. Select the Site you want to configure in the left-hand navigation menu.

4. Check Enable explicit SSL or Enable implicit SSL or check both.

5. Select the certificate file by clicking Browse next to Certificate file path. (from step 1)

6. Select the private key file by clicking Browse next to private key file path.

7. Enter the Private Key Passphrase.

8. Apply.


# Set Up FTP 

SFTP (SSH File Transfer Protocol) is a secure file transfer protocol. It runs over the SSH protocol. It supports the full security and authentication functionality of SSH.

SFTP has pretty much replaced legacy FTP as a file transfer protocol, and is quickly replacing FTP/S. It provides all the functionality offered by these protocols, but more securely and more reliably, with easier configuration. There is basically no reason to use the legacy protocols any more.

SFTP also protects against password sniffing and man-in-the-middle attacks. It protects the integrity of the data using encryption and cryptographic hash functions, and autenticates both the server and the user.

#pysftp 0.2.9: A friendly face on SFTP

A simple interface to SFTP. The module offers high level abstractions and task based routines to handle your SFTP needs.

#How to setup a restricted SFTP server on Ubuntu?

The best resource to help you begin setting up an ssh service on a Host machine using Ubuntu is OpenSSH Server. This will allow you to use SSH File Transfer Protocol (also Secure File Transfer Protocol, or SFTP) to access, transfer, and manage files over SSH from a Client machine.