import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_healthsecure_pdfs():
    # Setup styles
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#1A365D'),
        spaceAfter=12
    )
    
    h2_style = ParagraphStyle(
        'DocH2',
        parent=styles['Heading2'],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#2B6CB0'),
        spaceBefore=12,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['BodyText'],
        fontSize=10,
        leading=14,
        spaceAfter=8
    )

    documents_data = {
        "01_Member_Handbook.pdf": {
            "title": "HealthSecure Insurance - Member Handbook",
            "sections": [
                ("1. Welcome to HealthSecure", "Welcome to HealthSecure Insurance. We provide comprehensive healthcare coverage across Bronze, Silver, and Gold plans. This handbook explains how your plan works and how to navigate your care."),
                ("2. How HealthSecure Works", "HealthSecure operates an integrated provider network. Depending on your plan, services are covered through in-network providers or out-of-network benefits (see 02_Benefits_Guide.pdf)."),
                ("3. Member Responsibilities", "Members must present their HealthSecure ID card at appointments, pay required cost-sharing at point of service, and verify prior authorization requirements (see 04_Prior_Authorization_Guide.pdf)."),
                ("4. Key Terminology & Cost Sharing", "Understanding key insurance terms:\n• Deductible: The amount you pay out-of-pocket before benefits apply.\n• Copayment: A fixed fee paid per visit.\n• Coinsurance: Your percentage share of medical costs.\n• Out-of-Pocket Maximum: The limit on what you pay in a plan year."),
                ("5. Accessing Care & Privacy", "To schedule primary or specialist visits, contact network providers directly. Your privacy is protected under strict HIPAA guidelines."),
                ("6. Contact Information", "Customer Support: 1-800-555-SECURE | Email: support@healthsecure.com | Hours: Mon–Fri 8am–8pm EST")
            ]
        },
        "02_Benefits_Guide.pdf": {
            "title": "HealthSecure Insurance - Benefits Guide",
            "sections": [
                ("1. Plan Overview (Bronze, Silver, Gold)", "HealthSecure offers three core tiers:\n• Bronze: Lower premiums, higher deductibles ($5,000 deductible, 30% coinsurance).\n• Silver: Balanced coverage ($2,500 deductible, 20% coinsurance).\n• Gold: Comprehensive coverage ($500 deductible, 10% coinsurance)."),
                ("2. Primary & Specialist Care", "Primary care visits require a $25 copay (Silver/Gold). Specialist care requires a primary care referral for Bronze plans. See 03_Coverage_Policies.pdf for network details."),
                ("3. Emergency & Preventive Care", "Emergency care is covered 100% after copay at any facility. Preventive care (annual physicals, vaccinations) is covered with $0 copay across all plans."),
                ("4. Diagnostic Imaging & Physiotherapy", "Basic X-rays are covered in-office. MRIs and CT scans require prior authorization (refer to 04_Prior_Authorization_Guide.pdf). Physiotherapy is capped at 20 visits/year for Gold plans."),
                ("5. Prescription Drugs & Limits", "Prescriptions are tiered: Generic (Tier 1), Preferred Brand (Tier 2), Non-Preferred (Tier 3), and Specialty (Tier 4). Specialty drugs require prior approval.")
            ]
        },
        "03_Coverage_Policies.pdf": {
            "title": "HealthSecure Insurance - Coverage Policies",
            "sections": [
                ("1. Covered vs. Excluded Services", "Covered: Inpatient care, emergency medicine, preventive visits, outpatient surgery. Excluded: Cosmetic surgery, experimental therapies, adult dental/vision unless added via rider."),
                ("2. Medical Necessity Rules", "All treatments must meet HealthSecure Medical Necessity Guidelines. Non-necessary procedures will result in claim denials (see 05_Claims_Guide.pdf)."),
                ("3. Network Rules & Waiting Periods", "In-network providers bill HealthSecure directly. Pre-existing condition waiting periods do not apply to ACA-compliant plans. Annual coverage limits apply as outlined in 02_Benefits_Guide.pdf."),
                ("4. Scenarios & Examples", "Scenario A: Emergency Room Visit - Covered under emergency rules regardless of network.\nScenario B: Elective Surgery - Must be pre-authorized per 04_Prior_Authorization_Guide.pdf.")
            ]
        },
        "04_Prior_Authorization_Guide.pdf": {
            "title": "HealthSecure Insurance - Prior Authorization Guide",
            "sections": [
                ("1. Understanding Prior Authorization", "Prior Authorization (PA) ensures medical services are necessary and cost-effective before care is delivered."),
                ("2. When PA is Required", "Required for: Elective surgeries, outpatient MRIs/CT scans, specialty medications, and extended inpatient stays."),
                ("3. Submission & Timelines", "Providers submit PA requests online. Standard review: 3–5 business days. Urgent review: 24–48 hours."),
                ("4. Denial Reasons & FAQ", "Common denial grounds: Lack of clinical documentation, alternative treatments not attempted. Decisions can be appealed via 06_Appeals_Guide.pdf.")
            ]
        },
        "05_Claims_Guide.pdf": {
            "title": "HealthSecure Insurance - Claims Guide",
            "sections": [
                ("1. How Claims are Submitted", "In-network providers submit claims automatically. For out-of-network care, members submit a CMS-1500 or standard claim form with itemized receipts."),
                ("2. Claim Lifecycle & Statuses", "Lifecycle steps: Received -> Pending Review -> Approved/Denied -> Processed.\nCheck status online or call support listed in 01_Member_Handbook.pdf."),
                ("3. Common Denial Reasons & Processing", "Denials occur due to missing authorization (04_Prior_Authorization_Guide.pdf), non-covered services (03_Coverage_Policies.pdf), or filing after 90 days. Processing takes 14–30 calendar days.")
            ]
        },
        "06_Appeals_Guide.pdf": {
            "title": "HealthSecure Insurance - Appeals Guide",
            "sections": [
                ("1. Understanding Claim Denials", "Members have the right to challenge any adverse benefit determination within 180 days of notification."),
                ("2. Appeal Eligibility & Process", "First Level: Internal appeal reviewed by a neutral medical panel. Second Level: External independent review if internal appeal is upheld."),
                ("3. Required Documents & Timelines", "Submit the Appeal Form, provider supporting notes, and original Explanation of Benefits (EOB). Internal appeals are decided within 30 days.")
            ]
        }
    }

    # Ensure output directory exists
    os.makedirs("data/healthsecure_pdfs", exist_ok=True)

    for filename, data in documents_data.items():
        filepath = os.path.join("data/healthsecure_pdfs", filename)
        doc = SimpleDocTemplate(filepath, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
        story = []

        # Add Header Title
        story.append(Paragraph(data["title"], title_style))
        story.append(Spacer(1, 10))

        # Add Sections
        for heading, text in data["sections"]:
            story.append(Paragraph(heading, h2_style))
            # Support newlines in section text
            for para in text.split('\n'):
                story.append(Paragraph(para, body_style))
            story.append(Spacer(1, 6))

        doc.build(story)
        print(f"Generated: {filepath}")

if __name__ == "__main__":
    create_healthsecure_pdfs()