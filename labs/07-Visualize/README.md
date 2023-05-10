# Visualize lab exercises

Welcome to the Visualize lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Visualization basics
- Visualization types
- Visualization tools

## Exercise 1 - Visualization basics

This exercise helps you to understand the basics of how to interpretent visualizations, use and develop visualizations using OpenSearch Dashboards.

before we can start you have to import the `Sample web logs`. During `Getting Started` you also imported the `Sample ecommerce data` set. 

After a succesful import,  Nagivate to **Home** and top-right click **Dev Tools**.

### 1.1 - Data tables

We will start with our first visualization, which is part of the core package. Data tables are the most straightforward way of displaying your data.
Before we can start creating any visualization we either need a `saved search` or `index-pattern`.  You alredy got introduced into search, but I shortly wil explain what an index pattern is. Index pattern is used for translation OpenSearch Dashboards fields towards OpenSearch field. The configuration provides mapping and potential conflicts that can occur. Important to understand is that a index pattern may need to be refreshed if you add an additional field.

First look at example below and create an `index-pattern` for the cartoons alias.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/07-Visualize/content/index-patterns.gif" alt="index-patterns">

Now that you have created a index pattern called 'cartoons`. Our goal is to create insights in the average age within the specific families and overall.

We can start creating a visualization with the following characteristics.

**Metrics**
- One aggregation of type average on field 'age'.

**Buckets**
- One `split rows` using the `terms` aggregation on field 'family_name' using default ordering.

Additional options
- Ensure that you calculate the total average and percentages are shown.

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/07-Visualize/content/visual-datatable.gif" alt="visual-datatable">

Analyze, inspect the results and try to create a data table yourself.

### 1.2 - Pies and Donuts

Another great visualizations are Pies or Donuts. They help to give direct overview in categories. Let's create another example using the cartoons index pattern.

Our goal is to create insights in the Top 5 families, which is based on counting the family members.

We can start creating a visualization with the following characteristics.

**Metrics**
- One aggregation of type count on 'documents'.

**Buckets**
- One `split rows` using the `terms` aggregation on field 'family_name'. Order by count with a maximum of 5 results.

Additional options
- Ensure that you deselect the `Donut` option.

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/07-Visualize/content/visual-pie.gif" alt="visual-pie">

Now try to answer some questions regarding this visualization.
- Analyze and inspect the results.
- Can you include 'married' as another layer using an additional bucket?

### 1.3 - Timeseries with Lines

### 1.4 - Tag cloud
## Exercise 2 - Visualization types

This exercise explains you which types are available to create visualizations using OpenSearch Dashboards.

### 2.1 - Charts

### 2.2 - Counters and Gauges

### 2.3 - Heatmap

### 2.4 - Maps

### 2.5 - Purpose of Controls and Markdown 

### 3.2 - Using TSDB

### 3.3 - Using VisBuilder
## Exercise 3 - Visualization tools

This exercise helps you to understand the basics of how to interpretent / experience visualizations tools, use and develop visualizations using tools like Timeline, TSDB, and VisBuilder.

### 3.1 - Using Timeline

### 3.2 - Using TSDB

### 3.3 - Using VisBuilder
