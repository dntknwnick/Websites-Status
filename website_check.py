#!/usr/bin/env python3

import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class website_tester():

    def __init__(self):
        self.urls = 'https://apseveningcollege.in/', 'https://apspucollege.com/', 'https://commerceaftertenth.com/',\
            '\n https://dsctedu.in/', 'https://ektaschools.com/','https://eurokidsbgroad.com/', 'https://jeffinternational.com/', \
            '\nhttps://jsdegreecollege.com/','https://jspuc.com/', 'https://mlps.co.in/',\
            '\n https://newtonpublicschool.info/', 'https://nirmanschools.com/', 'https://www.nextelement.in/',\
            '\n https://npsjayanagar.com/', ' https://sahitya.school/',\
            '\n https://simsbangalore.com/', 'https://soundaryacbseschool.com/',\
            '\n https://soundaryacentralschool.com/', 'https://soundaryalaw.nextelement.co.in/',\
            '\n https://soundaryapucollege.com/', 'https://soundaryaschool.com/', 'https://vecjnr.edu.in/',\
            '\nhttps://yashasviinternationalschool.com/',\
            '\nhttps://soundaryatrust.nextelement.co.in/', 'https://apscommerce.in/', 'https://www.wpls.in/','https://spruhaedu.in/','https://nextelement.in/'
        self.results = []
        self.error = requests.ConnectionError
        self.error1 = requests.HTTPError
        self.error2 = requests.Timeout
        self.headers = {'Cache-Control': 'no-Cache','Pragma': 'no-cache'}

    def send_email(self, recipient_email, email_body):
        sender_email = 'shreyas@nextelement.in'
        sender_password = 'g00gle@it'
        message = MIMEMultipart()
        html = '''
                <html>
                <body>
                    <h3>Your website checking result is as follows:</h3>
                    <table style="border:2px">
                    <tr>
                    <td>Url</td>
                    <td>Status Code</td>
                    <td style="text-align:center">Reason </td> 
            '''

        for result in self.results:
            if "working fine" in result:
                html += f" <tr>" \
                        f"<td style='color:green;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{result}</td>" \
                        f"</tr>"
            elif "Needs little correction and maintenance" in result:
                html += f"" \
                        f"<tr>" \
                        f"<td style='color:orange;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{result}</td>" \
                        f"</tr>"
            elif "Needs proper maintenance" in result:
                html += f"" \
                        f"<tr>" \
                        f"<td style='color:red;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{result}</td>" \
                        f"</tr>"
            else:
                html += f"" \
                        f"<tr>" \
                        f"<td style='color:grey;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{result}</td>" \
                        f"</tr>"
        html += f'''

                </table>

                </body>
                </html>
                '''

        message.attach(MIMEText(html, 'html'))
        message['From'] = sender_email
        message['To'] = ','.join(recipient_email)
        message['Subject'] = f'Website status for {len(self.urls)} URLs'
        smtp_server = smtplib.SMTP('smtp.zoho.in', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)
        smtp_server.sendmail(sender_email, recipient_email, message.as_string())
        smtp_server.quit()

    def website_check(self, url, headers):
        try:
            response = requests.get(url, headers=headers)
            status_code = response.status_code

            reason = response.reason

            if 200 <= status_code < 300:
                result = f"<tr>" \
                         f"<td style='color:green;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{url} </td>" \
                         f"<td style='color:green;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{status_code}</td>" \
                         f"<td style='color:green;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{reason}</td>" \
                         f"</tr>"
            elif 300 <= status_code < 400:
                result = f"<tr>" \
                         f"<td style='color:orange;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{url} </td>" \
                         f"<td style='color:orange;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{status_code}</td>" \
                         f"<td style='color:orange;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{reason}</td>" \
                         f"</tr>"
            elif 400 <= status_code < 600:
                result = f"<tr>" \
                         f"<td style='color:red;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{url} </td>" \
                         f"<td style='color:red;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{status_code}</td>" \
                         f"<td style='color:red;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{reason}</td>" \
                         f"</tr>"
            else:
                result = f"<tr>" \
                         f"<td style='color:grey;border: 1px solid black; padding: 5px;border-spacing: 0px'>{url} </td>" \
                         f"<td style='color:grey;border: 1px solid black; padding: 5px;border-spacing: 0px'>{status_code}</td>" \
                         f"<td style='color:grey;border: 1px solid black; padding: 5px;border-spacing: 0px'>{reason}</td>" \
                         f"</tr>"

        except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError, requests.exceptions.Timeout) as e:
            result = f"<tr>" \
                     f"<td style='color:grey;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{url} </td>" \
                     f"<td style='color:grey;border: 1px solid black; padding: 5px;border-spacing: 0px;'>Error</td>" \
                     f"<td style='color:grey;border: 1px solid black; padding: 5px;border-spacing: 0px;'>{str(e)}</td>" \
                     f"</tr>"

        self.results.append(result)

    def check_all_website(self):

        for url in self.urls:
            self.website_check(url,self.headers)

        email_body = 'Your website checking result is as follows:' + ''.join(self.results)
        # recipient_email = ['manjukiran@nextelement.in', 'mahesh@nextelement.in', 'ravim@nextelement.in', 'sharath.patel@nextelement.in',
        #                     '\ndhanashree@nextelement.in','suganthi@nextelement.in']
        recipient_email = 'shreyas@nextelement.in'
        self.send_email(recipient_email, email_body)


if __name__ == '__main__':
    check = website_tester()
    check.check_all_website()

