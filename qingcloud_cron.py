#!/usr/bin/env python
# encoding: utf-8
import qingcloud.iaas
import schedule
import time

#run in tmux or supervisor
import logging
import logging.config

logging.config.fileConfig('logging.ini',defaults={'logfilename': 'qingcloud_cron.log'})

from send_emails import send_mail
from utils import ApplicationInstance
# create logger

from qingcloud_setting import zone,qy_access_key_id,qy_secret_access_key
conn = qingcloud.iaas.connect_to_zone(
        zone,
        qy_access_key_id,
        qy_secret_access_key,
    )


instance_id = u"instance_id"

def start_instance():
    ret = conn.start_instances(
        instances=[instance_id]
    )
    logger = logging.getLogger(__name__)
    logger.info(ret)
    send_mail("qingcloud",ret)
    return ret

def stop_instance():
    ret = conn.stop_instances(
        instances=[instance_id]
    )
    logger = logging.getLogger(__name__)
    logger.info(ret)
    send_mail("qingcloud",ret)
    #判断ret是否正常,发送email
    return ret


def job():
    message = "I am working"
    logger = logging.getLogger(__name__)
    send_mail("qingcloud",message)
    logger.info(message)
    #print("I'm working...")

#schedule.every(1).second.do(job)
schedule.every(1).minutes.do(job)
schedule.every().day.at("14:00").do(start_instance)
schedule.every().day.at("16:00").do(stop_instance)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

if __name__ == '__main__':
    ApplicationInstance()  # 保证脚本单例运行
    while True:
        schedule.run_pending()
        time.sleep(1)
