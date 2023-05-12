# Reporting lab exercises

Welcome to the Reporting lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Reporting basics
- Visual reporting
- Data reporting
- Reporting scheduling
- Branding

## Exercise 1 - Reporting basics

This exercise explains you what reporting delivers and it is implemented and flow within the OpenSearch Stack. 

### 1.1 - What is Reporting

Reporting is another plugin with both a API and UI that provides reporting capabilities. Reporting differs from dashboards since reports are rather a static moment that is stored in a preferrable easy shareable format. Formats are for example CSV and PDF.  This is also we the report capabilities differentiate from data to visual reports. For the real CLI freaks, there is also a CLI available.

Open the Reporting UI from the Navigator. You can find `Reporting` under OpenSearch Plugins.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/10-Reporting/content/report-ui.png" alt="report-ui">

Now try to answer some questions regarding reporting.
- Analyze, inspect where reports can be generated from.
- Can you explain from which parts of OpenSearch you can generate data and visual reports?

### 1.2 - Reporting flow

To get a better understanding were Reporting activities take place our friends from [OpenSearch Development](https://opensearch.org/blog/feature-highlight-reporting/). Especially since Chrominium is involved for generating the actual report,which run within `OpenSearch Dashboards`, but stores data on the actual `OpenSearch Cluster`.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/10-Reporting/content/flow-diagram.png" alt="flow-diagram">

Now try to answer some questions regarding reporting.
- Which component runs on `OpenSearch Dashboards` that is responsible for generating reports?
- Where is the actual reporting data stored?

## Exercise 2 - Visual Reporting

This exercise explains you how to generate visual reports and share them using formats like PDF and PNG. This is such as easy to open a Dashboard or Visualization, click **Reporting** and choose either **Generate Report** or **Schedule and Share**. 

### 2.1 - Download reports from Dashboard

No try to generate a report yourself and download the PDF and PNG version. For example using the Ecommerce dashboard.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/10-Reporting/content/report-download.png" alt="report-download">

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/10-Reporting/content/visual-reports.gif" alt="visual-reports credits AWS">

## Exercise 3 - Data Reporting

This exercise explains you how to generate data reports and share them using formats like CSV. This is such as easy to open Discover, create a table structure, click **Reporting** and choose either **Generate Report** or **Schedule and Share**. 

### 3.1 - Download reports from Discover

No try to generate a report yourself and download the CSV version. Create your own Search table from sample web logs using fields *clientip, machine.os, machine.ram, agent, geo.src and geo.dst*.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/10-Reporting/content/csv-download.png" alt="csv-download">

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/10-Reporting/content/csv-reports.gif" alt="csv-reports credits AWS">

## Exercise 4 - Reporting scheduling

This exercise explains you how to schedule a data reports and share this at the later moment.

### 4.1 - Create reporting definition

Create a report definition for the previous `data table` exercise. Name the report `customers` and make it a daily occurence report. Choose your own time-slot. 

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/10-Reporting/content/report-schedule.png" alt="report-schedule">

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/10-Reporting/content/create-report-definition.gif" alt="create-report-definition credits AWS">

## Exercise 5 - Branding

This exercise explains how to add branding to your visual report. You can also brand you OpenSearch environment, which is the last part, but strongly advice  to do this on a single-user environment.

### 5.1 - Add logo to Visual report

You are creating a report definition of the dashboard. The report of that dashboard wil include a Header. Headers and Footers are optional and accept HTML style coding. Ensure you create an on-demand report.

For example as Header add the following.

```
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Krones_Logo.svg/1200px-Krones_Logo.svg.png" alt="Krones logo">
```

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/10-Reporting/content/report-banner.png" alt="report-banner">


### 5.2 - Add custom branding to OpenSearch Dashboards

You may want to view this Youtube movie that explains about applying custom branding. It gives a good overview on the possibilities. 

https://www.youtube.com/watch?v=ouEIZbFTPuo 

Stil want to change your local environment. No problem use this as example.

Following hints & tips:
- Ensure you have pictures that load smoothly.
- Ensure correct resolution.

Bad images wil impact overall user experience, which is more important then custom branding.

You can find the `opensearch_dashboards.yml` in the OpenSearch container.

```
logo:
  defaultUrl: "https://localhost:5601/ui/assets/my-own-image.svg"
  darkModeUrl: "https://localhost:5601/ui/assets/dark-mode-my-own-image.svg"
mark:
  defaultUrl: "https://localhost:5601/ui/assets/my-own-image2.svg"
  darkModeUrl: "https://localhost:5601/ui/assets/dark-mode-my-own-image2.svg"
# loadingLogo:
#   defaultUrl: ""
#   darkModeUrl: ""
# faviconUrl: ""
applicationTitle: "My OpenSearch Lab Environment"
```

## Next Steps

You are ready to start with the next lab about [Reporting](../10-Reporting/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!