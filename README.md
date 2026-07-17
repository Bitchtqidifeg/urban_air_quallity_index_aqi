# urban_air_quallity_index_aqi

# Urban Air Quality Prediction — Deploy to Streamlit Cloud

Steps to deploy this app to Streamlit Cloud (recommended):

1. Create a new GitHub repository and push this project (root must contain `app.py` and `requirements.txt`).

   ```bash
   git init
   git add .
   git commit -m "Initial commit - Urban Air Quality Prediction"
   git branch -M main
   git remote add origin <your-git-remote-url>
   git push -u origin main
   ```

2. Go to https://streamlit.io/cloud and sign in with GitHub.

3. Click **New app** → choose the repository, branch `main`, and set the main file to `app.py`.

4. Click **Deploy**. Streamlit Cloud will install packages from `requirements.txt` and start the app.

Notes and tips:
- `runtime.txt` pins the Python version used on the host.
- `.streamlit/config.toml` sets `headless=true` and disables CORS for cloud hosting.
- If you use private API keys (e.g., OpenWeather API key), add them using Streamlit Cloud's **Secrets** (Dashboard → Settings → Secrets) as `API_KEY` and read them in `api.py` using `st.secrets`.

Local test before deployment:

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
streamlit run app.py
```

If you want help pushing to GitHub or setting secrets, tell me and I will provide the exact commands or add a `.gitignore` and other helper files.

