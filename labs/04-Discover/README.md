# Discover lab exercises

Welcome to the Discover lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to  get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Using Discover
- Applying Filters
- Dashboards Query Language
- Lucene

## Exercise 1 - Using Discover

This exercise helps you to understand how to use Discover for searching, filtering and experiment with search columns.

### 1.1 - Open Discover OpenSearch Dashboards

Login into OpenSearch Dashboards and ensure you are at the `Home - Landing page`. Click the hamburger button (top left) to open the navigator. Here you can open **Discover**. 

***Hint:** You may want to dock the navigator.*

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/04-Discover/content/open-discover.png" alt="open-discover">

Just type `shoes` in the search bar and look for all hits. Hit results are highlighted in yellow.

### 1.2 - Show last 7 days of documents

Now let's search in the default index for the **`last 7 days`** of documents. Take some minutes to analyze the documents. Try to expand a particular document and look for the differences between `Text` and `JSON` output. You may have spotted that `Text` is more user-friendly (Icons, Timezone, etc), but `JSON` provides better depth for the actual data.  All fields that are starting with ( #, @ and _/underscore ) are system related. For example `_source` contains all fields. For now enough, but keep in mind that differences can exist how you look at the data.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/04-Discover/content/search-results.png" alt="search-results">

### 1.3 - Find the field icon that deviates from all other field icons 

Durint this exercise task you will use the field tools that are available. You can easily identify fields by an icon. You maybe spotted the question-mark icon?

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/04-Discover/content/products-field.png" alt="products-field">

Later in exercise 3 we will look if the `products` field is ingested as expected.

### 1.4 - Experiment with adding columns

This exercise you have to replace the default `_source` column with five of the customer order related fields.

Fields:
- customer_id                 (ordered from Ascending)
- customer_full_name 
- customer_gender
- email	customer_phone        (Still empty)

Ensure that only the full name is added, everything is sorted by customer_id and the column order is set as mentioned above.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/04-Discover/content/order-columns.png" alt="order-colums">

You are required to save your results as `orders-table` for later usage.  You can find the save button at the top-right. 

## Exercise 2 - Applying filters

This exercise you are going to apply filters. You maybe already set a *Time Filter* and *Filter* as part of the previous exercises, but we will now look further into in-depth configuration. For example setting *Absolute* time instead of *Relative*.

### 2.1 - Setting an Absolute time filter

During this task you have set a specific *Abosolute* time filter. This differentiates from the already known *Relative* *like 7 days Ago* . For a particular reason you are asked to only show orders between a certain period.

Configure an absolute time (start date & end date) that only shows documents between <u>Sunday **14-05-2023 12:00** and **Monday 15-05-2023 10:00**</u>.

Ensure you have applied the Filter configuration.

### 2.2 - Applying a single filter

Some cases you just want to filter out certain documents. For example when you are only interested in *Women Shoes*. This can be easily done using Filters. Filters is a feature which is available in the UI.

At the top left click **Add Filter**.  Now search for the *category* field and you may see two types available. We will explain later, but for now just choose the `category.keyword` field. Ensure you use *is* as Operator. After this a selection menu is populated with options, where you can select *Women Shoes*. 

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/04-Discover/content/filter-sample.png" alt="filter-sample">

Take notice that before the actual creation the *Edit as Query DSL* is not yet available. This is populated after the actual creation of the filter. In essence filters are in fact easy to use UI that executes API calls.

Now apply this filter.

After succesfull creation you will see the filter enabled.  Click the filter and the filter options will be shown.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/04-Discover/content/filter-options.png" alt="filter-options">

Play around with the options like *Disable*, *Edit* and  extremely helpful option to *Exclude* results.

### 2.3 - Applying multiple filters

Most cases when multiple fields or values are involved you need to add multiple filters. Following task is about building such filter set by combing several filters for the use case below. Multiple fields can act as Boolean filter using AND/OR logic.

*Apply a search containing filtered results of Women’s shoes not sold in New York, sold to Mary, Brigitte or Betty with a price between 1 and 10 euros*

Now take some time to build all filters for this use case. Do you know another use case to  filter?


## Exercise 3 - Dashboards Query Language

This exercise is about another great way of filtering results using the search bar. It almost provides the same functionality as filters, but this is query syntax. Another more powerful text-search provided query syntax is `Lucene`. Let's go through several examples using `Dashboards Query Language` (DQL).

### 3.1 - Verify if DQL is enabled

Open `Discover` and at the right corner of the search bar you can see the currently selected query language. By default `DQL` is used, with `Lucene` as fallback. Click on `DQL` and you see the following options.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/04-Discover/content/dql-enabled.png" alt="dql-enabled">

### 3.2 - Using DQL Syntax

The following are example queries to help to get a deeper understanding of `DQL`.

Just apply the queries to answer the questions and note used query and total of results.

| Question                                                                                       | Total of results |
|------------------------------------------------------------------------------------------------|------------------|
| Does the field `customer_phone` exists as keyword?                                             |        ?         |
| Show only `fullcustomer_full_name` when first name start with 'Bo' and last name ends with 's' |        ?         |
| Only show documents where `customer_id` is greater then 10 and smaller then 20.                |        ?         |
| Only get documents from `MALE` customers that ordered either from 'GB' or 'FR'.                |        ?         |
| Get the all documents since yesterday.                                                         |        ?         |


### 3.3 - Combining multiple DQL as Boolean queries

Look back to exercise 2.3 and recreate the use case filter using DQL. Did you matched the same results?

*Apply a search containing filtered results of Women’s shoes not sold in New York, sold to Mary, Brigitte or Betty with a price between 1 and 10 euros*

## Exercise 4 - Lucene

This exercise is about the native OpenSearch text-search in the search bar. Again the same functionality as filters, but this is query syntax. Big difference with `DQL` is that `Lucene` focusses on 'text-search' rather then aggregations using 'Keywords'. Let's go through several examples using Lucene.

### 4.1 - Ensure that Lucene is enabled

Now set the query language temporary to `Lucene` and answer the questions below.

| Question                                                                                       | Total of results |
|------------------------------------------------------------------------------------------------|------------------|
| Show all emails that not start with 'clarice'                                                  |        ?         |
| Show all orders that are older then yesterday?                                                 |        ?         |
| Look for all orders and exclude 'manifacturer' 'Oceanavigations'                               |        ?         |
| Only get orders where the product has a price between 10 and 100 EURO (without Tax)            |        ?         |

### 4.2 - Combining multiple Lucene as Boolean queries

Look back to exercise 2.3 and recreate the use case filter using Lucene. Did you matched the same results?

*Apply a search containing filtered results of Women’s shoes not sold in New York, sold to Mary, Brigitte or Betty with a price between 1 and 10 euros*

## Next Steps

You are ready to start with the next lab about [Indices](../05-Indices/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!