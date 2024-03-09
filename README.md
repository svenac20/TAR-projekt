# TAR-projekt

Project for subject Text analysis and retreival.
Topic for the project is **Stress Analysis in Social media**

Final research paper can be found at: <https://github.com/svenac20/TAR-projekt/blob/main/paper/paper.pdf>

## Other realted papers

Attention-based LSTM for psychological stress detection from spoken language using distant supervision: <https://arxiv.org/abs/1805.12307>

## Dreaddit dataset

Dataset is dated between January 1, 2017 and November 19, 2018
Puts social media posts in 5 categories:
  1. Abuse
  2. Anxiety
  3. Financial
  4. PTSD
  5. Social

Stress is defined as something negative (possitive stress isn't considered as stress in this case). Data was labelled using Amazon Mechanical Turk and each person is given a paragraph of **5 sentences** (to give some context about the situation so that the annotators can decide on the labelling of the given text)

Dataset is devided in 2 subsets:
  - train (2838), 51.6% labeled stresfull
  - test(715), 52.4% labeled stresfull

## Data analysis

### **Domain**

LIWC word list is used to measure the % of words from specific lists that appear in our categories.
Word lists include 
  - **"negemo"** (negative emotions),
  - **"social"**,
  - **"anxiety"**.

We can clearly see the difference between the coverage of, for example, *negemo* word list in the financial and the anxiety category.

High coverage of *anxiety* word list

### **Label**

Data is labelled:
  - stressful - more first-person pronouns (self-focus)
  - non-stressful - more social words (social support network)

### **Agreement**

Less lexical variety yields higher agreement between annotators

### **Dataset features**

Lexical features
  - AVG, MAX, MIN scores for pleasantness, activation and imagery 
  - sentiment score

Syntactic features
  - POS unigrams and bigrams
  - Flesch-Kincaid Grade Level - istraziti
  - Automated Readbility Index - istraziti

Social media features
  - UTC timestamp of post (not really useful)
  - Ratio of upvotes/downvotes on post
  - total number of comments

## Results

In this paper we looked at different approaches for detecting stress from the Dreaddit dataset. We continued our research on findings of the authors and tried to find out if more complex models and solutions gave better results.

We believe that the simple model solves this problem well enough and that more complex and expensive transformer solutions are not worth the extra cost. In some rare cases, where not detecting stress could pose a problem, we can suggest trying the Chat GPT API service if the demand is not high and the budget is not limited. Transformers may be a better option if we just look at their capabilities, but at what cost? Sometimes the simpler solution gets the job done and we should stick to it.
