import sys
# import time  # For Test


class LoggerProgress():

    def __init__(self, value=0.0, end=1.0, bar_len=30):
        self.bar_len = bar_len
        self.value = value
        self.end = end
        self.text = None


    def _get_str(self):
        val = 1.0 * self.value / self.end
        bar_len_now = self.bar_len * val
        bar_tip_flag = 0 if bar_len_now % 1.0 < 0.5 else 1
        bar_len_now = int(bar_len_now)
        return "[%s%s%s] %.2f%%%s%s" % (
            '=' * bar_len_now,
            '>' if bar_len_now <= self.bar_len else '',
            ' ' * (self.bar_len - bar_len_now),
            val * 100.0,
            (' ' + self.text) if self.text else '',
            '\n' if self.value >= self.end else ''
        )


    def update(self, value, text=None):
        self.value = value
        self.text = text
        sys.stderr.write('\r\033[K' + self._get_str())
        sys.stderr.flush()


# For Test
# progress = LoggerProgress()
# for i in range(0, 170 + 1):
#     time.sleep(0.01)
#     progress.update(i / 170.0, str(i))
