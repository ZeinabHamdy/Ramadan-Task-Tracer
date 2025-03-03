
# Ramadan Task Tracker

## Project Overview
Ramadan Task Tracker is a web application designed to help users track their daily tasks efficiently during Ramadan.

[Demo video](Demo.mp4)
## Prerequisites
Ensure you have the following installed before proceeding:
- Python (>=3.8) - [Download here](https://www.python.org/downloads/)
- pip (Python package manager) - It comes pre-installed with Python, but you can verify by running:
  ```bash
  python -m ensurepip --default-pip
  ```


## Setup Instructions

Follow these steps to run the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/ZeinabHamdy/Ramadan-Task-Tracker
```

### 2. Navigate to the Project Directory
```bash
cd Ramadan-Task-Tracker
```


### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Copy the Environment File
```bash
cp .env.example .env
```

### 5. Generate a Secret Key
Run the following command to generate a secret key:
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

### 6. Set the Secret Key
Take the generated key and add it to the `.env` file under `SECRET_KEY`:
```ini
SECRET_KEY=your_generated_secret_key
```


### 7. Run the Development Server
```bash
python manage.py runserver
```

Now, the project should be running on [http://127.0.0.1:8000/](http://127.0.0.1:8000/).




