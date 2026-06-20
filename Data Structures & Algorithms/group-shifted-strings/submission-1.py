class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        all_sequences = {}
        def hash(s: str):
            key = []
            for a, b in zip(s, s[1:]):
                key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            return ''.join(key)

        for s in strings:
            h = hash(s)
            if h in all_sequences:
                all_sequences[h].append(s)
            else:
                all_sequences[h] = [s]
        print(all_sequences)
        return list(all_sequences.values())
