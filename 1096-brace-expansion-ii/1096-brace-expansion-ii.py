class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            result = {""}
            union = set()

            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    union |= result
                    result = {""}
                    i += 1

                elif expression[i] == '{':
                    sub, i = parse(i + 1)
                    result = {a + b for a in result for b in sub}

                else:
                    result = {a + expression[i] for a in result}
                    i += 1

            union |= result

            if i < len(expression) and expression[i] == '}':
                i += 1

            return union, i

        result, _ = parse(0)
        return sorted(result)