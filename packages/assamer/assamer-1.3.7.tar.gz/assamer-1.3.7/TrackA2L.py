from ASSAM import ASSAM, MEASUREMENT, FUNCTION
from difflib import SequenceMatcher
import numpy as np
import concurrent.futures

class Similarity:
    def __init__(self, Ksm=0.5, Kco=0.5, ifempty=0):
        self.Ksm = Ksm
        self.Kco = Kco
        self.ifempty = ifempty
    def similar(self, a, b):
        return SequenceMatcher(None, self.correct(a).lower(), self.correct(b).lower()).ratio()
    def correct(self, input_str):
        output_str = ""
        for i in range(len(input_str)):
            if i > 0 and input_str[i].isupper() and input_str[i - 1].islower():
                output_str += " "
            output_str += input_str[i]
        return output_str
    def co_sim(self, a, b):
        a_list = self.correct(a).split()
        b_list = self.correct(b).split()
        words = set(a_list) | set(b_list)
        a_dict = {word: a_list.count(word) for word in words}
        b_dict = {word: b_list.count(word) for word in words}
        a_vec = np.array([a_dict[word] for word in words])
        b_vec = np.array([b_dict[word] for word in words])
        dot_product = np.dot(a_vec, b_vec)
        norm_a = np.sqrt(np.sum(a_vec ** 2))
        norm_b = np.sqrt(np.sum(b_vec ** 2))
        return dot_product / norm_a / norm_b
    def coSimilar(self, a, b, Kr=1):
        if self.ifempty and (len(a) == 0 or len(b) == 0):
            return 0
        return (self.Ksm * self.similar(a, b) + self.Kco * self.co_sim(a, b)) / (self.Ksm + self.Kco) * Kr


class Node:
    def __init__(self, layer, name, tofunc, func):
        self.layer = layer
        self.name = name
        self.tofunc = tofunc
        self.func = func
        self.data = []


class TrackA2L:
    def __init__(self, ASSAMObject: ASSAM):
        self.assam = ASSAMObject
        self.tree = []
        self.functions = self.assam.a2l.getArea(FUNCTION)
        self.condition = lambda sig: True
        self.signalfiltthd = 0.1
        self.similarity = Similarity(0.75, 0.25)
        self.similar = self.similarity.coSimilar
        self.letfeedback = True
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=100)
        self.futures = []
    def similarscore(self, value):
        valuedesc = self.assam.find(value, MEASUREMENT).desc
        return (
            (self.similar(self.refsig[0], value, 2))
            + self.similar(self.refsig[0], valuedesc)
            + self.similar(self.refsig[1], valuedesc)
        ) / 4
    def addTree(self, signal, depth, fromfunc, tofunc):
        for thenode in self.tree:
            if thenode.func == fromfunc and tofunc == thenode.tofunc:
                thenode.data.append(signal)
                return 1
        node = Node(depth, fromfunc.name, tofunc, fromfunc)
        node.data.append(signal)
        self.tree.append(node)
        return 1
    def follow(self, value, depth):
        self.refsig = [value, self.assam.find(value, MEASUREMENT).desc]
        self.refthd = self.similarscore(value)
        for func in self.functions:
            if value in func.OUT_MEASUREMENT:
                if depth < 0:
                    return self._revfollowsig(value, depth, func)
                print(func, " -> ", value)
                self._followsig(value, depth, func)
                break
    def _followsig(self, value, depth, fromfunc):
        if depth < 1:
            return 0
        tofuncs = []
        if True:
            for func in self.functions:
                if (
                    value in func.IN_MEASUREMENT
                    and func != fromfunc
                    and (
                        func.name not in [i.name for i in self.tree]
                        or self.letfeedback
                    )
                    and self.similarscore(value) / self.refthd
                    > self.signalfiltthd
                ):
                    print(
                        f"{depth}\t{value}->{func} %[{self.similarscore(value)/self.refthd:0.2f}]"
                    )
                    tofuncs.append(func)
                    for outfs in func.OUT_MEASUREMENT:
                        if len(outfs) > 1 and self.condition(outfs):
                            future = self.executor.submit(
                                self._followsig, outfs, depth - 1, func
                            )  # self._followsig(outfs, depth-1, func)
                            self.futures.append(future)
        if len(tofuncs) > 0:
            self.addTree(value, depth, fromfunc, tofuncs)
    def _revfollowsig(self, value, depth, fromfunc):
        if depth > -1:
            return 0
        tofuncs = []
        last = True
        for inSig in fromfunc.IN_MEASUREMENT:
            if (
                self.similarscore(inSig) / self.refthd
                < self.signalfiltthd
                or len(inSig) <= 1
                or not self.condition(inSig)
            ):
                break
            for funcout in self.functions:
                if inSig in funcout.OUT_MEASUREMENT:
                    func = funcout
                    last = False
                    break
            if not last:
                print(
                    f"{depth}\t{func}->{inSig} & [{self.similarscore(inSig)/self.refthd}]"
                )
                future = self.executor.submit(
                    self._revfollowsig, inSig, depth + 1, func
                )  # self._revfollowsig(inSig, depth+1, func)
                self.futures.append(future)
                print(func)
                tofuncs.append(func)
                self.addTree(inSig, depth, func, [fromfunc])


if __name__ == "__main__":
    a2lpath = "a2lpath.a2l"
    hexpath = "hexpath.hex"
    assam = ASSAM(A2LPath=a2lpath, HEXPath=hexpath)
    track = TrackA2L(assam)
    track.follow("aCalName", -1)
