from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import os
import smtplib
import getpass

class EmailSender:
    '''
    Very crude email sender
    '''
    
    def __init__(
        self,
        sender: str,
        recipient: str,
        subject: str,
        text: str,
        smtp_server_name: str,
        smtp_server_port: int
        ) -> None:
        
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.text = text
        self.smtp_server_name = smtp_server_name
        self.smtp_server_port = smtp_server_port
        self.user = sender 
        self.password = getpass.getpass(prompt='Enter Password: ')
        self.msg = self.prepare_message()
        
    def prepare_message(self) -> MIMEMultipart:
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = self.recipient
        msg.attach(MIMEText(self.text, "plain"))
        return msg
        
    def attach_image(self, image_file: str) -> None:
        with open(image_file, 'rb') as f:
            img_data = f.read()
        image = MIMEImage(img_data, name=os.path.basename(image_file))
        self.msg.attach(image)
        
    def attach_pdf(self, pdf_file: str) -> None:
        with open(pdf_file, 'rb') as f:
            pdf_data = f.read()
        pdf = MIMEApplication(pdf_data, _subtype="pdf")
        pdf.add_header(
            'Content-Disposition', 
            'attachment', 
            filename=os.path.basename(pdf_file)
        )
        self.msg.attach(pdf)
        
    def send_message(self):
        server = smtplib.SMTP( self.smtp_server_name, self.smtp_server_port)
        server.ehlo()
        server.starttls()
        server.login(self.user, self.password)
        server.send_message(self.msg)
        server.quit()
        
if __name__ == '__main__':
    
    sender = EmailSender(
        sender = 'john.doe@somedomain.com',
        recipient = 'jane.doe@somedomain.com',
        subject = 'test',
        text = 'this is a test',
        smtp_server_name = 'smtp.somedomain.com',
        smtp_server_port = 587
    )
    sender.attach_image('/path/to/imagefile.png')
    sender.attach_pdf('/path/to/document.pdf')
    sender.send_message()
    
