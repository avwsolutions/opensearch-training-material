# Indices lab exercises

Welcome to the Indices lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to  get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Index basics
- Index management UI
- CAT API
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
### 1.4 - Extending shards

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

### 1.5 - Extending a replica

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
 This output shows all available CAT API endpoints. I have marked the endpoints that are helpfull throubleshooting index issues. Give some of the endpoints a try!

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

### Exercise 4 - Field mapping

Also for managing an index and documents there are multiple APIs available. From the regular CRUD operations till specialized API for Schrinking and Cloning an index or bulk indexing documents.

During this part you will use various APIs. The goal is to give the attendee a good grasp of API calls that can simplify daily operational tasks like adding an index with a required `field mapping`.

### 4.1 - Create our favorite cartoon index using the index API

Create an index that has your favorite cartoon as index name. Let's start with two shards, one replica and reuse the mapping. My favorite cartoon is Simpsons.

```
PUT simpsons
{
  "settings": {
    "index": {
      "number_of_shards": 4,
      "number_of_replicas": 0
    }
  },
  "mappings": {
    "properties": {
      "character_name": {
        "type": "keyword"
      },
      "family_name": {
        "type": "keyword"
      },
      "age": {
        "type": "integer"
      },
      "about": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 512
          }
        }
      },
      "married": {
        "type": "boolean"
      },
      "partner": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword"
          }
        }
      },
      "personality": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 512
          }
        }
      }
    }
  }
}

```

### 4.2 - Add our first cartoon character using the Document API

Add one of the characters using the Document API. I wil first add Homer Simpson. Using this type of data (instead of logs) you may want to use custom '_id' values. This way you always reinsert without creating duplicate documents.

```
PUT simpsons/_doc/1
{
  "character_name": "Homer Simpson",
  "family_name": "Simpsons",
  "age": 39,
  "about": "Homer Jay Simpson is a fictional character and the main protagonist of the American animated sitcom The Simpsons. He is voiced by Dan Castellaneta and first appeared, along with the rest of his family, in The Tracey Ullman Show short \"Good Night\" on April 19, 1987.",
  "married": true,
  "partner": "Marge Simpson",
  "personality": "Homer is clumsy, fat and very lazy. He is also an alcoholic, and is not very intelligent. He works as a Safety Inspector at the Springfield Nuclear Power Plant. Homer is one of the most popular and famous fictional characters and is thought of as one of the greatest comedic animated characters of modern times."
}
```

### 4.3 - Add our family members using the Bulk API

Let us add some other family members using the Bulk API. Bulk API now uses `create`, but `delete` and `update` are also available.

```
POST _bulk
{"create":{"_index":"simpsons","_id":2}}
{"character_name":"Marge Simpson","family_name":"Simpsons","age":36,"about":"Marjorie Jacqueline \"Marge\" Simpson is a character in the American animated sitcom The Simpsons and part of the eponymous family. Voiced by Julie Kavner, she first appeared on television in The Tracey Ullman Show short \"Good Night\" on April 19, 1987.","married":true,"partner":"Homer Simpson","personality":"Marge is generally a stereotypical sitcom mother, and she also plays the \"long-suffering wife\" who puts up with the antics of her children and her oafish husband.[3] While she usually takes her family's problems with good humor, in \"Homer Alone\" (season three, 1992), her workload and resultant stress caused her to have a mental breakdown. After spending time at \"Rancho Relaxo\", during which her family barely coped with her absence, she returned refreshed and everyone promised to help out more often."}
{"create":{"_index":"simpsons","_id":3}}
{"character_name":"Bart Simpson","family_name":"Simpsons","age":10,"about":"Bartholomew Jojo \"Bart\" Simpson is a fictional character in the American animated television series The Simpsons and part of the Simpson family. He is voiced by Nancy Cartwright and first appeared on television in The Tracey Ullman Show short \"Good Night\" on April 19, 1987.","married":false,"partner":"-","personality":"Bart is a kindhearted, loyal and energetic, but sometimes very rowdy and mischievous boy. Bart is a notorious prankster at Springfield Elementary, and his pranks are often elaborately complex, but can lead to unfortunate consequences."}
{"create":{"_index":"simpsons","_id":4}}
{"character_name":"Lisa Simpson","family_name":"Simpsons","age":8,"about":"Lisa Marie Simpson is a fictional character in the animated television series The Simpsons. She is the middle child and most accomplished of the Simpson family. Voiced by Yeardley Smith, Lisa was born as a character in The Tracey Ullman Show short \"Good Night\" on April 19, 1987.","married":false,"partner":"-","personality":"Lisa, despite being a child prodigy, often sees herself as a misfit within the Simpson family and other children due to possessing an unusually high level of intelligence. She shows characteristics rarely seen in Springfield, including spirituality and commitment to peaceful ways and is notably more concerned with world affairs than her life in Springfield, with her rebellion against social norms being depicted as constructive and heroic, yet she can be self-righteous at times.In \"Lisa the Vegetarian\", an increasing sense of moral righteousness leads her to disrupt her father's roast-pig barbecue, an act for which she later apologizes."}
{"create":{"_index":"simpsons","_id":5}}
{"character_name":"Maggie Simpson","family_name":"Simpsons","age":1,"about":"Margaret Evelyn Lenny \"Maggie\" Simpson is a fictional character in the animated television series The Simpsons and a part of the Simpson family, notably the youngest member. She first appeared on television in the Tracey Ullman Show short \"Good Night\" on April 19, 1987.","married":false,"partner":"-","personality":"Maggie is the youngest child of Homer and Marge, and the younger sister to Bart and Lisa. She is often seen sucking on her orange pacifier and, when she walks, she trips over her clothing and falls on her face (this running gag is used much more in earlier seasons). Being an infant, she has not yet learned how to talk. However, she did appear to talk in the first Tracey Ullman Show short."}
```

First count all documents using the count API and search for the first hits. Did you expect these results?

```
GET simpsons/_count
GET simpsons/_search
```

### 4.4 - Adding a rogue member using the Document API

Add a rogue character, which is part of the cartoon. For this we use a dynamic id.

```
POST simpsons/_doc
{
  "character_name": "Monty Burns",
  "family_name": "Burns",
  "age": 81,
  "about": "Charles Montgomery Plantagenet Schicklgruber \"Monty\" Burns, usually referred to as Mr. Burns, Monty, or C. Montgomery Burns, is a recurring character and the main antagonist of the animated television series The Simpsons, voiced initially by Christopher Collins and currently by Harry Shearer.",
  "married": false,
  "partner": "Smithers",
  "personality": "Mr. Burns' trademark expression is the word \"Excellent...\", muttered slowly in a low, sinister voice while steepling his fingertips. He occasionally orders Smithers to \"release the hounds\", so as to let his vicious guard dogs attack any intruders, enemies, or even invited guests. Mr. Burns is Springfield's richest and most-powerful citizen (and also the richest person in Springfield's state; his current net worth has been given as $1.3 billion by Forbes, though it fluctuates wildly depending on the episode). He uses his power and wealth to do whatever he wants, usually without regard for consequences and without interference from the authorities. These qualities led Wizard magazine to rate him the 45th-greatest villain of all time. TV Guide named him #2 in their 2013 list of the 60 nastiest villains of all time"
}
```

Insert the document above once again. And again count and search for the documents.

```
GET simpsons/_count
GET simpsons/_search
```

### 4.5 - Delete rogue members by query using Document API

Dynamic Ids are great, but do no really help outside logging use cases.

Let's remove the two rogue document using the `delete by query` API. Keep in mind that only the documents are  deleted, but storage is notgiven free.

```
POST simpsons/_delete_by_query
{
  "query": {
    "match": {
      "family_name": "Burns"
    }
  }
}
```

Again check to the number of documents is 'valid' again. In this cartoon we only want to see five documents.

```
GET simpsons/_count
GET simpsons/_search
```

### 4.6 - Shrink the index to 2 shards with the Index Shrink API

Let's try to shrink the index size.

First look what the total of shards, current storage usage and note the store results. On the fly we can't update the shard count.

```
GET simpsons/_stats
```

In our scenario.
```
"_shards": {
    "total": 4,
    "successful": 4,
    "failed": 0
},
 "store": {
        "size_in_bytes": 66824,
        "reserved_in_bytes": 0
},
```

Execute the shrink operation. Important that the index has all shards on the same node and the index set to read-only.
- First part we can achieve my adding 1 replica.
- Second  part we just have to add the index to read-only mode.

First try it without adding a replica and/or not putting the index in read-only.

Add a replica first.
```
PUT simpsons/_settings
{
  "number_of_replicas": 1
}
```

Up the index in read-only.
```
PUT /simpsons/_settings
{
  "index": {
    "blocks.read_only": true
  }
}
```

Execute the shrink process.
```
POST /simpsons/_shrink/simpsons-shrinked
{
  "settings": {
    "index": {
      "number_of_shards": 2,
      "number_of_replicas": 0
    }
  }
}
```

The following error is expected. Mainly a chicken-egg problem due read-only. Delete the target index and run the shrink process again.

```
{
  "error": {
    "root_cause": [
      {
        "type": "cluster_block_exception",
        "reason": "index [simpsons-shrinked] blocked by: [FORBIDDEN/5/index read-only (api)];"
      }
    ],
    "type": "cluster_block_exception",
    "reason": "index [simpsons-shrinked] blocked by: [FORBIDDEN/5/index read-only (api)];"
  },
  "status": 403
}
```

Let's compare the shard size and store stats again.

```
GET simpsons-shrinked/_count
GET simpsons-shrinked/_stats
GET simpsons-shrinked/_search
```

### 4.7 - Clone the index to another rogue with the Index Clone API

Last but not least we are going to ensure we have a separate index for the rogue characters. For this we will use the Clone API.

Up the source index in read-only.
```
PUT /simpsons/_settings
{
  "index": {
    "blocks.read_only": true
  }
}
```

Execute the clone process. Additional we add an alias 'cartoons'.
```
POST /simpsons-shrinked/_clone/simpsons-rogues
{
  "settings": {
    "index": {
      "number_of_shards": 2,
      "number_of_replicas": 0
    }
  },
  "aliases": {
    "cartoons": {}
  }
}
```
### 4.8 - Refresh index documents with the Bulk API

Last we delete all family members by id and introduce the rogue character again using the bulk API from the simpsons-rogues index. Ensure that the index is not in read-only.

```
POST _bulk
{"delete":{"_index":"simpsons-rogues","_id":1}}
{"delete":{"_index":"simpsons-rogues","_id":2}}
{"delete":{"_index":"simpsons-rogues","_id":3}}
{"delete":{"_index":"simpsons-rogues","_id":4}}
{"delete":{"_index":"simpsons-rogues","_id":5}}
{"create":{"_index":"simpsons-rogues","_id":6}}
{"character_name":"Monty Burns","family_name":"Burns","age":81,"about":"Charles Montgomery Plantagenet Schicklgruber \"Monty\" Burns, usually referred to as Mr. Burns, Monty, or C. Montgomery Burns, is a recurring character and the main antagonist of the animated television series The Simpsons, voiced initially by Christopher Collins and currently by Harry Shearer.","married":false,"partner":"Smithers","personality":"Mr. Burns' trademark expression is the word \"Excellent...\", muttered slowly in a low, sinister voice while steepling his fingertips. He occasionally orders Smithers to \"release the hounds\", so as to let his vicious guard dogs attack any intruders, enemies, or even invited guests. Mr. Burns is Springfield's richest and most-powerful citizen (and also the richest person in Springfield's state; his current net worth has been given as $1.3 billion by Forbes, though it fluctuates wildly depending on the episode). He uses his power and wealth to do whatever he wants, usually without regard for consequences and without interference from the authorities. These qualities led Wizard magazine to rate him the 45th-greatest villain of all time. TV Guide named him #2 in their 2013 list of the 60 nastiest villains of all time"}
```

## Exercise 5 - Aliases

### 5.1 - Validate alias usability

Let's use the alias for searching. Currently we only expect to see the rogue members.

```
GET cartoons/_search
```

Get a list with currently active aliases. 

```
GET _cat/aliases
GET _alias
```

### 5.2 - Add additional alias

Add the alias also to the shrinked index using the alias API.

```
POST _aliases
{
  "actions": [
    {
      "add": {
        "index": "simpsons-shrinked",
        "alias": "cartoons"
      }
    }
  ]
}
```

Search again to see the end results.

```
GET cartoons/_search
```

## Exercise 6 - Index templates

### 6.1 - Create index template

Above we included the {settings, mapping and aliases} in the creation of an index. We could also add this in an `index template`.

Take a look at the current templates.

```
GET _cat/templates
GET template
```

Create an index that matches both indices (my scenario 'simpsons-shrinked', simpsons-rogue') and that includes the alias.

```
PUT _template/favorite-cartoon
{
  "order": 100,
  "index_patterns": [
    "simpsons*"
  ],
  "settings": {
    "number_of_shards": "2",
    "number_of_replicas": "0"
  },
  "mappings": {
    "properties": {
      "about": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 512
          }
        }
      },
      "age": {
        "type": "integer"
      },
      "character_name": {
        "type": "keyword"
      },
      "family_name": {
        "type": "keyword"
      },
      "married": {
        "type": "boolean"
      },
      "partner": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword"
          }
        }
      },
      "personality": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 512
          }
        }
      }
    }
  },
  "aliases": {
    "cartoons": {}
  }
}
```

### 6.2 - Validate index template

Add yourself to the extended index. Ensure you are using an unique Id.

```
PUT simpsons-extended/_doc/10
{
  "character_name": "Arnold van Wijnbergen",
  "family_name": "van Wijnbergen",
  "age": 44,
  "about": "Just another IT guy that knows how to search...",
  "married": true,
  "partner": "Valerie",
  "personality": "Cloud-native geek"
}
```

Now validate if your name is included in the search results.

```
GET cartoons/_search
```

## Next Steps

You are ready to start with the next lab about [Visualize](../06-Visualize/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!