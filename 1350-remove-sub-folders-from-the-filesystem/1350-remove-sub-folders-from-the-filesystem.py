class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        s = sorted(folder)

        output = []
        found = set()

        for a in s:
            currpath = ""
            f = False
            for b in a.split('/')[1:]:
                currpath += "/" + b
                if currpath in found:
                    f = True
                    break
            if not f:
                found.add(currpath)
                output.append(currpath)

        return output
