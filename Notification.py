import yagmail

# Register only once (stores encrypted in keyring)
yagmail.register("rohitbhagasra4@gmail.com", "uinikxehmairbpei")  # Replace both

# Initialize mail sender
yag = yagmail.SMTP("rohitbhagasra4@gmail.com")  # Only email here

def notify_hr_email(emp_id, recs, to="roxhiit4@gmail.com"):
    subject = f"🚨 Attrition Alert: Employee {emp_id}"
    body = (
        f"Hi HR Team,\n\n"
        f"Employee ID: {emp_id} is predicted to be at high risk of leaving.\n\n"
        f"Top Recommendations:\n- " + "\n- ".join(recs) +
        "\n\nRegards,\nAttrition AI Assistant"
    )
    yag.send(to=to, subject=subject, contents=body)
    print(f"✅ Email sent to HR for Employee {emp_id}")
