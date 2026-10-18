import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""

        need = collections.Counter(t)   # required counts
        window = collections.Counter()  # current counts

        have = 0
        need_types = len(need)

        l = 0
        best_len = float("inf")
        best = (0, 0)

        for r, ch in enumerate(s):
            if ch in need:
                window[ch] += 1
                if window[ch] == need[ch]:
                    have += 1

            while have == need_types:
                # update answer
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best = (l, r)

                # shrink from left
                left_ch = s[l]
                if left_ch in need:
                    window[left_ch] -= 1
                    if window[left_ch] < need[left_ch]:
                        have -= 1
                l += 1

        if best_len == float("inf"):
            return ""
        l, r = best
        return s[l:r+1]
