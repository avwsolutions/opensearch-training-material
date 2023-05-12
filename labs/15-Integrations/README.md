# Integrations lab exercises

Welcome to the Integrations lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- FluentD

## Exercise 1 - FluentD

This exercise explains how to use a FluentD container to import a CSV file. Of course FluentD can be used for many cases, but this is just a code example.

The code example is based on the [Bundesliga data set](../../codesamples/fluentd/dataset/Bundesliga_Results.csv).

During this exercise you may have the following prereqs ready:

- Bash access, preferable Linux.
- Installed Docker locally, which can be the OpenSearch training server.
- Access to the OpenSearch port '9200'
- Internet access to Docker Hub.

As starting point copy the the **fluentd** folder under **codesamples** or execute from this folder.

```
cd codesamples/fluentd
pwd
```
### Adding the OpenSearch plugin to FluentD Docker image

It's a pity this isn't there by default, but let's creats this new container. If you are not used to use containers, no problem at all!

```
# ./buildContainer.sh
docker build -t fluentd-opensearch-training:1.0 .
```

### Let's ensure that you have the correct index template ready

To ensure settings and mapping we have to import an index template using cURL. Don't forget to provide the password for `admin` user. Additional you may want to change `localhost` to the server ip address. Ensure that you get a *acknowledged:true* as response.

```
# ./insertTemplate.sh
curl -XPUT -H 'Content-Type: application/json' https://localhost:9200/_template/bundesliga -d@index_template.json -u admin -k
```
### Update fluent.conf to reflect correct password

As you have learned fluentD uses a input, filer, output pipeline mechanism. Don't forget to update the *password* in the match block.

Some details:
- Input is defined as source block which imports a file (always from head) and parsed in `CSV format`.
- Additonal we add a tag `bundesliga`
- Output is defined as match block which is using the `opensearch output plugin`.

```
<source>
  @type tail
  read_from_head true
  path /tmp/Bundesliga_Results.csv #...or where you placed your Apache access log
  pos_file /var/log/Bundesliga_Results.csv.pos # This is where you record file position
  tag bundesliga
  <parse>
    @type csv
    keys dataset,date,hometeam,awayteam,fthg,ftag,ftr,hthg,htag,htr,season
    types dataset:string,date:string,hometeam:string,awayteam:string,fthg:integer,ftag:integer,ftr:string,hthg:integer,htag:integer,htr:string,season:string
  </parse>
</source>

<match bundesliga>
  # @log_level trace
  @type opensearch
  logstash_format false
  host localhost  #(optional; default="localhost")
  scheme https
  ssl_verify false
  port 9200 #(optional; default=9200)
  user admin
  password admin
  index_name bundesliga  #(optional; default=fluentd)
  type_name _doc #(optional; default=fluentd)
</match>
```

You may want to enable **@log_level trace** if something fails.

### Start FluentD to import bundesliga data set

This is easy by executing the provided script.

```
./load_dataset.sh
docker run --name fluentd  --network host --rm -v /${PWD}/dataset/Bundesliga_Results.csv:/tmp/Bundesliga_Results.csv -v /${PWD}/fluent.conf:/fluentd/etc/fluent.conf fluentd-opensearch-training:1.0
```

Expected output
```
2023-05-12 08:35:00 +0000 [info]: init supervisor logger path=nil rotate_age=nil rotate_size=nil
2023-05-12 08:35:00 +0000 [info]: parsing config file is succeeded path="/fluentd/etc/fluent.conf"
2023-05-12 08:35:00 +0000 [info]: gem 'fluentd' version '1.15.3'
2023-05-12 08:35:00 +0000 [info]: gem 'fluent-plugin-calyptia-monitoring' version '0.1.3'
2023-05-12 08:35:00 +0000 [info]: gem 'fluent-plugin-cmetrics' version '0.1.0'
2023-05-12 08:35:00 +0000 [info]: gem 'fluent-plugin-metrics-cmetrics' version '0.1.2'
2023-05-12 08:35:00 +0000 [info]: gem 'fluent-plugin-opensearch' version '1.1.0'
2023-05-12 08:35:01 +0000 [info]: using configuration file: <ROOT>
  <source>
    @type tail
    read_from_head true
    path "/tmp/Bundesliga_Results.csv"
    pos_file "/var/log/Bundesliga_Results.csv.pos"
    tag "bundesliga"
    <parse>
      @type "csv"
      keys dataset,date,hometeam,awayteam,fthg,ftag,ftr,hthg,htag,htr,season
      types dataset:string,date:string,hometeam:string,awayteam:string,fthg:integer,ftag:integer,ftr:string,hthg:integer,htag:integer,htr:string,season:string
      unmatched_lines 
    </parse>
  </source>
  <match bundesliga>
    @type opensearch
    logstash_format false
    host "localhost"
    scheme https
    ssl_verify false
    port 9200
    user "admin"
    password xxxxxx
    index_name "bundesliga"
    type_name _doc
  </match>
</ROOT>
2023-05-12 08:35:01 +0000 [info]: starting fluentd-1.15.3 pid=7 ruby="3.0.5"
2023-05-12 08:35:01 +0000 [info]: spawn command to main:  cmdline=["/usr/local/bin/ruby", "-Eascii-8bit:ascii-8bit", "/usr/local/bundle/bin/fluentd", "--config", "/fluentd/etc/fluent.conf", "--plugin", "/fluentd/plugins", "--under-supervisor"]
2023-05-12 08:35:01 +0000 [info]: init supervisor logger path=nil rotate_age=nil rotate_size=nil
2023-05-12 08:35:02 +0000 [info]: #0 init worker0 logger path=nil rotate_age=nil rotate_size=nil
2023-05-12 08:35:02 +0000 [info]: adding match pattern="bundesliga" type="opensearch"
2023-05-12 08:35:02 +0000 [info]: adding source type="tail"
2023-05-12 08:35:02 +0000 [warn]: parameter 'type_name' in <match bundesliga>
  @type opensearch
  logstash_format false
  host "localhost"
  scheme https
  ssl_verify false
  port 9200
  user "admin"
  password xxxxxx
  index_name "bundesliga"
  type_name _doc
</match> is not used.
2023-05-12 08:35:02 +0000 [info]: #0 starting fluentd worker pid=16 ppid=7 worker=0
2023-05-12 08:35:02 +0000 [info]: #0 following tail of /tmp/Bundesliga_Results.csv
2023-05-12 08:35:03 +0000 [info]: #0 fluentd worker is now running worker=0
^C2023-05-12 08:37:34 +0000 [info]: Received graceful stop
2023-05-12 08:37:35 +0000 [info]: #0 fluentd worker is now stopping worker=0
2023-05-12 08:37:35 +0000 [info]: #0 shutting down fluentd worker worker=0
2023-05-12 08:37:35 +0000 [info]: #0 shutting down input plugin type=:tail plugin_id="object:bb8"
2023-05-12 08:37:35 +0000 [info]: #0 shutting down output plugin type=:opensearch plugin_id="object:b90"
2023-05-12 08:37:35 +0000 [info]: Worker 0 finished with status 0
```

### Validate succesful import OpenSearch

To validate the import you may want to use **Dev Tools**. Open the Query Console.

Lookup the template
```
GET _template/bundesliga
```

Lookup the index and documents?
```
GET bundesliga/_search
```

Do you have all expected records?
```
GET bundesliga/_count
```

Now try to answer some questions regarding FluentD.
- What kind of data can FluentD collect for you?
- How are the document fields mapped?
- Create a dashboard of the data set that contains a minimum of Controls, Descriptions, Search panel and approx four Visualizations.

## Next Steps

You are ready to start with the next lab about [Development](../16-Development/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!