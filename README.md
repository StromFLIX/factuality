# Welcome to Factuality: The Misinformation Buster!

<img align="left" width="100" height="100" src="./assets/factuality.png">

Hey there, curious minds 👋 ! It's me, your digital sidekick **Factuality** on a quest to squash misinformation, one fact at a time. Welcome to the coolest tool in the cyber universe where we turn detective mode on and dive deep into the sea of information to bring you the truth, the whole truth, and nothing but the truth!

*High level overview:*
```bash
Extract `claims` from the statement provided
for claim in claims:
    Search for and fact check the `claim`
Provide conclusion based on statement and `claims`
```

---

> Based on [long-form-factuality](https://arxiv.org/abs/2403.18802) ->
> [github](https://github.com/google-deepmind/long-form-factuality)

![Demo of factuality](./assets/demo.svg) 

## Quick start

### Requirements

- Python 3.11 or higher is needed for typed GPT response support.
- Access to one of the two supported search engines (Bing, Google)
  - Google allows 100 free search queries per day. [How to setup](https://developers.google.com/custom-search/v1/overview)
  - Bing allows for 1000 free search queries per month. [How to
    setup](https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/create-bing-search-service-resource)
- Access to [Openai API](https://openai.com/blog/openai-api)

### Install

```bash
 python3.11 -m pip install factuality
```

### Run

```bash
factuality -s "test something is ridiculus" --oai-api-key "<oai-key-here>" --bing-search-v7-subscription-key "<bing-search-key-here>"
```

> ⚠️ Defaults are set to `gpt-3.5-turbo` better resultus especially for extraction and conclusion can be achived with
> `gpt-4-turbo-preview`

## Table of Content

- [Quick start](#quick-start)
- [Example](#example-for-a-markdown-output-of-factuality)
- [Options](#options)
- [Library](#library-usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Support](#example-for-a-markdown-output-of-factuality)

## Example for a markdown output of factuality

> Given the limit of having up to 16 ai search instances for each subscription [Azure Subscription
> Limits](https://learn.microsoft.com/en-us/azure/search/search-limits-quotas-capacity#subscription-limits), it doesn't work well
> to give every one of our 1000+ customers their own service. Instead, sharing these services makes more sense because
> we can then spread out up to 1000/3000 indices as needed [Index
> Limits](https://learn.microsoft.com/en-us/azure/search/search-limits-quotas-capacity#index-limits). However, for Document
> Intelligence and Language Services, it's better to keep them separate for each customer. This way, we avoid any problems if one
> customer uses too much and slows down the service for others. The limits are 15 transactions per second for Document
> Intelligence [Document Intelligence Service
> Limits](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/service-limits?view=doc-intel-4.0.0#model-usage)
> and 1000 transactions per minute for AI Language Service [AI Language Service Rate
> Limits](https://learn.microsoft.com/en-us/azure/ai-services/language-service/concepts/data-limits#rate-limits).

|                                                             Claim                                                              | Result |                                                         Source Reference                                                          |                                                                                                                                                                     Source Quote                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Azure Subscription Limits allow up to 16 AI search instances for each subscription.                                             |verified|https://learn.microsoft.com/en-us/azure/search/search-limits-quotas-capacity#subscription-limits                                   |You can create multiple billable search services (Basic and higher), up to the maximum number of services allowed at each tier. For example, you could create up to 16 services at the Basic tier and another 16 services at the S1 tier within the same subscription.                                                                                |
|Azure allows spreading out up to 1000/3000 indices as needed.                                                                   |verified|https://learn.microsoft.com/en-us/azure/search/search-limits-quotas-capacity#index-limits                                          |Maximum indexes 3 5 or 15 50 200 200 1000 per partition or 3000 per service 10 10                                                                                                                                                                                                                                                                     |
|For Document Intelligence and Language Services, it's better to keep them separate for each customer to avoid service slowdowns.|verified|https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/document-generative-ai-the-power-of-azure-ai-document/ba-p/3875015|Varying Document Formats: Document Types: Diverse document types, such as scanned PDFs, digitized PDFs, images, and office documents, present unique challenges due to their different formats. Extracting information from each type requires specialized techniques and tools to handle the variations in data structure and content representation.|
|Document Intelligence limits are 15 transactions per second.                                                                    |verified|https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/service-limits?view=doc-intel-4.0.0#model-usage          |By default the number of transactions per second is limited to 15 transactions per second for a Document Intelligence resource. For the Standard pricing tier, this amount can be increased.                                                                                                                                                          |
|AI Language Service has a rate limit of 1000 transactions per minute.                                                           |verified|https://learn.microsoft.com/en-us/azure/ai-services/language-service/concepts/data-limits#rate-limits                              |Your rate limit varies with your pricing tier. These limits are the same for both versions of the API. These rate limits don't apply to the Text Analytics for health container, which doesn't have a set rate limit. Tier Requests per second Requests per minute S / Multi-service 1000 1000 S0 / F0 100 300                                        |


> 🤖 Conclusion [100/100]: The statement accurately reflects the limitations and recommendations for managing Azure AI services across a large number of customers. It correctly cites the Azure Subscription Limits, allowing up to 16 AI search instances per subscription, and the strategy to spread out up to 1000/3000 indices as needed to accommodate the needs of 1000+ customers. Additionally, the statement correctly identifies the separate handling of Document Intelligence and Language Services to prevent service slowdowns due to high usage by individual customers, supported by the cited limits of 15 transactions per second for Document Intelligence and 1000 transactions per minute for AI Language Service. Each claim is verified and supported by the provided source references and quotes, indicating a high level of truthfulness in the statement.

> 💡 More examples can be found in the [examples.md](./docs/examples.md)

## Library usage

```py
from factuality.runner.factuality import Factuality
from factuality.utils.options import Options

factuality = Factuality(
    options=Options(
        oai_api_key="<api_key_here>",
        bing_search_v7_endpoint="https://api.bing.microsoft.com/",
        bing_search_v7_subscription_key="<subscription_key_here>"
    )
)

conclusion, _, _ = factuality.check("Neil armstrong land on the moon.")

print(conclusion.description, conclusion.score)
```

## Options

| Option | Environment Variable | Required | Description | Default |
|---|---|---|---|---|
| `--statement`, `-s` |  | Yes | Statement to fact-check can be text or path to a text file |  |
| `--output`, `-o` | `OUTPUT_FORMAT` | No | The output format for the fact-check results. Supported formats: console, markdown, json. | `console` |
| `--output-path` | `OUTPUT_PATH` | No | The output path for the fact-check results. | `.` |
| `--search-engine` | `SEARCH_ENGINE` | No | The search engine to use for extracting articles. Supported: Bing, Google. | `bing` |
| `--log-level` | `LOG_LEVEL` | No | Log level for the logger. Supported: DEBUG, INFO, WARNING, ERROR, CRITICAL. | `INFO` |
| `--oai-api-key` | `OPENAI_API_KEY` | Yes | OpenAI API key |  |
| `--allowlist` | `ALLOWLIST` | No | List of domains to allow for search results. Format ['domain1.com', 'domain2.com'] | `[]` |
| `--blocklist` | `BLOCKLIST` | No | List of domains to block for search results. Format ['domain1.com', 'domain2.com'] | `[]` |
| `--validation-checks-per-claim` | `VALIDATION_CHECKS_PER_CLAIM` | No | How many resources will factuality use to verify a claim. | `1` |
| `--same-site-allowed` | `SAME_SITE_ALLOWED` | No | If the same site is allowed to be used multiple times for the same claim. | `True` |
| `--bing-search-v7-subscription-key` | `BING_SEARCH_V7_SUBSCRIPTION_KEY` | No | Bing Search V7 Subscription Key |  |
| `--bing-search-v7-endpoint` | `BING_SEARCH_V7_ENDPOINT` | No | Bing Search V7 Endpoint URL | `https://api.bing.microsoft.com/` |
| `--google-search-api-key` | `GOOGLE_SEARCH_API_KEY` | No | Google Search API Key |  |
| `--google-search-cx` | `GOOGLE_SEARCH_CX` | No | Google Search identifier of the Programmable Search Engine |  |
| `--openai-model-extract` | `OPENAI_MODEL_EXTRACT` | No | OpenAI Model for Extract | `gpt-3.5-turbo` |
| `--openai-model-factcheck` | `OPENAI_MODEL_FACTCHECK` | No | OpenAI Model for Fact Check | `gpt-3.5-turbo` |
| `--openai-model-conclusion` | `OPENAI_MODEL_CONCLUSION` | No | OpenAI Model for Conclusion | `gpt-3.5-turbo` |
| `--search-extract-article-length` | `SEARCH_EXTRACT_ARTICLE_LENGTH` | No | Search Extract Article Length | `5000` |
| `--search-extract-article-overlap` | `SEARCH_EXTRACT_ARTICLE_OVERLAP` | No | Search Extract Article Overlap | `500` |
| `--maximum-search-results` | `MAXIMUM_SEARCH_RESULTS` | No | Maximum Search Results | `5` |

## Troubleshooting

### lxml installation issue

If you encounter an ImportError related to `lxml.html.clean` module when installing or running factuality, this is due to a recent
change where the `lxml.html.clean` functionality has been separated into its own project, lxml_html_clean. This change requires an
additional step during installation to ensure all dependencies are correctly met.

To resolve this issue, you need to install the lxml package with the html_clean extra. This can be achieved by running the
following command:

```
python3.11 -m pip install "lxml[html_clean]"
``` 

And for `ImportError: cannot import name '_imaging' from 'PIL' (/usr/lib/python3/dist-packages/PIL/__init__.py)`

You can resolve it with:

```
python3.11 -m pip install -U Pillow
``` 


## Contributing

I welcome contributions to this project! Whether you're fixing a bug, adding a new feature, or improving the documentation, your
help is greatly appreciated.

### How to Contribute

1. **Explore Issues:** Start by checking out the issues marked with the `[help wanted]` tag. These are areas where your
   contributions can make a significant impact.
1. **Fork and Clone:** Once you've identified an issue you're interested in tackling, fork the repository and clone it locally
   to start making your changes.
1. **Submit a Pull Request:** After you've made your changes, push them to your fork and submit a pull request to the main
   repository. Please provide a clear description of the problem and solution, including any relevant issue numbers.

## Support

This project is primarily designed for individual and developmental use, and as such, enterprise-level support and deployment
assistance are not provided. If you require help or have inquiries regarding the project, I encourage you to reach out through
my website. For further details and contact information, please visit
[https://felix.moenckemeyer.com](https://felix.moenckemeyer.com). Your feedback and questions are always welcome, and I'll do my
best to help you.

