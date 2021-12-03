# MSSQL EX3

以 Flask Tutorial 範例改寫，原範例使用SQLite，改用MSSQL。
練習 Store Procedure 呼叫。


## Installation
安裝 Python 3.9，並啟用虛擬環境。
```
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Database
0. 使用 Docker 啟動MSSQL資料庫服務
```bash
docker run --rm -e "ACCEPT_EULA=Y" \
  -e "SA_PASSWORD=yourpassword" \
  -e "MSSQL_COLLATION=Chinese_Taiwan_Stroke_CI_AS" \
  --name mssql2019 -p 1433:1433 \
  -d mcr.microsoft.com/mssql/server:2019-CU13-ubuntu-20.04
```

1. 操作 SQL Server 容器的`sqlcmd`工具，建立資料庫 `Sales`
```
docker exec -it mssql2019 /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P
yourpassword

# sqlcmd
> create database Sales;
> Go
```

2. 初始化結構
```
flask init-db
```

3. 建立 Store Procedure
同理，可用 sqlcmd 或偏好的GUI工具建立。


## Config
使用`dotenv`保存環境變數，新增`.env`
增加下列環境變數，帳號密碼請依自己的設定調整。
* MSSQL_USERNAME=sa
* MSSQL_PASSWORD=yourpassword
* MSSQL_DATABASE=Sales
* MSSQL_HOSTNAME=localhost
* FLASK_APP=sandbox
* FLASK_ENV=development

## Start
```
flask run
```

## Caveats
資料庫初始化，需拆多個腳本，無法一次完成。
