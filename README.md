# EasyApi

### Run mysql And redis By Docker

```
curl -fsSL https://get.docker.com | bash -s docker
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD={password} -d mysql
docker run --name redis -p 6379:6379 -d redis --requirepass "{redis-password}"
docker inspect mysql/redis | grep IPAddress
```

### Update System Environs

```
vim .bash_profile / .zshrc
# export ES_APP_DOMAIN=http://127.0.0.1

# export ES_MAIL_SERVER=smtp.exmail.xx.com
# export ES_MAIL_PORT=465
# export ES_MAIL_USERNAME=noreply@easysaas.com
# export ES_MAIL_PASSWORD=xxxxxxxxxxxxxxxxxxxxx

# export ES_REDIS_URI=redis://:password@host:port
# export ES_DATABASE_URI=sqlite:///{DIR}/main.db
# mysql+pymysql://user:password@host:port/dbname
source .bash_profile / .zshrc
```

### Install venv And requirements.txt

```
# Python3.8 required
cd {DIR} && python3.8 -m venv .venv
source .venv/bin/activate / deactivate
pip3 install -r requirements.txt
```

### Run Application With uvicorn

```
.venv/bin/uvicorn main:app --reload
```
