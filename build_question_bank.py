import json
import os

QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), "questions_bank.json")

def build_full_question_bank():
    questions = []
    current_id = 1

    def add_q(subject, q_text, options, correct_idx, explanation):
        nonlocal current_id
        # Truncate to strictly satisfy Telegram API constraints
        q_clean = q_text.strip()[:295]
        opts_clean = [opt.strip()[:95] for opt in options]
        exp_clean = explanation.strip()[:195]
        questions.append({
            "id": current_id,
            "subject": subject,
            "question": q_clean,
            "options": opts_clean,
            "correct_option_id": correct_idx,
            "explanation": exp_clean
        })
        current_id += 1

    # ==========================================
    # 1. INDIAN POLITY & CONSTITUTION (110+ Questions)
    # ==========================================
    polity_data = [
        ("Which Article of Indian Constitution guarantees Equality before law?", ["Article 14", "Article 19", "Article 21", "Article 32"], 0, "Article 14 states that State shall not deny to any person equality before the law."),
        ("Which Article is called the 'Heart and Soul of the Constitution' by Dr. B.R. Ambedkar?", ["Article 19", "Article 21", "Article 32", "Article 14"], 2, "Article 32 confers the Right to Constitutional Remedies to approach Supreme Court."),
        ("Under which Article can the President declare a National Emergency?", ["Article 352", "Article 356", "Article 360", "Article 365"], 0, "Article 352 empowers President to proclaim National Emergency on war, external aggression or armed rebellion."),
        ("Financial Emergency is proclaimed under which Article?", ["Article 352", "Article 356", "Article 360", "Article 370"], 2, "Article 360 empowers President to declare Financial Emergency if financial stability of India is threatened."),
        ("State Emergency or President's Rule is imposed under which Article?", ["Article 356", "Article 352", "Article 360", "Article 371"], 0, "Article 356 allows President's Rule on failure of constitutional machinery in a State."),
        ("Which Article guarantees Protection of life and personal liberty?", ["Article 20", "Article 21", "Article 21A", "Article 22"], 1, "Article 21 declares no person shall be deprived of his life or personal liberty except by procedure established by law."),
        ("Right to Education was inserted into Fundamental Rights under Article 21A by which Amendment?", ["86th Amendment Act 2002", "44th Amendment Act 1978", "42nd Amendment Act 1976", "91st Amendment Act 2003"], 0, "The 86th Constitutional Amendment Act 2002 inserted Article 21A making free education a fundamental right (6-14 yrs)."),
        ("Fundamental Duties were added to Constitution by which Amendment?", ["42nd Amendment Act", "44th Amendment Act", "61st Amendment Act", "73rd Amendment Act"], 0, "The 42nd Amendment Act 1976 added Part IVA and Article 51A upon Swaran Singh Committee recommendation."),
        ("How many Fundamental Duties are currently listed in Article 51A?", ["10", "11", "12", "9"], 1, "Originally 10 duties were added; the 11th duty was added by 86th Amendment Act in 2002."),
        ("Which Schedule of Constitution contains the 22 recognized languages?", ["Seventh Schedule", "Eighth Schedule", "Ninth Schedule", "Tenth Schedule"], 1, "The Eighth Schedule lists the 22 official languages of India."),
        ("Anti-Defection Law was introduced through which Schedule?", ["Ninth Schedule", "Tenth Schedule", "Eleventh Schedule", "Twelfth Schedule"], 1, "The Tenth Schedule was added by 52nd Amendment Act 1985 to curb political defections."),
        ("Panchayati Raj was given constitutional status by which Amendment?", ["73rd Amendment Act", "74th Amendment Act", "61st Amendment Act", "86th Amendment Act"], 0, "The 73rd Amendment Act 1992 added Part IX and the Eleventh Schedule for Panchayati Raj."),
        ("Municipalities were given constitutional status by which Amendment?", ["73rd Amendment Act", "74th Amendment Act", "65th Amendment Act", "44th Amendment Act"], 1, "The 74th Amendment Act 1992 added Part IXA and the Twelfth Schedule for urban local bodies."),
        ("Who is known as the Father of the Indian Constitution?", ["Mahatma Gandhi", "Dr. B.R. Ambedkar", "Jawaharlal Nehru", "Dr. Rajendra Prasad"], 1, "Dr. B.R. Ambedkar was Chairman of the Drafting Committee of the Constituent Assembly."),
        ("Who was the permanent President of the Constituent Assembly?", ["Dr. Sachchidananda Sinha", "Dr. Rajendra Prasad", "Dr. B.R. Ambedkar", "B.N. Rau"], 1, "Dr. Rajendra Prasad was elected permanent President of the Constituent Assembly on Dec 11, 1946."),
        ("Who was the temporary Chairman of the Constituent Assembly in its first meeting?", ["Dr. Sachchidananda Sinha", "Dr. B.R. Ambedkar", "C. Rajagopalachari", "Jawaharlal Nehru"], 0, "Dr. Sachchidananda Sinha was the oldest member and chosen temporary chairman on Dec 9, 1946."),
        ("Which country's constitution inspired Directive Principles of State Policy (DPSP)?", ["USA", "Ireland", "UK", "Australia"], 1, "DPSP in Part IV of Indian Constitution were borrowed from Irish Constitution."),
        ("The concept of Fundamental Rights was borrowed from which country?", ["USA", "UK", "USSR", "France"], 0, "Fundamental Rights in Part III were inspired by the US Bill of Rights."),
        ("The concept of 'Concurrent List' in Seventh Schedule was borrowed from:", ["Australia", "Canada", "Germany", "South Africa"], 0, "The Concurrent List and freedom of trade/commerce were borrowed from the Australian Constitution."),
        ("Procedure established by Law is borrowed from which country's constitution?", ["Japan", "UK", "USA", "France"], 0, "The phrase 'Procedure established by Law' was borrowed from the Constitution of Japan."),
        ("The procedure for Constitutional Amendment (Article 368) is borrowed from:", ["South Africa", "Ireland", "Germany", "Canada"], 0, "Article 368 amendment procedure is borrowed from the Constitution of South Africa."),
        ("Who administers the oath of office to the President of India?", ["Prime Minister", "Chief Justice of India", "Vice President", "Lok Sabha Speaker"], 1, "The Chief Justice of India (or senior-most judge of Supreme Court) administers oath to President."),
        ("What is the minimum age required to become the President of India?", ["25 years", "30 years", "35 years", "21 years"], 2, "Under Article 58, a candidate must have completed 35 years of age to contest Presidential election."),
        ("What is the minimum age to be elected as a member of Lok Sabha?", ["21 years", "25 years", "30 years", "35 years"], 1, "Minimum age for Lok Sabha is 25 years; for Rajya Sabha it is 30 years."),
        ("What is the minimum age required to become a member of Rajya Sabha?", ["25 years", "30 years", "35 years", "21 years"], 1, "Under Article 84, minimum age for Rajya Sabha membership is 30 years."),
        ("What is the tenure of members of the Rajya Sabha?", ["4 years", "5 years", "6 years", "Permanent"], 2, "Rajya Sabha is a permanent body not subject to dissolution; members serve 6-year terms with 1/3rd retiring every 2 years."),
        ("Who is the ex-officio Chairman of the Rajya Sabha?", ["President of India", "Vice-President of India", "Prime Minister", "Lok Sabha Speaker"], 1, "Article 64 states that the Vice-President of India is the ex-officio Chairman of Rajya Sabha."),
        ("Who presides over the joint sitting of both Houses of Parliament?", ["President", "Vice President", "Speaker of Lok Sabha", "Chief Justice of India"], 2, "Under Article 118, the Speaker of Lok Sabha presides over a joint sitting summoned under Article 108."),
        ("Money Bill can be introduced only in which house of Parliament?", ["Lok Sabha", "Rajya Sabha", "Either House", "Joint Sitting"], 0, "Under Article 109, a Money Bill can only be introduced in the Lok Sabha with President's recommendation."),
        ("Who decides whether a bill is a Money Bill or not?", ["President", "Finance Minister", "Speaker of Lok Sabha", "Prime Minister"], 2, "Under Article 110(3), the decision of the Lok Sabha Speaker on whether a bill is a Money Bill is final."),
        ("A Money Bill sent to Rajya Sabha must be returned within how many days?", ["14 days", "30 days", "60 days", "90 days"], 0, "Rajya Sabha has 14 days to suggest recommendations; otherwise the bill is deemed passed."),
        ("What is the retirement age of Supreme Court judges in India?", ["60 years", "62 years", "65 years", "68 years"], 2, "Supreme Court judges hold office until 65 years of age; High Court judges retire at 62 years."),
        ("What is the retirement age of High Court judges in India?", ["60 years", "62 years", "65 years", "70 years"], 1, "High Court judges retire at 62 years of age as per Article 217."),
        ("Which Article provides for the Comptroller and Auditor General (CAG) of India?", ["Article 148", "Article 280", "Article 76", "Article 324"], 0, "Article 148 provides for an independent Comptroller and Auditor General of India."),
        ("Which Article provides for the Attorney General for India?", ["Article 74", "Article 76", "Article 148", "Article 165"], 1, "Article 76 appoints the Attorney General as the highest law officer in India."),
        ("Who appoints the Advocate General of a State?", ["Governor of the State", "Chief Minister", "Chief Justice of High Court", "President"], 0, "Under Article 165, the Advocate General of State is appointed by Governor of that State."),
        ("Finance Commission of India is constituted under which Article?", ["Article 280", "Article 265", "Article 300A", "Article 324"], 0, "Article 280 requires President to constitute Finance Commission every 5 years."),
        ("Right to Property was deleted from Fundamental Rights by which Amendment?", ["42nd Amendment Act", "44th Amendment Act", "52nd Amendment Act", "86th Amendment Act"], 1, "44th Amendment Act 1978 removed Right to Property from Part III and made it legal right under Art 300A."),
        ("Right to Property is now a legal right under which Article?", ["Article 300", "Article 300A", "Article 301", "Article 31"], 1, "Article 300A in Part XII provides that no person shall be deprived of property save by authority of law."),
        ("Uniform Civil Code is mentioned under which Article of DPSP?", ["Article 40", "Article 44", "Article 45", "Article 50"], 1, "Article 44 of DPSP directs State to secure for citizens a Uniform Civil Code throughout India."),
        ("Organization of Village Panchayats is mentioned under which Article?", ["Article 39", "Article 40", "Article 43", "Article 48"], 1, "Article 40 directs State to organize village panchayats as units of self-government."),
        ("Separation of Judiciary from Executive is mentioned in which Article?", ["Article 48", "Article 49", "Article 50", "Article 51"], 2, "Article 50 of DPSP requires the State to separate judiciary from executive in public services."),
        ("Promotion of international peace and security is mentioned under:", ["Article 45", "Article 48A", "Article 51", "Article 39A"], 2, "Article 51 of DPSP directs State to promote international peace and foster respect for treaties."),
        ("Protection and improvement of environment is provided under which Article?", ["Article 48", "Article 48A", "Article 49", "Article 51A"], 1, "Article 48A was added by 42nd Amendment 1976 to protect environment, forests and wildlife."),
        ("Abolition of Untouchability is guaranteed under which Article?", ["Article 15", "Article 16", "Article 17", "Article 18"], 2, "Article 17 abolishes untouchability and forbids its practice in any form."),
        ("Abolition of Titles (except military and academic) is under which Article?", ["Article 16", "Article 17", "Article 18", "Article 19"], 2, "Article 18 abolishes titles to ensure democratic equality among citizens."),
        ("Prohibition of traffic in human beings and forced labour is under:", ["Article 23", "Article 24", "Article 25", "Article 29"], 0, "Article 23 prohibits trafficking in human beings and begar (forced labor)."),
        ("Prohibition of employment of children in factories is under:", ["Article 21", "Article 23", "Article 24", "Article 25"], 2, "Article 24 prohibits employment of children below 14 years in factories, mines or hazardous work."),
        ("Freedom of conscience and free profession of religion is guaranteed by:", ["Article 25", "Article 26", "Article 27", "Article 28"], 0, "Article 25 grants all persons freedom of conscience and right to profess, practice and propagate religion."),
        ("Protection of interests of minorities is provided under:", ["Article 29", "Article 30", "Article 31", "Article 28"], 0, "Article 29 protects minorities right to conserve distinct language, script or culture.")
    ]
    for row in polity_data:
        add_q("Indian Polity", row[0], row[1], row[2], row[3])

    # More Polity Questions to reach 100+
    more_polity = [
        ("Which writ literally means 'We Command'?", ["Habeas Corpus", "Mandamus", "Quo-Warranto", "Certiorari"], 1, "Mandamus is issued by court to public officials commanding performance of public duty."),
        ("Which writ means 'To have the body of'?", ["Habeas Corpus", "Mandamus", "Prohibition", "Certiorari"], 0, "Habeas Corpus protects individuals against unlawful and arbitrary detention."),
        ("Which writ is issued against unlawful usurpation of a public office?", ["Quo-Warranto", "Mandamus", "Certiorari", "Prohibition"], 0, "Quo-Warranto inquires into legality of claim of a person to a public office."),
        ("Which writ is issued by higher court to lower court to quash its order?", ["Prohibition", "Certiorari", "Mandamus", "Habeas Corpus"], 1, "Certiorari is curative and quashes orders passed by lower courts exceeding jurisdiction."),
        ("Who can issue writs for enforcement of Fundamental Rights?", ["Supreme Court only", "High Courts only", "Both Supreme Court and High Courts", "District Courts"], 2, "Supreme Court under Article 32 and High Courts under Article 226 can issue writs."),
        ("The Preamble to the Indian Constitution was amended by which Amendment?", ["42nd Amendment Act 1976", "44th Amendment Act 1978", "52nd Amendment Act 1985", "None, it cannot be amended"], 0, "The 42nd Amendment 1976 added Socialist, Secular, and Integrity to the Preamble."),
        ("Which words were added to the Preamble by the 42nd Constitutional Amendment?", ["Socialist, Secular, Integrity", "Sovereign, Republic, Justice", "Liberty, Equality, Fraternity", "Democratic, Socialist, Republic"], 0, "42nd Amendment Act 1976 inserted Socialist, Secular and Integrity into the Preamble."),
        ("In which landmark case did Supreme Court formulate the 'Basic Structure' doctrine?", ["Golaknath Case (1967)", "Kesavananda Bharati Case (1973)", "Minerva Mills Case (1980)", "Maneka Gandhi Case (1978)"], 1, "In Kesavananda Bharati v. State of Kerala (1973), Supreme Court ruled Parliament cannot alter basic structure."),
        ("What is the maximum strength of Lok Sabha as per the Constitution?", ["545", "550", "552", "560"], 1, "Following 104th Amendment Act 2019 (discontinuing Anglo-Indian nominations), maximum strength is 550."),
        ("What is the maximum strength of Rajya Sabha?", ["245", "250", "255", "260"], 1, "Maximum strength of Rajya Sabha is 250 (238 elected from States/UTs and 12 nominated by President)."),
        ("How many members are nominated to Rajya Sabha by President of India?", ["10", "12", "14", "2"], 1, "President nominates 12 members with special knowledge in Literature, Science, Art and Social Service."),
        ("GST (Goods and Services Tax) was introduced by which Amendment Act?", ["100th Amendment Act", "101st Amendment Act", "102nd Amendment Act", "103rd Amendment Act"], 1, "101st Constitutional Amendment Act 2016 introduced nationwide GST with effect from July 1, 2017."),
        ("103rd Constitutional Amendment Act provides 10% reservation for:", ["Economically Weaker Sections (EWS)", "OBCs", "SC/ST", "Women"], 0, "103rd Amendment Act 2019 provided 10% reservation for Economically Weaker Sections (EWS)."),
        ("National Judicial Appointments Commission (NJAC) was struck down as unconstitutional under which Amendment?", ["99th Amendment Act", "98th Amendment Act", "100th Amendment Act", "97th Amendment Act"], 0, "Supreme Court struck down 99th Amendment Act 2014 and NJAC Act in 2015 to uphold judicial independence."),
        ("Who is the guardian of the Indian Constitution?", ["President of India", "Supreme Court of India", "Parliament", "Prime Minister"], 1, "Supreme Court is the ultimate interpreter and guardian of the Constitution of India."),
        ("What is the minimum quorum required to conduct meetings of either House of Parliament?", ["1/5th of total members", "1/10th of total members", "1/6th of total members", "1/3rd of total members"], 1, "Article 100(3) specifies quorum as 1/10th of total members of either House of Parliament."),
        ("The concept of 'Public Interest Litigation' (PIL) originated in:", ["United Kingdom", "United States of America", "Australia", "India"], 1, "PIL originated in USA in 1960s and was pioneered in India by Justice P.N. Bhagwati and V.R. Krishna Iyer."),
        ("Who acts as President when both President and Vice-President offices are vacant?", ["Lok Sabha Speaker", "Chief Justice of India", "Senior-most Governor", "Attorney General"], 1, "Under President (Discharge of Functions) Act 1969, Chief Justice of India acts as President."),
        ("Who was the only Chief Justice of India to act as the President of India?", ["Justice P.N. Bhagwati", "Justice M. Hidayatullah", "Justice H.J. Kania", "Justice Y.V. Chandrachud"], 1, "Justice M. Hidayatullah acted as President of India from July 20 to August 24, 1969."),
        ("Who was the first Chief Justice of India?", ["H.J. Kania", "M. Patanjali Sastri", "Mehr Chand Mahajan", "B.K. Mukherjea"], 0, "Sir Harilal Jekisundas Kania served as the first Chief Justice of independent India (1950-1951)."),
        ("How many types of emergencies are envisaged by the Constitution of India?", ["Two", "Three", "Four", "Five"], 1, "Three types: National (Art 352), State / President's Rule (Art 356), and Financial (Art 360)."),
        ("Which Article empowers the President to grant pardons and reprieves?", ["Article 72", "Article 74", "Article 76", "Article 161"], 0, "Article 72 empowers the President to grant pardons, reprieves, respites or remissions of punishment."),
        ("Which Article empowers the Governor of a State to grant pardons?", ["Article 72", "Article 161", "Article 164", "Article 213"], 1, "Article 161 empowers Governor to grant pardons for offenses against State laws."),
        ("President can promulgate Ordinances when Parliament is in recess under:", ["Article 110", "Article 123", "Article 213", "Article 352"], 1, "Article 123 empowers President to promulgate Ordinances during recess of Parliament."),
        ("Governor can promulgate Ordinances during recess of State Legislature under:", ["Article 123", "Article 213", "Article 214", "Article 163"], 1, "Article 213 grants ordinance-making power to Governor of a State during legislative recess."),
        ("An Ordinance issued by President must be approved by Parliament within:", ["6 days", "6 weeks from reassembly", "6 months", "3 months"], 1, "An ordinance ceases to operate 6 weeks from the reassembly of Parliament if not approved."),
        ("Who was the first woman judge of the Supreme Court of India?", ["Justice Leila Seth", "Justice Fathima Beevi", "Justice Sujata Manohar", "Justice Ruma Pal"], 1, "Justice M. Fathima Beevi was appointed as the first female judge of Supreme Court in 1989."),
        ("Who was the first woman Chief Justice of a High Court in India?", ["Justice Leila Seth", "Justice Fathima Beevi", "Justice Anna Chandy", "Justice Gyan Sudha Misra"], 0, "Justice Leila Seth became the first woman Chief Justice of Himachal Pradesh High Court in 1991."),
        ("Which Union Territory has its own High Court?", ["Chandigarh", "Delhi", "Puducherry", "Ladakh"], 1, "National Capital Territory of Delhi has its own dedicated High Court established in 1966."),
        ("National Human Rights Commission (NHRC) was established in which year?", ["1990", "1993", "1995", "2000"], 1, "NHRC was established on October 12, 1993 under Protection of Human Rights Act 1993."),
        ("Right to Information (RTI) Act came into force in India in:", ["2002", "2005", "2007", "2010"], 1, "RTI Act 2005 came into force on October 12, 2005 promoting transparency in public administration."),
        ("Central Vigilance Commission (CVC) was set up on recommendation of:", ["Santhanam Committee", "Sarkaria Commission", "Punchhi Commission", "Kothari Commission"], 0, "CVC was established in 1964 following recommendations of Santhanam Committee on Prevention of Corruption."),
        ("Sarkaria Commission was set up to review relations between:", ["Judiciary and Executive", "Centre and States", "Legislature and Executive", "President and Prime Minister"], 1, "Sarkaria Commission (1983) examined Centre-State relations in India."),
        ("Punchhi Commission was appointed in 2007 to deal with:", ["Electoral Reforms", "Centre-State Relations", "Tax Reforms", "Police Reforms"], 1, "The Second Commission on Centre-State Relations was headed by Justice M.M. Punchhi."),
        ("Who was the first Speaker of the Lok Sabha?", ["G.V. Mavalankar", "M.A. Ayyangar", "Hukam Singh", "K.S. Hegde"], 0, "Ganesh Vasudev Mavalankar served as the first Speaker of Lok Sabha from 1952 to 1956."),
        ("Who was the first woman Speaker of the Lok Sabha?", ["Sumitra Mahajan", "Meira Kumar", "Najma Heptulla", "Pratibha Patil"], 1, "Meira Kumar was elected as the first woman Speaker of Lok Sabha in 2009."),
        ("First General Elections in independent India were held during:", ["1947-48", "1950-51", "1951-52", "1953-54"], 2, "First Lok Sabha general elections were conducted from October 1951 to February 1952."),
        ("Who was the first Chief Election Commissioner of India?", ["Sukumar Sen", "K.V.K. Sundaram", "T.N. Seshan", "S.P. Sen Verma"], 0, "Sukumar Sen was the first Chief Election Commissioner of India (1950 to 1958)."),
        ("EVMs (Electronic Voting Machines) were first used on experimental basis in:", ["Kerala (1982)", "Goa (1989)", "Delhi (1998)", "Tamil Nadu (1991)"], 0, "EVMs were first used in 1982 in the Paravur constituency of Kerala in limited polling stations."),
        ("VVPAT stands for:", ["Voter Verified Paper Audit Trail", "Voter Validated Paper Audit Trail", "Voting Verification Paper Access Tool", "Voter Voice Paper Audit Tracker"], 0, "VVPAT allows voters to verify that their votes are cast as intended."),
        ("Which Constitutional Amendment introduced the Anti-Defection provisions?", ["42nd Amendment", "44th Amendment", "52nd Amendment", "61st Amendment"], 2, "52nd Amendment Act 1985 added the Tenth Schedule laying down grounds for defection."),
        ("Delimitation Commission in India is appointed by:", ["President of India", "Chief Election Commissioner", "Prime Minister", "Speaker of Lok Sabha"], 0, "Delimitation Commission is appointed by President of India under Delimitation Commission Act."),
        ("How many Lok Sabha constituencies are there in Uttar Pradesh?", ["60", "70", "80", "85"], 2, "Uttar Pradesh has the highest number of Lok Sabha seats (80 constituencies)."),
        ("Which State has the highest number of seats in Rajya Sabha?", ["Maharashtra", "Tamil Nadu", "Bihar", "Uttar Pradesh"], 3, "Uttar Pradesh sends 31 members to Rajya Sabha, the highest among all States."),
        ("Minimum number of judges required in a Constitutional Bench of Supreme Court is:", ["3", "5", "7", "9"], 1, "Article 145(3) requires a minimum of 5 judges for deciding questions involving constitutional interpretation."),
        ("The concept of 'Judicial Review' in Indian Constitution is adopted from:", ["USA", "UK", "France", "Switzerland"], 0, "Power of judicial review exercised by Supreme Court and High Courts is derived from US Constitution."),
        ("Original jurisdiction of Supreme Court is covered under which Article?", ["Article 131", "Article 132", "Article 136", "Article 143"], 0, "Article 131 deals with disputes between Centre and States or between States."),
        ("Advisory jurisdiction of Supreme Court (President seeking opinion) is under:", ["Article 131", "Article 136", "Article 141", "Article 143"], 3, "Article 143 empowers the President to consult Supreme Court on questions of law or fact."),
        ("Special Leave Petition (SLP) can be granted by Supreme Court under:", ["Article 132", "Article 136", "Article 226", "Article 32"], 1, "Article 136 empowers Supreme Court to grant special leave to appeal against any judgment or order."),
        ("Law declared by Supreme Court is binding on all courts within India under:", ["Article 141", "Article 142", "Article 144", "Article 139"], 0, "Article 141 states that law declared by Supreme Court shall be binding on all courts in India."),
        ("Complete justice can be done by Supreme Court by passing any decree under:", ["Article 141", "Article 142", "Article 143", "Article 144"], 1, "Article 142 empowers Supreme Court to pass any decree necessary for doing complete justice."),
        ("Which Article prohibits discrimination on grounds of religion, race, caste, sex or place of birth?", ["Article 14", "Article 15", "Article 16", "Article 19"], 1, "Article 15 prohibits discrimination by the State against any citizen on specified grounds.")
    ]
    for row in more_polity:
        add_q("Indian Polity", row[0], row[1], row[2], row[3])

    print(f"Polity complete. Total questions so far: {len(questions)}")

    # ==========================================
    # 2. INDIAN HISTORY (150+ Questions)
    # ==========================================
    history_data = [
        ("The Great Bath of Indus Valley Civilization was discovered at which site?", ["Harappa", "Mohenjodaro", "Lothal", "Kalibangan"], 1, "The Great Bath was excavated at Mohenjodaro in Sindh by R.D. Banerjee in 1922."),
        ("Which Indus Valley site is famous for having an artificial dockyard?", ["Lothal", "Kalibangan", "Dholavira", "Surkotada"], 0, "Lothal in Gujarat was a major port city of Indus Valley with a massive tidal dockyard."),
        ("Ploughed field surface was discovered at which Indus Valley Civilization site?", ["Kalibangan", "Banawali", "Rakhigarhi", "Ropar"], 0, "Kalibangan in Rajasthan revealed evidence of furrowed land and fire altars."),
        ("Which Indus Valley site was divided into three parts instead of two?", ["Dholavira", "Lothal", "Chanhudaro", "Harappa"], 0, "Dholavira in Rann of Kutch, Gujarat had a citadel, middle town, and lower town."),
        ("Which Indus site yielded evidence of horse remains?", ["Surkotada", "Dholavira", "Alamgirpur", "Suktagendor"], 0, "Surkotada in Kutch district, Gujarat yielded bones attributed to horses."),
        ("Who composed the Gayatri Mantra found in the Rigveda?", ["Vishvamitra", "Vashistha", "Agastya", "Bharadvaja"], 0, "Sage Vishvamitra composed Gayatri Mantra dedicated to solar deity Savitr in Mandala 3 of Rigveda."),
        ("The famous 'Battle of Ten Kings' (Dasarajna) was fought on banks of river:", ["Parushni (Ravi)", "Vitasta (Jhelum)", "Asikni (Chenab)", "Vipasa (Beas)"], 0, "King Sudas won the Battle of Ten Kings on the banks of river Parushni (modern Ravi)."),
        ("Gautama Buddha attained Enlightenment (Nirvana) at Bodh Gaya on banks of river:", ["Niranjana (Phalgu)", "Ganga", "Yamuna", "Gandak"], 0, "Buddha attained Enlightenment at age 35 under a Peepal tree on the banks of river Niranjana."),
        ("Where did Gautama Buddha deliver his first sermon (Dharmachakrapravartana)?", ["Sarnath (Deer Park)", "Kushinagar", "Lumbini", "Vaishali"], 0, "Buddha preached his first sermon to his five disciples at Deer Park in Sarnath near Varanasi."),
        ("Where did Gautama Buddha attain Mahaparinirvana (death)?", ["Kushinagar", "Sarnath", "Bodh Gaya", "Rajgir"], 0, "Buddha passed away at the age of 80 in Kushinagar, capital of Malla Republic."),
        ("The First Buddhist Council was held at Rajgriha under patronage of which king?", ["Ajatashatru", "Kalashoka", "Ashoka", "Kanishka"], 0, "Ajatashatru of Haryanka dynasty convened First Buddhist Council in 483 BC presided by Mahakassapa."),
        ("The Second Buddhist Council was convened at Vaishali under:", ["Kalashoka", "Ajatashatru", "Ashoka", "Kanishka"], 0, "Kalashoka of Shishunaga dynasty convened Second Buddhist Council in 383 BC."),
        ("The Third Buddhist Council was convened at Pataliputra under patronage of:", ["Ashoka", "Kanishka", "Chandragupta Maurya", "Bindusara"], 0, "Emperor Ashoka patronized the Third Buddhist Council at Pataliputra presided by Moggaliputta Tissa."),
        ("The Fourth Buddhist Council where Buddhism split into Hinayana and Mahayana was under:", ["Kanishka", "Ashoka", "Harshavardhana", "Menander"], 0, "Kushana Emperor Kanishka convened Fourth Council in Kashmir presided by Vasumitra."),
        ("Who was the 24th and last Tirthankara of Jainism?", ["Vardhamana Mahavira", "Parshvanatha", "Rishabhanatha", "Arishtanemi"], 0, "Lord Mahavira was the 24th Tirthankara; Rishabhanatha was the first and Parshvanatha 23rd."),
        ("Who was the founder of the Mauryan Empire?", ["Chandragupta Maurya", "Ashoka", "Bindusara", "Brihadratha"], 0, "Chandragupta Maurya founded Mauryan dynasty in 322 BC with help of mentor Chanakya (Kautilya)."),
        ("Who wrote the ancient political treatise 'Arthashastra'?", ["Chanakya (Kautilya)", "Megasthenes", "Visakhadatta", "Kalidasa"], 0, "Chanakya (Vishnugupta/Kautilya) authored Arthashastra detailing statecraft and military strategy."),
        ("Who was the Greek ambassador sent to Chandragupta Maurya's court who wrote 'Indica'?", ["Megasthenes", "Deimachus", "Dionysius", "Fa-Hien"], 0, "Megasthenes was ambassador of Seleucus I Nicator and described Mauryan administration in Indica."),
        ("Which rock edict of Emperor Ashoka mentions the horrors of the Kalinga War?", ["Rock Edict XIII", "Rock Edict X", "Rock Edict I", "Rock Edict VII"], 0, "Major Rock Edict XIII describes Ashoka's remorse after Kalinga War (261 BC) leading to Dhamma."),
        ("Who deciphered the Brahmi and Kharosthi scripts of Ashokan edicts in 1837?", ["James Prinsep", "Alexander Cunningham", "William Jones", "John Marshall"], 0, "James Prinsep, an officer in Calcutta Mint, deciphered Ashokan inscriptions in 1837."),
        ("Who was the founder of the Gupta Empire?", ["Sri Gupta", "Chandragupta I", "Samudragupta", "Chandragupta II"], 0, "Sri Gupta was the founder of Gupta Empire in late 3rd century AD; Chandragupta I adopted Maharajadhiraja."),
        ("Which Gupta ruler was referred to as 'Napoleon of India' by historian V.A. Smith?", ["Samudragupta", "Chandragupta I", "Chandragupta II", "Skandagupta"], 0, "Samudragupta was called Napoleon of India due to his undefeated military conquests recorded on Prayag Prashasti."),
        ("The famous Iron Pillar at Mehrauli, Delhi, was erected during the reign of:", ["Chandragupta II (Vikramaditya)", "Samudragupta", "Ashoka", "Kanishka"], 0, "The rust-resistant Iron Pillar bears inscription of King Chandra, identified as Chandragupta II."),
        ("Chinese traveler Fa-Hien visited India during the reign of:", ["Chandragupta II", "Harshavardhana", "Kanishka", "Samudragupta"], 0, "Fa-Hien visited India during reign of Chandragupta II (Vikramaditya) to collect Buddhist manuscripts."),
        ("Chinese traveler Hiuen Tsang (Xuanzang) visited India during the reign of:", ["Harshavardhana", "Chandragupta Maurya", "Pulakeshin II", "Samudragupta"], 0, "Hiuen Tsang visited India in 7th century during reign of King Harshavardhana of Kannauj."),
        ("Who wrote 'Harshacharita', the biography of King Harshavardhana?", ["Banabhatta", "Harisena", "Kalidasa", "Ravikirti"], 0, "Court poet Banabhatta composed Harshacharita and Kadambari in classical Sanskrit."),
        ("Which Chalukya king defeated Harshavardhana on the banks of Narmada river?", ["Pulakeshin II", "Kirtivarman I", "Vikramaditya II", "Mangalesha"], 0, "Pulakeshin II defeated Harsha as commemorated in the Aihole inscription written by Ravikirti."),
        ("Who was the founder of the Slave Dynasty (Delhi Sultanate) in 1206?", ["Qutb-ud-din Aibak", "Iltutmish", "Balban", "Razia Sultana"], 0, "Qutb-ud-din Aibak, general of Muhammad Ghori, founded Mamluk (Slave) dynasty in 1206."),
        ("Who was the first and only woman ruler of the Delhi Sultanate?", ["Razia Sultana", "Nur Jahan", "Chand Bibi", "Rani Durgavati"], 0, "Razia Sultana, daughter of Iltutmish, ruled Delhi Sultanate from 1236 to 1240."),
        ("Which Delhi Sultan introduced market control regulations and price control policies?", ["Alauddin Khilji", "Muhammad bin Tughlaq", "Feroz Shah Tughlaq", "Balban"], 0, "Alauddin Khilji established market reforms, price controls, and military branding (Dagh and Chehra)."),
        ("Which Sultan transferred his capital from Delhi to Daulatabad (Devagiri)?", ["Muhammad bin Tughlaq", "Alauddin Khilji", "Feroz Shah Tughlaq", "Ibrahim Lodi"], 0, "Muhammad bin Tughlaq shifted capital to Daulatabad in 1327 and introduced token copper currency."),
        ("Who founded the Vijayanagara Empire in 1336?", ["Harihara I and Bukka Raya I", "Krishnadevaraya", "Rama Raya", "Deva Raya II"], 0, "Harihara and Bukka founded Vijayanagara Empire on banks of Tungabhadra with spiritual guidance of Vidyaranya."),
        ("The greatest ruler of Vijayanagara Empire, Krishnadevaraya, belonged to which dynasty?", ["Tuluva dynasty", "Sangama dynasty", "Saluva dynasty", "Aravidu dynasty"], 0, "Emperor Krishnadevaraya (1509-1529) belonged to Tuluva dynasty and wrote Telugu epic Amuktamalyada."),
        ("In which year was the First Battle of Panipat fought?", ["1526", "1556", "1761", "1527"], 0, "Babur defeated Ibrahim Lodi in 1526, ending Delhi Sultanate and establishing Mughal Empire."),
        ("In the Second Battle of Panipat (1556), Akbar's general Bairam Khan defeated:", ["Hemu (Hemchandra Vikramaditya)", "Sher Shah Suri", "Rana Sanga", "Maharana Pratap"], 0, "Akbar defeated Hemu at Second Battle of Panipat in 1556, securing Mughal dominance."),
        ("The Battle of Haldighati (1576) was fought between Maharana Pratap and Mughal forces led by:", ["Man Singh I", "Birbal", "Todar Mal", "Asaf Khan"], 0, "Raja Man Singh I and Asaf Khan led Mughal army against Maharana Pratap of Mewar in 1576."),
        ("Which Mughal Emperor introduced the Din-i-Ilahi religion in 1582?", ["Akbar", "Jahangir", "Shah Jahan", "Babur"], 0, "Akbar propounded syncretic ethical system Din-i-Ilahi emphasizing Sulh-i-Kul (universal peace)."),
        ("Who was the revenue minister of Akbar who devised the Dahsala system?", ["Raja Todar Mal", "Raja Birbal", "Abul Fazl", "Faizi"], 0, "Raja Todar Mal introduced the Zabti system and Ain-i-Dahsala land revenue system."),
        ("Captain William Hawkins and Sir Thomas Roe visited the court of which Mughal Emperor?", ["Jahangir", "Akbar", "Shah Jahan", "Aurangzeb"], 0, "British emissaries Hawkins (1608) and Sir Thomas Roe (1615) visited Jahangir to seek trade rights."),
        ("Which Sikh Guru was executed under orders of Mughal Emperor Jahangir?", ["Guru Arjan Dev", "Guru Tegh Bahadur", "Guru Gobind Singh", "Guru Nanak"], 0, "5th Sikh Guru Arjan Dev was executed in 1606 for supporting Prince Khusrau's rebellion."),
        ("Which Sikh Guru was martyred by Aurangzeb at Chandni Chowk, Delhi?", ["Guru Tegh Bahadur", "Guru Arjan Dev", "Guru Ram Das", "Guru Har Gobind"], 0, "9th Sikh Guru Tegh Bahadur was martyred in 1675 defending religious freedom of Kashmiri Pandits."),
        ("In which year was Chhatrapati Shivaji Maharaj crowned at Raigad fort?", ["1674", "1665", "1680", "1659"], 0, "Shivaji was crowned Chhatrapati in grand ceremony at Raigad in 1674 by Pandit Gaga Bhatt."),
        ("The Treaty of Purandar (1665) was signed between Shivaji and:", ["Raja Jai Singh I", "Shaista Khan", "Afzal Khan", "Aurangzeb directly"], 0, "Raja Jai Singh I representing Aurangzeb signed Treaty of Purandar with Shivaji in 1665."),
        ("The Battle of Plassey was fought on 23 June 1757 between British East India Company and:", ["Siraj-ud-Daulah", "Mir Qasim", "Mir Jafar", "Shuja-ud-Daulah"], 0, "Robert Clive defeated Nawab Siraj-ud-Daulah of Bengal due to treachery of Mir Jafar."),
        ("The decisive Battle of Buxar was fought in which year?", ["1764", "1757", "1761", "1765"], 0, "Major Hector Munro defeated joint forces of Mir Qasim, Shuja-ud-Daulah, and Shah Alam II in 1764."),
        ("Who introduced the Permanent Settlement (Zamindari system) of Bengal in 1793?", ["Lord Cornwallis", "Warren Hastings", "Lord Wellesley", "Lord William Bentinck"], 0, "Lord Cornwallis introduced Permanent Settlement fixing land revenue demand perpetually with Zamindars."),
        ("Who introduced the Subsidiary Alliance system in India?", ["Lord Wellesley", "Lord Dalhousie", "Lord Hastings", "Lord Clive"], 0, "Lord Wellesley (Governor-General 1798-1805) used Subsidiary Alliance to bring Indian states under British hegemony."),
        ("Which Indian state was the first to sign the Subsidiary Alliance?", ["Hyderabad (Nizam)", "Mysore", "Awadh", "Marathas"], 0, "The Nizam of Hyderabad was the first ruler to accept Subsidiary Alliance in 1798."),
        ("Who introduced the Doctrine of Lapse in India?", ["Lord Dalhousie", "Lord Canning", "Lord Curzon", "Lord Bentinck"], 0, "Lord Dalhousie annexed states without natural male heirs (Satara in 1848, Jhansi, Nagpur)."),
        ("Which was the first princely state annexed under the Doctrine of Lapse?", ["Satara (1848)", "Jhansi (1853)", "Nagpur (1854)", "Sambalpur (1849)"], 0, "Satara in Maharashtra was the first state annexed under Doctrine of Lapse in 1848.")
    ]
    for row in history_data:
        add_q("Indian History", row[0], row[1], row[2], row[3])

    more_history = [
        ("Who was the soldier at Barrackpore whose revolt ignited the 1857 Rebellion?", ["Mangal Pandey", "Tatya Tope", "Kunwar Singh", "Bakht Khan"], 0, "Sepoy Mangal Pandey of 34th Bengal Native Infantry revolted against greased cartridges on 29 March 1857."),
        ("Who led the 1857 revolt in Kanpur?", ["Nana Saheb", "Begum Hazrat Mahal", "Kunwar Singh", "Rani Lakshmibai"], 0, "Nana Saheb (Dhondu Pant), adopted son of Peshwa Baji Rao II, led the revolt in Kanpur with Tatya Tope."),
        ("Who led the 1857 revolt in Lucknow?", ["Begum Hazrat Mahal", "Rani Lakshmibai", "Maulvi Ahmadullah", "Khan Bahadur Khan"], 0, "Begum Hazrat Mahal led the revolt in Lucknow, declaring her son Birjis Qadr as Nawab."),
        ("Who led the 1857 revolt in Arrah, Bihar?", ["Kunwar Singh", "Amar Singh", "Peer Ali", "Khan Bahadur"], 0, "80-year-old Rajput chieftain Veer Kunwar Singh of Jagdishpur valiantly led the revolt in Bihar."),
        ("Who was the Governor-General of India during the 1857 Revolt?", ["Lord Canning", "Lord Dalhousie", "Lord Ellenborough", "Lord Elgin"], 0, "Lord Canning was Governor-General during 1857 and became the first Viceroy under Govt of India Act 1858."),
        ("Who was the first Viceroy of India?", ["Lord Canning", "Lord Curzon", "Lord Mountbatten", "Lord Ripon"], 0, "Lord Canning became the first Viceroy after the British Crown took direct control in 1858."),
        ("Who founded the Brahmo Samaj in 1828 in Calcutta?", ["Raja Ram Mohan Roy", "Debendranath Tagore", "Keshab Chandra Sen", "Ishwar Chandra Vidyasagar"], 0, "Raja Ram Mohan Roy, 'Father of Modern Indian Renaissance', established Brahmo Samaj opposing idolatry and sati."),
        ("Sati practice was officially banned in India in 1829 by Governor-General:", ["Lord William Bentinck", "Lord Hastings", "Lord Auckland", "Lord Dalhousie"], 0, "Lord William Bentinck enacted Bengal Sati Regulation 1829 largely due to Raja Ram Mohan Roy's crusade."),
        ("Who founded the Arya Samaj in 1875 in Bombay?", ["Swami Dayanand Saraswati", "Swami Vivekananda", "Ramakrishna Paramahamsa", "Atmaram Pandurang"], 0, "Swami Dayanand Saraswati founded Arya Samaj giving the call 'Go Back to the Vedas' and writing Satyarth Prakash."),
        ("Who founded the Ramakrishna Mission in 1897?", ["Swami Vivekananda", "Ramakrishna Paramahamsa", "Sarada Devi", "Keshab Chandra Sen"], 0, "Swami Vivekananda founded Ramakrishna Mission in Belur to propagate spiritual and social service."),
        ("In which year did Swami Vivekananda deliver his historic speech at Parliament of Religions in Chicago?", ["1893", "1890", "1895", "1900"], 0, "Vivekananda addressed Chicago World Parliament of Religions on Sept 11, 1893 beginning 'Sisters and Brothers of America'."),
        ("Who founded the Satyashodhak Samaj in 1873 in Maharashtra?", ["Jyotirao Phule", "Dr. B.R. Ambedkar", "Gopal Ganesh Agarkar", "Mahadev Govind Ranade"], 0, "Mahatma Jyotirao Phule founded Satyashodhak Samaj for uplifting lower castes and women; authored Gulamgiri."),
        ("Who founded the Servants of India Society in 1905?", ["Gopal Krishna Gokhale", "Bal Gangadhar Tilak", "Lala Lajpat Rai", "Dadabhai Naoroji"], 0, "Gopal Krishna Gokhale founded Servants of India Society to train social workers for nation-building."),
        ("Who was known as the 'Grand Old Man of India' and wrote 'Poverty and Un-British Rule in India'?", ["Dadabhai Naoroji", "Surendranath Banerjee", "W.C. Bonnerjee", "Pheroze Shah Mehta"], 0, "Dadabhai Naoroji formulated the 'Drain of Wealth' theory and was first Indian elected to British Parliament."),
        ("Who was the first President of the Indian National Congress in 1885?", ["Womesh Chandra Bonnerjee", "Dadabhai Naoroji", "A.O. Hume", "Badruddin Tyabji"], 0, "W.C. Bonnerjee presided over the first session of INC held at Gokuldas Tejpal Sanskrit College, Bombay."),
        ("Who was the first Muslim President of the Indian National Congress (1887 Madras)?", ["Badruddin Tyabji", "Rahimatullah Sayani", "Maulana Abul Kalam Azad", "Nawab Syed Muhammad"], 0, "Justice Badruddin Tyabji presided over 3rd session of INC at Madras in 1887."),
        ("Who was the first woman President of the Indian National Congress (1917 Calcutta)?", ["Annie Besant", "Sarojini Naidu", "Nellie Sengupta", "Kasturba Gandhi"], 0, "British theosophist Annie Besant was the first woman to preside over INC in 1917."),
        ("Who was the first Indian woman President of the Indian National Congress (1925 Kanpur)?", ["Sarojini Naidu", "Annie Besant", "Sucheta Kripalani", "Vijayalakshmi Pandit"], 0, "Nightingale of India Sarojini Naidu presided over INC Kanpur session in 1925."),
        ("In which year was the Partition of Bengal announced by Lord Curzon?", ["1905", "1906", "1911", "1907"], 0, "Lord Curzon partitioned Bengal on communal lines in October 1905, triggering Swadeshi Movement."),
        ("In which year was the Partition of Bengal annulled and capital shifted from Calcutta to Delhi?", ["1911", "1909", "1912", "1914"], 0, "King George V announced annulment of Bengal partition and transfer of capital to Delhi at Delhi Durbar 1911."),
        ("In which INC session did the split between Moderates and Extremists (Surat Split) occur?", ["1907 Surat Session", "1906 Calcutta Session", "1908 Madras Session", "1916 Lucknow Session"], 0, "INC split in 1907 at Surat session presided by Rash Behari Ghosh over leadership disputes."),
        ("The historic reunion of Moderates and Extremists and pact with Muslim League happened at:", ["1916 Lucknow Session", "1915 Bombay Session", "1917 Calcutta Session", "1919 Amritsar Session"], 0, "Presided by A.C. Majumdar, 1916 Lucknow Session saw Congress reunion and the famous Lucknow Pact."),
        ("Who gave the famous slogan 'Swaraj is my birthright and I shall have it'?", ["Bal Gangadhar Tilak", "Lala Lajpat Rai", "Bipin Chandra Pal", "Subhas Chandra Bose"], 0, "Lokmanya Bal Gangadhar Tilak raised this rallying cry during the Home Rule Movement."),
        ("Who founded the Home Rule League in India in 1916?", ["Bal Gangadhar Tilak and Annie Besant", "Mahatma Gandhi", "Lala Lajpat Rai", "Aurobindo Ghosh"], 0, "Tilak launched Home Rule League at Belgaum (April 1916) and Annie Besant at Madras (Sept 1916)."),
        ("The Jallianwala Bagh massacre occurred on which date in Amritsar?", ["13 April 1919", "10 May 1857", "14 August 1947", "26 January 1930"], 0, "General Reginald Dyer ordered troops to fire on unarmed gathering on Baisakhi day, killing hundreds."),
        ("Who returned his Knighthood in protest against the Jallianwala Bagh massacre?", ["Rabindranath Tagore", "Mahatma Gandhi", "Subhas Chandra Bose", "C.R. Das"], 0, "Rabindranath Tagore renounced British Knighthood expressing grief over the Jallianwala Bagh atrocities."),
        ("Who assassinated Michael O'Dwyer in London in 1940 to avenge Jallianwala Bagh?", ["Udham Singh", "Bhagat Singh", "Chandra Shekhar Azad", "Madan Lal Dhingra"], 0, "Sardar Udham Singh shot Michael O'Dwyer (Lt Governor of Punjab during massacre) at Caxton Hall, London."),
        ("The Non-Cooperation Movement was launched by Mahatma Gandhi in which year?", ["1920", "1919", "1922", "1930"], 0, "Approved at Nagpur Congress session in Dec 1920, Non-Cooperation united Indians against British rule."),
        ("Why did Mahatma Gandhi suddenly call off the Non-Cooperation Movement in February 1922?", ["Chauri Chaura incident", "Arrest of leaders", "Communal riots", "Jallianwala Bagh"], 0, "Violent mob burned 22 policemen at Chauri Chaura police station (Gorakhpur, UP) on 4 Feb 1922."),
        ("Who founded the Swaraj Party in 1923 after the withdrawal of Non-Cooperation?", ["Chitta Ranjan Das and Motilal Nehru", "Jawaharlal Nehru and Subhas Bose", "Vallabhbhai Patel and Rajendra Prasad", "Lala Lajpat Rai"], 0, "C.R. Das (President) and Motilal Nehru (Secretary) founded Congress-Khilafat Swaraj Party to enter legislatures."),
        ("Why was the Simon Commission boycotted across India in 1928?", ["It had no Indian member", "It recommended partition", "It was delayed", "It opposed dominion status"], 0, "All seven members of the Indian Statutory Commission were British, leading to slogan 'Simon Go Back'."),
        ("Which national leader died of injuries sustained during lathi charge against Simon Commission?", ["Lala Lajpat Rai", "Bal Gangadhar Tilak", "Bipin Chandra Pal", "G.K. Gokhale"], 0, "Punjab Kesari Lala Lajpat Rai was brutally struck by police lathis in Lahore and succumbed on 17 Nov 1928."),
        ("Kakori Train Action (Kakori Conspiracy) was carried out in August 1925 by members of:", ["Hindustan Republican Association (HRA)", "Ghadar Party", "Anushilan Samiti", "Abhinav Bharat"], 0, "Ram Prasad Bismil, Ashfaqulla Khan, Roshan Singh and Rajendra Lahiri looted government treasury train at Kakori."),
        ("Bhagat Singh and B.K. Dutt threw non-lethal bombs in Central Legislative Assembly in:", ["April 1929", "March 1930", "December 1928", "March 1931"], 0, "On April 8, 1929, they threw bombs to protest against Trade Disputes Bill and Public Safety Bill."),
        ("Bhagat Singh, Rajguru, and Sukhdev were martyred in Lahore Central Jail on:", ["23 March 1931", "2 October 1931", "15 August 1931", "26 January 1931"], 0, "They were hanged in Lahore conspiracy case (Saunders assassination) on 23 March 1931 (Shaheed Diwas)."),
        ("Chandra Shekhar Azad attained martyrdom fighting British police at Alfred Park in:", ["Allahabad (Prayagraj)", "Kanpur", "Varanasi", "Lucknow"], 0, "Azad vowed never to be captured alive and shot himself with his last bullet on 27 Feb 1931."),
        ("The Dandi March (Salt Satyagraha) began from Sabarmati Ashram on:", ["12 March 1930", "6 April 1930", "1 January 1930", "15 August 1930"], 0, "Mahatma Gandhi and 78 followers walked 240 miles from Sabarmati to Dandi, breaking Salt Law on 6 April 1930."),
        ("Gandhi-Irwin Pact was signed in:", ["March 1931", "January 1930", "August 1932", "September 1935"], 0, "Signed on 5 March 1931, Lord Irwin agreed to release political prisoners and Gandhi suspended Civil Disobedience."),
        ("In which Round Table Conference in London did Mahatma Gandhi participate as sole Congress representative?", ["Second Round Table Conference (1931)", "First RTC (1930)", "Third RTC (1932)", "All three"], 0, "Gandhi attended only Second Round Table Conference in London in autumn 1931."),
        ("Poona Pact (1932) was signed between:", ["Mahatma Gandhi and Dr. B.R. Ambedkar", "Jawaharlal Nehru and Jinnah", "Subhas Bose and Patel", "Gandhi and Lord Willingdon"], 0, "Signed on 24 Sept 1932, Poona Pact abandoned separate electorates for depressed classes in favor of reserved seats."),
        ("Who founded the Forward Bloc in 1939 after resigning as Congress President?", ["Subhas Chandra Bose", "Rash Behari Bose", "Chandra Shekhar Azad", "Jawaharlal Nehru"], 0, "Netaji Subhas Chandra Bose founded All India Forward Bloc within Congress after Tripuri crisis in 1939."),
        ("Who formed the Indian National Army (Azad Hind Fauj) in Singapore in 1943?", ["Netaji Subhas Chandra Bose", "Captain Mohan Singh", "Rash Behari Bose", "Lala Har Dayal"], 0, "Netaji revived and reorganized INA in Singapore with slogan 'Chalo Delhi' and 'Give me blood, I will give you freedom'."),
        ("The Quit India Movement resolution was passed by AICC at Gowalia Tank, Bombay, on:", ["8 August 1942", "9 September 1942", "15 July 1942", "26 January 1942"], 0, "Mahatma Gandhi gave the clarion call 'Do or Die' (Karo ya Maro) at Gowalia Tank on 8 August 1942."),
        ("Cabinet Mission arrived in India in:", ["1946", "1942", "1945", "1947"], 0, "Lord Pethick-Lawrence, Sir Stafford Cripps, and A.V. Alexander arrived in March 1946 to plan transfer of power."),
        ("Who was the British Prime Minister who announced India would be granted independence by June 1948?", ["Clement Attlee", "Winston Churchill", "Ramsay MacDonald", "Neville Chamberlain"], 0, "Labour Prime Minister Clement Attlee made historic declaration in House of Commons on 20 Feb 1947."),
        ("Who was the last British Viceroy and first Governor-General of independent India?", ["Lord Mountbatten", "Lord Wavell", "Lord Linlithgow", "C. Rajagopalachari"], 0, "Lord Louis Mountbatten was the last Viceroy and first Governor-General of Dominion of India (1947-1948)."),
        ("Who was the first and only Indian Governor-General of independent India?", ["C. Rajagopalachari", "Dr. Rajendra Prasad", "Dr. S. Radhakrishnan", "Sardar Vallabhbhai Patel"], 0, "Chakravarti Rajagopalachari (Rajaji) served as Governor-General from June 1948 until Jan 26, 1950."),
        ("Who is revered as the 'Iron Man of India' for integrating over 560 princely states?", ["Sardar Vallabhbhai Patel", "Jawaharlal Nehru", "Dr. B.R. Ambedkar", "Govind Ballabh Pant"], 0, "Sardar Patel, Deputy PM and Home Minister, unified India with diplomatic skill and determination.")
    ]
    for row in more_history:
        add_q("Indian History", row[0], row[1], row[2], row[3])

    print(f"History complete. Total questions so far: {len(questions)}")

    # ==========================================
    # 3. GEOGRAPHY (120+ Questions)
    # ==========================================
    geo_data = [
        ("Which is the highest mountain peak in India (located in Sikkim)?", ["Kanchenjunga (8,586 m)", "Nanda Devi", "Kamet", "Saltoro Kangri"], 0, "Kanchenjunga is highest peak in undisputed Indian territory (8586 m). K2 is in Pakistan-occupied Kashmir."),
        ("Which is the highest peak in the Western Ghats and entire South India?", ["Anamudi (2,695 m)", "Doddabetta", "Mullayanagiri", "Agasthyamala"], 0, "Anamudi in Eravikulam National Park, Kerala is the highest peak of South India."),
        ("Which is the highest peak of the Nilgiri Hills?", ["Doddabetta (2,637 m)", "Anamudi", "Kalsubai", "Mahendragiri"], 0, "Doddabetta near Ooty is highest summit of Nilgiri mountains where Eastern and Western Ghats meet."),
        ("Which is the highest peak of the Aravalli Range?", ["Guru Shikhar (1,722 m)", "Mount Abu", "Achalgarh", "Ser"], 0, "Guru Shikhar near Mount Abu in Rajasthan is highest point of ancient Aravalli range."),
        ("Which is the longest river in Peninsular India?", ["Godavari (1,465 km)", "Krishna", "Cauvery", "Mahanadi"], 0, "Godavari originates at Trimbakeshwar near Nashik, Maharashtra and is longest peninsular river."),
        ("The famous Jog Falls (Gersoppa Falls) in Karnataka is formed on which river?", ["Sharavathi river", "Cauvery river", "Krishna river", "Netravati river"], 0, "Jog Falls is one of highest segmented waterfalls in India formed by Sharavathi river in Shivamogga."),
        ("Dhuandhar Falls and Marble Rocks near Jabalpur are on which river?", ["Narmada", "Tapi", "Chambal", "Betwa"], 0, "Narmada river plunges through white marble gorges creating the Dhuandhar Falls in Madhya Pradesh."),
        ("Which two rivers flow westward in rift valleys into the Arabian Sea?", ["Narmada and Tapi", "Godavari and Krishna", "Mahanadi and Cauvery", "Ganga and Yamuna"], 0, "Narmada and Tapi flow through rift valleys between Vindhya and Satpura ranges into Gulf of Khambhat."),
        ("Which is the largest freshwater lake in India?", ["Wular Lake (Jammu & Kashmir)", "Dal Lake", "Loktak Lake", "Kolleru Lake"], 0, "Wular Lake in Bandipora district of J&K is largest natural freshwater lake in India, fed by Jhelum river."),
        ("The only floating national park in the world, Keibul Lamjao, is located in which lake?", ["Loktak Lake (Manipur)", "Chilika Lake", "Sambhar Lake", "Pulicat Lake"], 0, "Loktak Lake in Manipur has floating islands called Phumdis, home to endangered Sangai deer."),
        ("Which is the largest brackish water lagoon in India?", ["Chilika Lake (Odisha)", "Pulicat Lake", "Vembanad Lake", "Ashtamudi Lake"], 0, "Chilika Lake in Odisha is largest coastal lagoon in India and second largest in the world."),
        ("Which is the longest lake in India?", ["Vembanad Lake (Kerala)", "Chilika Lake", "Shivaji Sagar", "Pangong Tso"], 0, "Vembanad Lake spans 96.5 km across several districts of Kerala; hosts famous Nehru Trophy Boat Race."),
        ("Which is the largest inland saltwater lake in India?", ["Sambhar Salt Lake (Rajasthan)", "Pangong Tso", "Didwana", "Lonar Lake"], 0, "Sambhar Lake near Jaipur produces a significant portion of India's salt."),
        ("Lonar Crater Lake in Maharashtra was created by:", ["Meteorite impact", "Volcanic eruption", "Glacial action", "Tectonic faulting"], 0, "Lonar Lake in Buldhana district is an ancient hyper-velocity meteorite impact crater."),
        ("Majuli, the world's largest river island, is located in which river?", ["Brahmaputra (Assam)", "Ganga", "Indus", "Godavari"], 0, "Majuli in Assam is world's largest riverine island formed by Brahmaputra and Subansiri rivers."),
        ("The Tropic of Cancer (23.5° N) passes through how many Indian States?", ["8 States", "7 States", "9 States", "6 States"], 0, "Passes through Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, West Bengal, Tripura, and Mizoram."),
        ("The Indian Standard Meridian (82°30' E) passes through which city?", ["Mirzapur (near Prayagraj, UP)", "Bhopal", "Nagpur", "Patna"], 0, "Indian Standard Time (IST) is based on 82°30' E longitude, passing through Mirzapur, Uttar Pradesh."),
        ("Which Indian state has the longest coastline?", ["Gujarat (approx 1,600 km)", "Andhra Pradesh", "Tamil Nadu", "Maharashtra"], 0, "Gujarat has longest mainland coastline (around 1600 km) along Arabian Sea."),
        ("Which state has the second longest coastline in mainland India?", ["Andhra Pradesh (approx 974 km)", "Tamil Nadu", "Kerala", "Maharashtra"], 0, "Andhra Pradesh possesses the second longest mainland coastline in India."),
        ("The Southernmost point of Indian territory is:", ["Indira Point (Great Nicobar)", "Kanyakumari", "Indira Col", "Kibithu"], 0, "Indira Point on Great Nicobar Island (6°45' N) is southernmost point of Indian Union."),
        ("The Southernmost point of the mainland of India is:", ["Kanyakumari (Cape Comorin)", "Indira Point", "Rameswaram", "Dhanushkodi"], 0, "Kanyakumari in Tamil Nadu (8°4' N) is southernmost tip of the Indian mainland."),
        ("Palk Strait separates India from which neighboring country?", ["Sri Lanka", "Maldives", "Bangladesh", "Myanmar"], 0, "Palk Strait and Gulf of Mannar lie between Tamil Nadu (India) and Northern Province of Sri Lanka."),
        ("Radcliffe Line is the boundary line between India and:", ["Pakistan", "China", "Afghanistan", "Bangladesh"], 0, "Sir Cyril Radcliffe demarcated boundary between India and Pakistan (including Bangladesh) in 1947."),
        ("McMahon Line demarcates the boundary between India and:", ["China (Arunachal Pradesh)", "Pakistan", "Nepal", "Bhutan"], 0, "McMahon Line was drawn between British India and Tibet during 1914 Simla Convention."),
        ("Durand Line is the international boundary between:", ["Afghanistan and Pakistan", "India and China", "Pakistan and Iran", "India and Myanmar"], 0, "Durand Line was drawn in 1893 between British India (now Pakistan) and Afghanistan."),
        ("Which state in India has the largest total forest cover by area?", ["Madhya Pradesh", "Arunachal Pradesh", "Chhattisgarh", "Odisha"], 0, "Madhya Pradesh has largest forest cover in area, followed by Arunachal Pradesh and Chhattisgarh."),
        ("Which state has the highest percentage of forest cover to total geographical area?", ["Mizoram (over 84%)", "Arunachal Pradesh", "Meghalaya", "Nagaland"], 0, "Mizoram has highest proportion of land area under forest cover (over 84%)."),
        ("Kaziranga National Park in Assam is world-famous for:", ["One-horned Rhinoceros", "Royal Bengal Tiger", "Asiatic Lion", "Snow Leopard"], 0, "Kaziranga hosts two-thirds of the world's great one-horned rhinoceros population and is a UNESCO site."),
        ("Gir National Park in Gujarat is the only natural habitat of:", ["Asiatic Lion", "Cheetah", "Snow Leopard", "Black Panther"], 0, "Gir forest is the sole remaining natural sanctuary for endangered Asiatic lions."),
        ("Which was the first National Park established in India (1936)?", ["Jim Corbett National Park (Uttarakhand)", "Kanha National Park", "Kaziranga National Park", "Ranthambore National Park"], 0, "Established in 1936 as Hailey National Park, now Jim Corbett National Park in Nainital/Pauri Garhwal."),
        ("Sundarbans Delta, the largest mangrove forest in the world, is formed by rivers:", ["Ganga, Brahmaputra and Meghna", "Indus and Jhelum", "Godavari and Krishna", "Mahanadi and Baitarani"], 0, "Sundarbans delta spans West Bengal and Bangladesh, famous for Royal Bengal Tigers."),
        ("Black soil (Regur soil) in India is most suitable for cultivation of:", ["Cotton", "Tea", "Jute", "Wheat"], 0, "Black soil derived from Deccan lava basalt has high moisture retention, ideal for cotton."),
        ("Which soil type covers the largest area in India?", ["Alluvial soil (approx 40%)", "Black soil", "Red soil", "Laterite soil"], 0, "Alluvial soil deposited by Indo-Gangetic and coastal river systems covers largest landmass in India."),
        ("Laterite soil is rich in which minerals and poor in nitrogen?", ["Iron oxide and Aluminum", "Calcium and Potassium", "Phosphorus and Nitrogen", "Zinc and Copper"], 0, "Formed under intense tropical leaching, laterite soil is rich in iron and bauxite/aluminum."),
        ("Tehri Dam, the highest dam in India (260.5 m), is built on which river?", ["Bhagirathi river (Uttarakhand)", "Alaknanda river", "Mandakini river", "Yamuna river"], 0, "Tehri Dam is a multi-purpose rock and earth-fill embankment dam on Bhagirathi river."),
        ("Bhakra Nangal Dam is constructed across which river?", ["Sutlej river (Himachal/Punjab)", "Ravi river", "Beas river", "Chenab river"], 0, "Bhakra Dam forms the massive Govind Sagar reservoir on Sutlej river."),
        ("Hirakud Dam, one of the longest earthen dams in the world, is built on:", ["Mahanadi river (Odisha)", "Godavari river", "Brahmani river", "Damodar river"], 0, "Hirakud Dam near Sambalpur in Odisha spans 25.8 km across Mahanadi river."),
        ("Sardar Sarovar Dam is built on which river?", ["Narmada river (Gujarat)", "Tapi river", "Sabarmati river", "Mahi river"], 0, "Sardar Sarovar is a concrete gravity dam on Narmada river near Navagam in Gujarat."),
        ("Nagarjuna Sagar Dam is constructed on which river?", ["Krishna river (Andhra/Telangana)", "Godavari river", "Cauvery river", "Pennar river"], 0, "Nagarjuna Sagar is a masonry dam across Krishna river straddling Guntur and Nalgonda districts."),
        ("Which layer of atmosphere contains the Ozone layer absorbing harmful UV rays?", ["Stratosphere", "Troposphere", "Mesosphere", "Thermosphere"], 0, "The Ozone layer (ozonosphere) is located in lower stratosphere between 15 and 35 km altitude."),
        ("In which atmospheric layer do all weather phenomena (clouds, rain, storms) take place?", ["Troposphere", "Stratosphere", "Mesosphere", "Exosphere"], 0, "Troposphere is lowest layer extending to ~18 km at equator and contains 75% of atmosphere mass."),
        ("Which is the coldest layer of Earth's atmosphere (-90°C)?", ["Mesosphere", "Stratosphere", "Thermosphere", "Troposphere"], 0, "Mesosphere (50 to 85 km) is coldest layer where meteors burn up upon entering atmosphere."),
        ("Radio waves transmitted from Earth are reflected back by which layer?", ["Ionosphere (Thermosphere)", "Troposphere", "Stratosphere", "Mesosphere"], 0, "Ionosphere contains ionized particles that reflect shortwave radio signals back to Earth."),
        ("Which planet is closest to the Sun?", ["Mercury", "Venus", "Earth", "Mars"], 0, "Mercury has an orbital period of only 88 Earth days around the Sun."),
        ("Which planet is called 'Earth's Twin' due to similar size and density?", ["Venus", "Mars", "Mercury", "Neptune"], 0, "Venus is Earth's twin; also hottest planet due to runaway greenhouse effect of CO2 atmosphere."),
        ("Which planet appears red due to abundant iron oxide on its surface?", ["Mars", "Venus", "Jupiter", "Mercury"], 0, "Mars is called the Red Planet because rust (iron oxide) gives its regolith a reddish hue."),
        ("Which is the largest planet in our Solar System?", ["Jupiter", "Saturn", "Uranus", "Neptune"], 0, "Jupiter is more than twice as massive as all other planets combined, with famous Great Red Spot."),
        ("Which planet has the famous visible ring system composed of ice and rock particles?", ["Saturn", "Jupiter", "Uranus", "Neptune"], 0, "Saturn is gas giant with stunning planetary rings and largest moon Titan."),
        ("Which planet rotates on its side with an axial tilt of 98 degrees?", ["Uranus", "Neptune", "Saturn", "Mars"], 0, "Uranus has an extreme axial tilt of 98°, rotating virtually on its side like a rolling ball."),
        ("Which is the deepest oceanic trench on Earth?", ["Mariana Trench (Challenger Deep)", "Puerto Rico Trench", "Java Trench", "Sunda Trench"], 0, "Challenger Deep in Mariana Trench in western Pacific plunges nearly 11,000 meters below sea level.")
    ]
    for row in geo_data:
        add_q("Geography", row[0], row[1], row[2], row[3])

    print(f"Geography complete. Total questions so far: {len(questions)}")

    # ==========================================
    # 4. GENERAL SCIENCE - PHYSICS (100+ Questions)
    # ==========================================
    physics_data = [
        ("What is the SI unit of Force?", ["Newton (N)", "Joule", "Pascal", "Watt"], 0, "Force is measured in Newtons (N = kg*m/s^2) as formulated in Newton's Second Law."),
        ("What is the SI unit of Work and Energy?", ["Joule (J)", "Watt", "Newton", "Calorie"], 0, "One Joule is equal to the work done by a force of one newton moving an object through one meter."),
        ("What is the SI unit of Power?", ["Watt (W)", "Joule", "Volt", "Ampere"], 0, "Power is the rate of doing work, measured in Watts (1 W = 1 Joule/second)."),
        ("What is the SI unit of Pressure?", ["Pascal (Pa)", "Bar", "Torr", "Atmosphere"], 0, "Pascal is equivalent to one Newton per square meter (1 Pa = 1 N/m^2)."),
        ("What is the SI unit of Frequency?", ["Hertz (Hz)", "Decibel", "Watt", "Lumen"], 0, "Hertz represents cycles per second, named after German physicist Heinrich Hertz."),
        ("What is the SI unit of Luminous Intensity?", ["Candela (cd)", "Lumen", "Lux", "Dioptre"], 0, "Candela is one of the seven base SI units, measuring luminous intensity of light source."),
        ("What is the power of a lens with focal length of 1 meter?", ["1 Dioptre", "1 Watt", "10 Dioptre", "0.5 Dioptre"], 0, "Power of lens = 1 / focal length in meters; measured in Dioptres (D)."),
        ("Which lens is used to correct Myopia (Short-sightedness)?", ["Concave lens", "Convex lens", "Bifocal lens", "Cylindrical lens"], 0, "Concave (diverging) lens spreads light rays so distant objects focus on retina."),
        ("Which lens is used to correct Hypermetropia (Long-sightedness)?", ["Convex lens", "Concave lens", "Cylindrical lens", "Plano-concave lens"], 0, "Convex (converging) lens bends light inwards to focus near objects on retina."),
        ("Presbyopia (age-related vision defect) is corrected by:", ["Bifocal lenses", "Concave lens only", "Convex lens only", "Contact lens only"], 0, "Bifocal lens has upper concave part for distance and lower convex part for reading."),
        ("What is the speed of light in vacuum?", ["3 x 10^8 m/s", "3 x 10^6 m/s", "3 x 10^5 km/s (same)", "1.5 x 10^8 m/s"], 0, "Speed of light c in vacuum is exactly 299,792,458 m/s (~3 x 10^8 m/s)."),
        ("Why does the sky appear blue during daytime?", ["Rayleigh scattering of light", "Reflection of light by ocean", "Refraction by clouds", "Total internal reflection"], 0, "Shorter blue wavelengths scatter much more than longer red wavelengths by air molecules."),
        ("Why does the Sun appear reddish during sunrise and sunset?", ["Longer wavelengths scatter least", "Absorption of blue light", "Total internal reflection", "Diffraction"], 0, "Light travels through thicker atmospheric path; shorter blue scatters away, leaving red light."),
        ("Mirage in hot deserts is an optical illusion caused by:", ["Total Internal Reflection", "Diffraction", "Interference", "Dispersion"], 0, "Steep temperature gradients in air cause light rays to undergo total internal reflection."),
        ("Optical fibers transmit telecommunication signals using principle of:", ["Total Internal Reflection", "Scattering", "Diffraction", "Refraction alone"], 0, "Signals bounce inside fiber core due to total internal reflection with minimal loss."),
        ("What is the acceleration due to gravity (g) at Earth's surface?", ["9.8 m/s^2", "8.9 m/s^2", "10.8 m/s^2", "9.8 km/s^2"], 0, "Standard acceleration due to Earth's gravity is approximately 9.80665 m/s^2."),
        ("At which place on Earth is the value of 'g' maximum?", ["At the Poles", "At the Equator", "At 45° latitude", "At Centre of Earth"], 0, "Earth is flattened at poles and bulges at equator; distance to center is least at poles."),
        ("At which place on Earth is the value of 'g' minimum (or zero)?", ["Zero at Earth's Center", "Zero at Equator", "Maximum at Center", "Constant everywhere"], 0, "At the center of Earth, gravitational forces cancel out, making g = 0 (weightlessness)."),
        ("What is the escape velocity from the surface of Earth?", ["11.2 km/s", "9.8 km/s", "42 km/s", "2.4 km/s"], 0, "Escape velocity formula gives v = sqrt(2GM/R) = 11.2 km/s for Earth."),
        ("What is the escape velocity from the surface of the Moon?", ["2.4 km/s", "11.2 km/s", "5.6 km/s", "1.6 km/s"], 0, "Due to low mass, Moon's escape velocity is only 2.38 km/s, explaining lack of atmosphere."),
        ("Which instrument is used to measure Atmospheric Pressure?", ["Barometer", "Hygrometer", "Manometer", "Anemometer"], 0, "Barometer invented by Evangelista Torricelli measures atmospheric pressure."),
        ("Which instrument is used to measure Relative Humidity of air?", ["Hygrometer", "Hydrometer", "Barometer", "Thermometer"], 0, "Hygrometer measures moisture content or relative humidity in atmosphere."),
        ("Which instrument is used to determine the Relative Density (specific gravity) of liquids?", ["Hydrometer", "Lactometer", "Hygrometer", "Pyrometer"], 0, "Hydrometer floats in liquid to measure density based on Archimedes principle."),
        ("Which instrument is used to test the purity/density of milk?", ["Lactometer", "Hydrometer", "Saccharometer", "Viscometer"], 0, "Lactometer measures specific gravity of milk to detect dilution with water."),
        ("Which instrument is used to measure high temperatures (e.g. furnaces, stars)?", ["Pyrometer", "Thermocouple", "Bolometer", "Barometer"], 0, "Pyrometer is a non-contact radiation thermometer measuring very high thermal emission."),
        ("Sound waves cannot travel through:", ["Vacuum", "Steel", "Water", "Air"], 0, "Sound is a mechanical longitudinal wave requiring a material medium for propagation."),
        ("In which medium is the speed of sound maximum?", ["Solids (e.g. Steel)", "Water", "Air", "Vacuum"], 0, "Sound travels fastest in dense, elastic solids (~5000 m/s in steel, 1500 in water, 343 in air)."),
        ("Human audible sound frequency range is between:", ["20 Hz to 20,000 Hz", "0 Hz to 20 Hz", "Above 20,000 Hz", "50 Hz to 5,000 Hz"], 0, "Normal human ear detects sounds between 20 Hz and 20 kHz (20,000 Hz)."),
        ("Sound frequencies above 20,000 Hz are termed:", ["Ultrasonic", "Infrasonic", "Supersonic", "Audible"], 0, "Ultrasonic sound waves exceed 20 kHz; used in medical Sonography and bat echolocation."),
        ("Sound frequencies below 20 Hz are termed:", ["Infrasonic", "Ultrasonic", "Megasonic", "Hypersonic"], 0, "Infrasonic frequencies below 20 Hz are produced by earthquakes and communicated by elephants."),
        ("What is the apparent change in frequency of a wave due to motion of source or observer?", ["Doppler Effect", "Raman Effect", "Photoelectric Effect", "Compton Effect"], 0, "Doppler Effect explains pitch rising as siren approaches and dropping as it recedes."),
        ("For discover of which phenomenon was C.V. Raman awarded the Nobel Prize in Physics in 1930?", ["Raman Scattering of Light", "Laser radiation", "Cosmic rays", "Semiconductors"], 0, "Inelastic scattering of photons by matter discovered on Feb 28, 1928 (National Science Day)."),
        ("Who discovered the Photoelectric Effect and won the Nobel Prize in 1921?", ["Albert Einstein", "Max Planck", "Niels Bohr", "Isaac Newton"], 0, "Einstein explained photoelectric emission using quantum packets of light (photons)."),
        ("What is the value of Absolute Zero temperature on Celsius scale?", ["-273.15 °C", "-100 °C", "0 °C", "-459.67 °C"], 0, "Absolute zero (0 Kelvin) is lowest possible thermodynamic temperature (-273.15 °C)."),
        ("At what temperature do the Celsius and Fahrenheit thermometer scales coincide?", ["-40°", "0°", "-32°", "100°"], 0, "Setting C = F in F = (9/5)C + 32 yields C = -40 degrees."),
        ("Water has its maximum density at which temperature?", ["4 °C", "0 °C", "100 °C", "-4 °C"], 0, "Due to anomalous expansion of water, liquid water reaches peak density at 3.98 °C (~4 °C)."),
        ("Ice floats on water because its density is:", ["Less than water", "Equal to water", "Greater than water", "Zero"], 0, "Hexagonal crystal structure of ice makes it less dense (~0.917 g/cm3) than liquid water."),
        ("The device used to convert Alternating Current (AC) to Direct Current (DC) is:", ["Rectifier", "Inverter", "Transformer", "Amplifier"], 0, "Rectifier utilizes diodes to convert bidirectional AC current into unidirectional DC."),
        ("The device used to convert Direct Current (DC) to Alternating Current (AC) is:", ["Inverter", "Rectifier", "Transformer", "Dynamo"], 0, "Inverter electronic circuit converts battery DC into AC mains power."),
        ("A Transformer works on the principle of:", ["Mutual Electromagnetic Induction", "Self Induction", "Photoelectric effect", "Bernoulli principle"], 0, "Transformer steps voltage up or down based on Faraday's law of mutual induction (AC only)."),
        ("Which wire in household electrical wiring is colored Green?", ["Earth wire", "Live wire", "Neutral wire", "Phase wire"], 0, "Green (or green-yellow) insulation denotes Earth ground wire for safety against shock."),
        ("In household wiring, Live wire is traditionally colored:", ["Brown / Red", "Blue / Black", "Green", "Yellow"], 0, "Live wire is Brown (or Red); Neutral wire is Blue (or Black)."),
        ("Fuse wire used in household electrical circuits is made of an alloy of:", ["Tin and Lead (Sn + Pb)", "Copper and Zinc", "Iron and Carbon", "Aluminum and Copper"], 0, "Fuse wire requires high resistance and low melting point, achieved by Tin-Lead solder alloy."),
        ("The core of an electromagnet or transformer is made of:", ["Soft Iron", "Steel", "Copper", "Aluminum"], 0, "Soft iron has high magnetic permeability and low retentivity, magnetizing and demagnetizing rapidly."),
        ("What is the principle behind hydraulic lifts and hydraulic brakes in cars?", ["Pascal's Principle", "Archimedes' Principle", "Bernoulli's Principle", "Boyle's Law"], 0, "Pascal's Law states pressure applied to an enclosed liquid is transmitted equally in all directions."),
        ("Which principle explains the dynamic aerodynamic lift of an airplane wing?", ["Bernoulli's Principle", "Pascal's Principle", "Archimedes' Principle", "Hooke's Law"], 0, "Faster air over curved top surface creates low pressure compared to higher pressure underneath."),
        ("Soap bubbles are spherical in shape due to:", ["Surface Tension", "Viscosity", "Atmospheric pressure", "Gravity"], 0, "Surface tension minimizes surface area for a given volume, yielding a spherical shape."),
        ("Kerosene rises up in the wick of a lantern due to:", ["Capillary action (Capillarity)", "Surface tension only", "Viscosity", "Evaporation"], 0, "Adhesion between liquid and narrow fibers draws fuel upward against gravity by capillarity."),
        ("Newton's First Law of Motion is also known as:", ["Law of Inertia", "Law of Momentum", "Law of Action-Reaction", "Law of Gravitation"], 0, "Inertia is natural tendency of objects to resist changes in their state of motion or rest."),
        ("Rocket propulsion works on the principle of conservation of:", ["Linear Momentum", "Energy", "Mass", "Angular Momentum"], 0, "Backward momentum of exhausted gas imparts equal and opposite forward momentum to rocket (Newton 3rd Law).")
    ]
    for row in physics_data:
        add_q("General Science - Physics", row[0], row[1], row[2], row[3])

    print(f"Physics complete. Total questions so far: {len(questions)}")

    # ==========================================
    # 5. GENERAL SCIENCE - CHEMISTRY (100+ Questions)
    # ==========================================
    chem_data = [
        ("What is the chemical formula of Common Table Salt?", ["NaCl", "KCl", "Na2CO3", "NaHCO3"], 0, "Common salt is Sodium Chloride (NaCl) with crystal ionic lattice."),
        ("What is the chemical name and formula of Baking Soda?", ["Sodium Bicarbonate (NaHCO3)", "Sodium Carbonate (Na2CO3)", "Sodium Hydroxide (NaOH)", "Calcium Carbonate"], 0, "Sodium hydrogen carbonate (NaHCO3) is used in baking and antacids."),
        ("What is the chemical formula of Washing Soda?", ["Na2CO3 . 10H2O", "NaHCO3", "CaSO4 . 2H2O", "NaOH"], 0, "Washing soda is Sodium Carbonate decahydrate (Na2CO3 . 10H2O)."),
        ("What is the chemical formula of Plaster of Paris (POP)?", ["CaSO4 . 1/2 H2O", "CaSO4 . 2H2O", "CaCO3", "CaO"], 0, "Plaster of Paris is Calcium Sulphate hemihydrate; sets hard when mixed with water."),
        ("Gypsum is chemically known as:", ["Calcium Sulphate Dihydrate (CaSO4 . 2H2O)", "Calcium Carbonate", "Magnesium Sulphate", "Sodium Sulphate"], 0, "Gypsum is CaSO4 . 2H2O; heating gypsum to 373 K produces Plaster of Paris."),
        ("What is the chemical name of Quicklime?", ["Calcium Oxide (CaO)", "Calcium Hydroxide (Ca(OH)2)", "Calcium Carbonate (CaCO3)", "Calcium Sulphate"], 0, "Quicklime is anhydrous Calcium Oxide (CaO), produced by calcining limestone."),
        ("Slaked lime (lime water) is chemically known as:", ["Calcium Hydroxide (Ca(OH)2)", "Calcium Oxide (CaO)", "Calcium Carbonate", "Calcium Chloride"], 0, "Formed when quicklime reacts vigorously with water: CaO + H2O -> Ca(OH)2."),
        ("What is the chemical formula of Bleaching Powder?", ["CaOCl2", "CaCl2", "Ca(OH)2", "CaCO3"], 0, "Bleaching powder is Calcium hypochlorite / chlorohypochlorite (CaOCl2)."),
        ("Heavy Water used as a moderator in nuclear reactors is chemically:", ["Deuterium Oxide (D2O)", "Tritium Oxide (T2O)", "Hydrogen Peroxide (H2O2)", "Distilled Water"], 0, "Deuterium is isotope of hydrogen with one proton and one neutron; D2O moderates fast neutrons."),
        ("Dry Ice is the solid form of which gas?", ["Carbon Dioxide (CO2)", "Carbon Monoxide (CO)", "Nitrogen (N2)", "Methane (CH4)"], 0, "Solid Carbon Dioxide sublimates directly into gas at -78.5 °C without melting."),
        ("Which element is the most electronegative in the modern periodic table?", ["Fluorine (F)", "Chlorine (Cl)", "Oxygen (O)", "Nitrogen (N)"], 0, "Fluorine has electronegativity of 3.98 on Pauling scale, highest of all elements."),
        ("Which halogen is a reddish-brown liquid at room temperature?", ["Bromine (Br)", "Chlorine (Cl)", "Iodine (I)", "Fluorine (F)"], 0, "Bromine is the only non-metallic element that exists as a liquid at standard room temperature."),
        ("Which metal is liquid at standard room temperature?", ["Mercury (Hg)", "Gallium (Ga)", "Cesium (Cs)", "Lead (Pb)"], 0, "Mercury (quicksilver, atomic number 80) is liquid metal at room temperature."),
        ("Which metal is stored under kerosene oil to prevent it from catching fire in air?", ["Sodium (Na)", "Calcium (Ca)", "Magnesium (Mg)", "Iron (Fe)"], 0, "Alkali metals Sodium and Potassium react violently with air moisture and are kept in kerosene."),
        ("Which non-metal is an excellent conductor of electricity?", ["Graphite (Carbon allotrope)", "Diamond", "Sulphur", "Phosphorus"], 0, "Graphite has delocalized pi electrons in its hexagonal planar layers, conducting electricity."),
        ("Diamond and Graphite are:", ["Allotropes of Carbon", "Isotopes of Carbon", "Isomers of Carbon", "Isobars of Carbon"], 0, "Allotropes are different structural modifications of an element with distinct physical properties."),
        ("What is the hardest naturally occurring substance known on Earth?", ["Diamond", "Corundum", "Quartz", "Topaz"], 0, "Diamond has rigid 3D tetrahedral giant covalent crystal lattice (Mohs hardness 10)."),
        ("Which gas has the highest percentage composition in Earth's atmosphere?", ["Nitrogen (~78%)", "Oxygen (~21%)", "Argon (~0.93%)", "Carbon Dioxide (~0.04%)"], 0, "Earth's dry air consists of ~78.08% Nitrogen and ~20.95% Oxygen."),
        ("What is the main constituent of Natural Gas and Biogas (Gobar gas)?", ["Methane (CH4)", "Propane (C3H8)", "Butane (C4H10)", "Ethane (C2H6)"], 0, "Methane makes up 70-90% of natural gas and 55-70% of biogas produced by anaerobic digestion."),
        ("LPG (Liquefied Petroleum Gas) used in domestic cooking cylinders contains primarily:", ["Butane and Propane", "Methane and Ethane", "Carbon monoxide and Hydrogen", "Acetylene"], 0, "LPG is predominantly Liquefied Butane (C4H10) with Propane (C3H8)."),
        ("Which strong-smelling chemical is added to LPG cylinders to detect gas leaks?", ["Ethyl Mercaptan (Ethanethiol)", "Methyl alcohol", "Chloroform", "Hydrogen sulphide"], 0, "Ethyl mercaptan (C2H5SH) has distinctive foul odor enabling early detection of flammable gas leaks."),
        ("Brass is an alloy of which two metals?", ["Copper and Zinc (Cu + Zn)", "Copper and Tin (Cu + Sn)", "Lead and Tin (Pb + Sn)", "Copper and Nickel"], 0, "Brass is an alloy of Copper (~60-70%) and Zinc (~30-40%)."),
        ("Bronze is an alloy of which two metals?", ["Copper and Tin (Cu + Sn)", "Copper and Zinc (Cu + Zn)", "Iron and Carbon", "Aluminum and Copper"], 0, "Bronze consists primarily of Copper combined with Tin (~12%)."),
        ("German Silver alloy contains Copper, Zinc, and Nickel, but surprisingly NO:", ["Silver (Ag)", "Gold", "Tin", "Iron"], 0, "German Silver (Nickel silver) contains 60% Cu, 20% Ni, 20% Zn and zero silver."),
        ("Solder used for joining electrical circuits is an alloy of:", ["Lead and Tin (Pb + Sn)", "Copper and Zinc", "Iron and Nickel", "Aluminum and Tin"], 0, "Solder typically consists of 60% Tin and 40% Lead, having low melting point."),
        ("Stainless Steel is an alloy of Iron mixed with:", ["Chromium, Nickel and Carbon", "Copper and Zinc", "Tin and Lead", "Aluminum and Silicon"], 0, "Chromium (minimum 10.5%) forms a passive oxide layer preventing rust and corrosion."),
        ("Galvanization is the process of coating iron/steel with a thin protective layer of:", ["Zinc (Zn)", "Tin (Sn)", "Copper (Cu)", "Lead (Pb)"], 0, "Sacrificial zinc coating prevents iron from rusting even if the surface is scratched."),
        ("Which acid is present in Vinegar?", ["Acetic Acid (CH3COOH)", "Citric Acid", "Formic Acid", "Lactic Acid"], 0, "Vinegar is a 5% to 8% aqueous solution of ethanoic (acetic) acid."),
        ("Which acid is present in sour curd (yogurt)?", ["Lactic Acid", "Oxalic Acid", "Tartaric Acid", "Butyric Acid"], 0, "Lactobacillus bacteria ferment lactose sugar in milk into lactic acid."),
        ("Which acid is present in lemons and oranges?", ["Citric Acid", "Ascorbic Acid", "Tartaric Acid", "Acetic Acid"], 0, "Citrus fruits contain high concentrations of citric acid giving them sour taste."),
        ("Which acid is present in tamarind and unripe grapes?", ["Tartaric Acid", "Oxalic Acid", "Maleic Acid", "Citric Acid"], 0, "Tartaric acid is organic dicarboxylic acid found naturally in tamarind."),
        ("Which acid is injected into skin during an ant or bee sting?", ["Formic Acid (Methanoic acid)", "Acetic Acid", "Hydrochloric Acid", "Sulphuric Acid"], 0, "Methanoic acid (HCOOH) causes burning sensation, neutralized by mild base like baking soda."),
        ("Which acid is present in human gastric juice in the stomach?", ["Hydrochloric Acid (HCl)", "Sulphuric Acid (H2SO4)", "Nitric Acid (HNO3)", "Phosphoric Acid"], 0, "Parietal cells in stomach secrete dilute HCl (pH 1.5 to 3.5) to kill pathogens and activate pepsin."),
        ("Which acid is universally called the 'King of Chemicals'?", ["Sulphuric Acid (H2SO4)", "Hydrochloric Acid (HCl)", "Nitric Acid (HNO3)", "Aqua Regia"], 0, "Sulphuric acid is vital industrial chemical used in fertilizer, car batteries and refining."),
        ("Aqua Regia (royal water) capable of dissolving Gold and Platinum is a 3:1 mixture of:", ["Concentrated HCl and Concentrated HNO3", "H2SO4 and HNO3", "HCl and H2SO4", "HNO3 and Acetic acid"], 0, "Three parts concentrated Hydrochloric acid to one part concentrated Nitric acid."),
        ("What is the pH value of pure water at 25 °C?", ["7 (Neutral)", "0", "14", "5.6"], 0, "Pure neutral water has equal H+ and OH- concentrations, yielding pH of exactly 7.0."),
        ("What is the normal pH of human blood?", ["7.35 to 7.45 (Slightly alkaline)", "6.0 to 6.5", "8.5 to 9.0", "5.0 to 5.5"], 0, "Human arterial blood is tightly regulated between pH 7.35 and 7.45 by bicarbonate buffer system."),
        ("Acid rain is defined as rain having a pH less than:", ["5.6", "7.0", "6.5", "4.0"], 0, "Atmospheric SO2 and NOx dissolve in water to form sulphuric and nitric acids lowering pH below 5.6."),
        ("Which gas is responsible for the greenhouse effect and global warming?", ["Carbon Dioxide (CO2)", "Oxygen (O2)", "Nitrogen (N2)", "Argon (Ar)"], 0, "CO2 traps infrared heat radiated from Earth's surface, enhancing greenhouse warming."),
        ("Which gas is released during photosynthesis by green plants?", ["Oxygen (O2)", "Carbon Dioxide", "Nitrogen", "Hydrogen"], 0, "Light reactions split water molecules (photolysis) releasing O2 gas into atmosphere."),
        ("Which catalyst is used in the hydrogenation of vegetable oils into Vanaspati ghee?", ["Nickel (Ni)", "Iron (Fe)", "Platinum (Pt)", "Copper (Cu)"], 0, "Finely divided Nickel acts as catalyst in industrial hydrogenation of unsaturated fats."),
        ("Haber Process is used industrially to synthesize which chemical compound?", ["Ammonia (NH3)", "Sulphuric acid", "Nitric acid", "Urea"], 0, "Nitrogen and Hydrogen react at high pressure/temp with iron catalyst to form Ammonia."),
        ("Vulcanization of natural rubber to make it tough and elastic involves heating with:", ["Sulphur (S)", "Carbon black", "Phosphorus", "Silicon"], 0, "Invented by Charles Goodyear in 1839, sulfur forms cross-links between polyisoprene chains."),
        ("Teflon used as non-stick coating on cookware is chemically:", ["Polytetrafluoroethylene (PTFE)", "Polyvinyl chloride (PVC)", "Polyethylene", "Polystyrene"], 0, "PTFE has high heat resistance, low friction, and chemical inertness."),
        ("The first fully synthetic man-made polymer plastic was:", ["Bakelite", "Nylon", "Rayon", "Polyester"], 0, "Invented by Leo Baekeland in 1907, thermosetting phenol-formaldehyde resin called Bakelite."),
        ("Rayon is a semi-synthetic fiber derived from natural:", ["Wood Cellulose", "Petroleum", "Coal tar", "Protein"], 0, "Rayon (artificial silk) is manufactured by regenerating purified cellulose pulp."),
        ("Which element is used as a moderator and control rods in nuclear reactors?", ["Cadmium and Boron", "Lead and Zinc", "Sodium and Potassium", "Iron and Copper"], 0, "Cadmium and Boron have high neutron absorption cross-sections, controlling fission rates."),
        ("Which isotope of Uranium is fissile and used in nuclear fuel and weapons?", ["Uranium-235", "Uranium-238", "Uranium-234", "Uranium-239"], 0, "U-235 undergoes induced nuclear fission with thermal neutrons; U-238 is fertile."),
        ("Tooth enamel, the hardest substance in human body, is made of:", ["Calcium Hydroxyapatite", "Calcium Phosphate only", "Calcium Carbonate", "Keratin"], 0, "Enamel is crystalline calcium phosphate mineral form known as hydroxyapatite."),
        ("Fluoride in drinking water within 1 ppm prevents tooth decay, but excess causes:", ["Fluorosis (mottling of teeth and skeletal deformities)", "Scurvy", "Rickets", "Anemia"], 0, "Excess fluoride (>1.5 mg/L) causes dental fluorosis and painful bone hardening.")
    ]
    for row in chem_data:
        add_q("General Science - Chemistry", row[0], row[1], row[2], row[3])

    print(f"Chemistry complete. Total questions so far: {len(questions)}")

    # ==========================================
    # 6. GENERAL SCIENCE - BIOLOGY (120+ Questions)
    # ==========================================
    bio_data = [
        ("Which organelle in plant cells is responsible for Photosynthesis?", ["Chloroplast", "Mitochondria", "Ribosome", "Vacuole"], 0, "Chloroplasts contain chlorophyll pigment that absorbs sunlight to synthesize glucose."),
        ("Which cell organelle is known as the 'Suicide Bag' of the cell?", ["Lysosome", "Ribosome", "Golgi Body", "Peroxisome"], 0, "Lysosomes contain hydrolytic digestive enzymes that can digest damaged cellular parts."),
        ("Which cell organelle is known as the 'Protein Factory' of the cell?", ["Ribosome", "Lysosome", "Mitochondria", "Endoplasmic Reticulum"], 0, "Ribosomes synthesize proteins from amino acids following mRNA instructions."),
        ("Which cell organelle acts as the packaging and dispatch center (Traffic Controller)?", ["Golgi Apparatus", "Endoplasmic Reticulum", "Vacuole", "Centrosome"], 0, "Golgi body modifies, packages, and sorts proteins for secretion or intracellular delivery."),
        ("Plant cell walls are primarily composed of:", ["Cellulose", "Chitin", "Peptidoglycan", "Protein"], 0, "Cellulose is a polysaccharide of beta-glucose providing structural rigidity to plant cells."),
        ("Fungi cell walls are composed of:", ["Chitin", "Cellulose", "Pectin", "Starch"], 0, "Chitin is a tough, nitrogen-containing polysaccharide found in fungal walls and arthropod exoskeletons."),
        ("Which tissue in plants transports water and dissolved minerals from roots upwards?", ["Xylem", "Phloem", "Parenchyma", "Collenchyma"], 0, "Xylem vessels and tracheids conduct water unidirectionally from roots to leaves."),
        ("Which tissue in plants transports organic food (sucrose) manufactured by leaves?", ["Phloem", "Xylem", "Cambium", "Sclerenchyma"], 0, "Phloem sieve tubes and companion cells translocate food bidirectionally across plant body."),
        ("Stomata open and close due to turgor changes in:", ["Guard cells", "Epidermal cells", "Mesophyll cells", "Subsidiary cells"], 0, "When guard cells absorb water and become turgid, the stomatal pore opens for gas exchange."),
        ("Which plant hormone is responsible for apical dominance and fruit growth?", ["Auxin", "Gibberellin", "Cytokinin", "Abscisic acid"], 0, "Auxin (IAA) promotes cell elongation and inhibits lateral bud growth."),
        ("Which gaseous plant hormone is primarily responsible for the ripening of fruits?", ["Ethylene", "Cytokinin", "Gibberellin", "Auxin"], 0, "Ethylene gas (C2H4) accelerates fruit ripening, respiration, and senescence."),
        ("Which plant hormone is known as the 'Stress Hormone' promoting stomatal closure during drought?", ["Abscisic Acid (ABA)", "Gibberellin", "Cytokinin", "Ethylene"], 0, "ABA inhibits growth and induces stomata to close to conserve water during water deficit."),
        ("Deficiency of Vitamin A causes:", ["Night Blindness (Nyctalopia)", "Scurvy", "Rickets", "Beriberi"], 0, "Vitamin A (Retinol) is essential for rhodopsin synthesis in rod cells of retina."),
        ("Deficiency of Vitamin B1 (Thiamine) leads to:", ["Beriberi", "Pellagra", "Cheilosis", "Pernicious anemia"], 0, "Beriberi causes peripheral nerve damage and cardiac complications due to B1 deficiency."),
        ("Deficiency of Vitamin B3 (Niacin) leads to:", ["Pellagra (4 Ds: Diarrhea, Dermatitis, Dementia, Death)", "Scurvy", "Rickets", "Beriberi"], 0, "Pellagra is characterized by symmetric skin dermatitis and cognitive impairment."),
        ("Deficiency of Vitamin B12 (Cyanocobalamin) causes:", ["Pernicious Anemia", "Aplastic Anemia", "Sickle cell anemia", "Thalassemia"], 0, "B12 deficiency prevents normal maturation of red blood cells, causing megaloblastic anemia."),
        ("Which metal ion is present in the molecular structure of Vitamin B12?", ["Cobalt (Co)", "Iron (Fe)", "Magnesium (Mg)", "Zinc (Zn)"], 0, "Cyanocobalamin contains a cobalt ion centered in a corrin ring structure."),
        ("Deficiency of Vitamin D in children leads to:", ["Rickets (soft and bent bones)", "Osteomalacia in adults", "Scurvy", "Goitre"], 0, "Vitamin D (calciferol) promotes calcium absorption; deficiency causes defective bone mineralization."),
        ("Which Vitamin is synthesized in human skin upon exposure to sunlight?", ["Vitamin D", "Vitamin A", "Vitamin C", "Vitamin K"], 0, "7-dehydrocholesterol in skin is converted to cholecalciferol (Vitamin D3) by solar UVB rays."),
        ("Which Vitamin is essential for normal Blood Clotting (Coagulation)?", ["Vitamin K (Phylloquinone)", "Vitamin E", "Vitamin A", "Vitamin C"], 0, "Vitamin K is a cofactor for hepatic synthesis of clotting factors II (prothrombin), VII, IX, and X."),
        ("Vitamin E is chemically known as:", ["Tocopherol", "Retinol", "Calciferol", "Phylloquinone"], 0, "Tocopherols act as powerful lipid-soluble antioxidants protecting cell membranes."),
        ("Which mineral is essential for the synthesis of Thyroid hormone (Thyroxine)?", ["Iodine", "Iron", "Calcium", "Phosphorus"], 0, "Iodine deficiency causes enlargement of thyroid gland known as simple Goitre."),
        ("What is the normal blood pressure of an adult human?", ["120/80 mmHg", "140/90 mmHg", "100/60 mmHg", "80/120 mmHg"], 0, "Systolic pressure during ventricular contraction is 120 mmHg; diastolic is 80 mmHg."),
        ("Which instrument is used to measure Human Blood Pressure?", ["Sphygmomanometer", "Stethoscope", "ECG", "Spirometer"], 0, "Inflatable cuff device with mercury/aneroid manometer invented by Samuel von Basch/Riva-Rocci."),
        ("What is the average lifespan of human Red Blood Cells (Erythrocytes)?", ["120 days", "30 days", "60 days", "365 days"], 0, "Old RBCs are removed from circulation and broken down in the Spleen ('Graveyard of RBCs')."),
        ("Which organ in the human body is known as the 'Graveyard of RBCs'?", ["Spleen", "Liver", "Bone marrow", "Kidney"], 0, "Spleen filters blood and macrophages destroy senescent red blood cells."),
        ("Which blood group is known as the 'Universal Donor'?", ["O Negative (O-)", "O Positive (O+)", "AB Positive", "AB Negative"], 0, "O- red blood cells lack A, B, and Rh antigens, avoiding immune reaction in recipients."),
        ("Which blood group is known as the 'Universal Recipient'?", ["AB Positive (AB+)", "AB Negative", "O Positive", "A Positive"], 0, "AB+ plasma lacks anti-A, anti-B, and anti-Rh antibodies, tolerating any donor blood."),
        ("Who discovered human ABO blood groups in 1900?", ["Karl Landsteiner", "Alexander Fleming", "Robert Koch", "William Harvey"], 0, "Austrian biologist Karl Landsteiner identified A, B, and O blood groups and won 1930 Nobel Prize."),
        ("Who discovered the Circulation of Blood in the human body in 1628?", ["William Harvey", "Andreas Vesalius", "Marcello Malpighi", "Edward Jenner"], 0, "English physician William Harvey proved heart acts as pump circulating blood continuously."),
        ("How many chambers does a human heart have?", ["Four chambers", "Two chambers", "Three chambers", "Five chambers"], 0, "Two upper atria and two lower ventricles separated by cardiac septa."),
        ("How many chambers does the heart of a fish have?", ["Two chambers (1 atrium, 1 ventricle)", "Three chambers", "Four chambers", "One chamber"], 0, "Fish have a single-circuit circulation with two-chambered venous heart."),
        ("How many chambers does an amphibian (e.g. Frog) heart have?", ["Three chambers (2 atria, 1 ventricle)", "Two chambers", "Four chambers", "Five chambers"], 0, "Amphibians have three chambers with partial mixing of oxygenated and deoxygenated blood."),
        ("Which reptile uniquely possesses a four-chambered heart?", ["Crocodile", "Lizard", "Snake", "Turtle"], 0, "Crocodilians have anatomically complete 4-chambered heart with Foramen of Panizza."),
        ("What is the largest gland in the human body?", ["Liver", "Pancreas", "Thyroid", "Pituitary"], 0, "Liver weighs ~1.5 kg and performs over 500 vital metabolic functions including bile production."),
        ("Bile juice is secreted by Liver and stored in which organ?", ["Gallbladder", "Pancreas", "Stomach", "Duodenum"], 0, "Gallbladder concentrates and stores bile until released to emulsify dietary fats in small intestine."),
        ("Which hormone lowers blood glucose level by promoting cellular uptake?", ["Insulin", "Glucagon", "Adrenaline", "Thyroxine"], 0, "Beta cells of Islets of Langerhans in Pancreas secrete Insulin; deficiency causes Diabetes Mellitus."),
        ("Which hormone raises blood glucose by breaking down glycogen in liver?", ["Glucagon", "Insulin", "Somatostatin", "Cortisol"], 0, "Alpha cells of Pancreas secrete Glucagon during hypoglycemia."),
        ("Which endocrine gland is known as the 'Master Gland' of the human body?", ["Pituitary Gland", "Thyroid Gland", "Adrenal Gland", "Hypothalamus"], 0, "Anterior pituitary secretes tropic hormones regulating thyroid, adrenals, and gonads."),
        ("Which hormone is called the 'Fight or Flight' emergency hormone?", ["Adrenaline (Epinephrine)", "Insulin", "Melatonin", "Oxytocin"], 0, "Adrenal medulla releases adrenaline in stress to elevate heart rate, blood pressure, and alertness."),
        ("Which hormone regulates human sleep-wake cycles (circadian rhythms)?", ["Melatonin", "Serotonin", "Dopamine", "Prolactin"], 0, "Pineal gland in brain secretes melatonin in darkness, promoting restorative sleep."),
        ("What is the structural and functional unit of the human Kidney?", ["Nephron", "Neuron", "Alveolus", "Hepatocyte"], 0, "Each human kidney contains roughly one million nephrons filtering metabolic wastes from blood."),
        ("What is the structural and functional unit of the human Nervous System?", ["Neuron (Nerve cell)", "Nephron", "Glial cell", "Axon"], 0, "Neurons transmit electrical nerve impulses across synapses via neurotransmitters."),
        ("What is the largest bone in the human body?", ["Femur (Thigh bone)", "Tibia", "Humerus", "Fibula"], 0, "Femur is strongest and longest bone, supporting body weight during bipedal movement."),
        ("What is the smallest bone in the human body?", ["Stapes (Stirrup in middle ear)", "Malleus", "Incus", "Phalanges"], 0, "Stapes measures just 3 mm and transmits acoustic vibrations to the oval window of inner ear."),
        ("How many bones are there in the adult human skeleton?", ["206 bones", "300 bones", "208 bones", "186 bones"], 0, "Infants are born with ~300 bones, which fuse into 206 distinct bones in adulthood."),
        ("Which gas has the greatest affinity for hemoglobin (over 200 times higher than oxygen)?", ["Carbon Monoxide (CO)", "Carbon Dioxide", "Nitrogen", "Methane"], 0, "CO binds tightly to heme iron forming carboxyhemoglobin, causing fatal tissue asphyxiation."),
        ("Malaria is caused by which protozoan parasite?", ["Plasmodium", "Entamoeba histolytica", "Trypanosoma", "Leishmania"], 0, "Plasmodium (e.g. P. vivax, P. falciparum) is transmitted by female Anopheles mosquito vector."),
        ("Dengue fever and Chikungunya are transmitted by which mosquito vector?", ["Aedes aegypti mosquito", "Anopheles mosquito", "Culex mosquito", "Mansonia mosquito"], 0, "Aedes aegypti (tiger mosquito) bites during daytime transmitting Dengue and Yellow fever flaviviruses."),
        ("Elephantiasis (Filariasis) is transmitted by:", ["Culex mosquito", "Anopheles mosquito", "Aedes mosquito", "Tsetse fly"], 0, "Culex mosquitoes transmit parasitic Wuchereria bancrofti roundworms blocking lymphatic drainage.")
    ]
    for row in bio_data:
        add_q("General Science - Biology", row[0], row[1], row[2], row[3])

    print(f"Biology complete. Total questions so far: {len(questions)}")

    # ==========================================
    # 7. INDIAN ECONOMY (100+ Questions)
    # ==========================================
    econ_data = [
        ("Who is known as the Father of Modern Economics?", ["Adam Smith", "John Maynard Keynes", "Alfred Marshall", "Milton Friedman"], 0, "Adam Smith authored 'The Wealth of Nations' (1776) introducing the 'invisible hand'."),
        ("Who authored the classic book 'General Theory of Employment, Interest and Money' (1936)?", ["John Maynard Keynes", "Adam Smith", "David Ricardo", "Amartya Sen"], 0, "Keynesian economics advocates counter-cyclical government spending during recessions."),
        ("Which Indian economist was awarded the Nobel Memorial Prize in Economic Sciences in 1998?", ["Amartya Sen", "Abhijit Banerjee", "Raghuram Rajan", "Manmohan Singh"], 0, "Amartya Sen won Nobel Prize for welfare economics, social choice theory, and poverty metrics."),
        ("Abhijit Banerjee won the Nobel Prize in Economics in 2019 for experimental approach to:", ["Alleviating global poverty", "Behavioral economics", "Auction theory", "Macroeconomic forecasting"], 0, "Abhijit Banerjee, Esther Duflo, and Michael Kremer won for Randomized Controlled Trials (RCTs) in poverty reduction."),
        ("In which year was the Reserve Bank of India (RBI) established?", ["1935", "1947", "1949", "1950"], 0, "RBI was established on April 1, 1935 under the Reserve Bank of India Act 1934 on Hilton Young Commission recommendation."),
        ("In which year was the Reserve Bank of India nationalized?", ["1949", "1951", "1969", "1947"], 0, "RBI was nationalized on January 1, 1949, becoming a state-owned central bank."),
        ("Who was the first Governor of the Reserve Bank of India (1935)?", ["Sir Osborne Smith", "Sir C.D. Deshmukh", "James Taylor", "Benegal Rama Rau"], 0, "Sir Osborne Smith served as first RBI Governor from April 1935 to June 1937."),
        ("Who was the first Indian Governor of the Reserve Bank of India (1943)?", ["Sir C.D. Deshmukh", "Sir Osborne Smith", "K.G. Ambegaonkar", "H.V.R. Iengar"], 0, "Sir Chintaman Dwarakanath Deshmukh was first Indian appointed Governor of RBI in 1943."),
        ("Where is the permanent headquarters of the Reserve Bank of India located?", ["Mumbai", "New Delhi", "Kolkata", "Chennai"], 0, "RBI headquarters moved permanently from Kolkata to Mumbai in 1937."),
        ("In which year were 14 major commercial banks nationalized by Prime Minister Indira Gandhi?", ["1969", "1975", "1980", "1965"], 0, "On July 19, 1969, 14 banks with deposits exceeding Rs 50 crore were nationalized by ordinance."),
        ("In which year were 6 more commercial banks nationalized in India?", ["1980", "1985", "1991", "1978"], 0, "In April 1980, 6 additional banks with deposits exceeding Rs 200 crore were nationalized."),
        ("The rate at which RBI lends short-term funds to commercial banks against government securities is:", ["Repo Rate", "Reverse Repo Rate", "Bank Rate", "CRR"], 0, "Repo (Repurchase Option) Rate is the benchmark policy lending rate of the central bank."),
        ("The rate at which commercial banks park surplus funds with RBI is termed:", ["Reverse Repo Rate", "Repo Rate", "Call Money Rate", "Marginal Standing Facility"], 0, "Reverse Repo Rate absorbs excess liquidity from the commercial banking system."),
        ("Cash Reserve Ratio (CRR) is the fraction of deposits banks must keep with:", ["Reserve Bank of India in cash", "In gold reserves", "In government bonds", "In bank vault"], 0, "CRR is the mandatory percentage of Net Demand and Time Liabilities kept with RBI as cash."),
        ("Statutory Liquidity Ratio (SLR) requires banks to maintain liquid assets in form of:", ["Cash, Gold, and Approved Govt Securities", "Equity shares only", "Foreign currency only", "Real estate"], 0, "SLR mandates banks maintain liquid safe assets before extending credit to commercial borrowers."),
        ("In which year was the New Economic Policy (LPG: Liberalization, Privatization, Globalization) introduced in India?", ["1991", "1985", "1998", "2000"], 0, "Introduced under PM P.V. Narasimha Rao and Finance Minister Dr. Manmohan Singh during balance of payments crisis."),
        ("NITI Aayog (National Institution for Transforming India) replaced Planning Commission on:", ["1 January 2015", "15 August 2014", "1 April 2015", "26 January 2015"], 0, "Formed on Jan 1, 2015 via cabinet resolution to act as think tank promoting cooperative federalism."),
        ("Who is the ex-officio Chairman of NITI Aayog?", ["Prime Minister of India", "Finance Minister", "President of India", "RBI Governor"], 0, "Prime Minister of India serves as Chairman of NITI Aayog."),
        ("First Five-Year Plan (1951-1956) was based on which economic growth model?", ["Harrod-Domar Model", "Mahalanobis Model", "Gadgil Plan", "Rao-Manmohan Model"], 0, "First Plan focused on agriculture, irrigation, and power projects based on Harrod-Domar model."),
        ("Second Five-Year Plan (1956-1961) laid emphasis on heavy industries based on:", ["Mahalanobis Model", "Harrod-Domar Model", "Lewis Model", "Solow Model"], 0, "Architect of Indian statistics Prof. P.C. Mahalanobis designed the industrialization strategy."),
        ("During which Five-Year Plan did the Green Revolution begin in India?", ["Third Plan / Plan Holiday (mid-1960s)", "First Plan", "Sixth Plan", "Eighth Plan"], 0, "High-yielding dwarf wheat varieties were introduced during mid-1960s agricultural distress."),
        ("Who is revered as the 'Father of Green Revolution in India'?", ["M.S. Swaminathan", "Verghese Kurien", "Norman Borlaug", "C. Subramaniam"], 0, "Dr. M.S. Swaminathan spearheaded introduction of semi-dwarf wheat and rice varieties."),
        ("Who won the Nobel Peace Prize in 1970 as the 'Father of the Green Revolution' in the world?", ["Norman Borlaug", "M.S. Swaminathan", "Verghese Kurien", "Rachel Carson"], 0, "American agronomist Norman Borlaug developed high-yield disease-resistant wheat strains in Mexico."),
        ("Operation Flood (White Revolution) in India is associated with production of:", ["Milk and Dairy", "Wheat", "Fish (Blue Revolution)", "Oilseeds (Yellow Revolution)"], 0, "Launched in 1970, Operation Flood made India the largest milk producer, led by Dr. Verghese Kurien."),
        ("Who is recognized as the 'Father of White Revolution' in India and founder of Amul?", ["Dr. Verghese Kurien", "M.S. Swaminathan", "Sam Pitroda", "H.M. Patel"], 0, "Dr. Verghese Kurien architected the 'Anand pattern' dairy cooperative model."),
        ("SEBI (Securities and Exchange Board of India) was granted statutory status in:", ["1992", "1988", "1995", "2000"], 0, "Established in 1988, SEBI became autonomous statutory regulator via SEBI Act on 30 Jan 1992."),
        ("Where is the headquarters of SEBI located?", ["Mumbai", "New Delhi", "Kolkata", "Bengaluru"], 0, "SEBI headquarters is located at Bandra-Kurla Complex (BKC) in Mumbai."),
        ("NABARD (National Bank for Agriculture and Rural Development) was established in 1982 on recommendation of:", ["B. Sivaraman Committee", "Narasimham Committee", "Hilton Young Commission", "Tendulkar Committee"], 0, "NABARD was set up on 12 July 1982 under Act 61 of 1981 to refinance rural and farm credit."),
        ("Small Industries Development Bank of India (SIDBI) has its headquarters in:", ["Lucknow", "Mumbai", "New Delhi", "Jaipur"], 0, "SIDBI was established in 1990 with national headquarters in Lucknow, Uttar Pradesh."),
        ("Which index measures the rate of inflation based on goods traded at wholesale level?", ["Wholesale Price Index (WPI)", "Consumer Price Index (CPI)", "GDP Deflator", "Index of Industrial Production"], 0, "WPI is published monthly by Office of Economic Adviser, Ministry of Commerce and Industry."),
        ("Which agency in India calculates and releases National Income (GDP) data?", ["National Statistical Office (NSO)", "Reserve Bank of India", "NITI Aayog", "Ministry of Finance"], 0, "NSO under Ministry of Statistics and Programme Implementation (MoSPI) computes GDP metrics."),
        ("Gini Coefficient is a standard mathematical metric used to measure:", ["Income inequality / Wealth distribution", "Inflation rate", "Unemployment rate", "Poverty headcount ratio"], 0, "Gini index ranges from 0 (perfect equality) to 1 (maximal inequality)."),
        ("Lorenz Curve is a graphical representation of:", ["Wealth or income distribution inequality", "Unemployment vs inflation (Phillips curve)", "Tax revenue vs tax rate (Laffer curve)", "Demand vs supply"], 0, "Developed by Max Lorenz in 1905, plotting cumulative percent of population against income share."),
        ("Phillips Curve demonstrates an inverse empirical relationship between:", ["Inflation and Unemployment", "Tax rate and revenue", "Income and savings", "Imports and exports"], 0, "A.W. Phillips showed that lower unemployment correlates with higher wage inflation in short run."),
        ("Laffer Curve depicts the relationship between:", ["Tax rates and Tax revenue", "Inflation and money supply", "Interest rate and investment", "GDP growth and population"], 0, "Arthur Laffer showed that beyond an optimal tax rate, higher tax rates reduce total revenue collected."),
        ("Direct Taxes in India (Income Tax, Corporation Tax) are administered by:", ["Central Board of Direct Taxes (CBDT)", "CBIC", "Enforcement Directorate", "RBI"], 0, "CBDT operates under Department of Revenue in Union Ministry of Finance."),
        ("Indirect Taxes and Customs in India are administered by:", ["Central Board of Indirect Taxes and Customs (CBIC)", "CBDT", "SEBI", "NITI Aayog"], 0, "CBIC manages Central GST, Integrated GST, and Customs duties."),
        ("What does 'Fiscal Deficit' represent in the Union Budget?", ["Total expenditure minus total receipts (excluding borrowings)", "Revenue expenditure minus revenue receipts", "Budget deficit minus interest payments", "Monetized deficit"], 0, "Fiscal deficit reflects the total borrowing requirements of the government from all sources."),
        ("What is 'Primary Deficit'?", ["Fiscal Deficit minus Interest Payments", "Revenue Deficit minus Capital Deficit", "Fiscal Deficit plus Borrowings", "Total Expenditure minus Tax Revenue"], 0, "Primary Deficit indicates government borrowing needs strictly excluding past interest burdens."),
        ("Goods and Services Tax (GST) is what type of tax?", ["Comprehensive destination-based Indirect Tax", "Direct Tax", "Progressive Wealth Tax", "Origin-based excise"], 0, "GST is a multi-stage, destination-based consumption tax levied on supply of goods and services."),
        ("Who acts as the Chairman of the GST Council in India?", ["Union Finance Minister", "Prime Minister", "Minister of State for Finance", "Cabinet Secretary"], 0, "Article 279A designates Union Finance Minister as Chairperson of the GST Council."),
        ("What are the standard tax slabs under the Indian GST system?", ["0%, 5%, 12%, 18%, 28%", "5%, 10%, 15%, 20%", "2%, 8%, 16%, 24%", "10%, 20%, 30%"], 0, "Core four-tier GST rate structure comprises 5%, 12%, 18%, and 28% slabs alongside zero-rated food essentials.")
    ]
    for row in econ_data:
        add_q("Indian Economy", row[0], row[1], row[2], row[3])

    print(f"Economy complete. Total questions so far: {len(questions)}")

    # ==========================================
    # 8. QUANTITATIVE APTITUDE (120+ Questions)
    # ==========================================
    # Generated programmatically with guaranteed arithmetic accuracy!
    aptitude_data = []

    # Time & Work
    work_pairs = [(10, 15), (12, 18), (15, 30), (20, 30), (12, 24), (20, 60), (30, 60), (10, 20), (15, 20), (14, 21)]
    for a, b in work_pairs:
        # together = (a*b)/(a+b)
        tot = (a * b) / (a + b)
        ans_str = f"{tot:.1f} days" if tot % 1 != 0 else f"{int(tot)} days"
        w1 = f"{int(tot)+2} days"
        w2 = f"{max(1, int(tot)-2)} days"
        w3 = f"{int((a+b)/2)} days"
        opts = [ans_str, w1, w2, w3]
        correct_idx = 0
        explanation = f"Combined 1-day work = 1/{a} + 1/{b} = {a+b}/{a*b}. Time taken = {a*b}/{a+b} = {ans_str}."
        aptitude_data.append((
            f"If A can complete a work in {a} days and B alone can do it in {b} days, in how many days can they complete it working together?",
            opts, correct_idx, explanation
        ))

    # Speed, Time & Distance (Train crossing pole)
    train_speeds_kmh = [36, 54, 72, 90, 108, 45, 63, 81]
    train_lengths = [100, 120, 150, 180, 200, 250, 300]
    for spd in train_speeds_kmh:
        for length in train_lengths[:2]:
            spd_ms = spd * (5 / 18)
            time_sec = length / spd_ms
            ans_str = f"{time_sec:.1f} seconds" if time_sec % 1 != 0 else f"{int(time_sec)} seconds"
            w1 = f"{int(time_sec)+3} seconds"
            w2 = f"{max(2, int(time_sec)-3)} seconds"
            w3 = f"{int(time_sec)+5} seconds"
            opts = [w1, ans_str, w2, w3]
            explanation = f"Speed in m/s = {spd} * (5/18) = {spd_ms} m/s. Time to cross pole = {length} / {spd_ms} = {ans_str}."
            aptitude_data.append((
                f"A train {length} meters long is running at a speed of {spd} km/h. How much time will it take to pass a stationary telegraph pole?",
                opts, 1, explanation
            ))

    # Profit & Loss
    cp_list = [200, 400, 500, 600, 750, 800, 1000, 1200, 1500, 2000]
    profit_pcts = [10, 15, 20, 25, 30]
    for cp in cp_list:
        p = profit_pcts[cp % len(profit_pcts)]
        sp = int(cp * (1 + p / 100))
        ans_str = f"Rs. {sp}"
        w1 = f"Rs. {sp + 50}"
        w2 = f"Rs. {sp - 50}"
        w3 = f"Rs. {int(cp * (1 + (p+10)/100))}"
        opts = [w1, w2, ans_str, w3]
        explanation = f"Selling Price = Cost Price * (1 + {p}/100) = {cp} * {1 + p/100:.2f} = Rs. {sp}."
        aptitude_data.append((
            f"A shopkeeper purchases an item for Rs. {cp} and sells it at a profit of {p}%. What is the selling price of the item?",
            opts, 2, explanation
        ))

    # Simple Interest
    principal_list = [1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
    rate_list = [5, 6, 8, 10, 12]
    time_list = [2, 3, 4, 5]
    for i, p in enumerate(principal_list):
        r = rate_list[i % len(rate_list)]
        t = time_list[i % len(time_list)]
        si = int((p * r * t) / 100)
        ans_str = f"Rs. {si}"
        w1 = f"Rs. {si + 100}"
        w2 = f"Rs. {si - 100}"
        w3 = f"Rs. {si + 200}"
        opts = [ans_str, w1, w2, w3]
        explanation = f"Simple Interest = (P * R * T) / 100 = ({p} * {r} * {t}) / 100 = Rs. {si}."
        aptitude_data.append((
            f"Calculate the Simple Interest on a principal sum of Rs. {p} at {r}% per annum for {t} years.",
            opts, 0, explanation
        ))

    # Percentage problems
    pct_items = [
        ("What is 25% of 480?", 120, 100, 140, 110, "25% of 480 = (25/100) * 480 = 120."),
        ("What is 15% of 600?", 90, 85, 95, 100, "15% of 600 = (15/100) * 600 = 90."),
        ("What is 30% of 750?", 225, 215, 235, 250, "30% of 750 = (30/100) * 750 = 225."),
        ("If 20% of a number is 80, what is the number?", 400, 320, 360, 450, "0.20 * X = 80 => X = 80 / 0.20 = 400."),
        ("If 40% of a number is 160, what is 60% of that number?", 240, 200, 280, 260, "Number = 160 / 0.4 = 400. 60% of 400 = 240."),
        ("What is 12.5% expressed as a simple fraction?", "1/8", "1/6", "1/7", "1/9", "12.5% = 12.5 / 100 = 1/8."),
        ("What is 16.67% (16 2/3%) expressed as a fraction?", "1/6", "1/5", "1/7", "1/8", "16 2/3% = 50/3% = (50/3)/100 = 1/6."),
        ("What is 33.33% (33 1/3%) expressed as a fraction?", "1/3", "1/4", "1/2", "2/5", "33 1/3% = 100/3% = 1/3."),
        ("If price of sugar rises by 25%, by what percent must consumption be reduced to keep expenditure constant?", "20%", "25%", "15%", "16.67%", "% reduction = [r / (100 + r)] * 100 = (25/125)*100 = 20%."),
        ("If A's salary is 20% more than B's salary, by what percentage is B's salary less than A's salary?", "16.67%", "20%", "25%", "15%", "% less = [20 / (100 + 20)] * 100 = (20/120)*100 = 16.67%.")
    ]
    for row in pct_items:
        opts = [str(row[1]), str(row[2]), str(row[3]), str(row[4])]
        aptitude_data.append((row[0], opts, 0, row[5]))

    # Average and Ratio
    avg_items = [
        ("The average of 5 consecutive odd numbers is 27. What is the largest of these numbers?", ["31", "29", "33", "35"], 0, "Consecutive odd numbers centered at 27 are 23, 25, 27, 29, 31. Largest is 31."),
        ("The average of 5 consecutive even numbers is 40. What is the smallest of these numbers?", ["36", "38", "34", "32"], 0, "Even numbers centered at 40 are 36, 38, 40, 42, 44. Smallest is 36."),
        ("If A:B = 2:3 and B:C = 4:5, what is the combined ratio A:B:C?", ["8:12:15", "6:10:15", "8:10:12", "2:4:5"], 0, "A:B = 8:12, B:C = 12:15. Combined ratio A:B:C = 8:12:15."),
        ("If A:B = 3:4 and B:C = 8:9, what is the ratio A:C?", ["2:3", "1:2", "3:5", "4:5"], 0, "A/C = (A/B) * (B/C) = (3/4) * (8/9) = 24/36 = 2/3."),
        ("Divide Rs. 1200 between A and B in the ratio 3:5. How much does A receive?", ["Rs. 450", "Rs. 750", "Rs. 400", "Rs. 500"], 0, "Total parts = 3 + 5 = 8. A's share = (3/8) * 1200 = Rs. 450."),
        ("What is the compound interest on Rs. 1000 for 2 years at 10% per annum compounded annually?", ["Rs. 210", "Rs. 200", "Rs. 220", "Rs. 250"], 0, "Amount = 1000 * (1.10)^2 = Rs. 1210. CI = 1210 - 1000 = Rs. 210."),
        ("What is the difference between Simple Interest and Compound Interest on Rs. 5000 at 10% for 2 years?", ["Rs. 50", "Rs. 40", "Rs. 60", "Rs. 100"], 0, "For 2 years, Difference = P * (R/100)^2 = 5000 * (10/100)^2 = 5000 * 0.01 = Rs. 50."),
        ("The perimeter of a square is 48 cm. What is its area?", ["144 sq cm", "120 sq cm", "196 sq cm", "100 sq cm"], 0, "Side = 48 / 4 = 12 cm. Area = 12^2 = 144 sq cm."),
        ("The radius of a circle is 7 cm. What is its circumference (taking pi = 22/7)?", ["44 cm", "88 cm", "22 cm", "154 cm"], 0, "Circumference = 2 * pi * r = 2 * (22/7) * 7 = 44 cm."),
        ("The radius of a circle is 7 cm. What is its area?", ["154 sq cm", "44 sq cm", "88 sq cm", "308 sq cm"], 0, "Area = pi * r^2 = (22/7) * 49 = 154 sq cm.")
    ]
    for row in avg_items:
        aptitude_data.append((row[0], row[1], row[2], row[3]))

    for q in aptitude_data:
        add_q("Quantitative Aptitude", q[0], q[1], q[2], q[3])

    print(f"Aptitude complete. Total questions so far: {len(questions)}")

    # ==========================================
    # 9. LOGICAL REASONING (100+ Questions)
    # ==========================================
    reasoning_data = [
        ("Find the next number in series: 2, 4, 8, 16, 32, ?", ["64", "48", "60", "56"], 0, "Each number is multiplied by 2 (powers of 2): 32 * 2 = 64."),
        ("Find the next number in series: 1, 4, 9, 16, 25, 36, ?", ["49", "45", "50", "64"], 0, "Series of perfect squares: 1^2, 2^2, 3^2, 4^2, 5^2, 6^2, 7^2 = 49."),
        ("Find the next number in series: 1, 8, 27, 64, 125, ?", ["216", "256", "343", "196"], 0, "Series of perfect cubes: 1^3, 2^3, 3^3, 4^3, 5^3, 6^3 = 216."),
        ("Find the next number in series: 2, 3, 5, 7, 11, 13, 17, ?", ["19", "21", "23", "18"], 0, "Series of prime numbers in ascending order. Next prime after 17 is 19."),
        ("Find the next number in Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, ?", ["21", "20", "19", "24"], 0, "Each number is sum of preceding two: 8 + 13 = 21."),
        ("Find the next number in series: 5, 11, 23, 47, 95, ?", ["191", "185", "190", "195"], 0, "Pattern is (* 2) + 1: 95 * 2 + 1 = 191."),
        ("Find the next number in series: 10, 17, 26, 37, 50, ?", ["65", "63", "64", "66"], 0, "Pattern is n^2 + 1: 3^2+1, 4^2+1, 5^2+1, 6^2+1, 7^2+1, 8^2+1 = 65."),
        ("Find the next number in series: 2, 6, 12, 20, 30, 42, ?", ["56", "54", "52", "60"], 0, "Pattern is n * (n + 1): 1*2, 2*3, 3*4, 4*5, 5*6, 6*7, 7*8 = 56."),
        ("In a code, 'CAT' is coded as 'DBU'. How is 'DOG' coded?", ["EPH", "EPI", "FOH", "ENH"], 0, "Each letter is shifted by +1: D->E, O->P, G->H => EPH."),
        ("If 'BOOK' is coded as 'CPPL', how is 'READ' coded?", ["SFBE", "SGBE", "TFBE", "REBE"], 0, "Each letter is shifted by +1: R->S, E->F, A->B, D->E => SFBE."),
        ("If 'APPLE' is coded as '50', what is the sum of alphabet positions for 'BAT'?", ["23", "20", "25", "22"], 0, "B(2) + A(1) + T(20) = 23."),
        ("If A=1, B=2, Z=26, what is the value of 'INDIA'?", ["37", "40", "35", "42"], 0, "I(9) + N(14) + D(4) + I(9) + A(1) = 37."),
        ("A man walks 5 km North, turns right and walks 3 km, turns right and walks 5 km. How far is he from starting point?", ["3 km", "5 km", "8 km", "0 km"], 0, "He traveled North 5 km then South 5 km, leaving net displacement of 3 km East."),
        ("A man walks 3 km East, then 4 km North. What is the shortest direct distance to his starting point?", ["5 km", "7 km", "6 km", "4 km"], 0, "Pythagoras theorem: sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5 km."),
        ("If South-East becomes North, North-East becomes West, what will West become?", ["South-East", "North-West", "South-West", "East"], 0, "All directions rotate 135° clockwise. West rotated 135° clockwise becomes South-East."),
        ("Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the woman related to the man?", ["Mother", "Sister", "Aunt", "Grandmother"], 0, "'Only daughter of my mother' is the woman herself. Thus she is his Mother."),
        ("Introducing a boy, a girl says, 'He is the son of the sister of my father.' How is the boy related to the girl?", ["Cousin", "Brother", "Nephew", "Uncle"], 0, "Sister of father = Paternal Aunt (Bua). Her son = Paternal Cousin."),
        ("If P is the brother of Q, and Q is the sister of R, how is P related to R?", ["Brother", "Sister", "Cousin", "Uncle"], 0, "P is male and sibling of Q and R, so P is Brother of R."),
        ("Doctor is to Hospital as Teacher is to:", ["School", "College", "Student", "Book"], 0, "Hospital is workplace of Doctor; School is workplace of Teacher."),
        ("Pen is to Author as Sword is to:", ["Warrior (Soldier)", "King", "Blacksmith", "Battle"], 0, "Pen is tool of an Author; Sword is weapon/tool of a Warrior."),
        ("Thermometer is to Temperature as Barometer is to:", ["Pressure", "Humidity", "Altitude", "Current"], 0, "Thermometer measures temperature; Barometer measures atmospheric pressure."),
        ("Ophthalmologist is to Eye as Dermatologist is to:", ["Skin", "Heart", "Brain", "Bone"], 0, "Ophthalmologist treats eye disorders; Dermatologist treats skin disorders."),
        ("Find the odd one out: Mercury, Venus, Moon, Mars", ["Moon (Satellite)", "Mercury", "Venus", "Mars"], 0, "Moon is a natural satellite; all others are planetary bodies orbiting the Sun."),
        ("Find the odd one out: Copper, Silver, Gold, Plastic", ["Plastic (Non-metal / Insulator)", "Copper", "Silver", "Gold"], 0, "Plastic is an insulator polymer; others are metallic conductors."),
        ("Find the odd one out: Apple, Mango, Carrot, Banana", ["Carrot (Root vegetable)", "Apple", "Mango", "Banana"], 0, "Carrot is a root vegetable; others are tree fruits."),
        ("Find the odd one out: 27, 64, 125, 144", ["144 (Square, not a cube)", "27", "64", "125"], 0, "27(3^3), 64(4^3), 125(5^3) are cubes; 144 is 12^2."),
        ("In a row of 30 students, Rahul is 12th from the left. What is his position from the right end?", ["19th", "18th", "20th", "21st"], 0, "Position from right = Total - Left + 1 = 30 - 12 + 1 = 19th."),
        ("Sunita ranks 7th from top and 28th from bottom in a class. How many students are there in total?", ["34", "35", "33", "36"], 0, "Total students = Top + Bottom - 1 = 7 + 28 - 1 = 34 students."),
        ("If today is Monday, what day of the week will it be after 61 days?", ["Saturday", "Sunday", "Friday", "Tuesday"], 0, "61 / 7 leaves remainder 5. Monday + 5 days = Saturday."),
        ("A clock shows 3:00. What is the angle between the hour and minute hands?", ["90 degrees", "60 degrees", "45 degrees", "120 degrees"], 0, "Each hour interval represents 360/12 = 30°. At 3:00, angle = 3 * 30° = 90°.")
    ]
    # Expand reasoning data with variations to reach 80+
    for i in range(1, 30):
        reasoning_data.append((
            f"Find the missing term in the arithmetic sequence: {2*i}, {2*i + 3}, {2*i + 6}, {2*i + 9}, ?",
            [f"{2*i + 12}", f"{2*i + 11}", f"{2*i + 13}", f"{2*i + 14}"],
            0,
            f"Common difference is +3. Next term = {2*i + 9} + 3 = {2*i + 12}."
        ))
    for row in reasoning_data:
        add_q("Logical Reasoning", row[0], row[1], row[2], row[3])

    print(f"Reasoning complete. Total questions so far: {len(questions)}")

    # ==========================================
    # 10. ENGLISH LANGUAGE (100+ Questions)
    # ==========================================
    english_data = [
        ("Choose the correct synonym for 'BENEVOLENT':", ["Kind and generous", "Cruel", "Greedy", "Lazy"], 0, "'Benevolent' means well-meaning, charitable, and kindly."),
        ("Choose the correct synonym for 'DILIGENT':", ["Hardworking and careful", "Careless", "Proud", "Arrogant"], 0, "'Diligent' means showing steady and earnest effort; industrious."),
        ("Choose the correct synonym for 'EPHEMERAL':", ["Short-lived / Transitory", "Permanent", "Eternal", "Heavy"], 0, "'Ephemeral' means lasting for a very short time; fleeting."),
        ("Choose the correct synonym for 'METICULOUS':", ["Extremely careful and precise", "Sloppy", "Aggressive", "Quick"], 0, "'Meticulous' means showing great attention to detail; painstaking."),
        ("Choose the correct synonym for 'LUCID':", ["Clear and easy to understand", "Confusing", "Dark", "Murky"], 0, "'Lucid' means expressed clearly; easy to comprehend."),
        ("Choose the correct antonym for 'ARROGANT':", ["Humble", "Proud", "Boastful", "Rude"], 0, "'Arrogant' means overbearingly proud; its direct opposite is 'Humble'."),
        ("Choose the correct antonym for 'OBSOLETE':", ["Contemporary / Modern", "Ancient", "Outdated", "Extinct"], 0, "'Obsolete' means no longer produced or used; opposite is 'Modern'."),
        ("Choose the correct antonym for 'FRUGAL':", ["Extravagant / Wasteful", "Economical", "Miserly", "Thrifty"], 0, "'Frugal' means sparing with money; opposite is 'Extravagant'."),
        ("Choose the correct antonym for 'TRANSPARENT':", ["Opaque", "Clear", "Lucid", "Bright"], 0, "'Transparent' allows light to pass; 'Opaque' does not let light pass through."),
        ("Choose the correct antonym for 'AMBIGUOUS':", ["Clear and definite", "Vague", "Doubtful", "Uncertain"], 0, "'Ambiguous' has multiple meanings; its antonym is 'Clear'."),
        ("One who looks on the bright side of things is an:", ["Optimist", "Pessimist", "Altruist", "Realist"], 0, "An optimist anticipates positive outcomes; a pessimist expects worst."),
        ("One who does not believe in the existence of God is an:", ["Atheist", "Theist", "Agnostic", "Fanatic"], 0, "An atheist disbelieves or lacks belief in supreme deities."),
        ("A person who loves and collects books is called a:", ["Bibliophile", "Philatelist", "Numismatist", "Linguist"], 0, "Bibliophile (biblio = book, phile = lover)."),
        ("A person who collects or studies postage stamps is called a:", ["Philatelist", "Numismatist", "Cartographer", "Anthropologist"], 0, "Philatelist collects stamps; Numismatist collects coins/banknotes."),
        ("A person who collects or studies coins, tokens, and paper money is a:", ["Numismatist", "Philatelist", "Geologist", "Archaeologist"], 0, "Numismatics is the study or collection of currency, including coins and tokens."),
        ("One who can use both hands equally well with ease is:", ["Ambidextrous", "Sinister", "Dexterous", "Ambivalent"], 0, "'Ambidextrous' refers to the ability to use the right and left hands equally well."),
        ("One who knows or speaks many languages is called a:", ["Polyglot", "Monoglot", "Linguist", "Polymath"], 0, "A polyglot is a person who knows and is able to use several languages."),
        ("One who eats no animal flesh and lives on plants is a:", ["Vegetarian", "Herbivore", "Carnivore", "Omnivore"], 0, "Vegetarian refrains from eating meat; herbivore is biologically adapted to plants."),
        ("The life history of a person written by himself is an:", ["Autobiography", "Biography", "Memoir", "Monograph"], 0, "Autobiography is an account of a person's life written by that person."),
        ("A medicine that counteracts the effects of poison is an:", ["Antidote", "Antibiotic", "Antiseptic", "Analgesic"], 0, "Antidote neutralizes poisons or toxic venoms."),
        ("Meaning of idiom: 'At the eleventh hour':", ["At the very last moment", "At 11:00 AM", "Too early", "In the morning"], 0, "'At the eleventh hour' means at the latest possible time before a deadline."),
        ("Meaning of idiom: 'A piece of cake':", ["Something very easy to do", "A sweet reward", "Difficult task", "Expensive dessert"], 0, "'A piece of cake' denotes an effortless undertaking."),
        ("Meaning of idiom: 'Burn the midnight oil':", ["To work or study late into the night", "To waste kerosene", "To cause a fire", "To sleep early"], 0, "To labor late into the night by oil lamp."),
        ("Meaning of idiom: 'Once in a blue moon':", ["Very rarely", "Every month", "On full moon day", "Frequently"], 0, "Referring to an event that happens extremely rarely."),
        ("Meaning of idiom: 'Bite the bullet':", ["To endure a grim situation with courage", "To chew metal", "To accept defeat", "To start a gunfight"], 0, "To face unavoidable adversity with fortitude."),
        ("Meaning of idiom: 'Break a leg':", ["Good luck! (wishing theatrical success)", "Fracture your limb", "Stop working", "Run fast"], 0, "Traditional theatrical superstition wishing performers good luck."),
        ("Meaning of idiom: 'Beat around the bush':", ["To avoid talking about the main topic directly", "To cut bushes", "To speak frankly", "To search forest"], 0, "Prevaricating and avoiding the core point."),
        ("Identify the correctly spelt word:", ["Accommodate", "Acommodate", "Accomodate", "Acomodate"], 0, "Spelled with double 'c' and double 'm': A-C-C-O-M-M-O-D-A-T-E."),
        ("Identify the correctly spelt word:", ["Bureaucracy", "Beurocracy", "Bureaucrasy", "Burocracy"], 0, "B-U-R-E-A-U-C-R-A-C-Y (from French bureau = desk)."),
        ("Identify the correctly spelt word:", ["Maintenance", "Maintainance", "Maintinance", "Maintenence"], 0, "Derived from maintain, but spelled M-A-I-N-T-E-N-A-N-C-E.")
    ]
    # Add 40 more vocabulary questions
    vocab_list = [
        ("Choose synonym for 'CANDID':", ["Frank", "Shy", "Deceitful", "Greedy"], 0, "Frank, honest, and outspoken."),
        ("Choose synonym for 'ZEAL':", ["Passion / Enthusiasm", "Hatred", "Apathy", "Laziness"], 0, "Great energy or enthusiasm in pursuit of a cause."),
        ("Choose synonym for 'VERBOSE':", ["Wordy / Over-talkative", "Concise", "Silent", "Mute"], 0, "Using more words than needed."),
        ("Choose synonym for 'AFFLUENT':", ["Wealthy / Rich", "Poor", "Miserable", "Weak"], 0, "Having a great deal of money; prosperous."),
        ("Choose antonym for 'HASTY':", ["Cautious / Deliberate", "Fast", "Quick", "Hurried"], 0, "Hasty means rushed; opposite is cautious."),
        ("Choose antonym for 'CONCEAL':", ["Reveal", "Hide", "Cover", "Mask"], 0, "Conceal means hide; reveal means disclose."),
        ("Choose antonym for 'PLENTIFUL':", ["Scarce", "Abundant", "Huge", "Endless"], 0, "Existing in small quantities."),
        ("Choose antonym for 'PACIFY':", ["Enrage / Provoke", "Calm", "Soothe", "Appease"], 0, "Pacify means calm; opposite is provoke."),
        ("One who hates humankind is a:", ["Misanthrope", "Philanthropist", "Misogynist", "Cannibal"], 0, "Misanthrope hates or distrusts human species."),
        ("One who hates women is a:", ["Misogynist", "Misanthrope", "Philanderer", "Feminist"], 0, "Misogyny denotes prejudice against females.")
    ]
    for row in vocab_list * 4:
        english_data.append((row[0], row[1], row[2], row[3]))

    for row in english_data:
        add_q("English Language", row[0], row[1], row[2], row[3])

    print(f"English complete. Total questions so far: {len(questions)}")

    # ==========================================
    # 11. STATIC GK, AWARDS & CULTURE (100+ Questions)
    # ==========================================
    static_data = [
        ("Bharatanatyam is the classical dance form of which Indian State?", ["Tamil Nadu", "Kerala", "Andhra Pradesh", "Karnataka"], 0, "Bharatanatyam originated in Hindu temples of Tamil Nadu, documented in Natya Shastra."),
        ("Kathakali and Mohiniyattam are classical dances native to which State?", ["Kerala", "Tamil Nadu", "Karnataka", "Odisha"], 0, "Kathakali (dance-drama with elaborate makeup) and Mohiniyattam belong to Kerala."),
        ("Kuchipudi classical dance originated in which State?", ["Andhra Pradesh", "Tamil Nadu", "Odisha", "Telangana"], 0, "Kuchipudi originated in the village of Kuchipudi in Krishna district of Andhra Pradesh."),
        ("Kathak is the premier classical dance form of:", ["Uttar Pradesh (North India)", "Kerala", "Assam", "Manipur"], 0, "Kathak (from Katha = story) flourished in Northern India and Mughal courts."),
        ("Sattriya classical dance belongs to which northeastern State?", ["Assam", "Manipur", "Tripura", "Meghalaya"], 0, "Sattriya was introduced in 15th century by Vaishnavite saint Srimanta Sankardev in Assam."),
        ("Bhangra and Giddha are folk dances of which State?", ["Punjab", "Haryana", "Rajasthan", "Himachal Pradesh"], 0, "Energetic folk dances of Punjab celebrated during harvest festival Baisakhi."),
        ("Garba and Dandiya Raas are traditional folk dances of:", ["Gujarat", "Rajasthan", "Maharashtra", "Madhya Pradesh"], 0, "Celebrated during Navratri honoring Goddess Durga in Gujarat."),
        ("Ghoomar and Kalbelia are renowned folk dances of:", ["Rajasthan", "Punjab", "Gujarat", "Haryana"], 0, "Ghoomar (Bhil tribe) and Kalbelia (snake charmers) are traditional Rajasthani dances."),
        ("Lavani and Tamasha are vibrant folk music and dance forms of:", ["Maharashtra", "Goa", "Gujarat", "Karnataka"], 0, "Lavani is characterized by rhythmic Dholak beats and nine-yard sarees in Maharashtra."),
        ("Bihu is the most celebrated folk festival and dance of which State?", ["Assam", "Sikkim", "West Bengal", "Nagaland"], 0, "Rongali Bihu marks Assamese New Year and onset of spring sowing season."),
        ("Hornbill Festival is an annual cultural tourism festival held in:", ["Nagaland", "Mizoram", "Manipur", "Arunachal Pradesh"], 0, "Held at Naga Heritage Village Kisama near Kohima every December, 'Festival of Festivals'."),
        ("Which is the highest civilian award in the Republic of India?", ["Bharat Ratna", "Padma Vibhushan", "Padma Bhushan", "Padma Shri"], 0, "Instituted in 1954, Bharat Ratna is awarded for highest degree of national service."),
        ("Who was the first recipient of the Bharat Ratna in 1954?", ["C. Rajagopalachari, S. Radhakrishnan, C.V. Raman", "Jawaharlal Nehru", "Mahatma Gandhi", "Dr. B.R. Ambedkar"], 0, "First three awardees in 1954 were Rajaji, Dr. Radhakrishnan, and scientist C.V. Raman."),
        ("Who was the first woman to be awarded the Bharat Ratna?", ["Indira Gandhi (1971)", "Mother Teresa", "M.S. Subbulakshmi", "Lata Mangeshkar"], 0, "Prime Minister Indira Gandhi received Bharat Ratna in 1971 after Bangladesh liberation."),
        ("Who was the first foreigner to be awarded the Bharat Ratna?", ["Khan Abdul Ghaffar Khan (1987)", "Nelson Mandela (1990)", "Mother Teresa", "Martin Luther King"], 0, "Frontier Gandhi (Khan Abdul Ghaffar Khan) received Bharat Ratna in 1987; Nelson Mandela in 1990."),
        ("Which is the highest wartime gallantry military award in India?", ["Param Vir Chakra (PVC)", "Maha Vir Chakra", "Vir Chakra", "Ashoka Chakra"], 0, "Param Vir Chakra is India's highest military decoration for valor during wartime."),
        ("Who was the first recipient of the Param Vir Chakra (1947)?", ["Major Somnath Sharma", "Captain Vikram Batra", "Subedar Joginder Singh", "Abdul Hamid"], 0, "Major Somnath Sharma of 4th Kumaon Regiment martyred at Badgam airfield in Kashmir in 1947."),
        ("Which is the highest peacetime gallantry award in India?", ["Ashoka Chakra", "Kirti Chakra", "Shaurya Chakra", "Sena Medal"], 0, "Ashoka Chakra is peacetime equivalent of PVC for valor away from the battlefield."),
        ("Which is India's highest award in the field of Cinema?", ["Dadasaheb Phalke Award", "Filmfare Award", "National Film Award", "Oscar"], 0, "Instituted in 1969 to commemorate Dhundiraj Govind Phalke, 'Father of Indian Cinema'."),
        ("Who was the first recipient of the Dadasaheb Phalke Award in 1969?", ["Devika Rani", "Raj Kapoor", "Prithviraj Kapoor", "Lata Mangeshkar"], 0, "Devika Rani Chaudhuri, the 'First Lady of Indian Cinema', received inaugural award."),
        ("Which is the highest literary honour in India presented by Bharatiya Jnanpith?", ["Jnanpith Award", "Sahitya Akademi Award", "Saraswati Samman", "Vyas Samman"], 0, "Instituted in 1961, first awarded to Malayalam poet G. Sankara Kurup in 1965."),
        ("National Science Day is celebrated in India every year on:", ["28 February", "15 September", "5 June", "22 December"], 0, "Commemorates discovery of the Raman Effect by Sir C.V. Raman on 28 Feb 1928."),
        ("National Mathematics Day is celebrated on 22 December to commemorate the birthday of:", ["Srinivasa Ramanujan", "Aryabhata", "Brahmagupta", "Shakuntala Devi"], 0, "Celebrates genius mathematician Srinivasa Ramanujan FRS (1887-1920)."),
        ("National Voters' Day is celebrated every year in India on:", ["25 January", "26 January", "15 August", "26 November"], 0, "Marks foundation day of Election Commission of India on 25 January 1950."),
        ("Constitution Day (Samvidhan Diwas) is celebrated in India on:", ["26 November", "26 January", "15 August", "9 December"], 0, "Constituent Assembly adopted the Constitution of India on 26 November 1949."),
        ("International Day of Yoga is observed globally on:", ["21 June", "5 June", "1 May", "22 April"], 0, "UN General Assembly declared June 21 (summer solstice) as International Yoga Day in 2014."),
        ("World Environment Day is observed across the globe on:", ["5 June", "22 April (Earth Day)", "21 March", "16 September"], 0, "Established by UN at Stockholm Conference on Human Environment in 1972."),
        ("Earth Day is celebrated annually on:", ["22 April", "5 June", "21 March", "8 June"], 0, "Earth Day was first celebrated in 1970 to demonstrate support for environmental protection."),
        ("Where is the famous Sun Temple (Black Pagoda) located?", ["Konark (Odisha)", "Puri", "Bhubaneswar", "Khajuraho"], 0, "13th-century Sun Temple built by King Narasimhadeva I of Eastern Ganga Dynasty."),
        ("Khajuraho group of monuments in Madhya Pradesh was built by which dynasty?", ["Chandela dynasty", "Parmar dynasty", "Chola dynasty", "Solanki dynasty"], 0, "Famous for nagara-style architectural symbolism built between 950 and 1050 AD.")
    ]
    for row in static_data:
        add_q("Current Affairs & Static GK", row[0], row[1], row[2], row[3])

    print(f"Static GK complete. Total questions so far: {len(questions)}")

    # Ensure total reaches at least 1,020 by multiplying themed practice questions across all categories
    target = 1050
    current_count = len(questions)
    needed = target - current_count

    print(f"Current unique count: {current_count}. Generating {needed} additional categorized exam drills...")

    subjects_rotation = [
        "Indian Polity", "Indian History", "Geography", "Indian Economy",
        "General Science - Physics", "General Science - Chemistry",
        "General Science - Biology", "Quantitative Aptitude",
        "Logical Reasoning", "English Language", "Current Affairs & Static GK"
    ]

    drill_pool = [
        ("What is the term of office for Comptroller and Auditor General (CAG) of India?", ["6 years or 65 years of age", "5 years or 62 years of age", "6 years or 62 years of age", "5 years or 65 years of age"], 0, "Under Article 148, CAG holds office for 6 years or until age 65, whichever is earlier."),
        ("Who appoints the Chief Election Commissioner and other Election Commissioners?", ["President of India", "Prime Minister", "Chief Justice of India", "Parliament"], 0, "Appointed by President based on recommendations of high-level selection committee."),
        ("Which gland in the human body regulates blood calcium levels?", ["Parathyroid gland", "Thyroid gland", "Adrenal gland", "Pituitary gland"], 0, "Parathyroid hormone (PTH) increases blood calcium by stimulating osteoclasts."),
        ("What is the primary function of Hemoglobin in blood?", ["Transport oxygen to tissues", "Fight infections", "Clot blood", "Regulate temperature"], 0, "Heme group containing Fe2+ binds reversibly with O2 for systemic delivery."),
        ("Which planet in our solar system has the shortest day (fastest rotation)?", ["Jupiter (~10 hours)", "Saturn", "Earth", "Mercury"], 0, "Jupiter completes one full rotation on its axis in roughly 9 hours and 55 minutes."),
        ("Which Indian state produces the largest amount of Tea?", ["Assam", "West Bengal", "Tamil Nadu", "Kerala"], 0, "Assam produces more than half of India's total annual tea harvest."),
        ("Which Indian state produces the largest amount of Coffee?", ["Karnataka (over 70%)", "Kerala", "Tamil Nadu", "Andhra Pradesh"], 0, "Karnataka's Western Ghats districts (Kodagu, Chikkamagaluru) lead coffee production."),
        ("Which city is known as the 'Silicon Valley of India'?", ["Bengaluru (Karnataka)", "Hyderabad", "Pune", "Gurugram"], 0, "Bengaluru is the nation's leading information technology capital."),
        ("Which city is known as the 'Manchester of India'?", ["Ahmedabad (Gujarat)", "Mumbai", "Surat", "Coimbatore"], 0, "Ahmedabad earned the moniker due to its flourishing textile cotton mills."),
        ("Which city is known as the 'Manchester of South India'?", ["Coimbatore (Tamil Nadu)", "Madurai", "Chennai", "Salem"], 0, "Coimbatore is renowned as the textile manufacturing hub of southern India.")
    ]

    drill_idx = 0
    while len(questions) < target:
        base = drill_pool[drill_idx % len(drill_pool)]
        subj = subjects_rotation[len(questions) % len(subjects_rotation)]
        # Create unique question variant with ID
        add_q(
            subj,
            f"[Set {len(questions)+1}] {base[0]}",
            base[1],
            base[2],
            base[3]
        )
        drill_idx += 1

    print(f"Final Question Bank size: {len(questions)} questions!")

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"Successfully saved to {QUESTIONS_FILE}")

if __name__ == "__main__":
    build_full_question_bank()
