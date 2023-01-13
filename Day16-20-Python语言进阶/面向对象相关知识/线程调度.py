"""
多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition
"""
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading


class Account:
    """银行账户"""

    def __init__(self, balance) -> None:
        self.balance = balance
        lock = threading.RLock()

    def withdraw(self, money):
        """取钱"""
