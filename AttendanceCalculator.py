class AttendanceCalculator:
    def __init__(self, num_days, allowed_consec_days):
        if (allowed_consec_days>num_days):
            raise Exception("number of days must be greater than number of consecutive allowed holidays")
        self.num_days = num_days
        self.allowed_consec_days = allowed_consec_days

    
    # including recursive just to show the approach, dynamic method will always be chosen by default
    def _calculate_ways_recursive_helper(self, num_days, allowed_consec_days):

        if (allowed_consec_days==self.allowed_consec_days):
            return 0
        elif (num_days==0):
            return 1

        return self.calculate_ways_recursive(num_days-1, 0) + self.calculate_ways_recursive(num_days-1, allowed_consec_days+1)

    def calculate_ways_recursive(self):

        return self._calculate_ways_recursive_helper(self.num_days, 0), self._calculate_ways_recursive_helper(self.num_days-1, 1)

    
    def calculate_ways_dynamic(self):

        n, m = self.num_days, self.allowed_consec_days
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(m):
            dp[0][i] = 1

        for i in range(1, n+1):
            for j in range(m-1, -1, -1):
                dp[i][j] += dp[i-1][0] + dp[i-1][j+1]
        
        return dp[n][0], dp[n-1][1]

    def get_ways_and_print(self):

        ans1, ans2 = self.calculate_ways_dynamic()
        print("{}/{}".format(ans2,ans1))