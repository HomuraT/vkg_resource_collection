# Dest
https://github.com/ontopic-vkg/destination-tutorial/tree/master
## Statistic
### Ontology
#Class: 7

#Object Property: 4

#Data Property: 8

#Individual: 0

### Database
#Table: 8

#Cloumn: 80

#Row: 51117

# Deployment Steps
## Install docker
install docker
```shell
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
check
```shell
sudo docker run hello-world
```
You will see information below if successful:
```text
Hello from Docker!
This message shows that your installation appears to be working correctly.
```
## Install postgresSQL
install postgresSQL with **PostGIS**  using docker 
```shell
docker pull postgis/postgis
```
run postgres
```shell
docker run --name postgis -e POSTGRES_PASSWORD="tFG+}@9,9>58I£k£>|=" -p 5434:5432 -d postgis/postgis
```
- --name mysql-container: Names your container
- -e POSTGRES_PASSWORD=your_password: Sets the root password
- -d: Runs the container in detached mode (background)
- -p 5432:5432: Maps the container's postgresSQL port to your host
- postgres: Specifies the image to use

## Load dataset
**Create database**
1. Login into postgresSQL
```text
psql -h 127.0.0.1 -p 5434 -U postgres 
```
2. Create database
```text
CREATE DATABASE dest;
```
3. Quit postgresSQL
```text
\q
```

**Load data**

```shell
psql -h 127.0.0.1 -p 5434 -U postgres -d dest -f dest.sql
```
**check**
```shell
# 1. get into 
psql -h 127.0.0.1 -p 5432 -U postgres -d dest
# 2. check data
\dt
# 3. quit
enter q
```

You will see information below if successful:
```text
                   List of relations
  Schema  |           Name           | Type  |  Owner   
----------+--------------------------+-------+----------
 public   | spatial_ref_sys          | table | postgres
 tiger    | addr                     | table | postgres
 tiger    | addrfeat                 | table | postgres
 tiger    | bg                       | table | postgres
 tiger    | county                   | table | postgres
 tiger    | county_lookup            | table | postgres
 tiger    | countysub_lookup         | table | postgres
 tiger    | cousub                   | table | postgres
 tiger    | direction_lookup         | table | postgres
 tiger    | edges                    | table | postgres
 tiger    | faces                    | table | postgres
 tiger    | featnames                | table | postgres
 tiger    | geocode_settings         | table | postgres
 tiger    | geocode_settings_default | table | postgres
 tiger    | loader_lookuptables      | table | postgres
 tiger    | loader_platform          | table | postgres
 tiger    | loader_variables         | table | postgres
 tiger    | pagc_gaz                 | table | postgres
 tiger    | pagc_lex                 | table | postgres
 tiger    | pagc_rules               | table | postgres
 tiger    | place                    | table | postgres
 tiger    | place_lookup             | table | postgres
```

## Configure Database Connection
Modify the configuration in `dest-solution.properties`

## Deploy VKG
**Ensure you have downloaded [ontop-protege-bundle](https://github.com/ontop/ontop/releases).**

**Ensure you have opened ontop tabs (protege → Window → Tabs → Ontop SPARQL & Ontop Mappings)**

You will see information below if successful:

![protege_with_ontop_tabs](../../resources/imgs/protege_with_ontop_tabs.png)

Now start to deploy and check the VKG: 
1. Open the ontology file `dest-solution.ttl` (protege → File → Open)
2. Select the Ontop Reasoner (protege → Reasoner → Ontop)
3. Start the Ontop Reasoner (protege → Reasoner → Start reasoner)
4. Wait till `Reasoner active` is shown in the Protege's bottom right corner

![protege_with_ontop_tabs](../../resources/imgs/protege_reasoner_active.png)

5. Execute a SPARQL sample to check if the VKG is working (in tab **Ontop SPARQL**):
```text
SELECT ?e
WHERE {
  ?e a <http://destination.example.org/ontology/dest#OutdoorWater>.
}
```

**You will see information below if successful:**

![protege_sparql_query](../../resources/imgs/protege_sparql_query.png)