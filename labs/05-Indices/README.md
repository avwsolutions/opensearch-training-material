# Indices lab exercises

Welcome to the Indices lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to  get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Index basics
- Index management UI
- Available APIS
- Field mapping
- Aliases
- Index templates

## Exercise 1 - Index basics

This first exercise we will have a look at the file system after creating an index.  During this exercise you will learn the index basics like OpenSearch Index, OpenSearch Shard, Lucene Index and file system level stored Segments.


### 1.1 - Create a Hello World index

Login into OpenSearch Dashboards. Nagivate to **Home** and top-right click **Dev Tools**.

Create an index with 2 shards and no replicas.

```
PUT hello-world
{
  "settings": {
    "index": {
      "number_of_shards": 2,
      "number_of_replicas": 0
    }
  }
}
```

Now validate if your new index exists.

```
GET hello-world
```
### 1.2 - Lookup the created Index and Shard

First we need to get the UUID (part of the JSON output) and remember this. 
```
GET hello-world
```
Second part is the OpenSearch node to connect to. Either 'opensearch-node1' or 'opensearch-node2'
```
GET hello-world/_search_shards
```

In a Docker based environment open a Bash terminal into the OpenSearch container. 
```
docker ps | grep 9200
docker exec -it 2497d8557e66 bash
```

Let's get into the directory inside the container. 
```
cd data/nodes/0/indices/<uuid>
ls
```

Inspect all files and directories that are located
- `_state` folders are for OpenSearch internal state.
- `0 folder` is per-shard. This folder contains the `Lucene index` and a `translog` location.
- OpenSearch uses a per-shard Transaction log.
- In the `index` folder the `segment` files are stored.

### 1.3 - Lookup document ingestion

Now ingest a document into the index.
```
POST hello-world/_doc
{
  "message": "Enter the world with OpenSearch"
} 
```

Now go back to the OpenSearch node Terminal and find out that the document is still in the translog. Takes several seconds before the document enters the index.

```
#docker ps | grep 9200
#docker exec -it 2497d8557e66 bash
cat translog-2.tlog
```
### 1.3 - Extending shards

Another great experiment is increasing the total number of shards to five. To increase the total number of shards we have to delete the previous `hello-world` index.

```
DELETE hello-world

PUT hello-world
{
  "settings": {
    "index": {
      "number_of_shards": 4,
      "number_of_replicas": 0
    }
  }
}
```

Now go back to the OpenSearch node Terminal and look if the new UUID has multiple directories

- Do we expect a second folder?
- Does this also contain a Lucene Index and translog?

Try the following to find out.

```
docker ps | grep 9200
docker exec -it <uuid> bash
ls data/nodes/0/indices/<uuid>
0  2  _state
```

### 1.3 - Extending a replica

Last part is increasing with a replica. 

```
PUT hello-world/_settings
{
  "index": {
    "number_of_replicas": 1
  }
}
```

Try the following to find out.

```
docker ps | grep 9200
docker exec -it <uuid> bash
ls data/nodes/0/indices/<uuid>
0  1  2  3  _state
```

## Exercise 2 - Index management UI

This second exercise we will have a look at possibilities of managing an index using the UI. This is provided by a plugin and really helpful if users don't have API knowledge. First take some time to click around and learn about the indices that live in your cluster. Inspect the columns and try to some actions like close and open an index.

### 2.1 - Create index

Create a new index through the UI with the following settings

Settings:
- Named: 'starwars'
- 2 Shards
- 1 Replicas
- Refresh interval of 5m

After creation add an initial document.

```
POST starwars/_doc
{
  "message": "starfighter"
}
```

Now try to search for this document.
```
POST starwars/_search
```

Still no results? What's going wrong?  

Spoiler alert: Try to reconfigure one of the applied settings.

### 2.2 - Reconfigure settings on index

Open index management, go to indices and click on the starwars index. Now scroll down and update the Refresh interval to the minimum of 1s.

### 2.3 - Reindex an index

Now we are going to do a reindex using the UI. First we are going to add an additional document.

```
POST starwars/_doc
{
  "message": "darkfader"
}
```

Oeps, this shouldn't be there. Let's use the query below to reindex only the starfighter to a newly created starfighers index. Use the UI to complete this task.

Open index management, go to indices, click on the starwars index and select Reindex from Actions menu (topright), choose Reindex a subset of documents (Advanced) and use the following select query.

```
 "query": {
    "match": {
      "message": {
        "query": "starfighter"
      }
    }
  }
```

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/05-Indices/content/index-mgmt.png" alt="index-mgmt">

## Exercise 3 - Available APIS

This exercise the attendee will learn all about the APIS that are availabe. We will start with the CAT API followed by a selection of helpful APIs for aliases, indexing and document activities.

### 3.1 - CAT API for Index management

 CAT stands for 'compact and aligned text' which return human-readable text instead of JSON.  During this part we will show you the most helpful CAT APIs to use when handling with indices.

 Open your dev tools and execute the following.

 ```
GET _cat
 ```
 This output shows all available CAT API endpoints. I have marked the endpoints that are helpfull throubleshooting index issues.

| Endpoint |
|----------|
|  =^.^=                                |
| **/_cat/allocation** |
| **/_cat/segment_replication** |
| **/_cat/segment_replication/{index}** |
| **/_cat/shards** |
| **/_cat/shards/{index}** |
| /_cat/cluster_manager |
| /_cat/nodes |
| /_cat/tasks |
| **/_cat/indices** |
| **/_cat/indices/{index}** |
| **/_cat/segments** |
| **/_cat/segments/{index}** |
| **/_cat/count** |
| **/_cat/count/{index}** |
| **/_cat/recovery** |
| **/_cat/recovery/{index}** |
| /_cat/health |
| /_cat/pending_tasks |
| **/_cat/aliases** |
| **/_cat/aliases/{alias}** |
| /_cat/thread_pool |
| /_cat/thread_pool/{thread_pools} |
| /_cat/plugins |
| /_cat/fielddata |
| /_cat/fielddata/{fields} |
| /_cat/nodeattrs |
| /_cat/repositories |
| /_cat/snapshots/{repository} |
| **/_cat/templates** |
| /_cat/pit_segments |
/_cat/pit_segments/{pit_id} |

### 3.2 - Detecting index issues

For detecting index issues we recently learned that every index has a `index health state`. This health state provides a good indication when indices have problems like write issues, missing shards or else.

Which endpoint would you use to identify indices that are in a unhealthy state?
 ```
GET _cat/indices?v
```

Analyze the output below.

this output:
```
health status index                                       uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   security-auditlog-2023.04.30                6Nx8AFZ7S2ax1epcgS10ZQ   1   1        123            0    194.4kb        194.4kb
yellow open   hello-world                                 7PSiCFIoT-iqWoOrznmdzA   4   1          0            0       832b           832b
yellow open   shrinky                                     -0AiMwziQ_SLARF3sAQl2Q   1   1          0            0       208b           208b
green  open   .opendistro_security                        brQvzZqWT_qfGYz-xpZuhw   1   0         10            2     59.3kb         59.3kb
```

What could be the reason why the system index `.opendistro_security` is still in `index health state` green?

Most cases you may have lost a node or the cluster is out of storage. In these cases it's always helpful to have a replicas for recovery available.

After starting your second `OpenSearch node` again use the `recovery` operations endpoint to follow index recoveries within the cluster.

```
GET _cat/recovery?v
```

### 3.3 - Detecting unassigned shards

Below we will start with the Shards operation using the CAT API.

We will start with increasing the total number of replicas to 4. Since we have two nodes, we should have `UNASSIGNED SHARDS`.
Let's start.

```
PUT hello-world/_settings
{
  "index": {
    "number_of_replicas": 4
  }
}
```
Which endpoint would you use to identify shards that are UNASSIGNED?
What is the maximum number of replicas when you have two (data) nodes?
```
GET _cat/shards?v
```

As expected we can see the following in the output.
```
hello-world                                 1     r      UNASSIGNED                          
hello-world                                 1     r      UNASSIGNED                          
hello-world                                 1     r      UNASSIGNED                          
hello-world                                 2     p      STARTED        0    208b 172.18.0.3 opensearch-node1
hello-world                                 2     r      STARTED        0    208b 172.18.0.4 opensearch-node2
hello-world                                 2     r      UNASSIGNED                          
hello-world                                 2     r      UNASSIGNED                          
hello-world                                 2     r      UNASSIGNED     
```

Now let's fix the index and reconfigure the number of replicas to the maximum accepted value. Use the `PUT statement` above as example.



