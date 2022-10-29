

class SearchRange:

    def __init__(self, target):
        self.target = target

    def search(self, range, helper=None):
        # can use different helper function
        if helper is None:
            helper = self.helper

        # search while low doesn't exceed high
        l, h = range
        while l <= h:
            
            # get middle value and test w/ helper
            m = (l + h) // 2
            guess = helper(m)

            # found the target
            if guess == 0:
                return self.target
            # over-estimate of target
            if guess > 0:
                # eliminate [m, r]
                h = m - 1
            # under-estimate of target
            if guess < 0:
                # elimnate [l, m]
                l = m + 1 
            
    def helper(self, x):
        if x > self.target:
            return 1
        if x < self.target:
            return -1
        return 0

    def __call__(self, range, helper=None):
        return self.search(range, helper)

if __name__ == "__main__":
    search = SearchRange(40)
    print(search((-100, 100)))