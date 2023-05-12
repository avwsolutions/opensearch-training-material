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
- Aggregation of type average on field 'age'.

**Buckets**
- One `split rows` using the `terms` aggregation on field 'family_name' using default ordering.

**Additional options**
- Ensure that you calculate the total average and percentages are shown.

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/07-Visualize/content/visual-datatable.gif" alt="visual-datatable">

Analyze, inspect the results and try to create a data table yourself.

### 1.2 - Pies and Donuts

Another great visualizations are Pies or Donuts. They help to give direct overview in categories. Let's create another example using the cartoons index pattern.

Our goal is to create insights in the Top 5 families, which is based on counting the family members.

We can start creating a visualization with the following characteristics.

**Metrics**
- Aggregation of type count on 'documents'.

**Buckets**
- One `split rows` using the `terms` aggregation on field 'family_name'. Order by count with a maximum of 5 results.

**Additional options**
- Ensure that you deselect the `Donut` option.

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/07-Visualize/content/visual-pie.gif" alt="visual-pie">

Now try to answer some questions regarding this visualization.
- Analyze and inspect the results.
- Can you include 'married' as another layer using an additional bucket?

### 1.3 - Timeseries with Lines

Visuals are most of the time shown as line on a X-Y Axis. They help to easily spot increases and decreases within buckets like with a certain metric. Let's create another example using the cartoons index pattern.

Our goal is to create insights in the average increase of age based on ages periods. For age periods we will use
- 0 till 23 years.
- 23 till 65 years.
- 65 till 85 years.

We can start creating a visualization with the following characteristics.

**Metrics**
- Aggregation (`Y-Axis`) of type average on field 'age'.

**Buckets**
- One `X-Axis` using the `Range` aggregation on field 'age' with the following ranges [ "0-23", "23-65", "65-85" ].

**Additional options**
- Ensure that you selected line mode 'Normal' and the 'X-axis' is on the bottom.

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/07-Visualize/content/visual-line.gif" alt="visual-line">

Now try to answer some questions regarding this visualization.
- Analyze and inspect the results.
- Can you include a 'Threshold line` of for the age of '44'?
- Maybe you want to adjust or add another range to ensure everybody above 85 is included?

### 1.4 - Tag cloud

Ever looked for trending and frequently used words? Then you may have used a `word cloud`. Part of the core visualizations we can create a `tag cloud`.  Let's look a trending words in our `cartoons`. Our goal is to give insights in trending cartoon words.

We can start creating a visualization with the following characteristics.

**Metrics**
- Aggregation of type count on 'tag size'.

**Buckets**
- One `Tags` using the `Terms` aggregation on field 'about'. Order by count with a maximum of 50 results.

**Additional options**
- Ensure that the orientation is single.
- Ensure text-scale is linair.

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/07-Visualize/content/visual-cloud.gif" alt="visual-cloud">

Now try to answer some questions regarding this visualization.
- Analyze and inspect the results.
- Try to experiment with the orientation and text-scale.
- Can you change the `Terms` aggregation field from a text to a keyword, can you explain  what happens? 

## Exercise 2 - Visualization types

This exercise explains you which types are available to create visualizations using OpenSearch Dashboards.

### 2.1 - Charts

Charts are helpful in many ways like to depict trends. You already worked with the `line chart`, but not yet plotted on a timestamp based `X-Axis`.
Most common cases you wil plot things over a certain time period. Personally I always like a `stacked` `area chart`, but again this depends on expected visisbility. For this we are are using the `sample web logs`. Our goal is to give insights in the various machine operating systems that are using the web service over time.

We can start creating a visualization with the following characteristics.

**Metrics**
- Aggregation (`Y-Axis`) of type count on documents.

**Buckets**
- One `X-Axis` using the `Date Histogram` aggregation. For now keep the min interval on 'auto'.
- One `Split Series` using the `Terms` aggregation on field 'machine.os.keyword'. Keep the size on '5'.

**Additional options**
- Keep the chart type on 'area' and the mode on 'stack'.

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/07-Visualize/content/visual-area.gif" alt="visual-area">


Now try to answer some questions regarding this visualization.
- Analyze, inspect the results and start with optimizing the visualization.
- Try to experiment with the chart type and mode. What do you like here?
- Can you change the minimum interval to 12 hours (X-Axis)instead of auto?

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
