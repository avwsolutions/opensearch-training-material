# Aggregations lab exercises

Welcome to the Aggregations lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Aggregations basics
- Metric Aggregations
- Bucket Aggregations
- Pipeline Aggregations

## Exercise 1 - Aggregation basics

This exercise explains you what aggregations are and why they are helpful within OpenSearch. In the previous lab you already worked with aggregations using building visualizations. Now we are diving into the actual API.

### 1.1 - General structure

Aggregations are helpful when applying analytics on your data and extract statistics. Aggregations are not only available within visualizations, but also using the API.

Let's get introduced in the general structure of `aggregations`.

```
GET _search
{
  "size": 0,
  "aggs": {
    "NAME": {
      "AGG_TYPE": {}
    }
  }
}
```

Now try to answer some questions regarding aggregations.
- Analyze, inspect the aggregation structure. 
- Explain why the 'size' can be set to zero '0'?
- Build an aggregation that calculates the average `avg` of the field `taxful_total_price` using the name `avg_taxful_total_price`.

## Exercise 2 - Metric Aggregations

This exercise explains you which types are available for Metric Aggregations and provides an example to execute.

### 2.1 - Multi-value Metric Aggregation

Metric aggregations are divided in two main types, namely single- and multi-value metric aggregations. In the previous exercise you already used a single-value metric aggregation called `avg`. During this exercise you wil learn about a multi-value metric aggregation. The goal is to get a `percentile` overview of the used `bytes` ordered by the default range of percentiles.



```
GET opensearch_dashboards_sample_data_logs/_search
{
  "size": 0,
  "aggs": {
    "percentile_bytes_web_traffic": {
      "percentiles": {
        "field": "bytes",
        "
      }
    }
  }
}
```

Now try to answer some questions regarding aggregations.
- Analyze, inspect the aggregation output. 
- Explain how we can set custom ranges, so we can focus on extreme outliers [99%, 99,5%, 99,9%] above the 95%?

## Exercise 3 - Bucket Aggregations

This exercise explains you when to use Bucket Aggregations and provides an example to execute.

### 3.1 - Data histogram 

If you are looking for categorizing documents, then bucket aggregations are the way to go. Most commonly used is the `terms aggregation`.


```
GET /opensearch_dashboards_sample_data_ecommerce/_search?size=0
{
  "size": 0,
  "aggs": {
    "orders_over_time": {
      "date_histogram": {
        "field": "order_date",
        "calendar_interval": "month"
      }
    }
  }
}
```

Now try to answer some questions regarding aggregations.
- Analyze, inspect the aggregation output. 
- Explain how we need to configure `calendar_interval` to have interval set to a 21 days sales period?

## Exercise 4 - Pipeline Aggregations

This exercise explains you when to use Pipeline Aggregations and provides an example that combines two aggregations in a pipeline.

### 4.1 - Combined Pipeline aggregation

Looking at pipeline aggregations you consists of parent and sibling aggregations. Nice thing of using a Sibling aggregation that it uses the output of a parent aggregation for calcuting the output. Keep in mind to ensure the `buckets_path` is set correctly.

In the example below we combine the Bucket aggregation above, which is part of the `Parent Aggregation`. Next 'max_monthly_sales' is the `Sibling Aggregation` which uses the previous output as input. 

```
GET /opensearch_dashboards_sample_data_ecommerce/_search
{
  "size": 0,
  "aggs": {
    "orders_over_time": {
      "date_histogram": {
        "field": "order_date",
        "calendar_interval": "month"
      },
      "aggs": {
        "sales": {
          "sum": {
            "field": "products.price"
          }
        }
      }
    },
    "max_monthly_sales": {
      "max_bucket": {
        "buckets_path": "orders_over_time>sales" 
      }
    }
  }
}

```

Now try to answer some questions regarding aggregations.
- Analyze, inspect the aggregation output. 
- Explain how we need to configure `buckets_path` if we change 'sum' to 'avg'?

## Next Steps

You are ready to start with the next lab about [Developer Tools](../09-DeveloperTools/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!