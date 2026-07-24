#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FIA FOX — DG COMP / M.10815 : uplne znenie korespondencie AskTheEU, styl ako dgcomp-correspondence.html"""
import re, html

SRC = "https://www.asktheeu.org/en/request/request_for_access_to_documents_30"

M = []
def add(**k): M.append(k)

# ---------------------------------------------------------------- 1
add(who="peter", name="Peter Ferenc", date="10.12.2025", badge=("d","Delivered"),
    subject="Request for access to documents — Case M.10815",
    anchor="outgoing-32510",
    body="""
<p>Dear Competition,</p>
<p>Under the right of access to documents in the EU treaties, as developed in Regulation 1049/2001, I am requesting documents which contain the following information:</p>
<p>pursuant to <strong>Regulation (EC) No 1049/2001</strong>, <strong>Article 15 TFEU</strong> and <strong>Article 42 of the Charter of Fundamental Rights of the European Union</strong>, I hereby request full access to all documents related to case <strong>M.10815 – Deutsche Telekom / Orange / Telefónica / Vodafone – Joint Venture</strong>.</p>
<p>In particular, I request access to:</p>
<ul>
<li>The complete Joint Venture Agreement (unredacted)</li>
<li>All annexes and amendments to the JV Agreement</li>
<li>The Shareholders Agreement</li>
<li>Governance and operational rules of the joint venture</li>
<li>The complete and unredacted version of the Commission's decision</li>
<li>The Form CO notification submitted by the parties</li>
<li>All market analysis and internal assessments performed by DG COMP</li>
<li>All correspondence exchanged between DG COMP and the notifying parties concerning this joint venture</li>
</ul>
<p>Given that this joint venture fundamentally influences the competitive landscape of the EU telecommunications market and affects millions of EU citizens, I consider that the public interest in transparency clearly outweighs any potential claims of commercial confidentiality, in line with the principles established by the Court of Justice of the European Union.</p>
<p>Yours faithfully,<br>Peter Ferenc<br>Rammelkam 2, 84036 Kumhausen, Germany</p>""")

# ---------------------------------------------------------------- 2
add(who="commission", name="COMP-ACCESS-TO-DOCUMENTS@ec.europa.eu", date="10.12.2025",
    badge=("c","Registered"), subject="Acknowledgement of receipt — case number 2025/6534",
    anchor="incoming-62493",
    body="""
<p>Dear Sir or Madam,</p>
<p>We hereby acknowledge the receipt of your request for access to documents sent on 10/12/2025 and registered on 10/12/2025 under the case number <strong>2025/6534</strong>.</p>
<p>We will handle your request within <strong>15 working days</strong> as of the date of registration. The time-limit expires on <strong>12/01/2026</strong>. We will let you know if we need to extend this time limit for additional 15 working days.</p>
<p>To find more information on how we process your personal data, please see the privacy statement.</p>
<p>Yours faithfully,<br>Directorate-General for Competition – Access to Documents<br>European Commission</p>""")

# ---------------------------------------------------------------- 3
add(who="peter", name="Peter Ferenc", date="11.12.2025", badge=("d","Delivered"),
    subject="Reply — unredacted contract requested", anchor="outgoing-32516",
    body="""
<p>Dear Competition,</p>
<p>Thank you, I will wait for your response! I want an unblackened transparent contract!</p>
<p>Yours faithfully,<br>Peter Ferenc</p>""")

# ---------------------------------------------------------------- 4
add(who="commission", name="COMP-C5-MAIL@ec.europa.eu — Unit C.5 Mergers", date="07.01.2026",
    badge=("r","Refused"), subject="Your application for access to documents — Ref EASE No 2025/6534",
    anchor="incoming-62781",
    att=["image001.jpg", "EASE 2025 6534 Your request of 10 December for access to document.pdf (247K)"],
    body="""
<p>Dear Peter Ferenc,</p>
<p><strong>Subject:</strong> Your application for access to documents – Ref EASE No 2025/6534</p>
<p>We refer to your message dated 10/12/2025 in which you make a request for access to documents, registered on 10/12/2025 under the above-mentioned reference number.</p>
<p>Please find attached a scan of the reply to your request for access to documents, <strong>signed by the Director General</strong>.</p>
<p>You are kindly requested to reply to the present email acknowledging receipt thereof.</p>
<p>Yours faithfully,</p>
<p>European Commission<br>Directorate-General for Competition<br>Unit C.5 Mergers<br>Directorate C – Markets and cases: Information Technology, Communication and Media</p>""")

# ---------------------------------------------------------------- 5
add(who="peter", name="Peter Ferenc", date="19.01.2026", badge=("d","Delivered"),
    subject="Request for extension of the deadline to submit a confirmatory application — Ref. EASE 2025/6534",
    anchor="outgoing-32691",
    body="""
<p>Dear Sir or Madam,</p>
<p>I hereby formally request an extension of the deadline to submit a confirmatory application in relation to my request for access to documents registered under reference EASE 2025/6534.</p>
<p><strong>Grounds for the request</strong></p>
<p>Due to objective technical reasons, I currently do not have reliable access to all necessary technical means and authentication credentials required to prepare and submit a legally substantiated confirmatory application.</p>
<p>The scope and complexity of the grounds for refusal require a thorough legal and factual analysis, in particular with regard to:</p>
<ul>
<li>the application of exceptions to the right of access to documents,</li>
<li>the proportionality of the redactions applied,</li>
<li>and the assessment of compliance with EU law.</li>
</ul>
<p>Submitting a confirmatory application without such analysis would be purely formal and would undermine the very purpose of the remedy provided for under EU law.</p>
<p><strong>Legal basis</strong></p>
<p>This request is based, inter alia, on:</p>
<ul>
<li>Article 41 of the Charter of Fundamental Rights of the European Union (right to good administration),</li>
<li>Article 47 of the Charter of Fundamental Rights of the European Union (right to an effective remedy),</li>
<li>the principle of equality of arms and effective exercise of procedural rights,</li>
<li>and settled case-law according to which procedural deadlines must not be applied in a manner that renders the exercise of rights conferred by EU law practically impossible or excessively difficult.</li>
</ul>
<p><strong>Request</strong></p>
<p>In light of the above, I request an extension of <strong>30 days</strong>, calculated from the date of expiry of the original deadline for submitting the confirmatory application.</p>
<p>This request is submitted without any waiver of rights or admission of delay, and solely for the purpose of ensuring a proper, informed and legally effective exercise of my right to a remedy.</p>
<p>I kindly request written confirmation as to whether this extension has been granted.</p>
<p>Yours faithfully,<br>Peter Ferenc</p>""")

# ---------------------------------------------------------------- 6
add(who="commission", name="COMP-C5-MAIL@ec.europa.eu — Unit C.5 Mergers", date="20.01.2026",
    badge=("r","Refused"), subject="Extension of the 15-working-day deadline is not possible",
    anchor="incoming-62983",
    body="""
<p>Dear Mr Ferenc,</p>
<p>Thank you for your email of 19 January 2026, in which you enquire whether it is possible to extend the legal deadline of 15 working days as stipulated in Article 7(2) of Regulation 1049/2001 for filing a confirmatory application in response to a partial or total refusal as reply to a request for access to documents.</p>
<p>Please be informed that <strong>it is not possible to extend this deadline of 15 working days</strong> as the time limits set forth in Regulation 1049/2001 are not at the disposal of the parties and are determinative for the procedure of access to documents held by the institutions.</p>
<p>In this context, we would like to point out that <strong>the confirmatory stage serves as a full administrative review of the initial decision and must correct any omission from the initial decision even when not expressly contested in the confirmatory application by the applicant</strong>.</p>
<p>Given that the deadline for filing a confirmatory application in response to the initial negative reply of 7 January 2026 by the Directorate-General for Competition to your request for access to documents of 10 December 2025, registered under the reference EASE 2025/6534 <strong>has not expired yet</strong>, we would like to inform you that we are consequently not treating your enquiry as such a confirmatory application within the meaning of Regulation 1049/2001.</p>
<p>In this respect, we would once again like to draw your attention to section 5 of our initial negative reply of 7 January 2026, in which we explained the available means of redress, the applicable legal deadline and how and to which service of the European Commission to eventually submit such a confirmatory application, should you choose to do so.</p>
<p>Kind regards,</p>
<p>European Commission<br>Directorate-General for Competition<br>Unit C.5 Mergers<br>Directorate C – Markets and cases: Information Technology, Communication and Media</p>""")

# ---------------------------------------------------------------- 7
add(who="peter", name="Peter Ferenc", date="30.01.2026", badge=("d","Delivered"),
    subject="Confirmatory application — Article 7(2) of Regulation (EC) No 1049/2001",
    anchor="outgoing-32775",
    body="""
<p>Dear Sir or Madam,</p>
<p>This confirmatory application was already submitted on <strong>26 January 2026</strong> via the AskTheEU platform. Due to a technical error, it was sent through the wrong interface and did not reach the institution.</p>
<p>The AskTheEU / Access Info Europe team has confirmed in writing that the message was submitted in time and can attest to this if necessary. Below is the link to the document confirming that my confirmatory application was submitted in due time via an alternative channel, due to a technical error on the platform.</p>
<p>I hereby submit a confirmatory application pursuant to <strong>Article 7(2) of Regulation (EC) No 1049/2001</strong>, requesting a full administrative review of the initial negative reply dated 7 January 2026 issued by the Directorate-General for Competition in response to my request for access to documents of 10 December 2025, registered under reference EASE 2025/6534.</p>
<p>I respectfully maintain that the initial decision unlawfully restricts my right of access to documents and fails to comply with the principles of transparency, proportionality and good administration laid down in Regulation 1049/2001 and Article 15 TFEU.</p>
<p>In particular:</p>
<p><strong>1. Incorrect or overly broad application of exceptions</strong><br>
The initial reply relies on exceptions which have not been demonstrated to apply concretely and individually to the requested documents. The reasoning provided remains abstract and does not show how disclosure would specifically and actually undermine a protected interest, as required by settled case-law of the Court of Justice.</p>
<p><strong>2. Failure to properly assess the overriding public interest</strong><br>
The documents requested concern matters of significant public interest, including the functioning of competition enforcement, compliance with EU law and the protection of fundamental rights. The initial decision does not carry out a genuine and reasoned assessment of whether an overriding public interest in disclosure exists.</p>
<p><strong>3. Insufficient reasoning and lack of individual examination</strong><br>
The refusal does not demonstrate that each document was examined individually, nor does it explain why partial access could not be granted in accordance with Article 4(6) of Regulation 1049/2001.</p>
<p><strong>4. Relevance of data protection and GDPR compliance</strong><br>
To the extent that data protection considerations were invoked, I note that Regulation (EU) 2018/1725 and Regulation (EU) 2016/679 (GDPR) do not justify a blanket refusal. Any personal data issues could and should be addressed through appropriate redaction rather than a denial of access.</p>
<p>As recalled in your correspondence of 20 January 2026, the confirmatory stage constitutes a full administrative review of the initial decision. I therefore invite the Commission to reassess the request in its entirety and to remedy any omissions or errors contained in the initial reply, including those not expressly contested above.</p>
<p>I respectfully request that the Commission grant access to the requested documents, in full or at least in part, in accordance with Regulation 1049/2001.</p>
<p>Yours faithfully,<br>Peter Ferenc</p>""")

# ---------------------------------------------------------------- 8
add(who="commission", name="COMP-C5-MAIL@ec.europa.eu — COMP C-5", date="03.02.2026",
    badge=("c","Forwarded"), subject="Receipt acknowledged — forwarded to the Secretariat-General",
    anchor="incoming-63178",
    body="""
<p>Dear Mr Ferenc,</p>
<p>We hereby acknowledge receipt of your email of 30 January 2026, in which you submit a request for confirmatory decision.</p>
<p>Please be informed that <strong>we have forwarded your email to the competent Secretariat-General of the European Commission</strong>.</p>
<p>Kind regards<br>COMP C-5</p>""")

# ---------------------------------------------------------------- 9
add(who="commission", name="SG ACCES DOCUMENTS — Secretariat-General", date="03.02.2026",
    badge=("r","Rejected as out of time"),
    subject="Internal review of access to documents request — Ares(2026)1214166",
    anchor="incoming-63199",
    body="""
<p>Dear Applicant,</p>
<p>I refer to your email of 30 January 2026, by which you lodge a confirmatory application in accordance with Article 7(2) of Regulation 1049/2001 regarding public access to European Parliament, Council and Commission documents (hereafter Regulation 1049/2001).</p>
<p>I regret to inform you that <strong>your confirmatory application was lodged outside the applicable deadline</strong> defined in Article 7(2) of Regulation 1049/2001. That Article provides that in the event of a total or partial refusal, the applicant may, within 15 working days of receiving the institution's reply, make a confirmatory application asking the institution to reconsider its position.</p>
<p>Consequently, <strong>the Commission is not in a position to handle your application</strong>.</p>
<p>Yours sincerely,<br>European Commission<br>Access to Documents Team</p>""")

# ---------------------------------------------------------------- 10
add(who="peter", name="Peter Ferenc", date="08.02.2026", badge=("d","Delivered"),
    subject="Procedural clarification — confirmatory application submitted on 26 January 2026 (Case M.10815)",
    anchor="outgoing-32839",
    body="""
<p>Dear Sir or Madam,</p>
<p>I must formally object to the position now being advanced in this matter and request that the factual and procedural record be accurately reflected.</p>
<p><strong>1. Timely submission of the confirmatory application</strong><br>
My confirmatory application under Article 7(2) of Regulation (EC) No 1049/2001 was <strong>fully drafted and submitted on 26 January 2026</strong>, i.e. <strong>on the very last day of the statutory deadline</strong>, via the AskTheEU platform. This fact is <strong>not disputed</strong> and has been <strong>expressly confirmed in writing by Access Info Europe</strong>, including by documentary evidence (timestamped receipt of my message on 26 January 2026).</p>
<p><strong>2. Technical non-forwarding cannot be attributed to the applicant</strong><br>
Any failure to forward the confirmatory application to the Commission resulted exclusively from a technical and organisational issue on the side of the intermediary platform. Under settled case-law and general principles of EU law:</p>
<ul>
<li>an applicant <strong>cannot be penalised</strong> for technical malfunctions of an intermediary platform used in good faith;</li>
<li>procedural rights conferred by Regulation 1049/2001 <strong>cannot be extinguished by excessive formalism</strong>.</li>
</ul>
<p><strong>3. Legitimate expectations and procedural acceptance</strong><br>
Crucially, the confirmatory application was: acknowledged, processed internally, and forwarded to the competent services of the Commission. These acts constitute <strong>formal procedural steps</strong> that <strong>implicitly recognised the procedural validity</strong> of the confirmatory application. Once such procedural acceptance has occurred, it is <strong>legally impermissible</strong> to retroactively negate it, as this would breach:</p>
<ul>
<li>the principle of good administration (Article 41 Charter),</li>
<li>the protection of legitimate expectations,</li>
<li>and the effectiveness of EU law.</li>
</ul>
<p><strong>4. Consequences</strong><br>
Any attempt to now recharacterise a duly submitted confirmatory application as "out of time" would amount to arbitrary administrative conduct, manifestly disproportionate formalism, and a violation of Articles 41 and 47 of the Charter of Fundamental Rights. Such conduct would be <strong>independently reviewable</strong> by the European Ombudsman and, if necessary, by the EU Courts.</p>
<p><strong>5. Request</strong><br>
I therefore request that:</p>
<ul>
<li>the record be corrected to reflect the timely submission on 26 January 2026,</li>
<li>the confirmatory application be treated as validly lodged,</li>
<li>and the Commission proceed with the full administrative review required under Article 7(2) of Regulation 1049/2001.</li>
</ul>
<p>This message is submitted <strong>for the avoidance of doubt and without prejudice</strong> to any further remedies available to me under EU law.</p>
<p><strong>Additional procedural clarification</strong><br>
For the avoidance of any doubt, I hereby confirm that the same confirmatory application was also transmitted directly to the European Commission on <strong>7 February 2026</strong> via official e-mail channels, as well as to the Cabinet of a Member of the Commission. Accordingly, the content of the confirmatory application was unequivocally made available to the Commission through multiple official channels, further demonstrating my good faith, procedural cooperation, and genuine intention to exercise my rights under Regulation (EC) No 1049/2001 in a proper and diligent manner.</p>
<p>Yours sincerely,<br>Peter Ferenc<br>Case No.: TFIA-2026-JV-002</p>""")

# ---------------------------------------------------------------- 11
add(who="commission", name="Sg-Acc-Doc@ec.europa.eu — Transparency Unit", date="08.02.2026",
    badge=("c","Received"), subject="Automatic acknowledgement — Transparency Unit, Secretariat-General",
    anchor="incoming-63276",
    body="""
<p>Your message has been received by the Transparency Unit of the Secretariat-General of the European Commission.</p>
<p>Requests for public access to documents are treated on the basis of Regulation (EC) No 1049/2001 of 30 May 2001 regarding public access to European Parliament, Council and Commission documents.</p>
<p>The Secretariat-General will reply to your request within <strong>15 working days</strong> upon registration of your request and will duly inform you of the registration of the request (or of any additional information to be provided in view of its registration and/or treatment).</p>
<p><em>The same text followed in French and German.</em></p>""")

# ---------------------------------------------------------------- 12
add(who="commission", name="Sg-Acc-Doc@ec.europa.eu — Access to Documents Team", date="10.02.2026",
    badge=("r","Rejected"), subject="Third-party websites — use the official portal",
    anchor="incoming-63299",
    body="""
<p>Dear Applicant,</p>
<p><strong>The European Commission cannot be held responsible for issues with third party websites.</strong> We invite you to use the official portal for requesting European Commission documents.</p>
<p>Kind regards,<br>European Commission<br>Access to Documents Team</p>""")

# ---------------------------------------------------------------- 13
add(who="peter", name="Peter Ferenc", date="10.02.2026", badge=("d","Delivered"),
    subject="Applicant's procedural position — acceptance and processing of the confirmatory application",
    anchor="outgoing-32851",
    body="""
<p>Dear Sir or Madam,</p>
<p>I take note of your statement according to which the European Commission cannot be held responsible for the technical functioning of third-party websites such as the AskTheEU platform. <strong>I cannot agree with this assertion.</strong></p>
<p>The AskTheEU platform has been long-standing accepted, used and effectively relied upon by the European Commission as a standard tool for exercising the public right of access to documents, through which the Commission:</p>
<ul>
<li>regularly receives and handles access-to-documents requests,</li>
<li>communicates with applicants, and</li>
<li>systematically processes submissions under Regulation (EC) No 1049/2001.</li>
</ul>
<p>In these circumstances, AskTheEU cannot be regarded as a random or unauthorised third party, the use of which would be at the applicant's own risk.</p>
<p>Independently of the above, I emphasise that this issue is not decisive for the assessment of the procedural admissibility of my submission. <strong>The decisive fact is that the European Commission has received my confirmatory application, acknowledged its receipt and initiated its processing</strong>, as expressly confirmed by the message from the Transparency Unit of the Secretariat-General.</p>
<p>From the moment the Commission received the submission, placed it within the framework of Regulation (EC) No 1049/2001, and informed me that it would be handled within the statutory time-limit following registration, <strong>a formal procedural relationship arose between the applicant and the institution</strong>, for which full responsibility lies exclusively with the European Commission.</p>
<p>The question of the channel through which the submission was initially transmitted cannot retroactively affect its procedural admissibility, particularly where the Commission itself has confirmed receipt and the commencement of processing.</p>
<p>Under these circumstances, it is legally impermissible to retrospectively contest the timeliness or admissibility of the confirmatory application, or to transfer the consequences of technical or contractual arrangements between the Commission and a third party onto the applicant.</p>
<p>I therefore request that the Commission proceed with the full administrative review of the confirmatory application in accordance with Article 7(2) of Regulation (EC) No 1049/2001.</p>
<p>Yours faithfully,<br>Peter Ferenc</p>""")

# ---------------------------------------------------------------- 14
add(who="commission", name="Sg-Acc-Doc@ec.europa.eu — Transparency Unit", date="10.02.2026",
    badge=("c","Received"), subject="Automatic acknowledgement — Transparency Unit, Secretariat-General",
    anchor="incoming-63303",
    body="""
<p>Your message has been received by the Transparency Unit of the Secretariat-General of the European Commission.</p>
<p>Requests for public access to documents are treated on the basis of Regulation (EC) No 1049/2001 of 30 May 2001 regarding public access to European Parliament, Council and Commission documents.</p>
<p>The Secretariat-General will reply to your request within 15 working days upon registration of your request and will duly inform you of the registration of the request.</p>
<p><em>The same text followed in French and German.</em></p>""")

# ---------------------------------------------------------------- 15
add(who="peter", name="Peter Ferenc", date="12.02.2026", badge=("d","Delivered"),
    subject="Submission of criminal complaint — damage to the financial interests of the EU (Article 325 TFEU)",
    anchor="incoming-63355", att=["image001.jpg (52K)",
    "01_Criminal report on Landesjustizkasse Bamberg_EPPO_EN→DE→FR→ES→PL→IT→SK_signed QES.pdf"],
    note="EN → DE → FR → ES → PL → IT → SK · Email Tracking No.: 2428.022",
    body="""
<p>Dear Sir or Madam,</p>
<p>I hereby submit a criminal complaint by way of a link.</p>
<p>The complaint concerns suspected criminal offences affecting the financial interests of the European Union, within the meaning of <strong>Article 325 TFEU</strong> and <strong>Directive (EU) 2017/1371 (PIF)</strong>.</p>
<p>The criminal complaint was drawn up as a PDF document signed with a <strong>Qualified Electronic Signature (QES)</strong>, which, pursuant to Article 25(2) of Regulation (EU) No 910/2014 (eIDAS), has the same legal effect as a handwritten signature.</p>
<p>The submission is made in the Slovak language, which is an official language of the European Union. <strong>The Slovak language version is considered the original and legally binding version.</strong> The versions EN → DE → FR → ES → PL → IT are attached exclusively as faithful mirror translations to facilitate processing.</p>
<p>I expressly point out that <strong>no provision of EU law requires a criminal complaint to be submitted via a specific online form</strong>. Pursuant to Article 24 of Council Regulation (EU) 2017/1939, the European Public Prosecutor's Office may receive information on offences affecting the Union's financial interests from any source, including natural persons.</p>
<p>Any technical or procedural restriction which would:</p>
<ul>
<li>prevent the submission of the full content of the complaint,</li>
<li>require its shortening or lead to the loss of factual allegations or evidence,</li>
<li>or make its acceptance conditional upon additional "prior assessment",</li>
</ul>
<p>constitutes, in my view, an unlawful barrier to access to justice and a violation of Article 47 of the Charter of Fundamental Rights of the EU and Article 13 of the European Convention on Human Rights.</p>
<p>I therefore expect that the criminal complaint will be properly registered, examined and handled on the basis of its substance, in accordance with EU law, regardless of the technical means of its transmission.</p>
<p>Yours faithfully,<br>Kumhausen, 09.02.2026<br>Peter Ferenc</p>
<p><em>The identical text was transmitted in DE, FR, ES, PL, IT and SK in the same message.</em></p>""")

# ---------------------------------------------------------------- 16
add(who="peter", name="Peter Ferenc", date="16.02.2026", badge=("d","Delivered"),
    subject="Supplementary document", anchor="outgoing-32892",
    body="""
<p>Dear AskTheEU,</p>
<p>[link to the signed document]</p>
<p>Yours sincerely,<br>Peter Ferenc</p>""")

# ---------------------------------------------------------------- 17
add(who="peter", name="Peter Ferenc", date="20.07.2026", badge=("d","Delivered"),
    subject="Reply to the decision refusing access to documents — COMP/M.10815",
    anchor="", att=["image001.jpg (52K)",
    "03.12 The answer DG COMP EASE 2025 6534 ALL 9 Languages signed with QES.pdf (576K)"],
    note="File Ref.: EASE 2025/6534 · COMP/C5/LC/(2025)/6534 · TFIA-2026-JV-009 · Email Tracking No.: 2428.050 · DE, EN, SK",
    body="""
<p>Dear Director-General, dear Mr Whelan,</p>
<p>please find enclosed my reply to your decision of 7 January 2026 refusing me access to the documents in the case file in Case COMP/M.10815. The document bears a <strong>qualified electronic signature (QES)</strong> pursuant to Art. 25(2) of the eIDAS Regulation (No 910/2014) and is legally equivalent to a handwritten signature.</p>
<p>Access to documents of the institutions is not a matter for the Commission's discretion. Under <strong>Art. 15(3) TFEU</strong>, <strong>Art. 42 of the Charter</strong> and <strong>Art. 2(1) of Regulation (EC) No 1049/2001</strong>, every citizen of the Union has a right of access to documents of the institutions without having to state an interest or a reason. Refusal is the exception; it must, according to the settled case-law of the Court of Justice, be interpreted strictly, and <strong>the burden of proof lies with the institution, not with the applicant</strong>.</p>
<p>In my reply I set out five reasons why the decision cannot stand:</p>
<p><strong>1.</strong> You calculated the time limit from the date of the reply, although Art. 7(2) of the Regulation ties it to receipt. Moreover: on 20 January 2026 you informed me in writing that the time limit had not yet expired; on 30 January unit COMP C-5 acknowledged receipt and forwarded the submission to the Secretariat-General; on 3 February it was rejected as lodged out of time. <strong>Those three acts contradict one another.</strong></p>
<p><strong>2.</strong> You yourself describe the general presumption of non-disclosure as rebuttable, yet at the same time you hold against me that I have not demonstrated the contrary — while refusing to disclose to me even an inventory of the file. <strong>A presumption that cannot be rebutted is not a rebuttable presumption</strong> (Odile Jacob, C-404/10 P; Agrofert, C-477/10 P).</p>
<p><strong>3.</strong> The presumption covers neither the internal market analyses of DG Competition nor the unredacted version of the decision itself — these are acts of the institution, not submissions of the parties. Your decision contains no individual examination of those categories.</p>
<p><strong>4.</strong> You did not assess partial access under Art. 4(6); you refer me to documents that are public even without your decision.</p>
<p><strong>5.</strong> You dismissed the overriding public interest as considerations of a general nature, although I referred to <strong>recitals 138 to 142 of your own decision M.10815</strong>, in which the Commission itself states that it did not assess the parties' compliance with the GDPR.</p>
<p>I call upon you to handle the application on the substance, to provide me with the inventory of the file and to examine each requested document concretely and individually. Should the Commission fail to respond to this reply on the substance, I reserve the right to:</p>
<ul>
<li>lodge a complaint with the <strong>European Ombudsman</strong> for maladministration;</li>
<li>bring an <strong>action under Art. 263 TFEU</strong>.</li>
</ul>
<p>This reservation takes legal effect upon receipt of this letter.</p>
<p>Respectfully,<br>Peter Ferenc</p>
<p><em>The identical text was transmitted in German and Slovak in the same message.</em></p>""")

EXT = {
 1:[("privacy statement (DG COMP)","https://ec.europa.eu/info/principles-and-values/transparency/data-protection_en","trunc")],
 6:[("Access Info Europe — confirmation of timely submission (OneDrive)","","trunc")],
 11:[("Official portal for requesting Commission documents","https://ec.europa.eu/transparency/documents-register/","ok")],
 14:[("01_Criminal report on Landesjustizkasse Bamberg — EPPO, 7 languages, signed QES (Adobe Acrobat)","","trunc"),
     ("Facebook — StopTelekomKartell","","trunc")],
 15:[("Signed document (Adobe Acrobat)","","trunc")],
 16:[("Regulation (EC) No 1049/2001 — full text","https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32001R1049","ok")],
}
PHASES = {0:"Phase I — Initial request", 3:"Phase II — Initial refusal",
          6:"Phase III — Confirmatory application", 14:"Phase IV — Escalation"}

# ---------- hypertextove prepojenie pravnych citacii ----------
EL = "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:"
CUR = "https://curia.europa.eu/juris/liste.jsf?num="
LINKS = [
 (r"Regulation \(EC\) No 1049/2001",            EL+"32001R1049"),
 (r"Regulation 1049/2001",                      EL+"32001R1049"),
 (r"Article 7\(2\) of Regulation \(EC\) No 1049/2001", EL+"32001R1049"),
 (r"Article 7\(2\)",                            EL+"32001R1049"),
 (r"Art\. 7\(2\)",                              EL+"32001R1049"),
 (r"Article 4\(6\)",                            EL+"32001R1049"),
 (r"Art\. 4\(6\)",                              EL+"32001R1049"),
 (r"Art\. 2\(1\) of Regulation \(EC\) No 1049/2001", EL+"32001R1049"),
 (r"Article 15 TFEU",                           EL+"12016E015"),
 (r"Art\. 15\(3\) TFEU",                        EL+"12016E015"),
 (r"Article 42 of the Charter of Fundamental Rights of the European Union", EL+"12012P/TXT"),
 (r"Art\. 42 of the Charter",                   EL+"12012P/TXT"),
 (r"Article 41 of the Charter of Fundamental Rights of the European Union", EL+"12012P/TXT"),
 (r"Article 47 of the Charter of Fundamental Rights of the European Union", EL+"12012P/TXT"),
 (r"Articles 41 and 47 of the Charter of Fundamental Rights", EL+"12012P/TXT"),
 (r"Article 47 of the Charter of Fundamental Rights of the EU", EL+"12012P/TXT"),
 (r"Article 41 Charter",                        EL+"12012P/TXT"),
 (r"Regulation \(EU\) 2016/679 \(GDPR\)",       EL+"32016R0679"),
 (r"Regulation \(EU\) 2018/1725",               EL+"32018R1725"),
 (r"Directive \(EU\) 2017/1371 \(PIF\)",        EL+"32017L1371"),
 (r"Council Regulation \(EU\) 2017/1939",       EL+"32017R1939"),
 (r"Regulation \(EU\) No 910/2014 \(eIDAS\)",   EL+"32014R0910"),
 (r"eIDAS Regulation \(No 910/2014\)",          EL+"32014R0910"),
 (r"Article 325 TFEU",                          EL+"12016E325"),
 (r"Art\. 263 TFEU",                            EL+"12016E263"),
 (r"action under Art\. 263 TFEU",               EL+"12016E263"),
 (r"C-404/10 P",                                CUR+"C-404/10"),
 (r"C-477/10 P",                                CUR+"C-477/10"),
 (r"European Ombudsman",                        "https://www.ombudsman.europa.eu/"),
 (r"decision M\.10815",  "https://competition-cases.ec.europa.eu/cases/M.10815"),
 (r"M\.10815 – Deutsche Telekom / Orange / Telefónica / Vodafone – Joint Venture",
                         "https://competition-cases.ec.europa.eu/cases/M.10815"),
 (r"official portal for requesting European Commission documents",
                         "https://ec.europa.eu/transparency/documents-register/"),
]
_TOK = "\x00%d\x00"
def linkify(h):
    keep=[]
    def stash(m):
        keep.append(m.group(0)); return _TOK % (len(keep)-1)
    # chran existujuce <a>...</a> a vsetky tagy
    h = re.sub(r'<a\b.*?</a>', stash, h, flags=re.S)
    h = re.sub(r'<[^>]+>', stash, h)
    for pat,url in LINKS:
        h = re.sub(r'(?<![\w/])(' + pat + r')(?![\w/])',
                   lambda m,u=url: f'<a href="{u}" target="_blank" rel="noopener">{m.group(1)}</a>',
                   h, count=0)
    # znovu chran cerstvo vytvorene <a>
    for i,v in enumerate(keep):
        h = h.replace(_TOK % i, v)
    return h

CSS = open('css_from_existing.txt', encoding='utf-8').read()

def bubble(i, m):
    att = ""
    if m.get("att"):
        att = '<div class="att"><span class="attl">Attachments</span>' + "".join(
            f'<span class="attf">{html.escape(a)}</span>' for a in m["att"]) + '</div>'
    note = f'<div class="ref-box">{html.escape(m["note"])}</div>' if m.get("note") else ""
    src = (f'<a class="src" href="{SRC}#{m["anchor"]}" target="_blank" rel="noopener">source</a>'
           if m.get("anchor") else "")
    ext = ""
    if i in EXT:
        rows=[]
        for label,url,st in EXT[i]:
            if st=="ok":
                rows.append(f'<span class="extf"><a href="{url}" target="_blank" rel="noopener">{html.escape(label)}</a></span>')
            else:
                rows.append(f'<span class="extf trunc">{html.escape(label)} '
                            f'<em>— link truncated in the AskTheEU export; open the original message via “source”</em></span>')
        ext = '<div class="att"><span class="attl">Links in the message</span>' + "".join(rows) + '</div>'

    bad = f'<span class="badge badge-{m["badge"][0]}">{html.escape(m["badge"][1])}</span>'
    return f"""<div class="msg {m['who']}" id="msg-{i+1}">
<div class="bubble">
 <div class="subject">{html.escape(m['subject'])}</div>
 <div class="sender"><span class="sender-name">{html.escape(m['name'])}</span>
  <span class="sender-date">{m['date']}</span>{bad}{src}</div>
 {linkify(m['body'].strip())}
 {note}{att}{ext}
</div></div>"""

parts=[]
for i,m in enumerate(M):
    if i in PHASES:
        parts.append(f'<div class="phase-label"><span>{PHASES[i]}</span></div>')
    parts.append(bubble(i,m))

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>DG COMP · M.10815 — full correspondence (EASE 2025/6534)</title>
<style>
{CSS}
.src{{font-size:11px;color:#7a8899;text-decoration:none;border-bottom:1px dotted #b9c4d1}}
.src:hover{{color:var(--navy)}}
.att{{margin-top:12px;padding-top:10px;border-top:1px dashed var(--border);font-size:12px;color:#555}}
.attl{{display:block;font-weight:700;text-transform:uppercase;letter-spacing:.5px;font-size:11px;color:#7a8899;margin-bottom:4px}}
.attf{{display:block;padding-left:16px;position:relative}}
.attf::before{{content:'\\1F4CE';position:absolute;left:0}}
.extf{{display:block;padding-left:16px;position:relative;margin-bottom:3px}}
.extf::before{{content:'\\1F517';position:absolute;left:0}}
.extf.trunc{{color:#8a8a8a}}
.extf.trunc em{{font-size:11px}}
.note-verbatim{{background:var(--yellow);border:1px solid #f0c040;border-radius:4px;padding:12px 16px;margin:0 0 26px;font-size:13px}}
.msg.peter .bubble,.msg.commission .bubble{{max-width:none}}
</style>
</head>
<body>

<div id="langbar"><div class="lbinner">
<a class="lbhome" href="https://foxprof.club/kauzy-koncept/">← Back to case</a>
<a class="lbhome" href="dgcomp-correspondence.html">Summary version (9 languages) →</a>
</div></div>

<div class="case-header">
<h1>Request for access to documents — Case M.10815<br>Deutsche Telekom / Orange / Telefónica / Vodafone — Joint Venture</h1>
<div class="meta">Applicant: Peter Ferenc · Institution: European Commission, DG Competition, Unit C.5 Mergers · Secretariat-General, Transparency Unit<br>
Legal basis: Regulation (EC) No 1049/2001 · Article 15(3) TFEU · Article 42 of the Charter<br>
Channel: AskTheEU.org — 10 December 2025 to 20 July 2026 · {len(M)} messages</div>
<div class="ref">EASE 2025/6534 · COMP/C5/LC/(2025)/6534 · TFIA-2026-JV-009</div>
</div>

<div class="note-verbatim"><strong>Full record.</strong> Every message is reproduced in its original wording;
nothing has been shortened or paraphrased. Removed are only the platform elements of AskTheEU
(sidebar, “Link to this / Report”, “show quoted sections”, reference lists and automatic footers).
Messages sent in several languages are reproduced in English and marked accordingly.
A condensed nine-language overview of the same file is available
<a href="dgcomp-correspondence.html">here</a>.</div>

<div class="timeline">
{chr(10).join(parts)}
</div>

<div class="case-footer">
FIA FOX — Fair Internet Alliance · <a href="https://foxprof.club/">foxprof.club</a><br>
Source of the record: <a href="{SRC}" target="_blank" rel="noopener">asktheeu.org</a> ·
Case file M.10815 · EASE 2025/6534
</div>

</body>
</html>"""

open('dgcomp-correspondence-full.html','w',encoding='utf-8').write(HTML)
print("hotovo:", len(HTML), "znakov,", len(M), "sprav")
