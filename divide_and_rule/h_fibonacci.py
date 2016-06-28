from threading import Thread

class FibonacciThread(Thread):
	def __init__(self, number):
		if not isinstance(number, int):
			raise Exception("number is not an integer")
		self.number = number
		Thread.__init__(self)

	def run(self):
		one = 0;
		two = 1;

		for x in range(self.number):
			(one, two) = (two, one + two)

		print str(self.number) + " => " + str(one);
