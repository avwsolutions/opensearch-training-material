# Getting started lab exercises

Welcome to the Getting Started lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to  get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- First login experience
- Add some sample data
- Analyze and experiment with eCommerce orders

## Exercise 1 - First login experience

This exercise helps you to select a supported browser login into the console and setting some initial preferences.

### 1.1 - Open OpenSearch Dashboards in browser

During this first task you will open the `OpenSearch Dashboards` console in a web browser session. Now open a supported browser like Firefox, Chrome, Safari, Edge or any Chromium based. So almost everything except Internet Explorer. Use the provided IP address or local IP to connect like `http://127.0.0.1:5601`.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/03-GettingStarted/content/login-screen.png" alt="login-screen">

Use the user `admin` with the password you have received or created in the previous lab “Cluster deployment”.

### 1.2 - Accepting initial welcome message

In the following welcome screen click **Add data**.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/03-GettingStarted/content/welcome-msg.png" alt="welcome-msg">

### 1.3 - Setting our Tenant preference

We now are now asked to set our preffered `Tenant` to save our `Dashboards`. For now we can choose *Private* and **Confirm**.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/03-GettingStarted/content/tenant-msg.png" alt="tenant-msg">


## Exercise 2 - Adding eCommerce sample data

This exercise you have to add the eCommerce sample data that contains various customer orders. If you are lost, you can find the `Sample data` import at the `Home` landing page.

### 2.1 - Setting our Tenant preference

For now we are going to add sample eCommerce orders. Click **Add data**.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/03-GettingStarted/content/add-esample.png" alt="add-esample">

After some time we can view data. Click the **View data** button then the dashboard will be opened. 

## Exercise 3 - Analyze and experiment with eCommerce orders

During this exercise we are going to analyze and experiment with the eCommerce orders. We will work with the dashboard, browse through the provided functionality and try to answer the following questions below.

### 3.1 - Data analysis and experimentation

For approx 5 minutes click around and play with the `eCommerce controls`. After an analysis, try to answer these questions by using either control or other panels that are provided by the dashboard.

First look into the dashboard details looking to the last 7 days of data.

- Which gender has a larger percentage when looking at Sales by Gender?
- Which city has the third largest sales count on the map?
- How many times did the bell ring ?
- What is the most selling product ?
- Bonus: Most selling product was sold last in which city?

### 3.2 - Technical analysis and experimentatoin

Now let's find some more technical details.

Here you can also be allowed to use OpenSearch features!

- What happens when you select a specific vendor?
- How many days in total of data do we have?
- How many documents in total of data do we have?


As last task let’s dive further into the data set and try to discover which valuable field seem not yet properly indexed?

As hint: You may find it in the eCommerce Orders panel.

Following exercise we are going to explain this issue.

## Next Steps

You are ready to start with the next lab about [Discover](../04-Discover/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!