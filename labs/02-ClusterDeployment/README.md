# Cluster deployment lab exercises

Welcome to the Cluster Deployment lab exercises. During the lab exercises the student will experiential work through various tasks and activities to gain practical experience and develop new skills. In hands-on learning, attendees are given the opportunity to explore, experiment, and discover knowledge for themselves about OpenSearch.

The goal is to  get actively engage and ask questions if something is not clear or you are blocked. Important to understand that there are no strong dependencies between labs, so it's okay if you're behind and follow your own pace.

The following key topics are part of these exercises:

- Hardware/virtualization prerequisites
- Operating system preparation
- OpenSearch Installation
- Updating default passwords
- Managing the stack

## Exercise 1 - Validate your hardware/virtualization prerequisites

This exercise helps you to setup the hardware prerequisites. Most cases you will use a virtual machine (VM). Nowadays we can't do without virtualization hypervisors, but we explain the VirtualBox (instead of VMWare) setup. Additionally ensure that `Virtualization Technology support` is enabled in the System BIOS. 

Also for Macbook users, take notice that things might not work if you have a `modern M1 or M2 CPU compatibility`

### 1.1 - Setup VirtualBox

Installation is really straightforward, but be aware of above notes. You may want to download the installer from [VirtualBox.org](https://www.virtualbox.org/wiki/Downloads).

After setting up VirtualBox we can download a preprepped VDI from [OSBoxes](https://www.osboxes.org/ubuntu/]. Choose `Ubuntu 22.04 Jammy Jellyfish` the VirtuaBox download.

```
cd ~/opensearch-training-material
mkdir virt
cd virt
curl -L https://sourceforge.net/projects/osboxes/files/v/vb/55-U-u/22.04/64bit.7z/download -k -o virtbox.7z
# Use 7ZIP to extract
```

Now create a new a new VM, Ubuntu 64 based like below configuration. Ensure that you choose the `~/opensearch-training-material/virt/Ubuntu 22.04 (64bit).vdi` as image.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/02-ClusterDeployment/content/create-vdi.png" alt="create-vdi">

When the VM is created succesfully, you can configure `Port Forwarding` under 'Settings\Network\Adapter 1\Advanced.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/02-ClusterDeployment/content/port-vdi.png" alt="port-vdi">

Now start the Ubuntu instance and try to login (`ssh osboxes@127.0.0.1:2222`) using the credentials below.

Credentials are:
- username: osboxes
- password: osboxes.org

## Exercise 2 - Operating System configuration

Now that we have the Ubuntu VM up and running we can start with configuration some of the OS prereqs and installation of Docker engine. We currently use Docker since Podman still is not really well compatible with earlier `docker-compose` files.

### 2.1 - Configure Operating System prerequisites

Below the commands that need to hit the Terminal.

In short, let's summarize:
- We ensure that the OS has an updated list with the latest updates available.
- We install both `docker.io` and `docker-compose` packages.
- We ensure docker is `Running` and does survive a reboot.
- We disable swapping.
- We increase and load the `VM Maximum Map Count` and make the change persistent in the `sysctl.conf`.
- We ensure that your `non-root` user can use docker CLI properly.
- We logout the session to force certain changes to be applied, like the `usermod`.


```
sudo apt update -y
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo systemctl status docker
sudo systemctl enable docker
swapoff -a
sudo echo “vm.max_map_count=262144” >> /etc/sysctl.conf
sudo sysctl -p
sudo usermod -aG docker <your_user>
exit # force relogin to activate group membership
```

If you want to know more about the Docker Engine, just visit the [Docker website](https://www.docker.com/products/docker-desktop/alternatives/).

## Exercise 3 - OpenSearch Installation

This exercise we will install an OpenSearch Cluster using `docker-compose`. Docker-compose already described the `Stack Architecture` for us, including networking and volume configuration. Really helpful for demo and training purposes. Take a look at the `training-setup` diagram below, which parts you are going to implement.

<img src="https://raw.githubusercontent.com/avwsolutions/opensearch-training-material/main/labs/01-Introduction/content/training-setup.png" alt="training-setup">

### 3.1 - Examine Docker Compose configuration

Ensure that you are in the *root* folder of the training material (opensearch-training-material)

```
cd ~/opensearch-training-material
mkdir docker
cd docker
curl -O https://raw.githubusercontent.com/opensearch-project/documentation-website/2.6/assets/examples/docker-compose.yml
```

Examine the docker compose configuration.
- Can you find the core components that built OpenSearch?
- How many active instances are included in the service we created?


### 3.2 - Spin-up the OpenSearch cluster with Docker Compose

You can know spin-up the `OpenSearch Cluster`.

```
docker-compose up -d
```

## Exercise 4 - Updating default passwords

This exercise is really important when your cluster has an open connection to the Internet. Luckily the OpenSearch API is only accessible from inside the Docker host, but still OpenSearch Dashboards uses the default passwords. Here we want to avoid Security issues.

Below the tasks how to set new passwords.

### 4.1 - Update password from the default admin/admin and others

**Get the container ID for a OpenSearch node**
```
docker ps | grep 9200 # Note the container ID
docker exec -it <container ID> /bin/bash
```

**Create a hash from the new password**
```
docker exec -it <container ID> /bin/bash
~/plugins/opensearch-security/tools/hash.sh -p Kuursus123!
```

**Now in the container edit the `internal_users.yml`**
```
#docker exec -it <container ID> /bin/bash
vi  ~/config/opensearch-security/internal_users.yml

# Change all hashes for all users and save the file ( :wq)
```

**Additional in the container run the `securityadmin.sh` tool to update the internalusers configuration**
```
#docker exec -it <container ID> /bin/bash
~/plugins/opensearch-security/tools/securityadmin.sh -f ../../../config/opensearch-security/internal_users.yml -t internalusers -cacert ~/config/root-ca.pem -cert ~/config/kirk.pem -key ~/config/kirk-key.pem
```

### 4.2 - Update the opensearch-dashboards container password

Now we also have to provide OpenSearch Dashboards the new password. This is stored inside the `opensearch_dashboards.yml` configuration inside the container.

```
docker ps | grep 5601 # Note the container ID
docker exec -it <container ID> /bin/bash
vi config/opensearch_dashboards.yml
change this line opensearch.password: <kibanaserver to new password> and save the file ( :wq)
```

## Exercise 5 - Managing the stack

This last exercise we explain some simple tricks for managing your stack. Think about start and stopping, but also troubleshooting and debugging error logs.

### 5.1 - Stopping and starting environment

Simply remember the following commands. Don't use `docker up / docker down` since that will reset the whole environment to default again.

```
docker-compose stop
docker-compose start
```

### 5.2 - Troubleshooting

Watch out with docker-compose down, since you have to re-change the password again due reset!

```
docker-compose config (check if config is OK)
docker-compose ps ( check if all container services are running)
docker-compose logs (check logs)
```
## Next Steps

You are ready to start with the next lab about [Getting Started](../03-GettingStarted/README.md) in OpenSearch. Be aware that the trainer might have to explain the training material and provide additional instructions for a jump start.

Enjoy the exercises!!!