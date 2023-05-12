# Developer tools lab exercises

Welcome to the Developer tools lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Query console
- SQL/PPL Plugin
- OpenSearch clients

## Exercise 1 - Query Console

This exercise explains you what the Query Console is and why is it helpful when administering and managing OpenSearch. In the previous labs you already worked with Dev Tools. Also you already got introduced in the CAT API, but now we will dive further into some Administration details.

### 1.1 - Personalizing Query Console settings

You are going to look in to the available possibilities in the query console. Let's  start with opening the Query Console, which in fact is part of **Dev Tools**.

When the console is openened we have three options available.
- **History** with the possibility to re-play commands.
- **Settings** with all settings to futher personalize the settings like auto-complete behaviour.
- **Help** show all info about building requests and available keyword shortcuts. 

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/09-DeveloperTools/content/console-dev.png" alt="console-dev">

Now try the following and answer some questions regarding Query Console.
- Open the history and identify your last three commands and try to replay them.
- Open the Settings and verify if all autocomplete items are selected. Did you tried tab completion yourself? 
- Look into Help and lookup what the short-cut is for executing the current selected line.

### 1.2 - Initial cluster checks

Every cluster requires some checks before you start working with it. You can see this as asking most important five questions.
All questions will be asked using the CAT API. You may still remember it provides human-readable output. 

Helpful tools are that you directly can `jump to online documentation` or the selected Request gets `Auto Idented`. These features are accessible by clicking the constructor icon.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/09-DeveloperTools/content/auto-indent.png" alt="auto-ident">

First try to run the `Cluster health` by using the CAT API. 

```
GET _cat/health?v
```

You may already noticed auto completion shows some hits. See below when looking into the  `Node availability and roles`.

```
GET _cat/nodes?v
```

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/09-DeveloperTools/content/suggest-dev.png" alt="suggest-dev">

If you have a 'YELLOW or worse RED state' you may want to look further.  

In normal circumstances this wil display no output, which is good.
```
GET _cat/pending_tasks
```

Maybe we have unassigned shards. This can happen is the system is cannot allocate shards.
```
GET _cluster/allocation/explain
```

Or there are still recoveries in progress.
```
GET _cat/recovery
```

### 1.3 -  Using Auto Ident

Auto ident is one of the feature that is really helpful when you are typing PUT or POST requests. Everybody likes order and well set brackets.

Use the following as input for adding an index template. On purpose I have broken some brackets, so it's time to fix.

Insert this template (as PUT _template) under `auto-indent-complete`.

```
"index_patterns": ["logstash-*"],
  "version": 80001,
  "template": { "settings": {
      "index.refresh_interval": "5s",
      "number_of_shards": 1
    },
    "mappings": {
      "dynamic_templates": [ {
          "message_field": {
            "path_match": "message",
            "match_mapping_type": "string",
            "mapping": {
              "type": "text",
              "norms": false
            }
          }
        },
        {
          "string_fields": {
            "match": "*",
            "match_mapping_type": "string",
            "mapping": {
              "type": "text",
              "norms": false,
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        }
      ],
      "properties": {
        "@timestamp": {
          "type": "date"
        },
        "@version": {
          "type": "keyword"
        },
        "geoip": {
          "dynamic": true,
          "properties": {
            "ip": {
              "type": "ip"
            },
            "location": {
              "type": "geo_point"
            },
            "latitude": {
              "type": "half_float"
            },
            "longitude": {
              "type": "half_float"
            }
          }
        }
      }
    }
  }
```

## Exercise 2 - SQL/PPL Plugin

This exercise explains you what the SQL/PPL plugin is and why is it helpful, exspecially if you are familiar with SQL syntax.

### 2.1 - Query Workbench

When you are DBA or SQL oriented you are going to like this extensive set of functionality. Thanks to this rich plugin OpenSearch has a SQL-like interface. We will start with the introduction in `Query Workbench`. Query Workbench provides a really nice console for query developers, data analysts and scientists. They can build and run SQL queries as before without knowing too much about REST APIS.

When you are at the Home landing page, open the navigation and click `Query Workbench` from the OpenSearch Plugin items.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/09-DeveloperTools/content/sql-workbench.png" alt="sql-workbench">

Try-out the first example query `SHOW tables LIKE %;` and click *Run*. 

Now dive further into some topics and answer some questions regarding Query Workbench.
- Develop a query that only returns the character_name, partner and age from the cartoons index as columns, and belong to the same family.
- Download your results in CSV format.
- What does the `Explain` button learns us?
- What are the most spectacular SQL queries you can build?

More info on [SQL/DQL](https://github.com/opensearch-project/sql/tree/2.x/docs/user/dql).

### 2.2 -  Piped Processing Language (PPL)

Under the hood this plugin also provides another language called Pipe Processing Language (PPL in short). PPL, introduced in Open Distro (AWS) and is inspired 
by so called one-liners used by many engineers.

For example this PPL. Maybe the results may ring a bell?

```
search source=cartoons
| where family_name = 'Simpsons'
| fields character_name, partner, age
```

Now dive further into some topics and answer some questions regarding Query Workbench.
- Can you run this PPL also in Query workbench?
- Can you download the results?
- What does the `Explain` button learns us?
- What is the most spectacular PPL query you can build?

More info on [PPL](https://github.com/opensearch-project/sql/tree/2.x/docs/user/ppl).


### 2.3 -  SQL/PPL CLI

If you can't get enough of SQL or PPL as syntax and you want to go CLI, then we have another great extension for you.

Try to install the `opensearchsql` tool using `pip3` and login in to the opensearch cluster.

### 2.4 - SQL/PPL API

Another common way is using the Query console. Besides all query console benefits, you may combine this with SQL/PPL formatting. Below an example using the sql endpoint.

```
POST /_plugins/_sql/
{
  "query": "SELECT products.price FROM opensearch_dashboards_sample_data_ecommerce WHERE day_of_week=?",
  "parameters": [
    {
      "type": "string",
      "value": "Tuesday"
    }
  ]
}
```

Now dive further into some topics and answer some questions regarding Query Workbench.
- Is autocomplete working as expected?
- Can you add a 'query filter' ?
- Can you develop a PPL variant of this?

## Exercise 3 - OpenSearch Clients

This exercise is about OpenSearch Clients. In particular we are going to look into using Python with OpenSearch.

### 3.1 - OpenSearch low-level Python client

First part you are going to get introduced in `opensearchpy` which is another great Python module. We can install this using PIP.

```
python3 -m pip install opensearch-py==2.2.0
```

Now adjust the script below and save this as `HelloOpenSearch.py`.


```
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts = [{"host": "localhost", "port": 9200}],
    http_auth = ("admin", "admin"),
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False,
)
client.info()
```

Try to create install the module, create the script and get some `client info` back!!!

### 3.1 - OpenSearch Importing CSV with opensearch_py_ml module

This exercise explains how to use Python to import a CSV file. Of course Python modules can be used for many cases, but this is just a code example.

The code example is based on the [Cars data set](../../codesamples/opensearchpy/dataset/cars.csv).

During this exercise you may have the following prereqs ready:

- Bash access, preferable Linux.
- Installed Python 3.X locally, which can be the OpenSearch training server.
- Access to the OpenSearch port '9200'
- Internet access to Python PiPy.

As starting point copy the the **opensearchpy** folder under **codesamples** or execute from this folder.

```
cd codesamples/opensearchpy
pwd
pip3 install opensearch_py_ml
```

### 3.2 - Developing the piece of code

Below the example code. Only things you may have to edit are the host ('localhost') and the password (currently admin) value.

```
from opensearchpy import OpenSearch
import opensearch_py_ml as oml

host = 'localhost'
port = 9200
auth = ('admin', 'admin') # For testing only. Don't store credentials in code.
#ca_certs_path = '/full/path/to/root-ca.pem' # Provide a CA bundle if you use intermediate CAs with your root CA.

# Optional client certificates if you don't want to use HTTP basic authentication.
#client_cert_path = '/full/path/to/client.pem'
#client_key_path = '/full/path/to/client-key.pem'

# Create the client with SSL/TLS enabled, but hostname verification disabled.
client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_compress = True, # enables gzip compression for request bodies
    http_auth = auth,
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False,
)

client.indices.exists(index="cars")

df = oml.csv_to_opensearch("dataset/cars.csv",
                     os_client=client,
                     os_dest_index='cars',
                     os_if_exists='replace',
                     os_dropna=True,
                     os_refresh=True,
                     index_col=0)
```

### 3.3 - Executing import script

Most of the time you may have to add unique Ids into the first column. Important, other you may have documents that get overwritten. To add this I've added a `add_ID.sh` script, which is simple but does the job. For convinience this has already been done.

```
./import_cars.py
```

### 3.4 - Validate succesful import OpenSearch

To validate the import you may want to use **Dev Tools**. Open the Query Console.

Lookup the index and documents?
```
GET cars/_search
```

Do you have all expected records?
```
GET cars/_count
```

Now try to answer some questions regarding Python.
- What kind of activities/tasks can you do with Python and especially the ML library?
- How are the document fields mapped?

Now follow the last activities to make everything available in `OpenSearch Dashboards`.

- Create an index pattern `cars` using no date field.
- Create a dashboard of the data set that contains a minimum of Controls, Descriptions, Search panel and approx four Visualizations.

## Next Steps

You are ready to start with the next lab about [Reporting](../10-Reporting/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!