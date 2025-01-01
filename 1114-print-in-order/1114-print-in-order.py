class Foo(object):
    def __init__(self):
        self.second_semaphore = threading.Semaphore(0)  # Initially locked
        self.third_semaphore = threading.Semaphore(0)   # Initially locked


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_semaphore.release()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        
        self.second_semaphore.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_semaphore.release()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        self.third_semaphore.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()