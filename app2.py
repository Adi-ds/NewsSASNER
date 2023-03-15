from flask import Flask, jsonify

company_type = 'Product Based'

headline = "Apple (AAPL) Outpaces Stock Market Gains: What You Should Know"

news = "Apple (AAPL) closed the most recent trading day at $153.83, moving +1.85% from the previous trading session. This move outpaced the S&P 500's daily gain of 0.07%. At the same time, the Dow added 0.12%, and the tech-heavy Nasdaq lost 1.47%.Heading into today, shares of the maker of iPhones, iPads and other products had lost 2.25% over the past month, outpacing the Computer and Technology sector's loss of 3.15% and lagging the S&P 500's loss of 2% in that time.Investors will be hoping for strength from Apple as it approaches its next earnings release. In that report, analysts expect Apple to post earnings of $1.44 per share. This would mark a year-over-year decline of 5.26%. Our most recent consensus estimate is calling for quarterly revenue of $93.35 billion, down 4.04% from the year-ago period.Looking at the full year, our Zacks Consensus Estimates suggest analysts are expecting earnings of $6.04 per share and revenue of $392.12 billion. These totals would mark changes of -1.15% and -0.56%, respectively, from last year.Investors should also note any recent changes to analyst estimates for Apple. These revisions help to show the ever-changing nature of near-term business trends. As such, positive estimate revisions reflect analyst optimism about the company's business and profitability.Our research shows that these estimate changes are directly correlated with near-term stock prices. Investors can capitalize on this by using the Zacks Rank. This model considers these estimate changes and provides a simple, actionable rating system.The Zacks Rank system, which ranges from #1 (Strong Buy) to #5 (Strong Sell), has an impressive outside-audited track record of outperformance, with #1 stocks generating an average annual return of +25% since 1988. Over the past month, the Zacks Consensus EPS estimate has moved 1.7% lower. Apple is currently sporting a Zacks Rank of #3 (Hold).Investors should also note Apple's current valuation metrics, including its Forward P/E ratio of 24.99. Its industry sports an average Forward P/E of 8.7, so we one might conclude that Apple is trading at a premium comparatively.Story continuesWe can also see that AAPL currently has a PEG ratio of 2. The PEG ratio is similar to the widely-used P/E ratio, but this metric also takes the company's expected earnings growth rate into account. AAPL's industry had an average PEG ratio of 2.59 as of yesterday's close.The Computer - Mini computers industry is part of the Computer and Technology sector. This industry currently has a Zacks Industry Rank of 187, which puts it in the bottom 26% of all 250+ industries.The Zacks Industry Rank includes is listed in order from best to worst in terms of the average Zacks Rank of the individual companies within each of these sectors. Our research shows that the top 50% rated industries outperform the bottom half by a factor of 2 to 1.Make sure to utilize Zacks.com to follow all of these stock-moving metrics, and more, in the coming trading sessions.Want the latest recommendations from Zacks Investment Research? Today, you can download 7 Best Stocks for the Next 30 Days. Click to get this free reportApple Inc. (AAPL) : Free Stock Analysis ReportTo read this article on Zacks.com click here.Zacks Investment Research"

entities = "Apple (AAPL): Company \nS&P 500: US Stock Market Index \nDow: US Stock Market Index \nNasdaq: US Stock Market Index \nComputer and Technology sector: Industry \nZacks Rank: System \nZacks Investment Research: Company"

summary = "Apple Inc. (AAPL) closed the most recent trading day at $153.83, up 1.85% from the previous trading session. This move surpassed the S&P 500’s daily gain of 0.07%. Despite this, Apple had lost 2.25% over the past month, lagging the Computer and Technology sector’s loss of 3.15% and the S&P 500’s loss of 2%. Analysts expect Apple to post earnings of $1.44 per share and quarterly revenue of $93.35 billion in its next earnings report. The Zacks Consensus Estimates suggest analysts are expecting full-year earnings of $6.04 per share and revenue of $392.12 billion. Apple's P/E ratio is 24.99 and its PEG ratio is 2. Its industry has an average PEG ratio of 2.59. The Computer - Mini computers industry is part of the Computer and Technology sector and has a Zacks Industry Rank of 187, which puts it in the bottom 26% of all 250+ industries. Apple has a Zacks Rank of 3 (Hold)."

aspects="Positive:\n- Apple's stock price has outperformed the S&P 500 and Dow \n- Analysts expect Apple to post earnings of $1.44 per share \n- Analysts expect earnings of $6.04 per share and revenue of $392.12 billion \n- Positive estimate revisions reflect analyst optimism \n- Apple has a Zacks Rank of #3 (Hold) \n- Apple has a Forward P/E ratio of 24.99 compared to the industry average of 8.7 \n- Apple has a PEG ratio of 2 compared to the industry average of 2.59 \n\n\nNeutral:\n- Apple's stock price has declined 2.25% over the past month \n- The Computer and Technology sector has lost 3.15% in that time \n- The Zacks Consensus EPS estimate has moved 1.7% lower \n\n\nNegative:\n- Year-over-year earnings are expected to decline by 5.26% \n- Year-over-year revenue is expected to decline by 0.56% \n- Apple is in the bottom 26% of all 250+ industries"

sentiment = "Positive"

sentiment_reason = "The sentiment of the text is positive because it focuses on the gains Apple (AAPL) has made, as well as the potential for future gains. It also highlights the potential of the stock to outperform the market and its peers, which could be viewed as a positive sign for potential investors."


link_0 = [company_type, headline, news, entities, summary, aspects, sentiment, sentiment_reason]
analysis_order = ['company_type', 'headline', 'news', 'entities', 'summary', 'aspects', 'sentiment', 'sentiment_reason']

def make_entities_dict(entities):
    entities_dict = {}
    for entity in entities.split('\n'):
        entity_name = entity.split(':')[0].strip(' ')
        entity_type = entity.split(':')[1].strip(' ')
        entities_dict[entity_name]=entity_type
    return entities_dict

def make_aspect_dict(aspects):
    aspect_dict = {}
    for aspect in aspects.split('\n\n'):
        aspect_type = aspect.split(':')[0].strip('\n')
        aspect_opinion = aspect.split(':')[1]
        aspect_dict[aspect_type] = aspect_opinion.replace('\n','').split('- ')
    return aspect_dict

analysis = {}
for element,key_name in zip(link_0,analysis_order):
    if key_name == 'entities':
        analysis[key_name]=make_entities_dict(element)
    elif key_name == 'aspects':
        analysis[key_name]=make_aspect_dict(aspects)
    else:
        analysis[key_name]=element

collected_news = {}
collected_news['News_0'] = analysis


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'Get Ticker':'Enter the Ticker'})

@app.route('/<ticker>', methods = ['GET'])
def get_news(ticker):
    return jsonify({'Collected News':collected_news})

if __name__ == '__main__':
    app.run(debug = True)