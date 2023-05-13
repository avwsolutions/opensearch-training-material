# Observability lab exercises

Welcome to the Observability lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Applications
- Availability 
- Notebooks

## Exercise 1 - Applications

This exercise you learn about creating an application. You wil also see that this `Observability` plugin set is depending on OpenTelemetry data streams, especially traces, since they contain the Services, Traces and Spans to configure.

Create a application called `Order App` and use the sample web data logs as  `log source - Base query`.

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/12-Observability/content/o11y-appl.gif" alt="o11y-appl">

Now try the following activities and try to answer some questions.
- Analyze and inspect the various possibilities by opening the `Order App`.
- Why can't we add services or traces to the application yet?

Additional look around and further inspect Apps like Trace, Event and Metrics Analytics.

## Exercise 2 - Availability

This exercise you learn about adding availability level to your application. This can be simply done when opening the `Applications` view and using the default query that is provided (count).

Add three levels of availability and save the availability set as `Availability SLA Targets (SLO)`. Three levels are:
- Fatal at 0.
- Critical at 5.
- Warning at 10.

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/12-Observability/content/o11y-availabilityset.gif" alt="o11y-availbilityset">

Now try the following activities and try to answer some questions.
- Analyze and inspect the various possibilities by opening the `Log Events` and try-out `Events` and `Visualizations`.
- Why does it show Fatal at the moment when opening the App?

## Exercise 3 - Notebooks

This exercise you learn about using notebooks. Notebook are a single pain glass for analysts and reliability engineers that analyze and inspect data sets. Notebooks can be used to store snippets. We are going to add the sample notebooks that are provided.

Open `Notebooks` under `Observability`.  You wil see the possibility to import sample notebooks. Give that a try.

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/12-Observability/content/o11y-notebook.gif" alt="o11y-notebook">

Now try the following activities and try to answer some questions.
- Analyze and inspect the various notebooks that are created.
- Create now your own notebook that contains some queries and visuals.

## Next Steps

You are ready to start with the next lab about [Notifications](../13-Notifications/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!