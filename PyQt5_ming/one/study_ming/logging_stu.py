import logging

""" 设置警告级别从哪开始，我设置debug开始，就会从debug显示到critical """
logging.basicConfig(level=logging.DEBUG)

""" 生成一个utf-8的my_logs.log文件 """
# logging.basicConfig(filename='my_logs',
#                    encoding='utf-8',
#                    filemode='w')  #只写模式，意味着每次运行脚本都会覆盖原有内容

logging.debug('DEBUG')
logging.info('INFP')
logging.warning('WARNING')
logging.error('ERROR')
logging.critical('CRITICAL')

x: int = 10 + 10

logging.info('The answer is:%s', x)  # 两种写法而已
logging.info(f'The answer is:{x}')
