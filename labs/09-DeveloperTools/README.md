# Developer tools lab exercises

Welcome to the Developer tools lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Query console
- SQL/PPL API
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

First try to run the `Cluster health` by using the CAT API.

```
GET _cat/health
```

You may already noticed auto completion shows some hits. See below when looking into the  `Node availability and roles`.

```
GET _cat/nodes
```

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/09-DeveloperTools/content/suggest-dev.png" alt="suggest-dev">