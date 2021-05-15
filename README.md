# NYC-Taxi-Serving
- Streamlit + BentoML + Random Forest


<br />


### Architecture

<img src="https://www.dropbox.com/s/tjpq3dzdntksps6/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-05-16%20%EC%98%A4%EC%A0%84%203.02.06.png?raw=1">


- But, Pytorch model is not yet complete. I keep getting an error. I plan to correct the error in the future.
<br />


### Set Environment

```
pip3 install -r requirements.txt
```

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

<img src="https://www.dropbox.com/s/o2kgqt7brvia2qf/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202021-05-16%20%EC%98%A4%EC%A0%84%202.33.23.png?raw=1">


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

