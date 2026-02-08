# In Git Bash, run this command in your project folder:
echo "web: gunicorn app:app" > Procfile
```

**OR** manually create a file named exactly **`Procfile`** (no .txt extension) and paste this:
```
web: gunicorn app:app