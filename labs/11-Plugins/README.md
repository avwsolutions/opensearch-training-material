# Plugins lab exercises

Welcome to the Plugins lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Plugins basics
- Plugins installation

## Exercise 1 - Plugins basics

This exercise explains you what various methods there are available for requesting which plugins are loaded and/or installed. OpenSearch uses a Plugin architecture to extend functionality. 

### 1-1 Plugins management

Plugins are the active parts of `OpenSearch` community that introduces functionality by adding new features. Due this active part, plugins do require maintenance and correct management of handling the life-cycle. Especially when there are known bugs and vulnerabilities. Luckily for us most active plugin follow the OpenSearch version and update scheme.

Looking at plugins can from several perspectives. Most simple way is looking from cluster perspective. here we have another CAT API available.

```
GET _CAT/plugins?v
```

Another way is using a Terminal CLI. For this you have to access the running containers and execute the `opensearch-plugin` command. Advantage here is that you also see installed plugins which are not (yet) loaded.

```
docker ps | grep 9200
docker exec -it <containerId> opensearch-plugin list -v
```

## Exercise 2 - Plugin installation

This exercise explains you how plugins can be installed. OpenSearch uses a Plugin architecture to extend functionality. 

### 2-1 Plugin installation

Here you are going to install a plugin directly in a container. This is not stateful and certainly not a practice for production, but only for learning the installation itself. For correct activation you have to install the plugin on all OpenSearch nodes.

```
docker ps | grep 9200
docker exec -it <containerId> opensearch-plugin install repository-s3
```

Expected output ( You may also run the installation unattended with '--batch' flag)
```
-> Installing repository-s3
-> Downloading repository-s3 from opensearch
[=================================================] 100%?? 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@     WARNING: plugin requires additional permissions     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
* java.lang.RuntimePermission accessDeclaredMembers
* java.lang.RuntimePermission getClassLoader
* java.lang.reflect.ReflectPermission suppressAccessChecks
* java.net.NetPermission setDefaultAuthenticator
* java.net.SocketPermission * connect,resolve
* java.util.PropertyPermission opensearch.allow_insecure_settings read,write
See http://docs.oracle.com/javase/8/docs/technotes/guides/security/permissions.html
for descriptions of what these permissions allow and the associated risks.

Continue with installation? [y/N]y
-> Installed repository-s3 with folder name repository-s3
```

Now run list again to check to installation.

```
docker exec -it 2497d8557e66 opensearch-plugin list | grep s3
repository-s3
```

Repeat these two steps for all OpenSearch nodes.

### 2-2 Plugin (cluster) validation

Do you think this plugin is already acive in the OpenSearch cluster ?

```
GET _cat/plugins
```

No, not yet. You have to restart the nodes before the plugin becomes active.

```
docker-compose stop
docker-compose start
```

Now run again

```
GET _cat/plugins
```
And we see the following `repository-s3` plugin listed.

```
opensearch-node1 opensearch-sql                       2.6.0.0
opensearch-node1 repository-s3                        2.6.0
opensearch-node2 opensearch-alerting                  2.6.0.0
```

## Next Steps

You are ready to start with the next lab about [Observability](../12-Observability/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!