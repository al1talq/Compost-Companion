# Compost Companion
Start your composting journey strong with an assistant that can help turn your grocery list into a composting plan

## Run locally

1. Install the Python dependencies with `python -m pip install -r requirements.txt`.
2. Set `OPENAI_API_KEY` in your environment. `OPENAI_MODEL` is optional and
   defaults to `gpt-4o-mini`.
3. Run the app with `python app.py`.

The app reports a configuration error on the form if `OPENAI_API_KEY` is not
set; the key should not be committed to the repository.
