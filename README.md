# Streamlit Recipes

Collection of Streamlit recipes and learnings.

## Setup

### Set up Development Environment

1. Create a virtual environment (optional):

   ```bash
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   (.venv) $ # Should see the virtual env name as a prefix the shell prompt
   ```

### Set up Hosting

1. Set up for [Steamlit Community Cloud](https://streamlit.io/cloud) hosting.
1. Sign up with Github.

## Streamlit Notes

Assume `st` as a prefix for the package `streamlit`, ie. `import streamlit as st`.

### Runtime

* Anytime something on the web page is updated, streamlit reruns the entire python script.
* When there is an function associated to event handlers eg. `on_change` or `on_click` in a widget, the evetn 
  handler will br run before the rest of the script.

### Caching

* To speed things up, data or rendered content of a function (or event handler) can be cached via the `@st.cache_data` or 
  `@st.cache_resource` decorator.
* Use the `@st.cache_data` decorator for anything we can persist in the database eg. python primitive values, 
  dataframes, values from api calls, etc.
* Use the `@st.cache_resource` decorator for anything we can't persist in the database eg. ML models, database 
  connections, etc.

### Content

* Use `st.write` to write content to the web page. The function has some "smartness" built into it where it will 
  interpret the passed value type and determine how the content should be rendered. For example passing a dataframe 
  `df` to `st.write` would render `df` as an interactive table.
* Sometimes we may want to render the (above) dataframe `df` as a static table, so there are times when calling `st.
  table(df)` is more appropriate.
* We can implicitly write content to the app without calling `st.write` by using streamlit "magic" commands by 
  simply calling the variable literal value. So instead of the following:

  ```python
  st.write('Started computation')
  st.write(df)
  ``` 
  
  We can just call the string expression or variable.

  ```python
  'Started computation'
  df
  ``` 


## Reference

* [Streamlit homepage](https://streamlit.io)
