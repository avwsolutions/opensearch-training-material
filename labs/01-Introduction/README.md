# Introduction lab exercises

Welcome to the Introduction lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to  get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Git based training resources
- License models
- Training setup

## Exercise 1 - Using Git for downloading training resources

This first exercise you are required to download the training resources. Most simply way is using Curl or [Download the ZIP](https://github.com/avwsolutions/opensearch-training-material/archive/refs/heads/main.zip) using your favorite browser. Git is not part of this course, but we encourage using the Git client, which you can [download](https://git-scm.com/downloads/guis) for free.

Either choose one of the options to download the training material.

### 1.1 - Download using Curl

```
cd
curl -L https://github.com/avwsolutions/opensearch-training-material/archive/refs/heads/main.zip -o opensearch-training-material.zip
unzip opensearch-training-material-main.zip
mv opensearch-training-material-main opensearch-training-material
```

### 1.2 - Download using Git

```
cd
git clone https://github.com/avwsolutions/opensearch-training-material.git
cd opensearch-training-material
```

If you want to know more about Git, the Version Control System just visit the [Git-SCM Website](https://git-scm.com/).

Now that you have downloaded the material (and extracted the ZIP file) you may want to look into this directory.

```
cd ~/opensearch-training-material
ls
```

## Exercise 2 - Understanding the differences in license models

This exercise you will read through OpenSearch and Elasticsearch used license models and understand the comparison of both models. Important to understand are the benefits of the currently used OpenSearch license model.

For this exercise for both products we have the license model descriptions available [under licenses](licenses).

### 2.1 - Examine license model differences

Examine the differences in the licenses between OpenSearch and Elasticsearch.
- What do you notice and is the biggest difference?
- Explain a peer attendee why OpenSearch uses the Apache 2.0 model.


## Exercise 3 - Understanding the training setup

This exercise you will read through training setup for OpenSearch and understand the components we will use. Important to understand that OpenSearch Stack is built by two core components called `OpenSearch` and `OpenSearch Dashboards`. Data itself is stored in a `NoSQL` based DBMS as `JSON` documents. By nature `NoSQL` doesn't require a schema to start ingesting data. Additionally we will introduce `FluentD` and `OpenSearch Python client` to load two additional `data sets`, next to the two the `sample data sets`.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/01-Introduction/content/training-setup.png" alt="training-setup">

### 3.1 - Examine the training setup components and data sets

Examine the components that are used and which data sets are imported in OpenSearch.
- Can you find the core components that built OpenSearch?
- Explain a peer attendee what the core difference is between NoSQL and SQL based databases.

## Next Steps

You are ready to start with the second lab about [Cluster Deployment](01-ClusterDeployment/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!