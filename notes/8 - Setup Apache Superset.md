# Install Superset in your machine

```
brew install readline pkg-config libffi openssl mysql postgresql@14
```

```
brew install python@3.11
```

Setup the virtual environment

```
/opt/homebrew/bin/python3.11 -m venv superset-env
```

Activate the venv

```
source superset-env/bin/activate
```

Upgrade pip

```
pip install --upgrade setuptools pip
```

Export flags

```
export LDFLAGS="-L$(brew --prefix openssl)/lib"
export CFLAGS="-I$(brew --prefix openssl)/include"
```

Install superset

```
pip install apache_superset
```

Generate a secret key

```
openssl rand -base64 42
```

Export the secret key

```
export SUPERSET_SECRET_KEY=<your-secret-key>
```

```
export FLASK_APP=superset
```

Install marshmallow

```
pip install marshmallow==3.26.1
```

Then, you need to initialize the database:

```
superset db upgrade
```

Finish installing by running through the following commands:

Create an admin user in your metadata database (use `admin` as username to be able to load the examples)

```
superset fab create-admin
```

```
superset load_examples
```

```
superset init
```

```
superset run -p 8088 --with-threads --reload --debugger
```

If everything worked, you should be able to navigate to `hostname:port` in your browser (e.g. locally by default at `127.0.0.1:8088`) and login using the username and password you created.

![Pasted image 20250810192533.png](./images/Pasted%20image%2020250810192533.png)

# Connect to Database (Presto)

Before connecting, lets port-forward the presto cluster from inside the container to the host machine (localhost:8080) using below command and keep this terminal running:

```
kubectl port-forward svc/presto 8080:8080 -n presto
```

Now, select `Connect database`

![Pasted image 20250810192954.png](./images/Pasted%20image%2020250810192954.png)

Select `Presto`

![Pasted image 20250810193055.png](./images/Pasted%20image%2020250810193055.png)

Enter credentials

Display Name

```
Presto
```

SQLAlchemyURI

```
presto://localhost:8080/iceberg/default
```

Click on `Test Connection` to check the connection. `Connection looks good` message appears at the bottom-right corner.

![Pasted image 20250810193401.png](./images/Pasted%20image%2020250810193401.png)

Click `Connect`. `Database Connected` message appears.