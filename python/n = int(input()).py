import re

strok = "'CCATCACATT'"
s = len(re.findall("CAT", strok))

lst = [i for i in strok.split("CAT") if i != ""]
print(lst)
if (
    not (strok.startswith("C") and strok.endswith("T"))
    or "CT" in strok
    or "AA" in strok
):
    print(-1)

else:
    lst = [i for i in strok.split("CAT") if i != ""]
    for i in lst:
        for j in i:
            if (
                j + "T" == "CAT"
                or j + "AT" == "CAT"
                or "C" + j == "CAT"
                or "CA" + j == "CAT"
                or i == "A"
            ):
                s += 1
    print(s)
