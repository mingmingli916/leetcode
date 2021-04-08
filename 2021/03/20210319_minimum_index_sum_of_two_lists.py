"""
Suppose Andy and Doris want to choose a restaurant for dinner,
and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum.
If there is a choice tie between answers, output all of them with no order requirement.
You could assume there always exists an answer.



Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Example 3:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]
Example 4:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]
Example 5:

Input: list1 = ["KFC"], list2 = ["KFC"]
Output: ["KFC"]


Constraints:

1 <= list1.length, list2.length <= 1000
1 <= list1[i].length, list2[i].length <= 30
list1[i] and list2[i] consist of spaces ' ' and English letters.
All the stings of list1 are unique.
All the stings of list2 are unique.
"""
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = []
        minimum = 2001
        d = {}
        for i, restaurant in enumerate(list1):
            d[restaurant] = i

        for i, restaurant in enumerate(list2):
            if restaurant in d:
                current = i + d[restaurant]
                if current == minimum:
                    common.append(restaurant)
                elif current < minimum:
                    minimum = current
                    common = [restaurant]
        return common


if __name__ == '__main__':
    solution = Solution()

    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]

    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]

    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"]
    list1 = ["pkwenkodtlbbdgvopqaeygphtlrmo", "agfqdph", "vagpvsdzqhwnlogzyje", "lfsxwnhweveaaekybglvcluyeb", "gpgbqii",
             "fboaiwtlfccdolpqutf", "swgsvdptrtepv", "nqmgha", "rfbmlfacpec", "mjgmpewjnlwijzx",
             "fxtsgerpchszrkfjpwwigy",
             "yvizbmradwgxedumcbcktxublw", "p", "ijrbjrqopmbveayra", "ckhb", "fhjbrzhroorglgbltarrvtjnkz",
             "bsmqkkfmzszgtffpkpjouoxdmofivm", "vbqhjdqajtvy", "eelflqtsplanaahmxssqe", "gwurhajbnavidhipzhxvlf",
             "lfgztikdpethoionvs", "ywqhjouxx", "zegpdvbmdgslagpvsjnmchspix", "rooillldcagevixecdxffz",
             "huhwnjqriyiweilhjzijuftlzp", "lha", "ashrazctgqgwrm", "geg", "nkmofftbapqitraxtfnilsfvwvpas", "cblx",
             "xhc",
             "ykiatwmdigjxmxevdbd", "alzzxhra", "zcxbycuiqlvfpuslvv", "ufolcgdeo", "wnnhai",
             "eypstxtyxnnqnkmqptekdgpdqcdqn",
             "zosncavdfjcsdnrxdp", "ptopwfkziuttfeazrrglqdbszvr", "qlewoezxzmlhgypikhdl", "ykoyilcm",
             "fmgqdzvdtyethyynjjpbl",
             "dxeyeyejkosdpnub", "ymlznwinj", "qyfopqgmglfiofw", "wwqbevusanvcdzeshcglrzlarer",
             "tmsfjgfjdjdbczcseznowpptr",
             "zkrcckbowwjxmfmdikfsbpyxrmgg", "aooilovrtwqoaremskb", "acqnnodwqzwlqnynvb",
             "xinbdvhzfykpmzpecgngelczoukzd",
             "ugjnsgqlp", "vdztloyrjpzzylesddiewfemmbgfwe", "ucnfeysd", "cywlrzkl", "rezogqmazduvkcypiupyitmhrfmzki",
             "hydpvnbhqpkvrcc", "axdaqveyksrmpc", "l", "zuzgiuonhoaaqmafflrnsamdkefoki", "wbtrhqdbwqyrvjizkgj",
             "hyxexwoosybkpifyohasxtk", "kexssggfp", "eblxqnyke", "etwelbjtxilczjudlyziyosp", "coxufsaunxexcshrcqyjz",
             "hlcyxndydrxgebcjtgrjlfhhiqeh", "vlhyfvzcuuqrqymnzlbqwlwyk", "xo", "n", "hytiwcsrbwyj", "kbsglfxut",
             "mducxmhhvuuoaxazhwpsuisush", "fqoxrbegbqfseoiqvevfjua", "cugcsdfdgggnxbsrloqynmjisfxqcf",
             "gwmoxooqbgkuqhitqndhjknpoi", "tvwhfeoxshl", "ltvkvjigjqdjmfqihssvnnmxke", "tvhkudu", "utwqphdxvmtvtjw",
             "npjohbkidogcjbkpairnmmgslk", "xtzyn", "shufzxmpntnwkljqlayypynmnsvjnq", "iwmovzzkfpvixarqckonwqhb",
             "bdjntlktemditgnn", "tphnrrekc", "jbtpcxbxdbdpjztbvp", "jxejmmiwfrrknjyek", "jzfkmowocsuhipwvyavcimgslsa",
             "pgsbqvig", "fnxfo", "ys", "jovaimqzyyputxnatlgvtflxmjwrgy", "fndfnvpnmgcxjbfydgwiwpvst",
             "eikqjjhbfnabekalchmoigbsvj", "esvmtdtyojpoccpnhmweleclk", "idrkmks", "ucxqf", "qaaoyjczafkqyncmmuqfj",
             "xfhfqdqnklxq", "krtfunvglmtcwasqlvhq", "uilnponlhvulz", "hpzca", "fhukhpkax", "bv", "xxfrzciifwxwzkqlhzi",
             "upmawfjrcvyqphcgznqvlunehgm", "stbyc", "klgybdvijbdraoveascq", "zhcnue", "njnpajotnwihwedlefrukx",
             "mtndwtean",
             "oblhinaeguymmkleqeogwrzmbltl", "htjlnvbdfuzsjypkanhzg", "zhjn", "pjgfwoikxbybblja",
             "ljdkfxvylzmspudjqqugddxrnhn",
             "isl", "azusu", "ymyzwmsxcirfwhsafs", "uvpjsrqhwxdoeuc", "bl", "gfubyw", "sfxkoexlvpihhfhfq",
             "jsmzeshdnugttvppha",
             "vdvhdvfztaxcyhjdugctrvkgulmbj", "knwvl", "xengrpxq", "qggmtusbpnypjbxcisnoy", "rhehzhnlk", "ztanalcvncvm",
             "favfgqwpedkohfkoakisbmbxbxf", "mofdl", "fyfiwcckdrjjpqfyrldhdyvu", "fuosbwciqqzosy", "chnbkhdgyjoxeglvfc",
             "xflneeeaomxjphvgyohoakxhj", "stpuhrfbhoxf", "czoepwnymcz", "rvscpckcpjwgulnfnelspis", "frtrodsnrmsmaaws",
             "sykhquipjd", "rrwyr", "oglbicrgqvradxwtghghppnzznq", "lhaijmcqlnrgimhbptwmkwt",
             "lwdhpatigvhypgzrertalatqspohi",
             "leyshdfdlagoalvfbegapxregtuh", "occgkf", "gscljupcrmbbeobwvdht", "kiul", "syc", "uoejbnenp",
             "takqafyujrchibalhi",
             "gjcgpxz", "jiuiut", "faegljhiknwlygwhlu", "yxsybpiprmuhzplfphfeqazzyndtv", "ktbjtqyvuuxqajcesnaw",
             "huuftubpzskytmniladxkkgczftxp", "hjiq", "d", "udqooeglslqpajnip", "lztmnoajehsvz",
             "ybvtkizlmyfngyjwwowgsm",
             "xgvvsydndmgs", "smbvogzsmbaxktmqwleprmbdxqf", "izdo", "sdvhj", "qyn", "framwuszazkwdilvtylmkru",
             "jmbefcplwqosvfx", "kgsptbnifrvczouohrrprli", "gcydrneexbcuqopkpcmd", "tewapttno", "lmhuzhpzmym",
             "yqzblljae",
             "pgxnwszovqgqtcqpzmssneqejgjs", "xwetnsmpotlpn", "utraamepcsomyxsqbkshgyraleekxw", "dvjhqppvoowntco",
             "yohsoxdaubemaogltuk", "nasrnrizinuypjdnjehqqoitmvk", "xerymxgwvzcb", "ouzklsdedbvwwketdhcfeuluvckf",
             "ztindosdnqsyquuhzjzpxkbeefun", "kfjirgxu", "ypmskmp", "wsi", "pcfbmtafjvrurtrvjsumfjfttu",
             "aqlwxsrxggtfnz",
             "vbvbde", "ceyogdjazwskvjbdwrvufpqcjrxpws", "vfhpldeneeqxykmum", "vuqxhsrspvqath", "tloeehsq", "zo",
             "hsxjfwgbuorfznekqdvahrxgui", "ctsetmijpnp", "jjdizlchlorva", "rvrfcepmxpeofenooth", "qojwwpjt", "gtdq",
             "rbdbetwubqjppupythw", "ccdllhhubyjxfmvmxdcmpzdwy", "vs", "ndfm", "selamkurrltpjkt", "whxez",
             "woryubernrrwthyce",
             "ozzcx", "abtsca", "nqyxdju", "phuolroyieomapmirpvaldtksgl", "yaqhaymtozosbacorzavpgdgl",
             "dbzlkbdgrtavnorpfvuvnxwnzeoc", "user", "dbtfwbavxuxqzjtycorez", "hhemkmkwuikfasranjgsjtug",
             "obsskhdangnyiok",
             "ikkzxhjapdmkyiutryhzvsijxzeo", "hvbgprgostxbh", "ecnzsirsqqqwldmzsat", "pewwoxivlouurvfsadrc",
             "lbujpsqpfk",
             "eqjukrlgnbpuesgea", "sgsnxtsznntdptmxjg", "bpkwyfwccmnjqwdyhxrjaaxjcw", "omvzwyrzlwstnwhwhssajzhbsd",
             "ux",
             "exlyaiolmjrca", "zpdbagmcdfltcoiobkdrticgzeyn", "bqbebomqulgwltbortyu", "ihgevtuipgkvqgpkhlui",
             "tvrippfy",
             "pdbmjihtodwwa", "siucrhynh", "izvwi", "bxhsxqhtbdsgpfeiqpdjumcjm", "zrnnxdcd",
             "mfpobuitnnxmkddwwzlfauosuzd",
             "utolwmietafptpdnb", "mkointotmaled", "likkuxoyubyandcnm", "mszirwc", "qp",
             "dhvshmxnljtsozhsjugbokxjiiapmb",
             "jxibbfteyfqh", "strbmsndazagstxvojxc", "tpyrljqdhatboqrnnnq", "whjktettjhafcviiivw",
             "pqcetglnhibyhmveyblnlrymw",
             "fdrcqutgrpfdaec", "cyfypt", "iezxlfmnhwlvpgzensnq", "iznzwltutyxd", "dlwbfch",
             "qyxaibavemizoahxwhtjexaujzbm",
             "nrqifrrhcxkuny", "yymgcbawh", "wd", "ztuolqf", "slrdlcqyevsjvobfd", "glotjh", "dsbds", "tpetl",
             "fryosmcawjsvbutg", "hudmoskbkakhsjqyuhrrt", "aww", "xjluxthorodhosxkrn", "fkyhahxbisvfjxj",
             "vkslygnbphhvdpauxjnfn", "vvxoqmsatgqanusjbyrxwdshvven", "hyb", "qxxowalutfwwpv", "sntazpdaodhdaid", "ws",
             "tsg",
             "crpwxtfukvethkwhtisxqmvohsx", "qfcpjzokpxxhgqajgq", "svzaumwyydtuveq", "inmwdmzejyl", "aexhlovhykxeoyxfi",
             "zswuf", "hiuxr", "fcxnirvfxzevmveemo", "cffdctpjzpgvuinotvnywxqph", "yzjbscqhtfyuubljpkjmxt"]
    list2 = ["yzjbscqhtfyuubljpkjmxt", "cffdctpjzpgvuinotvnywxqph", "fcxnirvfxzevmveemo", "hiuxr", "zswuf",
             "aexhlovhykxeoyxfi",
             "inmwdmzejyl", "svzaumwyydtuveq", "qfcpjzokpxxhgqajgq", "crpwxtfukvethkwhtisxqmvohsx", "tsg", "ws",
             "sntazpdaodhdaid", "qxxowalutfwwpv", "hyb", "vvxoqmsatgqanusjbyrxwdshvven", "vkslygnbphhvdpauxjnfn",
             "fkyhahxbisvfjxj", "xjluxthorodhosxkrn", "aww", "hudmoskbkakhsjqyuhrrt", "fryosmcawjsvbutg", "tpetl",
             "dsbds",
             "glotjh", "slrdlcqyevsjvobfd", "ztuolqf", "wd", "yymgcbawh", "nrqifrrhcxkuny",
             "qyxaibavemizoahxwhtjexaujzbm",
             "dlwbfch", "iznzwltutyxd", "iezxlfmnhwlvpgzensnq", "cyfypt", "fdrcqutgrpfdaec",
             "pqcetglnhibyhmveyblnlrymw",
             "whjktettjhafcviiivw", "tpyrljqdhatboqrnnnq", "strbmsndazagstxvojxc", "jxibbfteyfqh",
             "dhvshmxnljtsozhsjugbokxjiiapmb", "qp", "mszirwc", "likkuxoyubyandcnm", "mkointotmaled",
             "utolwmietafptpdnb",
             "mfpobuitnnxmkddwwzlfauosuzd", "zrnnxdcd", "bxhsxqhtbdsgpfeiqpdjumcjm", "izvwi", "siucrhynh",
             "pdbmjihtodwwa",
             "tvrippfy", "ihgevtuipgkvqgpkhlui", "bqbebomqulgwltbortyu", "zpdbagmcdfltcoiobkdrticgzeyn",
             "exlyaiolmjrca", "ux",
             "omvzwyrzlwstnwhwhssajzhbsd", "bpkwyfwccmnjqwdyhxrjaaxjcw", "sgsnxtsznntdptmxjg", "eqjukrlgnbpuesgea",
             "lbujpsqpfk", "pewwoxivlouurvfsadrc", "ecnzsirsqqqwldmzsat", "hvbgprgostxbh",
             "ikkzxhjapdmkyiutryhzvsijxzeo",
             "obsskhdangnyiok", "hhemkmkwuikfasranjgsjtug", "dbtfwbavxuxqzjtycorez", "user",
             "dbzlkbdgrtavnorpfvuvnxwnzeoc",
             "yaqhaymtozosbacorzavpgdgl", "phuolroyieomapmirpvaldtksgl", "nqyxdju", "abtsca", "ozzcx",
             "woryubernrrwthyce",
             "whxez", "selamkurrltpjkt", "ndfm", "vs", "ccdllhhubyjxfmvmxdcmpzdwy", "rbdbetwubqjppupythw", "gtdq",
             "qojwwpjt",
             "rvrfcepmxpeofenooth", "jjdizlchlorva", "ctsetmijpnp", "hsxjfwgbuorfznekqdvahrxgui", "zo", "tloeehsq",
             "vuqxhsrspvqath", "vfhpldeneeqxykmum", "ceyogdjazwskvjbdwrvufpqcjrxpws", "vbvbde", "aqlwxsrxggtfnz",
             "pcfbmtafjvrurtrvjsumfjfttu", "wsi", "ypmskmp", "kfjirgxu", "ztindosdnqsyquuhzjzpxkbeefun",
             "ouzklsdedbvwwketdhcfeuluvckf", "xerymxgwvzcb", "nasrnrizinuypjdnjehqqoitmvk", "yohsoxdaubemaogltuk",
             "dvjhqppvoowntco", "utraamepcsomyxsqbkshgyraleekxw", "xwetnsmpotlpn", "pgxnwszovqgqtcqpzmssneqejgjs",
             "yqzblljae",
             "lmhuzhpzmym", "tewapttno", "gcydrneexbcuqopkpcmd", "kgsptbnifrvczouohrrprli", "jmbefcplwqosvfx",
             "framwuszazkwdilvtylmkru", "qyn", "sdvhj", "izdo", "smbvogzsmbaxktmqwleprmbdxqf", "xgvvsydndmgs",
             "ybvtkizlmyfngyjwwowgsm", "lztmnoajehsvz", "udqooeglslqpajnip", "d", "hjiq",
             "huuftubpzskytmniladxkkgczftxp",
             "ktbjtqyvuuxqajcesnaw", "yxsybpiprmuhzplfphfeqazzyndtv", "faegljhiknwlygwhlu", "jiuiut", "gjcgpxz",
             "takqafyujrchibalhi", "uoejbnenp", "syc", "kiul", "gscljupcrmbbeobwvdht", "occgkf",
             "leyshdfdlagoalvfbegapxregtuh",
             "lwdhpatigvhypgzrertalatqspohi", "lhaijmcqlnrgimhbptwmkwt", "oglbicrgqvradxwtghghppnzznq", "rrwyr",
             "sykhquipjd",
             "frtrodsnrmsmaaws", "rvscpckcpjwgulnfnelspis", "czoepwnymcz", "stpuhrfbhoxf", "xflneeeaomxjphvgyohoakxhj",
             "chnbkhdgyjoxeglvfc", "fuosbwciqqzosy", "fyfiwcckdrjjpqfyrldhdyvu", "mofdl", "favfgqwpedkohfkoakisbmbxbxf",
             "ztanalcvncvm", "rhehzhnlk", "qggmtusbpnypjbxcisnoy", "xengrpxq", "knwvl", "vdvhdvfztaxcyhjdugctrvkgulmbj",
             "jsmzeshdnugttvppha", "sfxkoexlvpihhfhfq", "gfubyw", "bl", "uvpjsrqhwxdoeuc", "ymyzwmsxcirfwhsafs",
             "azusu", "isl",
             "ljdkfxvylzmspudjqqugddxrnhn", "pjgfwoikxbybblja", "zhjn", "htjlnvbdfuzsjypkanhzg",
             "oblhinaeguymmkleqeogwrzmbltl",
             "mtndwtean", "njnpajotnwihwedlefrukx", "zhcnue", "klgybdvijbdraoveascq", "stbyc",
             "upmawfjrcvyqphcgznqvlunehgm",
             "xxfrzciifwxwzkqlhzi", "bv", "fhukhpkax", "hpzca", "uilnponlhvulz", "krtfunvglmtcwasqlvhq", "xfhfqdqnklxq",
             "qaaoyjczafkqyncmmuqfj", "ucxqf", "idrkmks", "esvmtdtyojpoccpnhmweleclk", "eikqjjhbfnabekalchmoigbsvj",
             "fndfnvpnmgcxjbfydgwiwpvst", "jovaimqzyyputxnatlgvtflxmjwrgy", "ys", "fnxfo", "pgsbqvig",
             "jzfkmowocsuhipwvyavcimgslsa", "jxejmmiwfrrknjyek", "jbtpcxbxdbdpjztbvp", "tphnrrekc", "bdjntlktemditgnn",
             "iwmovzzkfpvixarqckonwqhb", "shufzxmpntnwkljqlayypynmnsvjnq", "xtzyn", "npjohbkidogcjbkpairnmmgslk",
             "utwqphdxvmtvtjw", "tvhkudu", "ltvkvjigjqdjmfqihssvnnmxke", "tvwhfeoxshl", "gwmoxooqbgkuqhitqndhjknpoi",
             "cugcsdfdgggnxbsrloqynmjisfxqcf", "fqoxrbegbqfseoiqvevfjua", "mducxmhhvuuoaxazhwpsuisush", "kbsglfxut",
             "hytiwcsrbwyj", "n", "xo", "vlhyfvzcuuqrqymnzlbqwlwyk", "hlcyxndydrxgebcjtgrjlfhhiqeh",
             "coxufsaunxexcshrcqyjz",
             "etwelbjtxilczjudlyziyosp", "eblxqnyke", "kexssggfp", "hyxexwoosybkpifyohasxtk", "wbtrhqdbwqyrvjizkgj",
             "zuzgiuonhoaaqmafflrnsamdkefoki", "l", "axdaqveyksrmpc", "hydpvnbhqpkvrcc",
             "rezogqmazduvkcypiupyitmhrfmzki",
             "cywlrzkl", "ucnfeysd", "vdztloyrjpzzylesddiewfemmbgfwe", "ugjnsgqlp", "xinbdvhzfykpmzpecgngelczoukzd",
             "acqnnodwqzwlqnynvb", "aooilovrtwqoaremskb", "zkrcckbowwjxmfmdikfsbpyxrmgg", "tmsfjgfjdjdbczcseznowpptr",
             "wwqbevusanvcdzeshcglrzlarer", "qyfopqgmglfiofw", "ymlznwinj", "dxeyeyejkosdpnub", "fmgqdzvdtyethyynjjpbl",
             "ykoyilcm", "qlewoezxzmlhgypikhdl", "ptopwfkziuttfeazrrglqdbszvr", "zosncavdfjcsdnrxdp",
             "eypstxtyxnnqnkmqptekdgpdqcdqn", "wnnhai", "ufolcgdeo", "zcxbycuiqlvfpuslvv", "alzzxhra",
             "ykiatwmdigjxmxevdbd",
             "xhc", "cblx", "nkmofftbapqitraxtfnilsfvwvpas", "geg", "ashrazctgqgwrm", "lha",
             "huhwnjqriyiweilhjzijuftlzp",
             "rooillldcagevixecdxffz", "zegpdvbmdgslagpvsjnmchspix", "ywqhjouxx", "lfgztikdpethoionvs",
             "gwurhajbnavidhipzhxvlf", "eelflqtsplanaahmxssqe", "vbqhjdqajtvy", "bsmqkkfmzszgtffpkpjouoxdmofivm",
             "fhjbrzhroorglgbltarrvtjnkz", "ckhb", "ijrbjrqopmbveayra", "p", "yvizbmradwgxedumcbcktxublw",
             "fxtsgerpchszrkfjpwwigy", "mjgmpewjnlwijzx", "rfbmlfacpec", "nqmgha", "swgsvdptrtepv",
             "fboaiwtlfccdolpqutf",
             "gpgbqii", "lfsxwnhweveaaekybglvcluyeb", "vagpvsdzqhwnlogzyje", "agfqdph", "pkwenkodtlbbdgvopqaeygphtlrmo"]
    result = solution.findRestaurant(list1, list2)
    print(result)
