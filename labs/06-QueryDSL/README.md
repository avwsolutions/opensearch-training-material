# Query DSL lab exercises

Welcome to the Query DSL lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to  get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Query DSL basics
- Scoring
- Full-text queries
- Term-level queries
- Boolean queries
- Search templates

## Exercise 1 - Query DSL basics

This exercise helps you to understand the basics of how to interpretent, use and develop queries using the Query Domain Specific Language. 

### 1.1 - First experience

We start with a first experience query. You may already used `Query DSL` during the previous exercises. Again it's always good to repeat certain practices.

First again login into OpenSearch Dashboards. Nagivate to **Home** and top-right click **Dev Tools**.

When the console is opened you directly wil see an example query. Query DSL is a `search language`, which interfaces to JSON format. Most `queries` consist of one or more `query clauses`. Query clause can either run in `filter context` or `query context`. 

Let's give the example query a try!

```
GET _search
{
  "query": {
    "match_all": {}
  }
}
```

Now try to answer some questions regarding this query.
- Which indices do you hit?
- Which documents are included in the match?
- How many documents are by default returned?
- How do we increase the total (for example, 50) of returned documents?

### 1.2 - Applying filter context

It's time to practice by executing a filter context query. 

- What is the question this query is going to answer for us?
- Does the document match the query clause and which filters do we apply here?

Below the query. Ensure that you still have the index available  from the previous exercise.

```
GET cartoons/_search
{
  "query": { 
    "bool": { 
      "filter": [ 
        { "term":  { "married": true }},
        { "range": { "age": { "gte": 18, "lte": 50 }}}
      ]
    }
  }
}

```

Now try to answer some questions regarding this query.
- Which indices do you hit?
- How many documents did return?
- Does order apply here?

### 1.3 - Applying query context

It's time to practice by executing a query context query. 

- What is the question this query is going to answer for us?
- How well does certain documents match the query clause and what do we apply here?

```
GET cartoons/_search
{
  "query": {
    "match": {
      "about": "mr and ms cartoon figure"
    }
  }
}
```

Now try to answer some questions regarding this query.
- Which indices do you hit?
- How many documents did return?
- Does order apply here?

Looking to both queries we can conclude the differences in using `filter context` and  `query context` which is all about ordering results on scoring.

## Exercise 2 - Scoring

This exercise helps you to understand the scoring and explains this by some examples below.

### 2.1 - Entering the scoring mechanism

As you have learned in the previous exercise. Order does matter when scoring is applied. Scoring is the method of certainty how precise the results match. How relevant is the document?. Scoring value is calculated within the API, but it's important to understand that we can influence the scoring process.

Using the following examples we go through the scoring mechanism.

But before we can start you have to import the `Sample flight data`. During `Getting Started` you also imported the `Sample ecommerce data` set. 

After a succesful import,  Nagivate to **Home** and top-right click **Dev Tools**.

First we want to execute the following `full-text search`.
```
GET opensearch_dashboards_sample_data_flights/_search
{
  "query": {
    "multi_match": {
      "query": "Sunny",
      "fields": ["OriginWeather", "DestWeather"]
    }
  }
}
```

Now try to answer some questions regarding this query.
- Which field has priority?
- What do you expect as first hit?
- Analyze which type of `multi_match` is by default used.

### 2.2 - Manipulating scoring

You might expected that scoring will be higher when multiple fields are hit, but using the default `type` we are looking for the `best_fields`.
Let's adjust this behavior and look for the `most_fields` that match.

Our scenario we know that we are looking for a Sunny destination. 

```
GET opensearch_dashboards_sample_data_flights/_search
{
  "query": {
    "multi_match": {
      "query": "Sunny",
      "type": "most_fields", 
      "fields": ["OriginWeather", "DestWeather"]
    }
  }
}
```

Analyze the results again and you can conclude that first results have both 'OriginWeather' and 'DestWeather` are 'Sunny'.

If you want to inspect more and get nitty gritty nerdy details you may want to run the `_search` query using the `explain function`.

```
GET opensearch_dashboards_sample_data_flights/_search?explain=true
{
  "query": {
    "multi_match": {
      "query": "Sunny",
      "type": "most_fields", 
      "fields": ["OriginWeather", "DestWeather"]
    }
  }
}
```

Now try to answer some questions regarding this query.
- What do you expect as first hit?
- Analyze the effect of changing the query type.
- Analyze and inspect the explain results to understand the API logic that is applied.

### 2.3 - Boosting field weights

But yes, does it make sense? Properly we just want to ensure that 'DestWeather' has a higher weight. We can easily do this by applying a boost on one or more fields. Let's create a query, 'best_fields' again, but with a boost of '^4' on 'DestWeather'

```
GET opensearch_dashboards_sample_data_flights/_search?
{
  "query": {
    "multi_match": {
      "query": "Sunny",
      "fields": ["OriginWeather", "DestWeather^4"]
    }
  }
}
```

Now try to answer some questions regarding this query.
- What do you expect as first hit?
- Analyze the effect of changing the query type.
- Analyze and inspect the results again with the explain function to understand the API logic that is applied.

## Exercise 3 - Full-text queries

This exercise helps you to understand the various types of full-text queries. You already worked with `match`, `multi_match`, `match_all`, but know get introduced in `match_phrase` and `query string`.

### 3.1 - Applying a match_phrase

Some use cases you are not only looking at single words, but also the phrase matters. These scenarios `match_phrase` becomes handy.

For example when using text-search with a `match` will match both values like 'men's', 'men's shoes', but also 'clothing'. At the moment we are only looking for 'men's clothing'. Let's create such query using the `match_phrase` query.

```
GET opensearch_dashboards_sample_data_ecommerce/_search
{
  "query": {
    "match": {
      "category": {
        "query": "men's clothing"
      }
    }
  }
}
```

```
GET opensearch_dashboards_sample_data_ecommerce/_search
{
  "query": {
    "match_phrase": {
      "category": {
        "query": "men's clothing"
      }
    }
  }
}
```

Now try it again, but with `match` query.

Now try to answer some questions regarding this query.
- What do you expect as differences?
- What happens when we apply a `slop` value to the `match_prhase` query?
- Analyze and inspect the results again with the explain function to understand the API logic that is applied.

### 3.2 - Applying a query string

Some do you still remember lucene query language? This can also be used with the `query string` API. Let's try out an example.
This example we are looking for flights to Sunny destinations that departed second or third day of the week without any delay.

```
GET opensearch_dashboards_sample_data_flights/_search
{
  "query": {
    "query_string": {
      "query": "FlightDelayType:\"No Delay\" AND DestWeather:\"Sunny\" AND dayOfWeek:[2 TO 3]"
    }
  }
}
```

Now try to answer some questions regarding this query.
- By which characteristics do  you recognize this is Lucene syntax?
- Analyze and inspect the results again with the explain function to understand the API logic that is applied.

## Exercise 4 - Term-level queries

This exercise helps you to understand the various types of term-level queries. You already worked with `term`, but know get introduced in `terms` and `range`.

### 4.1 - Term and terms queries

Easy way of filtering data is using a term query. Term queries match against a single term, but in some cases you might have multiple terms. This scenario `terms query` becomes interesting. Let's build some queries.

As example we only provide the `term query`.  Try to format the `terms query` yourself!

```
GET /opensearch_dashboards_sample_data_flights/_search
{
  "query": {
    "term": {
      "Carrier": {
        "value": "BeatsWest"
      }
    }
  }
}

```

Now try to answer some questions regarding this query.
- Rebuild above query as 'terms', so we can include the carrier 'OpenSearch-Air'.
- Analyze and inspect the results again with the explain function to understand the API logic that is applied.

## Exercise 5 - Boolean queries

This exercise helps you to understand to combine most queries into boolean queries.  Again really helpful for advanced querying.
### 5.1 - Boolean structure

First let's look at the query structure.

```
GET /opensearch_dashboards_sample_data_flights/_search
{
  "query": {
    "bool": {
      "must": [
        {}
      ],
      "must_not": [
        {}
      ],
      "should": [
        {}
      ],
      "filter": {}
    }
  }
}
```

Now try to answer some questions regarding this query.
- Which sections are part of scoring and which not?
- If some fields are optionally interesting for scoring, which section do you use? 

### 5.2 - Boolean Query as example

Now it's time to build a boolean query on your own, but first look at the example below.

We are looking for all products of that are ordered by 'MALE' persons.
- Which must be bought on Tuesday.
- Not manufactured by "Low Tide Media" due reference.
- Color of blue is interesting.

```
GET /opensearch_dashboards_sample_data_ecommerce/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "day_of_week": {
              "query": "Tuesday"
            }
          }
        }
      ],
      "must_not": [
        {
          "match": {
            "manufacturer": {
              "query": "Low Tide Media"
            }
          }
        }
      ],
      "should": [
        {
          "match": {
            "products.product_name": {
              "query": "blue"
            }
          }
          
        }
      ],
      "filter": [
        {
          "term": {
            "customer_gender": "MALE"
          }
        }
      ]
    }
  }
}
```

Now try to answer some questions regarding this query.
- What field type is required for match of 'blue in the 'products.product_name' field?
- Analyze and inspect the results and reproduce individual query steps.

### 5.3 - Build Your Own Boolean Query

It's time to build your own boolean Query. Take the query string from exercise 3.2 as example.

 ```"query": "FlightDelayType:\"No Delay\" AND DestWeather:\"Sunny\" AND dayOfWeek:[2 TO 3]"```

 Additionally to that we have the following input:

 - We are only interested if the origin country is 'DE'.
 - Day of the week should be a preference.
 - Only mandatory inputs are 'No Delay' and 'Sunny' weather.

## Exercise 6 - Search templates

This exercise helps you to understand how to use search templates. 

### 6.1 - Search template usage

Most of the time queries are not build for life. Additional fine-tuning is always necessary. This requires specific expertise. Also from flexibility view it doesn't really help to make this part of the compiled application code. That's why `search templates` are an ideal way of decoupling and abstracting complexity.

Let's use your cartoons alias again, so you can create your own template. I will continue with the 'Simpons'.

```
GET /cartoons/_search/template
{
  "source": {
    "from": "{{from}}",
    "size": "{{size}}",
    "query": {
      "match": {
        "family_name": "{{Family}}"
      }
    }
  },
  "params": {
    "Family": "Simpsons",
    "size": 1,
    "from": 3
  }
}
```

Now try to answer some questions regarding this query.
- Analyze and inspect the results.
- Explain what happens if you change the 'size' and 'from' values?

### 6.2 - Setting default values

Benefits of templates are `default values`. Let's add these to the above created `search template`.

Just replace the current 'from' and 'size' values with those Mustache templating values.

```
"from": "{{from}}{{^from}}3{{/from}}",
"size": "{{size}}{{^size}}1{{/size}}",
```
Now try to answer some questions regarding this query.
- Analyze and inspect the results.
- What is recognizable when using Mustache is used?

### 6.3 - Storing as script & usage

This last part you are going to store the previous search template as script. This can be done using the script endpoint.
Below the example.

```
POST _scripts/cartoon_search_template
{
  "script": {
    "lang": "mustache",
    "source": {
      "from": "{{from}}{{^from}}3{{/from}}",
      "size": "{{size}}{{^size}}1{{/size}}",
      "query": {
        "match": {
          "family_name": "{{Family}}"
        }
      }
    },
    "params": {
      "Family": "Simpsons"
    }
  }
}
```

Now try to answer some questions regarding this query.
- Analyze and inspect the results.
- Validate various param configurations using the `render` API.
- Last step is to execute a search based on the 'cartoon_search_template'.

## Next Steps

You are ready to start with the next lab about [Visualize](../07-Visualize/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!