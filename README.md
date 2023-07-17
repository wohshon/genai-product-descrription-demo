## Gen AI with Google Search

Uses Vertex AI GenAI models to summarize results returned from google search results.

### Setup:

- Setting up Custom Search API (Google Search) with Langchain:

https://python.langchain.com/docs/modules/agents/tools/integrations/google_search

Need to set the following as environment variables:

```
GOOGLE_CSE_ID
GOOGLE_API_KEY
```

### Running as streamlit app

`streamlit run Home.py --server.port 8080`

_Some fringe cases may run into parsing errors (occurring at langchain), currently the demo does not filter out those cases, if any error is encountered, simply re-submit the query._

