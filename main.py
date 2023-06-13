import subprocess

def send_email(subject, body, recipient):
  script = """
  tell application "Mail"
    set newMessage to make new outgoing message with properties {{subject:"{subject}", content:"{body}", visible:"true"}}
    tell newMessage
      make new to recipient at end of to recipients with properties {{address:"{recipient}"}}
      set content type to "text/html"
      send
    end tell
  end tell
  """.format(subject = subject, body = body, recipient = recipient)

  subprocess.run(["osascript", "-e", script])

html = open("index.html").read()

email_subject = "Hello from Python!"
# email_body = html
email_body = "<h1>This is the html content of the body</h1>"
recipient_email = "mkutaybzkrt01101011@gmail.com"

send_email(email_subject, email_body, recipient_email)