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
            title="Breakthrough Study Reveals New Insights into Alzheimer's Disease",
            description="Scientists identify key molecular pathways linked to disease progression.",
            content="""
A recent study has uncovered **novel molecular mechanisms** that contribute to the development of Alzheimer's disease, offering hope for new therapeutic targets.

> "Understanding these pathways opens doors for more effective treatments," commented lead researcher Dr. James Wu.

The research, conducted over five years, employed advanced imaging and genetic analysis techniques. Results highlight the role of neuroinflammation and protein aggregation in cognitive decline.

Clinical trials based on these findings are expected to commence within the next two years.
""",
            html="",
            authors=["James Wu"],
            tags=["health", "science"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy1",
        ),
        Article(
            title="Global Supply Chains Adjust to Geopolitical Tensions",
            description="Companies restructure operations amid increasing international uncertainty.",
            content="""
Recent geopolitical developments have prompted businesses to **reassess and diversify global supply chains** to mitigate risk.

> "Flexibility and local sourcing are now strategic priorities," explained logistics analyst Mark Patel.

Manufacturers are investing in nearshoring and stockpiling critical components to reduce exposure. Trade policies and tariffs continue to influence corporate decisions.

The shift is expected to reshape global trade patterns in the coming decade.
""",
            html="",
            authors=["Mark Patel"],
            tags=["economy", "politics"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy2",
        ),
        Article(
            title="Breakthrough in Quantum Computing Performance",
            description="Researchers achieve new milestones in qubit coherence and error rates.",
            content="""
Quantum computing research has made significant strides with a new experimental system achieving longer qubit coherence times and reduced error rates.

> "These improvements bring us closer to practical quantum advantage," said physicist Dr. Elena Petrova.

The technology leverages novel materials and cooling methods to stabilize fragile quantum states. Industry and academic partnerships are accelerating development.

Applications range from cryptography to complex simulations, promising transformative impacts.
""",
            html="",
            authors=["Elena Petrova"],
            tags=["technology", "science"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy3",
        ),
        Article(
            title="Renewed Focus on Mental Health in Workplace Policies",
            description="Employers implement programs to support employee wellbeing and productivity.",
            content="""
Workplace mental health has gained renewed attention as companies introduce **comprehensive wellbeing initiatives** to support their staff.

> "Supporting mental health improves overall organizational resilience," noted HR expert Olivia Grant.

Programs include counseling services, flexible schedules, and stress management training. Employers report benefits such as reduced absenteeism and higher engagement.

Legislators are also exploring regulations to promote mental health in professional environments.
""",
            html="",
            authors=["Olivia Grant"],
            tags=["health", "lifestyle"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy4",
        ),
        Article(
            title="Breakthroughs in Crop Engineering Boost Food Security",
            description="Scientists develop drought-resistant and nutrient-enhanced crops.",
            content="""
Agricultural biotechnology has delivered promising **crop engineering advances** that address challenges posed by climate change and population growth.

> "These crops can thrive in harsher conditions and improve nutritional outcomes," said agronomist Dr. Ahmed Farouk.

The innovations include gene-editing techniques that enhance water efficiency and vitamin content. Field trials show significant yield improvements.

Stakeholders emphasize the importance of regulatory frameworks to ensure safety and acceptance.
""",
            html="",
            authors=["Ahmed Farouk"],
            tags=["science", "environment"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy5",
        ),
        Article(
            title="Advances in Autonomous Vehicle Technology",
            description="New sensors and AI algorithms improve safety and navigation capabilities.",
            content="""
Autonomous vehicle developers have announced breakthroughs in sensor integration and artificial intelligence, enabling safer and more reliable self-driving cars.

> "Our latest models can better interpret complex urban environments," said company CTO Lisa Huang.

Enhanced machine learning algorithms allow vehicles to predict pedestrian movements and navigate obstacles. Safety testing continues, with regulators evaluating deployment timelines.

Industry leaders remain optimistic about achieving full autonomy within the next five years.
""",
            html="",
            authors=["Lisa Huang"],
            tags=["technology", "transportation"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy6",
        ),
        Article(
            title="New Study Links Urban Green Spaces to Improved Mental Health",
            description="Researchers find significant psychological benefits from access to parks and nature.",
            content="""
A comprehensive study has established a strong correlation between **urban green spaces** and improved mental health outcomes among city residents.

> "Access to nature reduces stress and promotes wellbeing," said lead researcher Dr. Kevin Moore.

The research analyzed data across multiple cities and demographic groups, highlighting benefits such as lower anxiety and depression rates. Urban planners are encouraged to integrate more green areas in city designs.

Community initiatives aim to increase public engagement with natural environments.
""",
            html="",
            authors=["Kevin Moore"],
            tags=["health", "environment"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy7",
        ),
        Article(
            title="Financial Technology Startups Drive Inclusion in Banking",
            description="Innovative platforms provide underserved populations with access to financial services.",
            content="""
Fintech startups are expanding financial inclusion by offering **affordable and accessible banking solutions** to previously underserved communities.

> "Digital platforms are breaking down barriers to credit and savings," stated entrepreneur Maya Johnson.

Mobile banking apps, microloans, and digital wallets are among the tools driving this change. Partnerships with traditional banks and regulators help scale offerings.

Experts predict continued growth in inclusive finance globally.
""",
            html="",
            authors=["Maya Johnson"],
            tags=["technology", "economy"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy8",
        ),
        Article(
            title="New Regulations Target Carbon Emissions from Shipping Industry",
            description="International bodies adopt stricter standards to reduce maritime pollution.",
            content="""
Global maritime regulators have implemented **new carbon emissions standards** aiming to curb pollution from shipping vessels.

> "The shipping industry must contribute to climate goals," said IMO secretary-general Kitack Lim.

The regulations mandate cleaner fuels, improved vessel efficiency, and emissions monitoring. Shipping companies face increasing pressure to comply or risk penalties.

This initiative represents a significant step toward sustainable global logistics.
""",
            html="",
            authors=["Kitack Lim"],
            tags=["environment", "politics"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy9",
        ),
        Article(
            title="New Cybersecurity Protocols Mandated for Public Institutions",
            description="Government introduces updated digital security standards following surge in attacks.",
            content="""
Following a string of high-profile data breaches, the federal government has announced a **new cybersecurity directive** for all public institutions. 

> "No agency should operate on legacy protocols in 2025," said the Chief Information Security Officer during a joint press briefing.

The new measures include mandatory two-factor authentication, quarterly penetration testing, and encrypted communications across all departments.

Institutions are expected to comply within six months. Non-compliant agencies may face operational audits and potential funding freezes.
""",
            html="",
            authors=["Natalie Dunn"],
            tags=["technology", "politics"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy10",
        ),
        Article(
            title="UN Panel Urges Global Restrictions on Autonomous Weapon Systems",
            description="Concerns over AI-led military systems prompt fresh international talks.",
            content="""
A UN special panel has called for **binding international agreements** to restrict the deployment of autonomous weapons. Delegates warned of the risks posed by machine-led decisions in active combat zones.

> "The speed of technological advancement outpaces our legal frameworks," stated rapporteur Hans Keller.

Discussions remain stalled as major military powers resist formal limitations, citing national security and strategic deterrence.
""",
            html="",
            authors=["Hans Keller"],
            tags=["world", "technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy11",
        ),
        Article(
            title="Breakthrough Therapy Offers New Hope for Alzheimer's Patients",
            description="Researchers unveil promising results in early clinical trials.",
            content="""
A team of neurologists has reported **significant cognitive improvements** in early-stage Alzheimer's patients using a novel monoclonal antibody treatment.

> "This may represent a new era in neurodegenerative care," said Dr. Julia Simmons.

The therapy, which targets beta-amyloid deposits, showed a 30% reduction in cognitive decline markers over a 12-month period.

Regulatory approval is pending further Phase III trial data expected later this year.
""",
            html="",
            authors=["Dr. Julia Simmons"],
            tags=["health"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy12",
        ),
        Article(
            title="Trade Bloc Finalizes New Digital Services Agreement",
            description="Landmark deal introduces shared standards for online platforms.",
            content="""
The Pan-Pacific Trade Bloc has signed a **Digital Services Framework Agreement**, standardizing data transparency and platform liability across member states.

> "This is a major win for consumer protection and cross-border interoperability," said trade commissioner Elena Kwok.

Key provisions include universal takedown mechanisms, content moderation transparency, and digital rights portability. Implementation begins in Q1 next year.
""",
            html="",
            authors=["Elena Kwok"],
            tags=["politics"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy13",
        ),
        Article(
            title="Drought Forces Rethink of European Water Infrastructure",
            description="Persistent water scarcity accelerates infrastructure reforms.",
            content="""
With large parts of southern Europe entering their third consecutive year of drought, governments are investing in **adaptive water infrastructure** and policy reform.

> "We're not just reacting anymore — we're redesigning," said EU climate coordinator Maria Leone.

Projects underway include closed-loop desalination plants, greywater recovery systems, and precision irrigation subsidies.
""",
            html="",
            authors=["Maria Leone"],
            tags=["environment"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy14",
        ),
        Article(
            title="Surge in Global Shipping Costs Sparks Inflation Concerns",
            description="Container rates reach highest levels since pandemic recovery.",
            content="""
International shipping rates have surged by over 40% this quarter, with analysts pointing to **bottlenecks at major ports** and rising fuel prices as primary drivers.

> "We're seeing a repeat of 2021 congestion patterns, minus the buffer stock," said logistics economist Ray Singh.

Central banks are monitoring the impact on core inflation indicators, particularly in food and electronics.
""",
            html="",
            authors=["Ray Singh"],
            tags=["economy"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy15",
        ),
        Article(
            title="High Court Rejects Facial Recognition Ban Appeal",
            description="Landmark ruling allows continued police use of AI surveillance.",
            content="""
In a 5-4 decision, the Supreme Judicial Council ruled that **facial recognition software does not violate constitutional privacy protections** when used under warrant.

> "The burden of proof for misuse still lies with the state," wrote Chief Justice Thompson in the majority opinion.

Civil liberties groups say the ruling sets a troubling precedent and have pledged to pursue legislative reform.
""",
            html="",
            authors=["Clara Jung"],
            tags=["politics", "technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy16",
        ),
        Article(
            title="Youth Smoking Rates Hit Historic Lows",
            description="Public health campaigns show significant progress.",
            content="""
A new health ministry report reveals that **youth smoking has declined by over 70%** in the past decade, marking the lowest rate since records began.

> "Years of targeted awareness campaigns and taxation are paying off," said Deputy Health Secretary Rachel Lin.

E-cigarette use remains stable, however, prompting renewed calls for stricter age verification on online sales.
""",
            html="",
            authors=["Rachel Lin"],
            tags=["health"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy17",
        ),
        Article(
            title="Cultural Heritage Site Damaged by Unlicensed Drone Activity",
            description="UNESCO condemns recent aerial disturbances over protected zones.",
            content="""
An archaeological site in northern Peru sustained **moderate surface damage** after an unregistered drone crashed into a fragile mosaic area.

> "This is not just careless — it's criminal negligence," said site curator Daniela Ruiz.

The government has pledged to increase patrols and install jamming devices in sensitive regions.
""",
            html="",
            authors=["Daniela Ruiz"],
            tags=["world"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy18",
        ),
        Article(
            title="Major Insurer Launches Climate Risk Coverage for Agriculture",
            description="New product suite addresses volatility in crop yields.",
            content="""
GreenShield Insurance has introduced a **climate-adjusted insurance product** tailored for agribusiness clients facing weather unpredictability.

> "Farmers need protection from volatility they can't control," said CEO Henrik Baas.

Coverage factors in rainfall deficits, heatwave duration, and soil degradation metrics to calculate dynamic premiums.
""",
            html="",
            authors=["Henrik Baas"],
            tags=["environment"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy19",
        ),
        Article(
            title="Private Investment in Fusion Energy Hits Record High",
            description="Venture funding accelerates as technical milestones approach.",
            content="""
Private equity investments in **nuclear fusion startups** have more than doubled year-on-year, surpassing $6 billion globally in 2025.

> "The sector is finally moving from theory to engineering," said energy analyst Priya Ghosh.

Key drivers include stable plasma tests, novel reactor geometries, and rising demand for carbon-free baseload power.
""",
            html="",
            authors=["Priya Ghosh"],
            tags=["technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy20",
        ),
        Article(
            title="Public Broadcasting Network to Transition Fully to Digital",
            description="Legacy FM and analog TV services to phase out by 2027.",
            content="""
The national broadcasting authority has announced that all analog **radio and TV transmissions will end by 2027**, completing the digital migration.

> "The goal is modern, universal access without fragmentation," said PBN director Ilse Wagner.

Audiences are advised to upgrade equipment or access content through official apps and web portals.
""",
            html="",
            authors=["Ilse Wagner"],
            tags=["technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy21",
        ),
        Article(
            title="Foreign Minister Concludes East African Diplomatic Tour",
            description="Talks focused on trade, security, and educational exchange.",
            content="""
The foreign minister has returned from a **ten-day tour across East Africa**, securing bilateral agreements on trade liberalization and student exchange programs.

> "We aim to foster durable partnerships rooted in mutual economic benefit," she said at the closing conference in Nairobi.

Observers called the trip a strategic pivot toward south-south cooperation.
""",
            html="",
            authors=["Amina Bayo"],
            tags=["world"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy22",
        ),
        Article(
            title="AI-Powered Medical Diagnostics Approved for Public Hospitals",
            description="Automated systems to assist in triage and screening workflows.",
            content="""
The Ministry of Health has certified an AI-based diagnostics tool for **deployment in all public hospitals**, following successful pilot trials in urban clinics.

> "This improves access to fast, reliable early diagnosis," said Dr. Johan Mertz, lead of the regulatory review.

The tool assists with X-ray triage, symptom classification, and digital referral routing.
""",
            html="",
            authors=["Dr. Johan Mertz"],
            tags=["health", "technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy23",
        ),
        Article(
            title="New Literacy Campaign Launched in Rural Provinces",
            description="Program aims to close education gaps by 2030.",
            content="""
The Department of Education has launched a **nationwide adult literacy campaign** targeting under-resourced rural districts.

> "Literacy is foundational to every other right and opportunity," said minister Leila Ahmed.

Initiatives include mobile libraries, community-led reading centers, and partnerships with regional universities.
""",
            html="",
            authors=["Leila Ahmed"],
            tags=["politics"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy24",
        ),
        Article(
            title="Global Markets React to Sudden Interest Rate Hike",
            description="Central banks worldwide raise rates unexpectedly to combat inflation.",
            content="""
In an unexpected move, several central banks announced **interest rate hikes** to curb rising inflation. The coordinated action surprised investors and analysts, who had anticipated a more gradual approach.

> "We must take decisive measures to maintain price stability," stated the European Central Bank governor.

Markets reacted sharply with increased volatility; bond yields surged while equities retreated. Analysts warn this could slow economic growth, but many agree inflationary pressures require urgent attention.

Economic indicators will be closely monitored in the coming weeks to assess the impact on consumer spending and business investment.
""",
            html="",
            authors=["Helen Murray"],
            tags=["economy"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy25",
        ),
        Article(
            title="Breakthrough in Renewable Energy Storage Announced",
            description="Researchers develop a new battery technology with unprecedented capacity and lifespan.",
            content="""
A team of scientists has unveiled a **next-generation battery technology** promising to revolutionize renewable energy storage. The innovation could address one of the biggest challenges facing solar and wind power — intermittent supply.

> "Our design significantly extends battery life while increasing energy density," explained lead researcher Dr. Ana Gomez.

The breakthrough involves a novel material that enhances charge cycles and reduces degradation. Experts believe this advancement could accelerate the transition to a low-carbon energy future.

Pilot projects are planned to test scalability in real-world grid systems.
""",
            html="",
            authors=["Ana Gomez"],
            tags=["technology", "environment"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy26",
        ),
        Article(
            title="New Legislation Targets Data Privacy Protections",
            description="Lawmakers introduce sweeping reforms to strengthen user data security online.",
            content="""
In response to growing concerns over data misuse, legislators have proposed **comprehensive data privacy laws** aimed at protecting consumers from unauthorized information sharing.

> "Privacy is a fundamental right in the digital age," stated the bill's sponsor during the hearing.

The reforms include stricter consent requirements, enhanced transparency from companies, and tougher penalties for breaches. Industry groups have expressed reservations about compliance costs, while consumer advocates largely support the measures.

The bill will undergo committee review before a full vote later this year.
""",
            html="",
            authors=["David Kim"],
            tags=["politics", "technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy27",
        ),
        Article(
            title="Innovations in Telemedicine Improve Rural Healthcare Access",
            description="Healthcare providers leverage new technologies to reach underserved populations.",
            content="""
Telemedicine has seen remarkable growth, enabling doctors to provide care remotely, especially in rural areas where access is limited.

> "Digital health tools are closing gaps that have persisted for decades," said Dr. Maria Lopez, director of rural health programs.

Recent advances include AI-powered diagnostics, remote patient monitoring, and expanded broadband connectivity. These technologies reduce travel burdens and improve timely intervention.

Healthcare systems continue to invest in telehealth platforms, ensuring regulatory frameworks keep pace with innovation.
""",
            html="",
            authors=["Maria Lopez"],
            tags=["health", "technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy28",
        ),
        Article(
            title="Urban Planning Strategies Focus on Sustainable Growth",
            description="City governments adopt innovative approaches to balance development and environmental concerns.",
            content="""
Municipalities around the world are embracing **sustainable urban planning** to manage population growth while protecting natural resources.

> "Smart zoning and green infrastructure are key to resilient cities," explained urban planner Jacob Foster.

Efforts include expanding green spaces, promoting public transit, and implementing energy-efficient building codes. Public participation in planning processes is also increasing, ensuring community needs are met.

These strategies aim to reduce carbon footprints and improve quality of life.
""",
            html="",
            authors=["Jacob Foster"],
            tags=["environment", "politics"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy29",
        ),
        Article(
            title="Artificial Intelligence Enhances Fraud Detection in Finance",
            description="Financial institutions deploy AI algorithms to identify and prevent fraudulent activity.",
            content="""
Banks and payment processors are turning to **artificial intelligence** to strengthen fraud detection systems and protect customer assets.

> "Machine learning models can identify subtle patterns that humans might miss," stated fintech expert Sarah Nguyen.

AI-powered systems analyze transaction data in real time, flagging suspicious activity with high accuracy. This technology reduces false positives and improves response times.

The finance sector is investing heavily in AI, balancing innovation with regulatory compliance.
""",
            html="",
            authors=["Sarah Nguyen"],
            tags=["technology", "economy"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy30",
        ),
        Article(
            title="Cultural Heritage Sites Benefit from Digital Preservation",
            description="New techniques allow for virtual access and conservation of historical landmarks.",
            content="""
Advances in 3D scanning and virtual reality are transforming how cultural heritage sites are preserved and experienced.

> "Digitization provides a way to protect and share our history with future generations," remarked archaeologist Dr. Lena Schmidt.

Virtual tours and digital archives enable global audiences to explore landmarks without physical wear and tear. Additionally, these technologies assist in restoration efforts after damage from natural disasters.

Institutions are collaborating to expand digital collections and improve accessibility.
""",
            html="",
            authors=["Lena Schmidt"],
            tags=["science", "culture"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy31",
        ),
        Article(
            title="Advances in Battery Recycling Aim to Reduce E-Waste",
            description="Innovative methods increase efficiency and sustainability of battery material recovery.",
            content="""
With the surge in electric vehicle production, effective **battery recycling** is critical to minimizing environmental impact.

> "Recycling reduces the need for new mining and lowers carbon emissions," explained materials scientist Dr. Tom Becker.

Recent breakthroughs involve chemical and mechanical processes that reclaim lithium, cobalt, and other valuable metals. Companies are scaling pilot programs to commercial levels, hoping to close the circular economy loop.

Government incentives and stricter regulations are accelerating industry adoption.
""",
            html="",
            authors=["Tom Becker"],
            tags=["environment", "technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy32",
        ),
        Article(
            title="Education Technology Expands Opportunities for Lifelong Learning",
            description="Digital platforms enable flexible skill development for adults worldwide.",
            content="""
The rise of **edtech platforms** offers accessible learning options for professionals seeking to upskill or reskill throughout their careers.

> "Continuous education is essential in today's fast-changing job market," said education specialist Karen Liu.

Interactive courses, micro-credentials, and AI-driven personalized learning paths are among the innovations driving this trend. Employers increasingly recognize digital certifications as valid indicators of skills.

This evolution supports workforce adaptability and economic competitiveness.
""",
            html="",
            authors=["Karen Liu"],
            tags=["education", "technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy33",
        ),
        Article(
            title="Innovative Approaches to Plastic Waste Management",
            description="Scientists and policymakers collaborate on sustainable solutions to reduce pollution.",
            content="""
Efforts to address **plastic pollution** have intensified, with innovations ranging from biodegradable materials to advanced recycling technologies.

> "Reducing plastic waste requires systemic changes," said environmental advocate Claire Bennett.

Governments and industry partners are piloting circular economy models and extended producer responsibility schemes. Public awareness campaigns complement technical efforts.

Success depends on coordinated global action and consumer participation.
""",
            html="",
            authors=["Claire Bennett"],
            tags=["environment", "science"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy34",
        ),
        Article(
            title="Breakthrough in Cancer Immunotherapy Shows Promising Results",
            description="Clinical trials demonstrate enhanced efficacy and reduced side effects.",
            content="""
New cancer immunotherapy treatments have achieved **notable success** in recent clinical trials, improving patient outcomes while minimizing adverse effects.

> "Harnessing the immune system is a game changer," said oncologist Dr. Raj Patel.

The therapies stimulate targeted immune responses against tumor cells. Researchers are optimistic about broader applications across cancer types.

Further studies are underway to optimize protocols and accessibility.
""",
            html="",
            authors=["Raj Patel"],
            tags=["health", "science"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy35",
        ),
        Article(
            title="AI-Powered Tools Transform Creative Industries",
            description="Artificial intelligence reshapes design, music, and writing workflows.",
            content="""
AI technologies are increasingly integrated into creative processes, enabling artists to explore new frontiers of expression.

> "The collaboration between humans and AI expands creative possibilities," said tech innovator Sarah Lin.

From AI-generated music to automated design suggestions, these tools accelerate production and inspire innovation.

Ethical discussions continue about authorship and originality in AI-assisted art.
""",
            html="",
            authors=["Sarah Lin"],
            tags=["technology", "art"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy36",
        ),
        Article(
            title="Renewable Energy Storage Breakthroughs Enhance Grid Stability",
            description="New battery technologies enable more efficient energy storage solutions.",
            content="""
Advancements in renewable energy storage promise improved grid reliability and energy access worldwide.

> "Efficient storage is key to unlocking renewable potential," stated energy expert Michael Ross.

Innovations include solid-state batteries and large-scale flow batteries that provide longer lifespans and higher safety.

These developments support integration of intermittent sources like solar and wind.
""",
            html="",
            authors=["Michael Ross"],
            tags=["energy", "technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy37",
        ),
        Article(
            title="Urban Farming Initiatives Gain Momentum in Major Cities",
            description="Innovative agriculture methods bring fresh produce closer to consumers.",
            content="""
Urban farming projects are expanding globally, utilizing vertical farming and hydroponics to grow food sustainably in cities.

> "Local food production reduces carbon footprints and enhances community resilience," noted urban planner Ana Morales.

These initiatives promote food security and reconnect city dwellers with agriculture.

Support from governments and nonprofits is critical for scaling efforts.
""",
            html="",
            authors=["Ana Morales"],
            tags=["environment", "urban"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy38",
        ),
        Article(
            title="Breakthrough in Carbon Capture Technology Offers Hope for Climate Goals",
            description="New methods significantly improve efficiency and cost-effectiveness.",
            content="""
Recent breakthroughs in carbon capture technologies could accelerate progress toward global emissions targets.

> "Reducing atmospheric CO2 is essential to mitigating climate change," said environmental scientist Dr. Rajiv Kumar.

Innovative sorbents and modular capture units increase scalability and reduce energy consumption.

Deployment in industrial facilities is planned for the near future.
""",
            html="",
            authors=["Rajiv Kumar"],
            tags=["environment", "science"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy39",
        ),
        Article(
            title="Advancements in Telemedicine Expand Access to Healthcare",
            description="Remote consultations and diagnostics become more sophisticated and widespread.",
            content="""
Telemedicine adoption has surged, offering new opportunities to provide healthcare services remotely.

> "Technology bridges gaps in healthcare accessibility," said Dr. Emily Carter.

AI-powered diagnostic tools and video consultations improve patient outcomes, especially in rural areas.

Regulatory frameworks continue evolving to support these innovations.
""",
            html="",
            authors=["Emily Carter"],
            tags=["health", "technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy40",
        ),
        Article(
            title="Next-Generation Robotics Enhance Manufacturing Efficiency",
            description="Collaborative robots streamline production lines and improve safety.",
            content="""
Robotics technology continues to evolve, with collaborative robots ("cobots") working alongside humans safely.

> "Cobots increase productivity without compromising worker wellbeing," explained engineer Luis Fernandez.

Applications range from assembly tasks to quality control, enabling flexible manufacturing.

Companies report reduced costs and faster turnaround times.
""",
            html="",
            authors=["Luis Fernandez"],
            tags=["technology", "industry"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy41",
        ),
        Article(
            title="Breakthroughs in Personalized Nutrition Using Genetic Data",
            description="Custom diets based on DNA analysis improve health outcomes.",
            content="""
Personalized nutrition, guided by genetic insights, is transforming dietary recommendations.

> "Understanding individual variability enables tailored health strategies," said nutritionist Dr. Mia Chen.

Companies offer DNA-based tests to design optimal meal plans for metabolism and disease risk factors.

Early studies show promising improvements in wellbeing and chronic condition management.
""",
            html="",
            authors=["Mia Chen"],
            tags=["health", "science"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy42",
        ),
        Article(
            title="Smart Cities Integrate IoT for Improved Urban Living",
            description="Internet of Things devices optimize transportation, energy, and public services.",
            content="""
IoT technologies enable smart cities to enhance efficiency and quality of life for residents.

> "Data-driven decision making supports sustainable urban development," remarked city planner Daniel Park.

Sensors monitor traffic flows, air quality, and energy consumption, allowing responsive management.

Privacy and cybersecurity remain important considerations.
""",
            html="",
            authors=["Daniel Park"],
            tags=["technology", "urban"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy43",
        ),
        Article(
            title="Innovations in Water Purification Address Global Shortages",
            description="Advanced filtration and desalination technologies increase fresh water availability.",
            content="""
Water purification advances provide critical solutions to meet rising global demand for clean water.

> "Access to potable water is fundamental for health and development," emphasized engineer Fatima Hassan.

Technologies include graphene filters and solar-powered desalination units.

Implementation in vulnerable regions is prioritized by international agencies.
""",
            html="",
            authors=["Fatima Hassan"],
            tags=["environment", "technology"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy44",
        ),
        Article(
            title="New Developments in Space Exploration Inspire Scientific Collaboration",
            description="International missions aim for lunar bases and Mars exploration.",
            content="""
Space agencies worldwide are collaborating on ambitious missions to establish human presence beyond Earth.

> "Exploring space advances technology and inspires humanity," said astronaut Carlos Vega.

Upcoming projects include lunar habitats and robotic Mars explorers.

These efforts foster multinational partnerships and scientific exchange.
""",
            html="",
            authors=["Carlos Vega"],
            tags=["science", "space"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy45",
        ),
        Article(
            title="Emerging Trends in Cybersecurity for the Digital Age",
            description="New strategies combat increasingly sophisticated cyber threats.",
            content="""
Cybersecurity innovations focus on AI-powered threat detection and zero-trust architectures.

> "Proactive defense is critical as cyberattacks grow in complexity," said security expert Nina Patel.

Organizations are adopting continuous monitoring and adaptive response systems.

Education and awareness remain key components of cyber resilience.
""",
            html="",
            authors=["Nina Patel"],
            tags=["technology", "security"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy46",
        ),
        Article(
            title="Breakthroughs in Genetic Editing Open New Medical Frontiers",
            description="CRISPR and related technologies offer hope for treating genetic disorders.",
            content="""
Gene editing technologies have made dramatic progress, enabling precise corrections of disease-causing mutations.

> "We are entering a new era of personalized medicine," said geneticist Dr. Hannah Lee.

Clinical applications target rare diseases and certain cancers, with ongoing trials.

Ethical frameworks are evolving alongside scientific advancements.
""",
            html="",
            authors=["Hannah Lee"],
            tags=["health", "science"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy47",
        ),
        Article(
            title="Sustainable Fashion Gains Popularity Among Consumers",
            description="Eco-friendly materials and ethical production reshape the apparel industry.",
            content="""
The fashion industry is increasingly embracing sustainability through innovative fabrics and supply chain transparency.

> "Consumers demand accountability and environmental stewardship," noted fashion analyst Laura Kim.

Brands are investing in recycled textiles and fair labor practices.

This shift aims to reduce the sector's carbon footprint and waste.
""",
            html="",
            authors=["Laura Kim"],
            tags=["environment", "lifestyle"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy48",
        ),
        Article(
            title="Advances in Neuroscience Reveal Brain Plasticity Mechanisms",
            description="New research uncovers how the brain adapts and reorganizes itself.",
            content="""
Neuroscientists have identified key processes underlying the brain's ability to change in response to experience.

> "Understanding plasticity informs treatments for neurological disorders," explained researcher Dr. Mark Jensen.

Studies utilize imaging and molecular tools to map neural pathways.

Therapies targeting plasticity show promise in recovery after injury.
""",
            html="",
            authors=["Mark Jensen"],
            tags=["science", "health"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy49",
        ),
        Article(
            title="Electric Aviation Poised to Revolutionize Regional Travel",
            description="Electric aircraft development aims to reduce emissions and noise pollution.",
            content="""
Innovations in electric propulsion are advancing the feasibility of small electric aircraft for regional flights.

> "Electric aviation will transform short-haul travel," said aerospace engineer Sophia Grant.

Battery improvements and lightweight materials contribute to range and performance gains.

Regulatory bodies assess certification and safety standards.
""",
            html="",
            authors=["Sophia Grant"],
            tags=["technology", "transportation"],
            datetime_made=datetime.now(),
            datetime_edited=datetime.now(),
            cover_image_id="dummy50",
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
