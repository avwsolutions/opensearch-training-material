# Notifications lab exercises

Welcome to the Notifications lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Notifications
- Alerts

## Exercise 1 - Notifications

This exercise you learn about setting up notifications. Notifications wil replace `destinations`. Notifications require a channel and optional an `email sender` and `email recipient group`. Channels can be email, SES, Slack, Webhook and more. We wil configure a example email, but if we have time we can look into the Slack integration.

**Setup a email sender with the following specifications:**
- Set name to `local-mail-server`
- Set outbound email to `opensearch@local.domain`
- Set mail host and port to `smtp.local.domain` , 465.

**Setup a email recipient group with the following specifications:**
- Set name to `Admins`
- Set  email to `admins@local.domain`
- Set description to `OpenSearch Admins`

**Setup a channel with the following specifications:**
- Set name to `cluster-health-alerts`
- Set type to `email`
- Set email recipient to `Admins`
- Set email sender to `local-mail-server`


Take notice this is a fake SMTP configuration, which doesn't work.

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/13-Notifications/content/notif-set.gif" alt="notif-set">

Now try the following activities and try to answer some questions.
- Analyze and inspect the various possibilities by opening the Notification Apps.
- Try to create an channel that integates with Slack.

Additional look around and further inspect Notification possibilites.

## Exercise 2 - Alerting

This exercise you learn about setting up monitors provided by the Alerting plugin. Monitors are condition based and work with the Query DSL. During this example we will create a monitor that checks the `cluster health` every 5 minutes.

Below the example input to create the `cluster-health` monitor. For demo purposes you can set the interval to 1 minute.

```

{
   "name": "cluster-health",
   "type": "monitor",
   "monitor_type": "cluster_metrics_monitor",
   "enabled": true,
   "schedule": {
      "period": {
         "unit": "MINUTES",
         "interval": 1
      }
   },
   "inputs": [
      {
         "uri": {
            "api_type": "CLUSTER_HEALTH",
            "path": "_cluster/health/",
            "path_params": "",
            "url": "http://localhost:9200/_cluster/health/"
         }
      }
   ],
   "triggers": [
      {
         "query_level_trigger": {
            "id": "npqlFIgB1PAfAxe6aP-m",
            "name": "outside-green",
            "severity": "1",
            "condition": {
               "script": {
                  "source": "ctx.results[0].status != \"green\"",
                  "lang": "painless"
               }
            },
            "actions": [
               {
                  "id": "n5qlFIgB1PAfAxe6aP-o",
                  "name": "sendoutnotifications",
                  "destination_id": "yUejFIgBRl__aZ14TPKz",
                  "message_template": {
                     "source": "Monitor {{ctx.monitor.name}} just entered alert status. Please investigate the issue.\n  - Trigger: {{ctx.trigger.name}}\n  - Severity: {{ctx.trigger.severity}}\n  - Period start: {{ctx.periodStart}}\n  - Period end: {{ctx.periodEnd}}",
                     "lang": "mustache"
                  },
                  "throttle_enabled": false,
                  "subject_template": {
                     "source": "cluster health degraded",
                     "lang": "mustache"
                  }
               }
            ]
         }
      }
   ],
   "ui_metadata": {
      "schedule": {
         "timezone": null,
         "frequency": "interval",
         "period": {
            "unit": "MINUTES",
            "interval": 5
         },
         "daily": 0,
         "weekly": {
            "tue": false,
            "wed": false,
            "thur": false,
            "sat": false,
            "fri": false,
            "mon": false,
            "sun": false
         },
         "monthly": {
            "type": "day",
            "day": 1
         },
         "cronExpression": "0 */1 * * *"
      },
      "monitor_type": "cluster_metrics_monitor",
      "search": {
         "searchType": "clusterMetrics",
         "timeField": "",
         "aggregations": [],
         "groupBy": [],
         "bucketValue": 1,
         "bucketUnitOfTime": "h",
         "where": {
            "fieldName": [],
            "fieldRangeEnd": 0,
            "fieldRangeStart": 0,
            "fieldValue": "",
            "operator": "is"
         }
      }
   }
}

```

As guidance see the following example.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/13-Notifications/content/notif-monitor.gif" alt="notif-monitor">

Now try the following activities and try to answer some questions.
- Analyze and inspect the various possibilities by opening the Alerting Apps.
- Just add an index with too many replicas and see if an alert is triggered. See below an example in the `Alert console`. 

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/13-Notifications/content/alert.png" alt="alert">

- Try to create a rogue monitor yourself that triggers on a custom index value.

As example you can monitor if any rogue `family_name` enters the `simpsons` index again. For this you should use a **Per query monitor** using the **Extraction query editor** method. For the query you can use a simple **Term query** to catch the rogue family name. Customize the **trigger** and **action** message for your needs.

Just create the monitor and reuse the rogue character from [Exercise 4.4](../04-Discover/README.md).

Interested in the actual JSON document that defined your monitor?

```
GET _plugins/_alerting/monitors/_search
{
  "query": {
    "match" : {
      "monitor.name": "rogue"
    }
  }
} 
```
## Next Steps

You are ready to start with the next lab about [Anomaly detection](../14-AnomalyDetection/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!