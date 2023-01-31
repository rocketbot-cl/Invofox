# Invofox
  
Module to connect to Invofox and automate invoices  

*Read this in other languages: [English](Manual_Invofox.md), [Español](Manual_Invofox.es.md), [Português](Manual_Invofox.pr.md).*
  
![banner](imgs/Banner_Invofox.jpg)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Configure Invofox credentials
  
Configure credentials to connect to the Invofox API.
|Parameters|Description|example|
| --- | --- | --- |
|Session|Session to use|Invofox1|
|API Key|Invofox API Key|$2b$10$3/6YJ2kYHE0rtUrks8PO7.IPDdgrNsGGTCpDLY6s8pTNzcjiQFFFe|
|Assign result to variable|Assign connection result to variable|result|

### Upload documents
  
Upload one or more documents to the Invofox platform. Use one of the two upload methods: File or Folder.
|Parameters|Description|example|
| --- | --- | --- |
|Session|Session to use|Invofox1|
|File|Path of the file to upload|C:/Users/user/Desktop/File.pdf|
|Files|Path of the folder that contains the files to upload|C:/Users/user/Desktop/Files|
|Document type|Document type to upload|invoice|
|Company ID|Company ID to which the document will be associated|54aadbb7e79e2aba5d25f3e3|
|Load batch ID|ID of the load batch to which the document will be associated|2|
|Close batch|Check this box if you want to close the load batch after uploading the files.|True|
|Additional data|Additional data that will be attached to the files. It must be an array of objects with the name of the file to which the data will be attached and the data itself.|[ { _filename: \<name of the file to which attach this data>, \<key>: \<value> }, ... { _filename: \<name of the file to which attach this data>, \<key>: \<value> } ]|
|Assign result to variable|Assign result of file upload to a variable.|result|

### Get documents
  
Get a list with the documents ID of a Invofox session.
|Parameters|Description|example|
| --- | --- | --- |
|Session|Session to use|Invofox1|
|Skip|Amount of documents to skip|0|
|Documents limit|Maximum amount of documents to get|50|
|Document type|Document type to get|invoice|
|Public state|Public state of the documents to get|processing|
|Company ID|Company ID from which the documents will be obtained|54aadbb7e79e2aba5d25f3e3|
|Assign result to variable|Assign result of execution to a variable|result|

### Get document by ID
  
Get information of a document passing its ID.
|Parameters|Description|example|
| --- | --- | --- |
|Session|Session to use|Invofox1|
|Document ID|ID of the document to get|52543ec6d13ac7000bb90823|
|Values to get|Values to get from the document|_id,account,environment,company,creator,clientData|
|Assign result to variable|Assign result of the query to a variable|result|

### Create company
  
Create a company in Invofox.
|Parameters|Description|example|
| --- | --- | --- |
|Session|Session to use|Invofox1|
|Name|Company name|Rocketbot|
|Tax ID|Company Tax ID|12345|
|Country code|Company country code|ES|
|Assign result to variable|Assign result of the query to a variable|result|

### Get companies
  
Get a list of companies and their data.
|Parameters|Description|example|
| --- | --- | --- |
|Session|Session to use|Invofox1|
|Skip|Amount of documents to skip|0|
|Companies limit|Maximum amount of companies to get|10|
|Assign result to variable|Assign result of the query to a variable|result|
