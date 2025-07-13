from datetime import datetime
from db.models import db, Article
from app import app

with app.app_context():
    db.create_all()

    articles = [
        Article(
            title="Government Announces New Economic Stimulus Plan",
            description="The administration unveils a $250 billion package to support small businesses and infrastructure development.",
            content="""
## Government Announces New Economic Stimulus Plan

The federal government has unveiled a **$250 billion economic stimulus package** aimed at revitalizing the economy after months of sluggish growth. The plan includes substantial investments in infrastructure, targeted tax credits for small businesses, and funding to improve public transportation networks.

> "We are committed to creating jobs, supporting local businesses, and modernizing our nation's infrastructure," said the finance minister during a press conference in the capital.

Analysts note that the stimulus could boost GDP growth by up to 1.5% over the next year. Critics, however, argue that the plan risks adding to the national debt without addressing underlying structural issues. The government insists the debt burden remains sustainable.

### Key Measures
- $100 billion for roads, bridges, and transit systems
- $75 billion in small business loans and grants
- Tax incentives for renewable energy projects
- Expansion of workforce training programs

Economists are divided on the long-term effects but broadly welcome the short-term relief for struggling sectors.
""",
            html="""
<h2>Government Announces New Economic Stimulus Plan</h2>
<p>The federal government has unveiled a <strong>$250 billion economic stimulus package</strong> aimed at revitalizing the economy after months of sluggish growth. The plan includes substantial investments in infrastructure, targeted tax credits for small businesses, and funding to improve public transportation networks.</p>
<blockquote>"We are committed to creating jobs, supporting local businesses, and modernizing our nation's infrastructure," said the finance minister during a press conference in the capital.</blockquote>
<p>Analysts note that the stimulus could boost GDP growth by up to 1.5% over the next year. Critics, however, argue that the plan risks adding to the national debt without addressing underlying structural issues. The government insists the debt burden remains sustainable.</p>
<h3>Key Measures</h3>
<ul>
<li>$100 billion for roads, bridges, and transit systems</li>
<li>$75 billion in small business loans and grants</li>
<li>Tax incentives for renewable energy projects</li>
<li>Expansion of workforce training programs</li>
</ul>
<p>Economists are divided on the long-term effects but broadly welcome the short-term relief for struggling sectors.</p>
""",
            authors=["Jane Smith"],
            tags=["economy", "politics"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="123",
        ),
        Article(
            title="International Community Responds to Escalating Conflict",
            description="World leaders call for ceasefire as violence intensifies between rival factions.",
            content="""
## International Community Responds to Escalating Conflict

World leaders have urged an **immediate ceasefire** in the wake of escalating violence between rival factions in the region. The conflict, which has displaced over 200,000 civilians in recent weeks, has drawn condemnation from the United Nations and neighboring countries.

UN Secretary-General António Guterres called the situation "deeply troubling" and emphasized the need for humanitarian corridors to allow aid agencies to deliver critical supplies.

> "We cannot stand by while innocent lives are lost," he said in an emergency session.

Diplomatic talks have stalled, with both sides accusing the other of violating previous agreements. Meanwhile, international NGOs warn of a looming humanitarian crisis if the fighting continues.

### Key Developments
- Over 500 confirmed civilian casualties
- Major cities experiencing power and water shortages
- Border nations preparing for refugee influx
- Ongoing negotiations mediated by neutral states

Observers say the international community faces significant challenges in brokering a sustainable peace deal.
""",
            html="""
<h2>International Community Responds to Escalating Conflict</h2>
<p>World leaders have urged an <strong>immediate ceasefire</strong> in the wake of escalating violence between rival factions in the region. The conflict, which has displaced over 200,000 civilians in recent weeks, has drawn condemnation from the United Nations and neighboring countries.</p>
<p>UN Secretary-General António Guterres called the situation "deeply troubling" and emphasized the need for humanitarian corridors to allow aid agencies to deliver critical supplies.</p>
<blockquote>"We cannot stand by while innocent lives are lost," he said in an emergency session.</blockquote>
<p>Diplomatic talks have stalled, with both sides accusing the other of violating previous agreements. Meanwhile, international NGOs warn of a looming humanitarian crisis if the fighting continues.</p>
<h3>Key Developments</h3>
<ul>
<li>Over 500 confirmed civilian casualties</li>
<li>Major cities experiencing power and water shortages</li>
<li>Border nations preparing for refugee influx</li>
<li>Ongoing negotiations mediated by neutral states</li>
</ul>
<p>Observers say the international community faces significant challenges in brokering a sustainable peace deal.</p>
""",
            authors=["Ahmed Khan"],
            tags=["world", "conflict"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="123",
        ),
        Article(
            title="Major Tech Firm Announces Breakthrough in AI Safety Research",
            description="Company reveals new tools designed to improve transparency and reduce risks in large language models.",
            content="""
## Major Tech Firm Announces Breakthrough in AI Safety Research

One of the world's leading technology companies has unveiled **new research aimed at making large language models safer and more transparent**. At a conference yesterday, the firm demonstrated tools that help users better understand how AI systems generate responses and identify potentially harmful outputs.

> "AI has tremendous potential, but we must ensure it's developed responsibly," said the company's Chief AI Scientist.

The new suite includes explainability dashboards, red-teaming frameworks for stress-testing models, and policy guidance for developers. Critics argue these tools, while a step forward, may not go far enough to mitigate misuse.

### Highlights of the Announcement
- Open-source auditing tools for AI models
- Improved detection of biased or unsafe content
- Partnerships with universities for ethics research
- Commitments to align AI development with human values

Industry observers see the move as part of broader efforts to win public trust and respond to regulatory scrutiny. The firm plans to release its tools in phases over the next year.
""",
            html="""
<h2>Major Tech Firm Announces Breakthrough in AI Safety Research</h2>
<p>One of the world's leading technology companies has unveiled <strong>new research aimed at making large language models safer and more transparent</strong>. At a conference yesterday, the firm demonstrated tools that help users better understand how AI systems generate responses and identify potentially harmful outputs.</p>
<blockquote>"AI has tremendous potential, but we must ensure it's developed responsibly," said the company's Chief AI Scientist.</blockquote>
<p>The new suite includes explainability dashboards, red-teaming frameworks for stress-testing models, and policy guidance for developers. Critics argue these tools, while a step forward, may not go far enough to mitigate misuse.</p>
<h3>Highlights of the Announcement</h3>
<ul>
<li>Open-source auditing tools for AI models</li>
<li>Improved detection of biased or unsafe content</li>
<li>Partnerships with universities for ethics research</li>
<li>Commitments to align AI development with human values</li>
</ul>
<p>Industry observers see the move as part of broader efforts to win public trust and respond to regulatory scrutiny. The firm plans to release its tools in phases over the next year.</p>
""",
            authors=["Laura Chen"],
            tags=["technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="123",
        ),
        Article(
            title="Health Authorities Warn of Rising Respiratory Infections",
            description="Public health agencies report a surge in respiratory illnesses as winter approaches.",
            content="""
## Health Authorities Warn of Rising Respiratory Infections

Public health officials have issued a **warning about rising cases of respiratory infections** as colder weather sets in. Hospitals are seeing increased admissions for influenza, RSV, and COVID-19, prompting calls for renewed vigilance.

> "We are urging everyone to get vaccinated where possible and practice basic preventive measures," said the national health director.

Hospitals in major cities report higher occupancy rates, with some reactivating emergency surge plans. Pharmacies have also seen elevated demand for antiviral medications and over-the-counter symptom relief.

### Recommended Precautions
- Get vaccinated against flu and COVID-19
- Wash hands regularly
- Stay home if experiencing symptoms
- Wear masks in crowded indoor settings

Health agencies emphasize that vulnerable populations, including the elderly and immunocompromised, face the highest risk. Officials say they are working to expand access to testing and treatments ahead of peak winter months.
""",
            html="""
<h2>Health Authorities Warn of Rising Respiratory Infections</h2>
<p>Public health officials have issued a <strong>warning about rising cases of respiratory infections</strong> as colder weather sets in. Hospitals are seeing increased admissions for influenza, RSV, and COVID-19, prompting calls for renewed vigilance.</p>
<blockquote>"We are urging everyone to get vaccinated where possible and practice basic preventive measures," said the national health director.</blockquote>
<p>Hospitals in major cities report higher occupancy rates, with some reactivating emergency surge plans. Pharmacies have also seen elevated demand for antiviral medications and over-the-counter symptom relief.</p>
<h3>Recommended Precautions</h3>
<ul>
<li>Get vaccinated against flu and COVID-19</li>
<li>Wash hands regularly</li>
<li>Stay home if experiencing symptoms</li>
<li>Wear masks in crowded indoor settings</li>
</ul>
<p>Health agencies emphasize that vulnerable populations, including the elderly and immunocompromised, face the highest risk. Officials say they are working to expand access to testing and treatments ahead of peak winter months.</p>
""",
            authors=["Dr. Samuel Lee"],
            tags=["health", "society"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="123",
        ),
        Article(
            title="Education Reform Bill Passes Amid Heated Debate",
            description="Lawmakers approve new standards and funding increases for public schools.",
            content="""
## Education Reform Bill Passes Amid Heated Debate

After weeks of contentious debate, lawmakers have passed a sweeping **education reform bill** that aims to raise academic standards and increase funding for under-resourced schools. The bill passed narrowly in the lower chamber before gaining enough support in the upper house.

> "This legislation will help close achievement gaps and ensure every child has access to quality education," said the education minister.

The reform package includes higher minimum teacher salaries, curriculum modernization, and expanded support for special education. Opponents argue the bill fails to address administrative inefficiencies and risks imposing unfunded mandates on local districts.

### Main Provisions
- $15 billion in new education funding over 5 years
- Teacher salary floor raised by 20%
- New national curriculum guidelines
- Grants for special education services

Education unions largely support the reforms, though some have called for further negotiations on implementation details. The bill now awaits the president's signature.
""",
            html="""
<h2>Education Reform Bill Passes Amid Heated Debate</h2>
<p>After weeks of contentious debate, lawmakers have passed a sweeping <strong>education reform bill</strong> that aims to raise academic standards and increase funding for under-resourced schools. The bill passed narrowly in the lower chamber before gaining enough support in the upper house.</p>
<blockquote>"This legislation will help close achievement gaps and ensure every child has access to quality education," said the education minister.</blockquote>
<p>The reform package includes higher minimum teacher salaries, curriculum modernization, and expanded support for special education. Opponents argue the bill fails to address administrative inefficiencies and risks imposing unfunded mandates on local districts.</p>
<h3>Main Provisions</h3>
<ul>
<li>$15 billion in new education funding over 5 years</li>
<li>Teacher salary floor raised by 20%</li>
<li>New national curriculum guidelines</li>
<li>Grants for special education services</li>
</ul>
<p>Education unions largely support the reforms, though some have called for further negotiations on implementation details. The bill now awaits the president's signature.</p>
""",
            authors=["Michael Torres"],
            tags=["politics", "society"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="123",
        ),
    ]

    for article in articles:
        article.authors = article.authors  # triggers setter
        article.tags = article.tags  # triggers setter
        db.session.add(article)

    db.session.commit()
    print("Inserted dummy articles.")
