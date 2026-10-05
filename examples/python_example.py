# pip install apify-client
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("automationnation/google-videos-scraper").call(run_input={
  "queries": [
    "how to make sourdough bread"
  ],
  "maxResultsPerQuery": 30
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("channel"), item.get("duration"), item.get("url"))
