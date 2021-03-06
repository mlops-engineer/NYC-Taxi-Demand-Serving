# NYC-Taxi-Demand-Serving
- Streamlit + BentoML + Random Forest, Torch


<br />


### Architecture

<img src="https://www.dropbox.com/s/gzk8gpkdpcciem5/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-05-16%20%EC%98%A4%EC%A0%84%203.12.53.png?raw=1">


- But, Pytorch model is not yet complete. I keep getting an error. I plan to correct the error in the future.
<br />


### Set Environment

```
virtualenv env
source env/bin/activate

pip3 install -r requirements.txt
```

<br />

### Airflow 
- airflow init

```
airflow init
```

- run airflow webserver

```
airflow webserver -p 8080
```

- run airflow scheduler

```
airflow scheduler
```

- Then, `localhost:8080` : Airflow Webserver

<br />


### Training
```
cd src
python3 main.py
```


- Then, Save BentoML Service

<br />


### Check BentoML Service

```
bentoml list
```

<img src="https://www.dropbox.com/s/fmz9mas25omldhq/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-05-16%20%EC%98%A4%EC%A0%84%203.21.40.png?raw=1">


<br />

### Run streamlit & Serving
```
cd streamlit_app
streamlit run app.py
```


<img src="https://www.dropbox.com/s/lvybnn3a6vhk31s/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-05-16%20%EC%98%A4%EC%A0%84%202.31.26.png?raw=1">


- `localhost:8501`
- Login
    - username : user / password : fsdl

<br />

### Predict(Inference)
- Select Feature in Streamlit Sidebar

<img src="https://www.dropbox.com/s/kv87zshvwg6wfy6/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-05-16%20%EC%98%A4%EC%A0%84%202.30.35.png?raw=1">

- Request

<img src="https://www.dropbox.com/s/yau6zfguczu2bgu/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-05-16%20%EC%98%A4%EC%A0%84%202.30.49.png?raw=1">

<br />


### Project improvement plan(TODO)
- [ ] Pytorch Model
- [ ] Model Manager : MLFlow
- [ ] Model Output Management : Save BigQuery Table
- [ ] Hyper Parameter Tuning : Microsoft NNI
- [ ] Scheduling Tool : Prefect
- [ ] Dockerize, Docker Compose
- [ ] Streamlit Dashboard : Production Data Distribution, Explainable AI
- [ ] Deploy Google App Engine


<br />