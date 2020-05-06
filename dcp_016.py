# =-=-=-= DAY 16 [Easy] =-=-=-=
#
# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
#
#  * record(order_id): adds the order_id to the log
#  * get_last(i): gets the ith last element from the log. i is guaranteed to be
#    smaller than or equal to N.
#
# You should be as efficient with time and space as possible.


class OrderLog:
    order_ids = []

    def record(self, order_id):
        self.order_ids.append(order_id)

    def get_last(self, i):
        return self.order_ids[-(len(self.order_ids) - i)]


o = OrderLog()
o.record(1234)
o.record(1235)
o.record(1236)
print(o.get_last(1))
