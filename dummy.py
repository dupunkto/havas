import os
from datetime import datetime
import requests

from flask import current_app

from app import app
from db.models import db, Article
from db.media import media_bp
from manager.manager import build_HTML

with app.app_context():
    db.create_all()

    articles = [
        Article(
            title="Government Announces New Economic Stimulus Plan",
            description="The administration unveils a $250 billion package to support small businesses and infrastructure development.",
            content="""
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
            html="",
            authors=["Jane Smith"],
            tags=["politics"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy1",
        ),
        Article(
            title="International Community Responds to Escalating Conflict",
            description="World leaders call for ceasefire as violence intensifies between rival factions.",
            content="""
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
            html="",
            authors=["Ahmed Khan"],
            tags=["world"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy2",
        ),
        Article(
            title="Major Tech Firm Announces Breakthrough in AI Safety Research",
            description="Company reveals new tools designed to improve transparency and reduce risks in large language models.",
            content="""
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
            html="",
            authors=["Laura Chen"],
            tags=["technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy3",
        ),
        Article(
            title="Health Authorities Warn of Rising Respiratory Infections",
            description="Public health agencies report a surge in respiratory illnesses as winter approaches.",
            content="""
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
            html="",
            authors=["Dr. Samuel Lee"],
            tags=["health"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy4",
        ),
        Article(
            title="Education Reform Bill Passes Amid Heated Debate",
            description="Lawmakers approve new standards and funding increases for public schools.",
            content="""
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
            html="",
            authors=["Michael Torres"],
            tags=["politics"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy4",
        ),
        Article(
            title="Climate Change Impact on Global Agriculture",
            description="Scientists warn of drastic changes in crop yields due to shifting weather patterns.",
            content="""
Recent studies reveal that **climate change is altering global agricultural patterns**, potentially reducing crop yields in many regions.

> "Farmers must adapt quickly to unpredictable weather," said Dr. Emily Rogers, a leading climatologist.

### Effects Observed So Far
- Increased frequency of droughts
- Flooding in low-lying farmland
- Shift in growing seasons

#### Regional Impacts

| Region        | Impact                   | Adaptation Measures           |
|---------------|--------------------------|-------------------------------|
| North America | Longer drought periods   | Drought-resistant crops       |
| Asia          | Increased monsoons       | Improved drainage systems     |
| Africa        | Desertification          | Soil conservation techniques  |

Farmers and policymakers are exploring sustainable farming techniques to mitigate these effects.

For more info, visit [IPCC Agriculture Report](https://www.ipcc.ch/srccl/chapter/chapter-5/).

![Crop Field](https://picsum.photos/seed/cropfield/800/400)
""",
            html="",  # Assuming your app generates HTML from markdown
            authors=["Emily Rogers"],
            tags=["environment"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy5",
        ),
        Article(
            title="Exploring the Depths: New Oceanic Discoveries",
            description="Marine biologists uncover previously unknown species in the Mariana Trench.",
            content="""
The latest expedition to the Mariana Trench has uncovered **several new marine species** that thrive in extreme conditions.

> "These discoveries challenge our understanding of life in deep ocean environments," said expedition leader Dr. Carlos Medina.

### Notable Finds
- Bioluminescent jellyfish with unique patterns
- A species of crab adapted to high pressure
- Deep-sea corals previously thought extinct

The team used **state-of-the-art submersibles** equipped with cameras and sampling tools to document the findings.

#### Expedition Timeline
1. Departure from port: June 1st
2. Descent to trench bottom: June 10th
3. Sample collection: June 11-15th
4. Return to surface: June 20th

Marine biology enthusiasts can follow the expedition blog [here](http://oceanexplorers.example.com).

![Deep Sea Submersible](https://picsum.photos/seed/submersible/800/400)
""",
            html="",
            authors=["Carlos Medina"],
            tags=["science"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy6",
        ),
        Article(
            title="The Rise of Electric Vehicles in Urban Transport",
            description="How electric cars and bikes are transforming city commuting worldwide.",
            content="""
Urban centers worldwide are seeing a **significant increase in electric vehicle (EV) adoption** as cities aim to reduce emissions and traffic congestion.

> "Electric vehicles are the future of clean urban mobility," said transportation expert Linda Park.

### Benefits of EVs
- Zero tailpipe emissions
- Lower operating costs
- Quiet and smooth driving experience

#### Challenges Ahead
- Charging infrastructure expansion
- Battery recycling and disposal
- Initial purchase costs

**Statistics:**

| Year | EVs Sold Globally | % Increase YoY |
|-------|-------------------|---------------|
| 2020  | 2 million         | —             |
| 2023  | 10 million        | 50%           |

Cities are also promoting electric bikes and scooters, integrating them into public transport networks.

Learn more about sustainable transport at [Global EV Outlook](https://www.iea.org/reports/global-ev-outlook-2023).

![Electric Vehicles](https://picsum.photos/seed/ev/800/400)
""",
            html="",
            authors=["Linda Park"],
            tags=["technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy7",
        ),
        Article(
            title="Advancements in Space Tourism",
            description="Private companies push the boundaries of commercial space travel.",
            content="""
The space tourism industry has accelerated, with multiple private companies offering **commercial flights beyond Earth's atmosphere**.

> "We are entering a new era where space travel is accessible to civilians," said CEO of SpaceXplorer Inc.

### Milestones Reached
- First all-civilian orbital flight completed
- Development of space hotels underway
- Reduced costs through reusable rockets

#### Experience Highlights
- Zero-gravity environments
- Stunning Earth views from orbit
- Educational sessions with astronauts

The sector faces regulatory and safety challenges but continues to attract enthusiastic investors and tourists.

Interested in booking a trip? Check [Space Tourism Association](https://spacetourism.org).

![Space Tourism](https://picsum.photos/seed/spacetourism/800/400)
""",
            html="",
            authors=["Anita Kumar"],
            tags=["science"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy8",
        ),
        Article(
            title="Culinary Trends: The Rise of Plant-Based Diets",
            description="How plant-based eating is reshaping the global food industry.",
            content="""
Plant-based diets are becoming increasingly popular for health, ethical, and environmental reasons.

> "Switching to plant-based can significantly reduce your carbon footprint," said nutritionist Dr. Mark Taylor.

### Popular Plant-Based Foods
- Tofu and tempeh
- Legume-based meat substitutes
- Plant milks like oat and almond

#### Tips for Transitioning
- Start with meatless Mondays
- Experiment with new recipes
- Focus on whole foods rather than processed

Many restaurants and supermarkets are expanding their plant-based offerings to meet growing demand.

Explore delicious recipes at [Plant-Based Kitchen](https://plantbasedkitchen.example.com).

![Plant-Based Meal](https://picsum.photos/seed/plantbased/800/400)
""",
            html="",
            authors=["Mark Taylor"],
            tags=["lifestyle"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy9",
        ),
    ]

    for article in articles:
        article.html = build_HTML(article.content)
        article.authors = article.authors  # triggers setter
        article.tags = article.tags  # triggers setter
        db.session.add(article)

    db.session.commit()
    print("Inserted dummy articles.")

    def download_images(amount):
        url = "https://picsum.photos/1920/1080"
        for i in range(amount):
            name = f"dummy{i + 1}"

            image_dir = os.path.join(
                current_app.root_path, media_bp.static_folder, "images"
            )

            image_path = os.path.join(image_dir, f"{name}.jpg")

            os.makedirs(image_dir, exist_ok=True)

            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                with open(image_path, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded: {image_path}")
            except requests.RequestException as e:
                print(f"Failed to download {image_path} from {url}: {e}")

    download_images(len(articles))
