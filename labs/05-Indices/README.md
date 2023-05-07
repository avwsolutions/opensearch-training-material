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

This second exercise we will have a look at possibilities of managing an index using the UI. This is provided by a plugin and really helpful if users don't have API knowledge.

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

Open index management, go to indices, click on the starwars index and select Reindex from Actions menu (topright).

```
 "query": {
    "match": {
      "message": {
        "query": "starfighter"
      }
    }
  }
```
