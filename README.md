# Welcome to Factuality: The Misinformation Buster!

<img src="./assets/factuality.png" width="300" />

👋 Hey there, curious minds! It's me, your digital sidekick **Factuality** on a quest to squash misinformation, one fact at a time. Welcome to the coolest tool in the cyber universe where we turn detective mode on and dive deep into the sea of information to bring you the truth, the whole truth, and nothing but the truth!


> Based on [long-form-factuality](https://arxiv.org/abs/2403.18802) -> [github](https://github.com/google-deepmind/long-form-factuality)

## First Test

> Biden’s strategy is very simple:
> 1. Get as many illegals in the country as possible.
> 2. Legalize them to create a permanent majority – a one-party state.
>
> That is why they are encouraging so much illegal immigration. Simple, yet effective.


|                                                    Claim                                                    |      Result       |                                                            Source Reference                                                            |                                                                                                                                                             Source Quote                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Biden's strategy is to get as many illegals in the country as possible.                                      |ResultType.REJECTED|https://www.politifact.com/factchecks/2024/feb/06/elon-musk/elon-musk-is-wrong-to-say-joe-biden-is-recruiting/                          |On his first day as president, Joe Biden asked Congress to create a path to citizenship for immigrants in the country illegally. But the current Senate bill, which Biden supports, would not do that.                                                                                                                                 |
|Biden's strategy includes legalizing illegal immigrants to create a permanent majority and a one-party state.|ResultType.REJECTED|https://www.poynter.org/fact-checking/2024/elon-musk-is-wrong-to-say-joe-biden-is-recruiting-immigrants-to-create-a-democratic-majority/|Musk provided no evidence to show such a Biden strategy exists. And the claim doesn’t add up, because it takes immigrants years to become U.S. citizens, and there’s no guarantee that immigrants who gain citizenship will vote for Democrats.                                                                                        |
|The Biden administration is encouraging much illegal immigration.                                            |ResultType.VERIFIED|https://www.factcheck.org/2024/02/breaking-down-the-immigration-figures/                                                                |Encounters on the southern border of those trying to enter the U.S. without authorization have gone up significantly under President Joe Biden. Government statistics show that in the initial processing of millions of encounters, 2.5 million people have been released into the U.S. and 2.8 million have been removed or expelled.|

> 🤖 Conclusion [20/100]: The statement that Biden's strategy is to encourage illegal immigration to create a permanent majority and a one-party state is largely unfounded. The claim that Biden's strategy involves getting as many illegal immigrants into the country as possible and then legalizing them to ensure a one-party state is rejected by reputable sources. PolitiFact and Poynter both refute the idea that Biden is actively recruiting illegal immigrants for the purpose of creating a Democratic majority, noting that there is no evidence to support such a strategy and highlighting the lengthy process for immigrants to become U.S. citizens, with no guarantee of their political allegiance. However, it is verified that encounters on the southern border have significantly increased under President Biden, with millions of people either being released into the U.S. or removed. This fact alone does not substantiate the broader claim of a deliberate strategy to alter the political landscape through immigration policy. Therefore, the overall truthfulness of the statement is low, given the lack of evidence for the alleged strategy and the rejection of key claims by credible fact-checking organizations.

## Second Test

> I think you are right having ai search service per customer makes no sense.
> We should share it as we then have the limit of up to 1000/3000 indices if needed.
> For the other two (document intelligence and language ) i think they should stay as per customer so we do not have issues when one customer overloads the system for other customers. 

|                                             Claim                                              |      Result       |                                                   Source Reference                                                   |                                                                                              Source Quote                                                                                               |
|------------------------------------------------------------------------------------------------|-------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Having an AI search service per customer is not practical.                                      |ResultType.REJECTED|https://blog.hubspot.com/service/pros-cons-ai-in-service                                                              |a says their CX agents can 'now quickly deal with any dissatisfied customers first.' This has helped them 'dramatically improve the customer experience' and 'significantly reduce the risk of churning.'|
|Sharing an AI search service allows for up to 1000/3000 indices.                                |ResultType.VERIFIED|https://learn.microsoft.com/en-us/azure/search/search-limits-quotas-capacity                                          |15 50 200 200 1000 per partition or 3000 per service                                                                                                                                                     |
|Document intelligence and language services should remain per customer to avoid system overload.|ResultType.VERIFIED|https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/language-support-custom?view=doc-intel-4.0.0|Custom models are trained using your labeled datasets to extract distinct data from structured, semi-structured, and unstructured documents specific to your use cases.                                  |

> 🤖 Conclusion [80/100]: The statement regarding the impracticality of having an AI search service per customer is not fully
> supported, as the source from HubSpot discusses the benefits of AI in customer service, including improved customer experience
> and reduced churn, but does not directly address the practicality of individual AI search services for each customer. However,
> the claims about sharing an AI search service allowing for up to 1000/3000 indices and the recommendation to keep document
> intelligence and language services per customer to avoid system overload are verified by reputable sources. Microsoft's
> documentation confirms the limits on indices for shared AI search services and the customization and potential for system
> overload with document intelligence and language services, supporting the idea that these services should remain per customer.
> Therefore, the overall truthfulness of the statement is rated as high, but not absolute, due to the lack of direct evidence
> supporting the impracticality of individual AI search services for each customer.

## Third test

> Obama is actually born in Kenya, the country of his father. This means Obama is not "a natural-born citizen of the U.S."
> and is therefore not fit for office. 

|                                        Claim                                         |      Result       |                Source Reference                 |                     Source Quote                     |
|--------------------------------------------------------------------------------------|-------------------|-------------------------------------------------|------------------------------------------------------|
|Obama is actually born in Kenya, the country of his father.                           |ResultType.REJECTED|https://www.snopes.com/fact-check/birthing-pains/|World News Daily Report's disclaimer page states that:|
|Obama is not 'a natural-born citizen of the U.S.' and is therefore not fit for office.|ResultType.REJECTED|https://www.snopes.com/fact-check/native-son/    |Status: False.                                        |

> 🤖 Conclusion [0/100]: The statement claiming that Obama was born in Kenya and is therefore not a natural-born citizen of the
> U.S., making him unfit for office, is entirely false. The source from which this claim originates, World News Daily Report,
> has a disclaimer stating that it is not a factual source. Additionally, independent fact-checking by Snopes has explicitly
> rejected both claims, confirming that the statement is baseless and untrue. Therefore, the statement has no truthfulness.


---

> Obama is actually born in Kenya, the country of his father. This means Obama is not "a natural-born citizen of the U.S."\n> and is therefore not fit for office.

    |                                        Claim                                         |      Result       |                Source Reference                 |                                                                                                                                                                        Source Quote                                                                                                                                                                        |
    |--------------------------------------------------------------------------------------|-------------------|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    |Obama is actually born in Kenya, the country of his father.                           |ResultType.REJECTED|https://www.snopes.com/fact-check/birthing-pains/|World News Daily Report\'s disclaimer page states that: World News Daily Report is a news and political satire web publication, which may or may not use real names, often in semi-real or mostly fictitious ways. All news articles contained within worldnewsdailyreport.com are fiction, and presumably fake news.                                        |
    |Obama is not \'a natural-born citizen of the U.S.\' and is therefore not fit for office.|ResultType.VERIFIED|https://www.snopes.com/fact-check/native-son/    |The minimum qualifications for the presidency of the United States specified in Article II of the Constitution are few and seemingly straightforward: In order to be President, a person must be a natural-born citizen of the United States, must be at least thirty-five years old, and must have been a resident of the United States for fourteen years.|

