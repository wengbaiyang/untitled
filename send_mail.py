import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('895279343@qq.com','U201772900@hust.edu.cn',
                """To: U201772900@hust.edu.cn
                From: 895279343@qq.com
                
                hello world.
                """)
server.quit()