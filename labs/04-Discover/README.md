# Discover lab exercises

Welcome to the Discover lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to  get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Using Discover
- Applying Filters
- Dashboard Query Language
- Saving searches

## Exercise 1 - Using Discover

This exercise helps you to understand how to use Discover for searching, filtering and experiment with search columns.

### 1.1 - Open Discover OpenSearch Dashboards

Login into OpenSearch Dashboards and ensure you are at the `Home - Landing page`. Click the hamburger button (top left) to open the navigator. Here you can open **Discover**.

***Hint:** You may want to dock the navigator.*

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/04-Discover/content/open-discover.png" alt="open-discover">

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

You may want to save your results as `orders-table`.
## Exercise 2 - Applying filters

This exercise you are going to appy
