# NPD
https://ontop-vkg.org/npd-benchmark/
## Statistic
### Ontology
#Class: 342

#Object Property: 142

#Data Property: 238

#Individual: 855

### Database
#Table: 70

#Cloumn: 962

#Row: 257271

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
install postgresSQL using docker
```shell
docker pull postgres
```
run postgres
```shell
docker run --name my-postgres -e POSTGRES_PASSWORD=root -p 5432:5432 -d postgres
```
- --name mysql-container: Names your container
- -e POSTGRES_PASSWORD=your_password: Sets the root password
- -d: Runs the container in detached mode (background)
- -p 5432:5432: Maps the container's postgresSQL port to your host
- postgres: Specifies the image to use

## Load NPD dataset
**Create NPD database**
1. Login into postgresSQL
```text
psql -h 127.0.0.1 -p 5432 -U postgres 
```
2. Create database
```text
CREATE DATABASE npd;
```
3. Quit postgresSQL
```text
\q
```

**Load data**

```shell
psql -h 127.0.0.1 -p 5432 -U postgres -d npd -f npd.psql
```
**check**
```shell
# 1. get into 
psql -h 127.0.0.1 -p 5432 -U postgres -d npd
# 2. check data
\dt
# 3. quit
enter q
```

You will see information below if successful:
```text
Schema |                   Name                    | Type  |  Owner   
--------+-------------------------------------------+-------+----------
 public | apaAreaGross                              | table | postgres
 public | apaAreaNet                                | table | postgres
 public | baaArea                                   | table | postgres
 public | bsns_arr_area                             | table | postgres
 public | bsns_arr_area_area_poly_hst               | table | postgres
 public | bsns_arr_area_licensee_hst                | table | postgres
 public | bsns_arr_area_operator                    | table | postgres
 public | bsns_arr_area_transfer_hst                | table | postgres
 public | company                                   | table | postgres
 public | company_reserves                          | table | postgres
 public | discovery                                 | table | postgres
 public | discovery_reserves                        | table | postgres
 public | dscArea                                   | table | postgres
 public | facility_fixed                            | table | postgres
 public | facility_moveable                         | table | postgres
 public | fclPoint                                  | table | postgres
```

## Configure Database Connection
Modify the configuration in `npd.properties`

## Deploy VKG
**Ensure you have downloaded [ontop-protege-bundle](https://github.com/ontop/ontop/releases).**

**Ensure you have opened ontop tabs (protege → Window → Tabs → Ontop SPARQL & Ontop Mappings)**

You will see information below if successful:

![protege_with_ontop_tabs](../../resources/imgs/protege_with_ontop_tabs.png)

Now start to deploy and check the VKG: 
1. Open the ontology file `npd.owl` (protege → File → Open)
2. Select the Ontop Reasoner (protege → Reasoner → Ontop)
3. Start the Ontop Reasoner (protege → Reasoner → Start reasoner)
4. Wait till `Reasoner active` is shown in the Protege's bottom right corner

![protege_with_ontop_tabs](../../resources/imgs/protege_reasoner_active.png)

5. Execute a SPARQL sample to check if the VKG is working (in tab **Ontop SPARQL**):
```text
SELECT ?wellbore
WHERE {
  ?wellbore a <http://www.w3.org/2004/02/skos/core#Concept>.
}
```

**You will see information below if successful:**

![protege_sparql_query](../../resources/imgs/protege_sparql_query.png)